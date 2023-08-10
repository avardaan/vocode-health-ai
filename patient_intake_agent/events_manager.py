import typing
from patient_intake_agent.logger import logger
from vocode.streaming.utils import events_manager
from vocode.streaming.models.events import Event, EventType
from vocode.streaming.models.transcript import TranscriptCompleteEvent


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
            logger.info(
                transcript_complete_event.transcript.to_string(
                    include_timestamps=False
                ),
            )
            


inbound_call_events_manager = InboundCallEventsManager()
