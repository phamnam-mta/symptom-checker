import logging
from typing import Dict, Text, List, Any, Callable
from rasa_sdk import Tracker
from rasa_sdk.events import SlotSet

logger = logging.getLogger(__name__)

def get_latest_bot_utter(tracker: Tracker):
    bot_utter = [event['metadata'].get('utter_action') for event in reversed(
        tracker.events) if event.get('event') == 'bot' and event['metadata'].get('utter_action')]
    if bot_utter:
        return bot_utter[0]
    else:
        return ""

def all_slots_reset(tracker: Tracker, excluded: List[Text]):
    events = []
    for s in tracker.slots:
        if s not in excluded:
            events.append(SlotSet(s, None))
    return events