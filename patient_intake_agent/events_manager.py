from patient_intake_agent.logger import logger
from vocode.streaming.utils import events_manager
from vocode.streaming.models.events import (
    Event,
    EventType,
)


class CustomEventsManager(events_manager.EventsManager):
    def __init__(self):
        super().__init__(
            subscriptions=[
                # EventType.TRANSCRIPT,
                EventType.TRANSCRIPT_COMPLETE,
            ]
        )

    def handle_event(self, event: Event):
        logger.info(event)


custom_events_manager = CustomEventsManager()
