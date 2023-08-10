import os
from dotenv import load_dotenv
import asyncio
import signal
from fastapi import FastAPI
from vocode.helpers import create_streaming_microphone_input_and_speaker_output
from vocode.streaming.streaming_conversation import StreamingConversation
import vocode

from patient_intake_agent.inbound_call_engine import create_inbound_telephony_server

# load environment variables from .env file
load_dotenv()

http_server = FastAPI(docs_url=None)

vocode.setenv(
    BASE_URL=os.getenv("BASE_URL"),
    OPENAI_API_KEY=os.getenv("OPENAI_API_KEY"),
    DEEPGRAM_API_KEY=os.getenv("DEEPGRAM_API_KEY"),
    AZURE_SPEECH_KEY=os.getenv("AZURE_SPEECH_KEY"),
    AZURE_SPEECH_REGION=os.getenv("AZURE_SPEECH_REGION"),
)

if __name__ == "__main__":
    inbound_call_server = create_inbound_telephony_server()
    http_server.include_router(inbound_call_server.get_router())
