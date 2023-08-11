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
        # TODO: persist parsed patient data
        parsed_patient_data = get_patient_data_from_transcript(
            transcript_str, PATIENT_DATA_WITH_APPOINTMENT
        )
        logger.info(parsed_patient_data)
        # validate parsed patient data
        if not parsed_patient_data:
            logger.error("Error retrieving patient data from transcript")
            return

        patient_phone_number = parsed_patient_data.get("contact").get("phone")
        patient_first_name = parsed_patient_data.get("first_name")
        patient_appointment = parsed_patient_data.get("appointment")
        # send appointment confirmation SMS
        send_appointment_sms(
            patient_phone_number, patient_first_name, patient_appointment
        )

    def handle_event(self, event: Event):
        # TODO: get caller number from CallConfig?
        if event.type == EventType.TRANSCRIPT_COMPLETE:
            transcript_complete_event = typing.cast(TranscriptCompleteEvent, event)
            # TODO: persist transcript
            # handle post call processing
            self.post_call_handler(transcript_complete_event)


inbound_call_events_manager = InboundCallEventsManager()
