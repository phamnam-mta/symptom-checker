
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
    'utter_chest_pain_self_treatment':['dept02','dept01'],
    'utter_suspected_heart_attack': ['dept02','dept01'],
    'utter_chest_pain_warning_signs':['dept02','dept01'],
    'utter_chest_pain_progression':['dept02','dept01'],
    'utter_chest_pain_period':['dept02','dept01'],
    'utter_chest_pain_at_night':['dept02','dept01'],
    'utter_chest_pain_duration':['dept02','dept01'],
    'utter_chest_pain_related_symptom':['dept02','dept01']
}

# fever
FEVER_DEPT = {
    'utter_fever_elder_urgent_out':['dept03','dept01','dept02'],
    'utter_fever_elder':['dept03','dept01','dept02'],
    'utter_fever_children_urgent_out':['dept04','dept03'],
    'utter_fever_children':['dept04','dept03'],
    'utter_high_fever_urgent_out':['dept03'],
    'utter_high_fever':['dept03'],
    'utter_fever_headache_stiffneck_urgent_out':['dept03','dept01'],
    'utter_fever_headache_stiffneck':['dept03','dept01'],
    'utter_fever_skinspot_urgent_out':['dept01'],
    'utter_fever_skinspot':['dept01'],
    'utter_heartbeat_urgent_out':['dept02','dept03'],
    'utter_heartbeat':['dept02','dept03'],
    'utter_fever_mentalchange_urgent_out':['dept07','dept03'],
    'utter_fever_mentalchange':['dept07','dept03'],
    'utter_fever_bloodpressure_urgent_out':['dept02','dept03'],
    'utter_fever_bloodpressure':['dept02','dept03'],
    'utter_fever_relocation_gp_out':['dept06','dept03','dept01'],
    'utter_fever_relocation':['dept06','dept03','dept01'],
    'utter_fever_medication_gp_out':['dept03'],
    'utter_fever_medication':['dept03'],
    'utter_fever_respiratory_gp_out':['dept01'],
    'utter_fever_respiratory':['dept01'],
    'utter_fever_end_virtualcare_out':['dept03'],
    'utter_fever_end':['dept03'],
    'utter_fever_children_selfcare_out':['dept04'],
    'utter_fever_children':['dept04']
}

# headache
HEADACHE_DEPT = {
    "utter_headache_hospitalize_1": ['dept07'],
    "utter_headache_hospitalize_2": ['dept07'],
    "utter_headache_hospitalize_3": ['dept07'],
    "utter_headache_virtual_care_1": ['dept07'],
    "utter_headache_virtual_care_2": ['dept07'],
    "utter_headache_virtual_care_3": ['dept07'],
    "utter_headache_virtual_care_4": ['dept07'],
    'utter_headache_warning_signs':['dept07'],
    'utter_headache_unusual':['dept07'],
    'utter_headache_onset':['dept07'],
    'utter_ask_headache_migraine':['dept07'],
    'utter_ask_headache_tension':['dept07'],
    'utter_ask_headache_cluster':['dept07']
}

SYMPTOM_TO_DEPT = {
    'chest_pain':CHEST_PAIN_DEPT,
    'fever':FEVER_DEPT,
    'headache':HEADACHE_DEPT
}

SYMTPOM_TO_VI = {
    'chest_pain' : "đau ngực",
    'fever' : "sốt",
    'headache' : "đau đầu"
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
            "type": "postback",
            "payload": "/book_appt"
        }
    ]
}

AVATAR_MALE = 'https://img.freepik.com/free-vector/doctor-icon-avatar-white_136162-58.jpg'
AVATAR_FEMALE = 'https://www.freepik.com/premium-vector/doctor-nurse-line-icon-avatar-doctor-medicine-character-doodle-line-style-vector-illustration_22528348.htm#page=3&query=doctor%20icon%20avatar%20white&position=10&from_view=search'

END_MSG = 'Dựa trên các thông tin Ông/Bà cung cấp, chúng tôi xin gợi ý các bác sĩ phù hơp nhất.'

