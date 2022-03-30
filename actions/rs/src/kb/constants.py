'''
Author: Nguyen Phuc Minh
Lastest update: 23/3/2022
'''

import os

WORK_DIR = os.path.abspath(os.getcwd())
WORK_DIR = os.path.join(WORK_DIR,'actions','rs','src','kb')

# DISEASE - SYMPTOMS - SPECIALITY
DISEASE_PATH = os.path.join(WORK_DIR, "data/processed/diseases.csv")
SPECIALTY_PATH = os.path.join(WORK_DIR, "data/processed/specialties.csv")
SYMPTOM_PATH = os.path.join(WORK_DIR, "data/processed/symptoms.csv")
DISEASE_SYMPTOM_PATH = os.path.join(WORK_DIR, "data/processed/diseases_has_symptoms.csv")
DISEASE_SPECIALTY_PATH = os.path.join(WORK_DIR, "data/processed/diseases_health_specialties.csv")

# DOCTOR - PATIIENT
DOCTOR_PATH = os.path.join(WORK_DIR,"data/processed/doctor_data.csv")
PATIENT_PATH = os.path.join(WORK_DIR,"data/processed/patient_data.csv")

# INFANT_AGE
INFANT_AGE = 16
SPECS_SYMPTOM_PATH = os.path.join(WORK_DIR,"data/raw/spec_symptom.csv")
FUZZ_THRESHOLD = 80