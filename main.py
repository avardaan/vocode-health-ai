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


# async def main():
#     (
#         microphone_input,
#         speaker_output,
#     ) = create_streaming_microphone_input_and_speaker_output(use_default_devices=False)
#     await inbound_call_server.start()
#     print("Conversation started, press Ctrl+C to end")
#     signal.signal(
#         signal.SIGINT, lambda _0, _1: asyncio.create_task(inbound_call_server.terminate())
#     )
#     while inbound_call_server.is_active():
#         chunk = await microphone_input.get_audio()
#         inbound_call_server.receive_audio(chunk)


if __name__ == "__main__":
    inbound_call_server = create_inbound_call_server()
    inbound_call_server.run(port=3000)
