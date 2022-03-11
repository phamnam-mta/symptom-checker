from typing import Any, Text, Dict, List

import logging
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

from actions.utils.rasa_util import (
    get_latest_bot_utter
)

logger = logging.getLogger(__name__)

class ActionChestPainRiskFactor(Action):

    def name(self) -> Text:
        return "action_chest_pain_risk_factor"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            age = tracker.get_slot('age')
            bot_utter = get_latest_bot_utter(tracker)
            if not age:
                return []
            
            if int(age) <= 55:
                if bot_utter == "utter_chest_pain_period":
                    dispatcher.utter_message(template="utter_chest_pain_virtual_care_1")
                if bot_utter == "utter_chest_pain_duration":
                    dispatcher.utter_message(template="utter_chest_pain_virtual_care_3")
            elif int(age) > 55:
                if bot_utter == "utter_chest_pain_period":
                    dispatcher.utter_message(template="utter_chest_pain_virtual_care_2")
                if bot_utter == "utter_chest_pain_duration":
                    dispatcher.utter_message(template="utter_chest_pain_virtual_care_4")

            return []
        except Exception as ex:
            logger.exception(ex)
            return []
