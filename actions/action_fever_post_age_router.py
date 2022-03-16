from typing import Any, Text, Dict, List

import logging
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, FollowupAction, AllSlotsReset, Restarted

from actions.utils.rasa_util import (
    get_latest_bot_utter
)

logger = logging.getLogger(__name__)

class ActionFeverPostAgeRouter(Action):
    def __init__(self):
        self.INFANT_AGE = 3

    def name(self) -> Text:
        return "action_fever_post_age_router"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        ''' Check respiratory if age<=3, otherwise return utter_fever_end_virtualcare_out
        '''
        try:
            age = tracker.get_slot('age')
            
            if int(age) <= self.INFANT_AGE:
                return [FollowupAction("utter_fever_respiratory")]

            return [FollowupAction("utter_fever_end_virtualcare_out")]                

        except Exception as ex:
            logger.exception(ex)
            return []
