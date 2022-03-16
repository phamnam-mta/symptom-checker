from typing import Any, Text, Dict, List

import logging
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, FollowupAction, AllSlotsReset, Restarted

from actions.utils.rasa_util import (
    get_latest_bot_utter
)

logger = logging.getLogger(__name__)

class ActionFeverAgeRouter(Action):
    def __init__(self):
        self.URGENT_INFANT_AGE = 1
        self.URGENT_OLD_AGE = 65

    def name(self) -> Text:
        return "action_fever_pre_age_router"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        ''' Check whether is fever within urgent age
        '''
        try:
            age = tracker.get_slot('age')
            bot_utter = get_latest_bot_utter(tracker)
            if not age:
                return []
            
            if int(age) <= self.URGENT_INFANT_AGE:
                dispatcher.utter_message(template="utter_fever_children_urgent_out")
                return [FollowupAction("action_recommend_doctors"),Restarted()]

            if int(age) >= self.URGENT_OLD_AGE:
                dispatcher.utter_message(template="utter_fever_elder_urgent_out")
                return [FollowupAction("action_recommend_doctors"),Restarted()]

            return [FollowupAction("utter_fever_level")]

        except Exception as ex:
            logger.exception(ex)
            return []
