import os
from dotenv import load_dotenv
import asyncio
import signal
from vocode.helpers import create_streaming_microphone_input_and_speaker_output
from vocode.streaming.streaming_conversation import StreamingConversation
import vocode

from patient_intake_agent.inbound_call_engine import create_inbound_call_server

# load environment variables from .env file
load_dotenv()

vocode.api_key = os.getenv("VOCODE_API_KEY")
vocode.setenv(
    OPENAI_API_KEY=os.getenv("OPENAI_API_KEY"),
    DEEPGRAM_API_KEY=os.getenv("DEEPGRAM_API_KEY"),
    AZURE_SPEECH_KEY=os.getenv("AZURE_SPEECH_KEY"),
    AZURE_SPEECH_REGION=os.getenv("AZURE_SPEECH_REGION"),
)

if __name__ == "__main__":
    inbound_call_server = create_inbound_call_server()
    inbound_call_server.run(port=3000)
