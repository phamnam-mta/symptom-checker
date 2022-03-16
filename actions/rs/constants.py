
# Database

DOCTOR_PATH = 'actions/rs/data/doctor.json'

DEPARTMENT_ID = {
    'dept01':'hô hấp',
    'dept02':'tim mạch',
    'dept03':'nội',
    'dept04':'nhi',
    'dept05':'ngoại',
    'dept06':'nhiễm',
    'dept07':'thần kinh',
    'dept08': 'da liễu'
}

# chest pain - dept-id
CHEST_PAIN_DEPT = {
    'utter_warning_heart_attack':['dept02','dept01'],
    'utter_chest_pain_emergency':['dept02','dept01'],
    'utter_chest_pain_hospitalize_1':['dept02','dept01'],
    'utter_chest_pain_hospitalize_2':['dept02','dept01'],
    'utter_chest_pain_hospitalize_3':['dept02','dept01'],
    'action_chest_pain_risk_factor':['dept02','dept01'],
    'utter_chest_pain_virtual_care_5':['dept02','dept01'],
    'utter_chest_pain_self_treatment':['dept02','dept01']
}

# fever
FEVER_DEPT = {
    'utter_fever_elder_urgent_out':['dept03','dept01','dept02'],
    'utter_fever_children_urgent_out':['dept04','dept03'],
    'utter_high_fever_urgent_out':['dept03'],
    'utter_fever_headache_stiffneck_urgent_out':['dept03','dept01'],
    'utter_fever_skinspot_urgent_out':['dept01'],
    'utter_heartbeat_urgent_out':['dept02','dept03'],
    'utter_fever_mentalchange_urgent_out':['dept07','dept03'],
    'utter_fever_bloodpressure_urgent_out':['dept02','dept03'],
    'utter_fever_relocation_gp_out':['dept06','dept03','dept01'],
    'utter_fever_medication_gp_out':['dept03'],
    'utter_fever_respiratory_gp_out':['dept01'],
    'utter_fever_end_virtualcare_out':['dept03'],
    'utter_fever_children_selfcare_out':['dept04']
}

# headache
HEADACHE_DEPT = {

}

SYMPTOM_TO_DEPT = {
    'chest_pain':CHEST_PAIN_DEPT,
    'fever':FEVER_DEPT,
    'headache':HEADACHE_DEPT
}

# CAROUSEL
CAROUSEL = {
    "type": "template",
    "payload": {
        "template_type": "generic",
        "elements":[]
    }
}
CAROUSEL_ELEMENT = {
    "title": "", # name
    "subtitle": "", # degree
    "image_url": "",
    "buttons": [
        {
            "title": "Đặt lịch", 
            "type": "degree",
            "payload": "/greet"
        }
    ]
}