from typing import Any, Text, Dict, List

import logging
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, FollowupAction, AllSlotsReset, Restarted

from actions.utils.rasa_util import (
    get_latest_bot_utter
)

from actions.rs.recommender import Recommender
from actions.rs.constants import (
    CAROUSEL,
    CAROUSEL_ELEMENT,
    DEPARTMENT_ID,
    END_MSG
)

logger = logging.getLogger(__name__)

class ActionRecommendDoctors(Action):
    def __init__(self):
        self.rs = Recommender()

    def name(self) -> Text:
        return "action_recommend_doctors"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        ''' Check whether is fever within urgent age
        '''
        try:
            age = tracker.get_slot('age')
            gender = tracker.get_slot('gender')
            symptom = tracker.get_slot('symptom')
            bot_utter = get_latest_bot_utter(tracker)

            doctors = self.rs(
                symptom=symptom,
                utterance=bot_utter,
                age=age,
                gender=gender
            )
            
            msg = self.generate_carousel(doctors)

            # display message
            dispatcher.utter_message(text=END_MSG)

            # display carousel
            dispatcher.utter_message(attachment=msg)

            return []

        except Exception as ex:
            logger.exception(ex)
            return []

    def generate_carousel(self,doctors:List[Dict]) -> Dict:
       ''' Fill-in rasa carousel template
       '''
       carousel = CAROUSEL
       for doctor in doctors:
           e = CAROUSEL_ELEMENT
           e['title'] = doctor['doctor_name']
           e['subtitle'] = doctor['degree'] + '- Khoa ' + str(DEPARTMENT_ID[doctor['department_id']])
           e['image_url'] = doctor['avatar']
           
           carousel['payload']['elements'].append(e) 
       return carousel