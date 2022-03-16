import json
from typing import List, Dict, Text
from actions.utils.util import read_json
from actions.rs.constants import (
    DEPARTMENT_ID,
    DOCTOR_PATH,
    CHEST_PAIN_DEPT,
    FEVER_DEPT,
    HEADACHE_DEPT,
    SYMPTOM_TO_DEPT
)

class Recommender:
    ''' Handle recommend appropriate doctor
    '''
    def __init__(self) -> None:
        self.doctor = read_json(DOCTOR_PATH)
    
    def __call__(self, 
                department_id:Text='',
                symptom:Text='', 
                utterance:Text='',
                age:int='',
                gender:Text='') -> List[Dict]:
        '''
        Args:
            - department_id (str) 
            - symptom (str)
            - age (str)
            - gender (str)
        Return:
            - result (List[Dict]) :
                    [{​​​​​​​​
                         "doctor_id": "3",
                         "doctor_name": "Nguyen Van C",
                         "department_id": "dept06",
                         "degree": "ThS BS",
                         "consultant_fee": "500k/1h",
                         "avatar": "https://image.freepik.com/free-vector/doctor-icon-avatar-white_136162-58.jpg",
                         "time_slots": [
                         {​​​​​​​​
                             "time": "8:00",
                             "date": "07/06/2021",
                             "fee": "300.000 VND"
                         }​​​​​​​​,
                         {​​​​​​​​
                             "time": "16:00",
                             "date": "07/06/2021",
                             "fee": "100.000 VND"
                        }
                     }​​​​​​​​]
        '''
        # suggest by department_id
        if department_id != "":
            relevant_doctors = self.get_doctors_by_dept_id(department_id)
            return relevant_doctors

        # suggest by utterance/action and/or symptom
        if utterance != "" or symptom != "":
            relevant_doctors = self.get_doctors_by_utter_symptom(symptom,utterance)
            return relevant_doctors
    
    def get_doctors_by_utter_symptom(self,symptom:Text,utterance:Text) -> List[Dict]:
        ''' Get doctors by symptom and/or utterance
        '''
        if symptom != '' and utterance != '':
            result = []
            
            dept_ids = self.get_dept_id_from_symptom_utter(symptom,utterance)

            # from dept_id to doctors
            for dept_id in dept_ids:
                doctors = self.get_doctors_by_dept_id(dept_id)
                result.extend(doctors)
            return result

        if symptom != '':
            doctors = self.get_doctors_by_symptom(symptom)
            return doctors
        
        if utterance != '':
            doctors = self.get_doctors_by_utter(utterance)
            return doctors

    def get_dept_id_from_symptom_utter(self,symptom:Text,utterance:Text) -> List:
        # symptom -> symptom depertment 
        symptom_dept = SYMPTOM_TO_DEPT[symptom]
        # symptom department + utterance -> department id
        return symptom_dept[utterance]

    def get_dept_id_from_utter(self,utterance:Text) -> List:
        symptom_dept = SYMPTOM_TO_DEPT.values()

        for symp_dept in symptom_dept:
            for k,v in symp_dept.items():
                if k == utterance:
                    return v
        return []

    def get_doctors_by_symptom(self,symptom:Text) -> List[Dict]:
        ''' Get all related department then return doctors
        '''
        dept = {}
        result = []

        symptom_dept = SYMPTOM_TO_DEPT[symptom]

        for k,v in symptom_dept.items():
            for d in v:
                if d not in dept:
                    dept[d] = 1
                else:
                    dept[d] += 1
        
        dept = list(sorted(dept.items(), key=lambda item: item[1]))

        for dept_id in dept:
            doctors = self.get_doctors_by_dept_id(dept_id)
            result.extend(doctors)

        return result

    def get_doctors_by_dept_id(self,dept_id:Text) -> List[Dict]:
        ''' Get doctor based on given department_id
        '''
        result = []
        for doctor in self.doctor:
            if doctor['department_id'] == dept_id:
                result.append(doctor)
        return result

    def get_doctors_by_utter(self,utterance:Text) -> List[Dict]:
        ''' Get department_id then return doctors
        '''
        department_id = self.get_dept_id_from_utter(utterance)

        if department_id == []:
            print(f"{utterance} is not registered in `constants.py`")
            return [{}]
        
        result = []
        for dept_id in department_id:
            d = self.get_doctors_by_dept_id(dept_id)
            result.extend(d)
        return result

