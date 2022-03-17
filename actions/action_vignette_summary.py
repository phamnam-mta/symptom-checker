from typing import Any, Text, Dict, List

import logging
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

from actions.vignette_summary.bot_utter_to_questionnaire import QUESTIONNAIRE
from actions.vignette_summary.export_vignette import generate_report

logger = logging.getLogger(__name__)

class ActionVignetteSummary(Action):

    def name(self) -> Text:
        return "action_vignette_summary"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            user_info = {
                "name": tracker.get_slot("user_name", ""),
                "age": tracker.get_slot("age", ""),
                "gender": tracker.get_slot("gender", "")
            }

            symptom = tracker.get_slot("symptom")
            questionnaire = QUESTIONNAIRE[symptom]
            suggestions = ""
            qa_pairs = []
            qa = {}
            find_answer = False
            for event in tracker.events:
                if  event.get('event') == 'bot' and event['metadata'].get('utter_action') in questionnaire['questions']:
                    qa['question'] = event.get('text')
                    find_answer = True
                    continue
                if find_answer and event.get('event') == 'user':
                    qa['answer'] = event.get('text')
                    qa_pairs.append(qa)
                if  event.get('event') == 'bot' and event['metadata'].get('utter_action') in questionnaire['suggestions']:
                    suggestions = event.get('text')
                
            generate_report(user_info, symptom, qa_pairs, suggestions)
            return []
        except Exception as ex:
            logger.exception(ex)
            return []
