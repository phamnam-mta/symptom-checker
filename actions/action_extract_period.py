import logging
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

logger = logging.getLogger(__name__)

class ActionExtractPeriod(Action):

    def name(self) -> Text:
        return "action_extract_period"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            last_entities = list(tracker.get_latest_entity_values('period'))
            if last_entities:
                return [SlotSet(last_entities[0], True)]

            return []
        except Exception as ex:
            logger.exception(ex)
            return []
