from typing import Any, Text, Dict, List

import logging
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, SessionStarted

from actions.vignette_summary.bot_utter_to_questionnaire import QUESTIONNAIRE
from actions.vignette_summary.export_vignette import generate_report

logger = logging.getLogger(__name__)

class ActionBookAppt(Action):

    def name(self) -> Text:
        return "action_book_appt"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            user_info = {
                "name": tracker.get_slot("user_name"),
                "age": tracker.get_slot("age"),
                "gender": tracker.get_slot("gender")
            }

            symptom = tracker.get_slot("symptom")
            questionnaire = QUESTIONNAIRE.get(symptom)
            if questionnaire:
                suggestions = ""
                qa_pairs = []
                qa = {}
                find_answer = False
                convo_index = [index for index, event in enumerate(tracker.events) if event['event'] == 'restart' or  event['event'] == 'session_started']
                if convo_index:
                    latest_convo = tracker.events[convo_index[-1]:]
                else:
                    latest_convo = tracker.events
                for event in latest_convo:
                    if  event.get('event') == 'bot' and event['metadata'].get('utter_action') in questionnaire['questions']:
                        qa['question'] = event.get('text')
                        find_answer = True
                        continue
                    if find_answer and event.get('event') == 'user':
                        qa['answer'] = event.get('text')
                        qa_pairs.append(qa)
                        qa = {}
                        find_answer = False
                    if  event.get('event') == 'bot' and event['metadata'].get('utter_action') in questionnaire['suggestions']:
                        suggestions = event.get('text')
                    
                generate_report(user_info, symptom, qa_pairs, suggestions)
                dispatcher.utter_message(template="utter_book_appt_successful")
            return [SessionStarted()]
        except Exception as ex:
            logger.exception(ex)
            return []
