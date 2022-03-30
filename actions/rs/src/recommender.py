''' 
Author: Nguyen Phuc Minh
Lastest update: 28/3/2022
'''

import os
from typing import List,Dict,Text
from actions.rs.src.kb.neo4j_provider import Neo4jProvider
from actions.rs.src.reranker.reranking import Reranker

class Recommender:
    def __init__(
        self,
        uri:Text,
        user:Text,
        password:Text
        ) -> None:
        
        self.data_provider = Neo4jProvider(uri,user,password)
        self.re_ranker = Reranker()

    def suggest_doctors(self,request:Dict) -> List[Dict]:
        ''' Suggest doctors from given request dict
        Args:
            - request : {
                symptom': "sốt",
                'speciality': '',
                'age': '30'
            }
        '''
        doctors = self.data_provider.query_doctors(request)
        doctors = self.re_ranker.reranking_doctor(doctors) # list[dict]
        return doctors

    