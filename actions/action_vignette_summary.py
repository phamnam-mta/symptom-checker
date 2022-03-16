from typing import Any, Text, Dict, List

import logging
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

logger = logging.getLogger(__name__)

class ActionVignetteSummary(Action):

    def name(self) -> Text:
        return "action_vignette_summary"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            

            return []
        except Exception as ex:
            logger.exception(ex)
            return []
