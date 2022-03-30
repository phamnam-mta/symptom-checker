from typing import Any, Text, Dict, List

import os
import logging
import copy

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, FollowupAction, AllSlotsReset, Restarted
from actions.utils.rasa_util import (
    get_latest_bot_utter
)

from actions.rs.src.recommender import Recommender
from actions.rs.constants import (
    CAROUSEL,
    CAROUSEL_ELEMENT,
    AVATAR_MALE,
    AVATAR_FEMALE,
    END_MSG,
    SYMTPOM_TO_VI
)

logger = logging.getLogger(__name__)


class ActionRecommendDoctors(Action):
    def __init__(self):

        NEO4J_URL = os.getenv("NEO4J_URL", None)
        NEO4J_AUTH = os.getenv("NEO4J_AUTH", None)
        user = NEO4J_AUTH.split("/")[0]
        password = NEO4J_AUTH.split("/")[1]

        self.rs = Recommender(
            NEO4J_URL,
            user,
            password
        )

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

            request = {
                "symptom" : SYMTPOM_TO_VI[symptom],
                "age" : age,
                "gender" : gender,
            }
            doctors = self.rs.suggest_doctors(request)
            
            msg = self.generate_carousel(doctors)
            print(msg)
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
       carousel = copy.deepcopy(CAROUSEL)
       for doctor in doctors:
            e = copy.deepcopy(CAROUSEL_ELEMENT)
            e['title'] = doctor['doctor']['name']
            e['subtitle'] = doctor['doctor']['title'] + '- Khoa ' + doctor['doctor']['speciality']

            if doctor['doctor']['gender'] == 'male':
               e['image_url'] = AVATAR_MALE
            else:
               e['image_url'] = AVATAR_FEMALE

            carousel['payload']['elements'].append(e) 
       return carousel