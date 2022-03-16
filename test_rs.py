from actions.rs.recommender import Recommender
from actions.action_recommend_doctors import ActionRecommendDoctors

if __name__ == '__main__':
    rs = Recommender()

    # symptom + utter
    symptom = 'fever'
    utter = 'utter_fever_elder_urgent_out'

    try:
        doctors = rs(
            symptom=symptom,
            utterance=utter
        )
        print("case 1 success")
    except:
        print('case 1 fail')

    symptom = 'fever'

    try:
        doctors = rs(
            symptom=symptom,
        )
        print("case 2 success")
    except:
        print('case 2 fail')

    utter = 'utter_fever_elder_urgent_out'

    try:
        doctors = rs(
            utterance=utter
        )
        print("case 3 success")
    except:
        print('case 3 fail')


    try:
        doctors = rs(
            department_id='dept04'
        )
        print("case 4 success")
    except:
        print('case 4 fail')
 
    # test template carousel    
    rs_action = ActionRecommendDoctors()
    symptom = 'fever'
    utter = 'utter_fever_elder_urgent_out'
    doctors = rs(
        symptom=symptom,
        utterance=utter
    )
    template = rs_action.generate_carousel(doctors)
