import json
import os
import openai
from patient_intake_agent.logger import logger


# TODO: ADD ERROR HANDLIING
def get_patient_data_from_transcript(call_transcript: str, structured_output: dict):
    openai.api_key = os.getenv("OPENAI_API_KEY")
    structured_output_json = json.dumps(structured_output)

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": f"You will be provided with an unstructured call transcript between a patient  \
                    intake bot agent and a human. You will also be given an output JSON shape with empty values. \
                    Your task is to parse the call transcript and output a JSON in the desired shape with the \
                    appropriate values filled from the human's responses. Values that are not provided by the \
                    human may remain None.\nOutput JSON shape - {structured_output_json}",
            },
            {
                "role": "user",
                "content": call_transcript,
            },
        ],
        # top_p=1,
        # frequency_penalty=0,
        # presence_penalty=0,
    )
    response_message: str = (
        response.choices[0].message.content if response.choices[0] else ""
    )
    parsed_json = json.loads(response_message)
    return parsed_json
