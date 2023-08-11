import typing
from patient_intake_agent.logger import logger
from vocode.streaming.utils import events_manager
from vocode.streaming.models.events import Event, EventType
from vocode.streaming.models.transcript import TranscriptCompleteEvent
from patient_intake_agent.transcript_parser import get_patient_data_from_transcript
from patient_intake_agent.constants import PATIENT_DATA_WITH_APPOINTMENT


def post_call_handler(transcript_complete_event: TranscriptCompleteEvent):
    transcript_str = transcript_complete_event.transcript.to_string(
        include_timestamps=False
    )
    logger.info(transcript_str)
    gpt_response = get_patient_data_from_transcript(
        transcript_str, PATIENT_DATA_WITH_APPOINTMENT
    )


class InboundCallEventsManager(events_manager.EventsManager):
    def __init__(self):
        super().__init__(
            subscriptions=[
                # EventType.TRANSCRIPT,
                EventType.TRANSCRIPT_COMPLETE,
            ]
        )

    def handle_event(self, event: Event):
        if event.type == EventType.TRANSCRIPT_COMPLETE:
            transcript_complete_event = typing.cast(TranscriptCompleteEvent, event)
            post_call_handler(transcript_complete_event)


inbound_call_events_manager = InboundCallEventsManager()
