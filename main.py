import os
from fastapi import FastAPI
import vocode

from voice_agent.inbound_call_server import create_inbound_telephony_server

vocode.setenv(
    BASE_URL=os.getenv("BASE_URL"),
    OPENAI_API_KEY=os.getenv("OPENAI_API_KEY"),
    DEEPGRAM_API_KEY=os.getenv("DEEPGRAM_API_KEY"),
    AZURE_SPEECH_KEY=os.getenv("AZURE_SPEECH_KEY"),
    AZURE_SPEECH_REGION=os.getenv("AZURE_SPEECH_REGION"),
)

# init http server
app = FastAPI()
# create inbound call server
inbound_call_server = create_inbound_telephony_server()
# attach to http server
app.include_router(inbound_call_server.get_router())
