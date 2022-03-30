''' 
Author: Nguyen Phuc Minh
Lastest update: 28/3/2022
'''

import math
import numpy as np

from numpy import sort
from typing import List,Dict
from actions.rs.src.reranker.constants import *

class Reranker:
    def __init__(self) -> None:
        self.confident_score = []
    
    def numerical_converter(self,doctors) -> List:
        ''' Convert str to numerical
        '''
        doctors_features = []
        for i in doctors:
            for j in i.values():
                doctor_feature = [None] * 7
                for k, l in j.items():
                    # print(k,l)
                    if k == "review":
                        doctor_feature[4] = l
                    if k == "hourly_rate" and l != "No Info":
                        doctor_feature[2] = int(l) / 100000
                    if k == "hourly_rate" and l == "No Info":
                        doctor_feature[2] = 1
                    if k == "rating":
                        doctor_feature[1] = l
                    if k == "title" and l == "THsBS":
                        doctor_feature[0] = 2
                    if k == "title" and l == "BS":
                        doctor_feature[0] = 1
                    if k == "experience":
                        doctor_feature[3] = 1
                    if k == "gender":
                        doctor_feature[6] = 1
                    if k == "age" and l != "No Info":
                        doctor_feature[5] = 1
                    if k == "age" and l == "No Info":
                        doctor_feature[5] = 1
                doctor_feature = [1 if v is None else v for v in doctor_feature]
                doctor_feature = [1 if v == 0 else v for v in doctor_feature]
                doctor_feature = [1 if v == "No Info" else v for v in doctor_feature]
                doctors_features.append(doctor_feature)
        return doctors_features

    def priority_doctor_by_a_patient(self, doctor, numerial_values_a_patient) -> List:

        priority_by_a_patient = []
        # numerical_values_a_patient = [Gender 1, Income 1]
        # doctor = [feature 1, ..., feature 7]
        for i in range(0, NUMBER_DOCTOR_FEATURES):
            if i == 0:
                priority_by_a_patient.append(i + 1 - math.log10(doctor[i]))
            if i == 1:
                if doctor[i] < 4:
                    priority_by_a_patient.append(i + 1 + math.log10(doctor[i]))
                else:
                    priority_by_a_patient.append(i + 1 - math.log10(doctor[i]))
            if i == 2:
                if numerial_values_a_patient[1]  == 2:
                    priority_by_a_patient.append(i + 1 + math.log10(doctor[2]) - math.log10(2))
                if numerial_values_a_patient[1] == 4:
                    priority_by_a_patient.append(i + 1 + math.log10(doctor[2]) + math.log10(4))
                else:
                    priority_by_a_patient.append(i + 1 + math.log10(doctor[2]))
            #else:
            #    priority_by_a_patient.append(i + 1 - math.log10(doctor[i]))
            if i == 3:
                priority_by_a_patient.append(i + 1 - math.log10(doctor[i]))

            if i == 4:
                priority_by_a_patient.append(i + 1 - math.log10(doctor[i]))
            if i == 5:
                priority_by_a_patient.append(i + 1 - math.log10(doctor[i]))
            if i == 6:
                priority_by_a_patient.append(i + 1 - math.log10(doctor[i]))
        return  priority_by_a_patient

    def priority_doctor_by_all_patients(self, doctor, numerical_values_all_patients) -> List:
        # calculation piority
        #doctor = [feature 1, ..., feature 7]
        #numerical_values_all_patients = [[Gender 1, Income 1], [Gender 2, Income 2], ...]
        priority_a_doctor_by_all_patients = []
        for i in numerical_values_all_patients:
            priority_a_doctor_by_all_patients.append(self.priority_doctor_by_a_patient(doctor, i))
        return priority_a_doctor_by_all_patients

    def weight_all_doctors_by_all_patients(self, numerical_values_all_doctors, numerical_values_all_patients):
        weight_all_doctors = []

        for doctor in numerical_values_all_doctors:
            weight_a_doctor = []
            p = self.priority_doctor_by_all_patients(doctor, numerical_values_all_patients)
            alpha = []
            for i in p:
                i = [5/x for x in i]
                self.confident_score.append(sum(i))
                alpha.append(i)
            alpha_aggregate = [sum(i) for i in zip(*alpha)]
            for i in alpha_aggregate:
                weight_a_doctor.append(i/sum(alpha_aggregate))
            weight_all_doctors.append(weight_a_doctor)

        return weight_all_doctors

    def reranking_doctor(self, doctors:List) -> List[Dict]:
        result = []
        doctors_features = self.numerical_converter(doctors)
        numerical_patients =[[1,1]]
        #doctor ranking
        rank = self.weight_all_doctors_by_all_patients(doctors_features, numerical_patients)
        #top@K = 5
        k = 5
        ind = np.argpartition(self.confident_score, -k)[-k:]
        #index of rank list
        index = sort(ind)

        for i in index:
            result.append({
                "doctor" : doctors[i]['properties(s)'],
                'conf_score' : self.confident_score[i]
            })
        return result
    