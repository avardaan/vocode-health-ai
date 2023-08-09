from vocode.streaming.streaming_conversation import StreamingConversation
from vocode.streaming.transcriber import *
from vocode.streaming.agent import *
from vocode.streaming.synthesizer import *
from vocode.streaming.models.transcriber import *
from vocode.streaming.models.agent import *
from vocode.streaming.models.synthesizer import *
from vocode.streaming.models.message import BaseMessage

from patient_intake_agent.constants import INITIAL_MESSAGE, PROMPT_PREAMBLE
from patient_intake_agent.logger import logger
from patient_intake_agent.events_manager import custom_events_manager


def create_conversation_engine(
    input_device: BaseInputDevice, output_device: BaseOutputDevice
):
    custom_transcriber = DeepgramTranscriber(
        DeepgramTranscriberConfig.from_input_device(
            input_device=input_device,
            endpointing_config=PunctuationEndpointingConfig(),
        )
    )

    custom_agent = ChatGPTAgent(
        ChatGPTAgentConfig(
            initial_message=BaseMessage(text=INITIAL_MESSAGE),
            prompt_preamble=PROMPT_PREAMBLE,
            track_bot_sentiment=True,
            end_conversation_on_goodbye=True,
        )
    )

    custom_synthesizer = AzureSynthesizer(
        AzureSynthesizerConfig.from_output_device(output_device=output_device)
    )

    return StreamingConversation(
        events_manager=custom_events_manager,
        output_device=output_device,
        transcriber=custom_transcriber,
        agent=custom_agent,
        synthesizer=custom_synthesizer,
        logger=logger,
    )
