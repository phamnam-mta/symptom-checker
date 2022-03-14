from typing import Text, List, Any, Dict

from rasa_sdk import Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict


class ValidateAgetForm(FormValidationAction):
    def __init__(self):
        self.MAX_AGE = 120
        self.MIN_AGE = 0
        self.NOTIFY_TEXT = f'Tuổi hợp lệ nên từ {self.MIN_AGE} đến {self.MAX_AGE}'

    def name(self) -> Text:
        return "validate_user_info_form"

    def validate_age(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate age value."""

        if int(slot_value) <=  self.MAX_AGE and int(slot_value) >= self.MIN_AGE:
            # validation succeeded, set the value of the "age" slot to value
            return {"age": slot_value}
        else:
            # validation failed, set this slot to None so that the
            # user will be asked for the slot again
            dispatcher.utter_message(text=self.NOTIFY_TEXT)
            return {"age": None}