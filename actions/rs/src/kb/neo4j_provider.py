'''
Author: Nguyen Phuc Minh
Lastest update: 23/3/2022
'''

import os
import itertools
import pandas as pd

from typing import Text, List, Dict
from py2neo import Graph, Node
from actions.rs.src.kb.nlptoolkit import NLP
from actions.rs.src.kb.constants import (
    INFANT_AGE, 
    SPECS_SYMPTOM_PATH,
    FUZZ_THRESHOLD
)

class Neo4jProvider():
    def __init__(self, uri: Text = None, user: Text = None, password: Text = None):
        if not uri:
            uri = NEO4J_URL
            user = NEO4J_AUTH.split("/")[0]
            password = NEO4J_AUTH.split("/")[1]

        self.graph = Graph(uri, auth=(user, password))
        self.nlp = NLP()

        self.spec_symptom = pd.read_csv(SPECS_SYMPTOM_PATH)
        
    def query_doctors(self,request:Dict) -> List[Dict]:
        ''' Query doctor from database
        Args:
            - request : {
                'symptom' (str)
                'speciality' (str)
                'age' (str)
            }
        Return:
        '''
        # get relevant doctors by specility
        try:
            # Priority 1 : age
            age = int(request['age'])

            if age <= INFANT_AGE:
                doctors = self.get_doctors_by_speciality('nhi')
                return doctors

            # Priority 2 : symptom
            if request['symptom'] != '':
                doctors = []
                specs = self.get_spec_from_symptom(request['symptom'])

                for sp in specs:
                    d = self.get_doctors_by_speciality(sp)
                    if d != []:
                        doctors.extend(d)
                return doctors

            # Priority 3 : speciality
            doctors = self.get_doctors_by_speciality(request['speciality'])
            return doctors
        except:
            print(f"No doctor has speciality is {request['speciality']}")
            return [{}]

    def get_doctors_by_speciality(self,speciality:Text) -> List[Dict]:
        query = f"""
            MATCH (s:Doctor)
            WHERE s.speciality = "{speciality}"
            RETURN properties(s)
            """
        ans = self.graph.run(query).data()
        return ans

    def get_spec_from_symptom(self,symptom:Text) -> List:
        ''' Get specs from given symptom
        '''
        specs = []
        for index, row in self.spec_symptom.iterrows():
            keywords = row[3]
            keywords = keywords.split(',')
            for k in keywords:
                out = self.nlp.compare_string(
                    str1=k,
                    str2=symptom,
                    method='fuzzy',
                    threshold=FUZZ_THRESHOLD
                )
                if out.result:
                    specs.append(row[2]) # speciality 
                    break
        print(specs)
        return specs