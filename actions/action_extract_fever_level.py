import logging
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

logger = logging.getLogger(__name__)

class ActionExtractFeverLevel(Action):

    def name(self) -> Text:
        return "action_extract_fever_level"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            last_entities = list(tracker.get_latest_entity_values('fever_level'))
            if last_entities:
                return [SlotSet("fever_level", last_entities[0])]

            return []
        except Exception as ex:
            logger.exception(ex)
            return []
