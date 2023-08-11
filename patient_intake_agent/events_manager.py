import typing
from patient_intake_agent.logger import logger
from vocode.streaming.utils import events_manager
from vocode.streaming.models.events import Event, EventType
from vocode.streaming.models.transcript import TranscriptCompleteEvent
from patient_intake_agent.transcript_parser import get_patient_data_from_transcript
from patient_intake_agent.constants import PATIENT_DATA_WITH_APPOINTMENT
from patient_intake_agent.sms import send_appointment_sms


class InboundCallEventsManager(events_manager.EventsManager):
    def __init__(self):
        super().__init__(
            subscriptions=[
                # EventType.TRANSCRIPT,
                EventType.TRANSCRIPT_COMPLETE,
            ]
        )

    def post_call_handler(self, transcript_complete_event: TranscriptCompleteEvent):
        transcript_str = transcript_complete_event.transcript.to_string(
            include_timestamps=False
        )
        # get structured patient data from unstructured transcript
        parsed_patient_data = get_patient_data_from_transcript(
            transcript_str, PATIENT_DATA_WITH_APPOINTMENT
        )
        logger.info(parsed_patient_data)

        patient_phone_number = parsed_patient_data.get("contact").get("phone")
        patient_first_name = parsed_patient_data.get("first_name")
        patient_appointment = parsed_patient_data.get("appointment")
        send_appointment_sms(
            patient_phone_number, patient_first_name, patient_appointment
        )

    def handle_event(self, event: Event):
        if event.type == EventType.TRANSCRIPT_COMPLETE:
            transcript_complete_event = typing.cast(TranscriptCompleteEvent, event)
            self.post_call_handler(transcript_complete_event)


inbound_call_events_manager = InboundCallEventsManager()
