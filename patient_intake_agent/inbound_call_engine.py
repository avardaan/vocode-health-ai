import os
from vocode.streaming.transcriber import *
from vocode.streaming.agent import *
from vocode.streaming.synthesizer import *
from vocode.streaming.models.transcriber import *
from vocode.streaming.models.agent import *
from vocode.streaming.models.synthesizer import *
from vocode.streaming.models.message import BaseMessage
from vocode.streaming.telephony.server.base import TelephonyServer, InboundCallConfig
from vocode.streaming.telephony.config_manager.in_memory_config_manager import (
    InMemoryConfigManager,
)
from vocode.streaming.models.telephony import TwilioConfig

from patient_intake_agent.constants import INITIAL_MESSAGE, PROMPT_PREAMBLE
from patient_intake_agent.logger import logger
from patient_intake_agent.events_manager import inbound_call_events_manager


def create_inbound_telephony_server() -> TelephonyServer:
    BASE_URL = os.getenv("BASE_URL")
    config_manager = InMemoryConfigManager()

    custom_twilio_config = TwilioConfig(
        account_sid=os.getenv("TWILIO_ACCOUNT_SID"),
        auth_token=os.getenv("TWILIO_AUTH_TOKEN"),
    )
    custom_transcriber_config = DeepgramTranscriberConfig(
        endpointing_config=PunctuationEndpointingConfig(),
        sampling_rate=DEFAULT_SAMPLING_RATE,
        audio_encoding=DEFAULT_AUDIO_ENCODING,
        chunk_size=DEFAULT_CHUNK_SIZE,
    )

    custom_agent_config = ChatGPTAgentConfig(
        model_name="gpt-3.5-turbo",
        temperature=1.0,
        max_tokens=512,
        allowed_idle_time_seconds=30,
        initial_message=BaseMessage(text=INITIAL_MESSAGE),
        prompt_preamble=PROMPT_PREAMBLE,
        generate_responses=True,
        # end_conversation_on_goodbye=True,
        allow_agent_to_be_cut_off=False,
        send_filler_audio=FillerAudioConfig(
            silence_threshold_seconds=FILLER_AUDIO_DEFAULT_SILENCE_THRESHOLD_SECONDS,
            use_phrases=False,
            use_typing_noise=True,
        ),
    )

    custom_synthesizer_config = AzureSynthesizerConfig(
        sampling_rate=DEFAULT_SAMPLING_RATE,
        audio_encoding=DEFAULT_AUDIO_ENCODING,
    )

    custom_inbound_call_config: InboundCallConfig = InboundCallConfig(
        url="/inbound",
        twilio_config=custom_twilio_config,
        transcriber_config=custom_transcriber_config,
        agent_config=custom_agent_config,
        synthesizer_config=custom_synthesizer_config,
    )

    return TelephonyServer(
        base_url=BASE_URL,
        config_manager=config_manager,
        inbound_call_configs=[custom_inbound_call_config],
        logger=logger,
        events_manager=inbound_call_events_manager,
    )
