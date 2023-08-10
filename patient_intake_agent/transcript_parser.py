import os
import openai
from patient_intake_agent.constants import PATIENT_DATA_JSON


def get_patient_data_from_transcript(call_transcript: str):
    openai.api_key = os.getenv("OPENAI_API_KEY")

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": f"""You will be provided with an unstructured call transcript between a patient 
              intake bot agent and a human. You will also be given an output JSON shape with empty values. 
              Your task is to parse the call transcript and output a JSON in the desired shape with the 
              appropriate values filled from the human\'s responses. Values that are not provided by the 
              human may remain None.\nOutput JSON shape - {PATIENT_DATA_JSON}""",
            },
            {
                "role": "user",
                "content": {call_transcript},
            },
        ],
        temperature=0,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
    )
    return response
