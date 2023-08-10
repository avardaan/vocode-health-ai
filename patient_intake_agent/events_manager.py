import typing
from patient_intake_agent.logger import logger
from vocode.streaming.utils import events_manager
from vocode.streaming.models.events import Event, EventType
from vocode.streaming.models.transcript import TranscriptCompleteEvent

from patient_intake_agent.transcript_parser import get_patient_data_from_transcript


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
            # cid = transcript_complete_event.conversation_id
            parsed_patient_data = get_patient_data_from_transcript(
                transcript_complete_event.transcript.to_string(include_timestamps=False)
            )
            # logger.info(
            #     f"Patient data parsed from transcript: {parsed_patient_data.json()}"
            # )


custom_events_manager = InboundCallEventsManager()
