import os
import openai


def get_patient_data_from_transcript(call_transcript: str, structured_output: dict):
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
              human may remain None.\nOutput JSON shape - {structured_output}""",
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
