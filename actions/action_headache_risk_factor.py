from typing import Any, Text, Dict, List

import logging
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

from actions.utils.rasa_util import (
    get_latest_bot_utter
)

logger = logging.getLogger(__name__)

class ActionHeadacheRiskFactor(Action):

    def name(self) -> Text:
        return "action_headache_risk_factor"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            age = tracker.get_slot('age')
            if not age:
                return []
            
            if int(age) <= 50:
                dispatcher.utter_message(template="utter_ask_headache_migraine")
            elif int(age) > 50:
                dispatcher.utter_message(template="utter_headache_onset")

            return []
        except Exception as ex:
            logger.exception(ex)
            return []
