import os
from vocode.streaming.streaming_conversation import StreamingConversation
from vocode.streaming.transcriber import *
from vocode.streaming.agent import *
from vocode.streaming.synthesizer import *
from vocode.streaming.models.transcriber import *
from vocode.streaming.models.agent import *
from vocode.streaming.models.synthesizer import *
from vocode.streaming.models.message import BaseMessage
from vocode.streaming.telephony.hosted.inbound_call_server import InboundCallServer
from vocode.streaming.models.telephony import TwilioConfig

from patient_intake_agent.constants import INITIAL_MESSAGE, PROMPT_PREAMBLE
from patient_intake_agent.logger import logger
from patient_intake_agent.events_manager import custom_events_manager


def create_inbound_call_server():
    twilio_config = TwilioConfig(
        account_sid=os.getenv("TWILIO_ACCOUNT_SID"),
        auth_token=os.getenv("TWILIO_AUTH_TOKEN"),
    )
    custom_transcriber = DeepgramTranscriber(
        DeepgramTranscriberConfig(
            endpointing_config=PunctuationEndpointingConfig(),
            sampling_rate=DEFAULT_SAMPLING_RATE,
            audio_encoding=DEFAULT_AUDIO_ENCODING,
            chunk_size=DEFAULT_CHUNK_SIZE,
        )
    )

    custom_agent = ChatGPTAgent(
        ChatGPTAgentConfig(
            initial_message=BaseMessage(text=INITIAL_MESSAGE),
            prompt_preamble=PROMPT_PREAMBLE,
            track_bot_sentiment=True,
        )
    )

    custom_synthesizer = AzureSynthesizer(
        AzureSynthesizerConfig(
            sampling_rate=DEFAULT_SAMPLING_RATE,
            audio_encoding=DEFAULT_AUDIO_ENCODING,
        )
    )

    general_transcriber_config: TranscriberConfig = TranscriberConfig(
        sampling_rate=DEFAULT_SAMPLING_RATE,
        audio_encoding=DEFAULT_AUDIO_ENCODING,
        chunk_size=DEFAULT_CHUNK_SIZE,
        endpointing_config=PunctuationEndpointingConfig(),
    )

    return InboundCallServer(
        twilio_config=twilio_config,
        transcriber_config=general_transcriber_config,
        agent_config=custom_agent.get_agent_config(),
        synthesizer_config=custom_synthesizer.get_synthesizer_config(),
    )

    return StreamingConversation(
        events_manager=custom_events_manager,
        output_device=output_device,
        transcriber=custom_transcriber,
        agent=custom_agent,
        synthesizer=custom_synthesizer,
        logger=logger,
    )
