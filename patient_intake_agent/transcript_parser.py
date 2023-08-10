from langchain import OpenAI, PromptTemplate
from langchain.output_parsers import PydanticOutputParser
from patient_intake_agent.constants import PatientData


def get_patient_data_from_transcript(call_transcript: str) -> PatientData:
    model_name = "text-davinci-003"
    temperature = 0.0
    model = OpenAI(model_name=model_name, temperature=temperature)
    # Set up a parser + inject instructions into the prompt template.
    patient_data_parser = PydanticOutputParser(pydantic_object=PatientData)
    prompt = PromptTemplate(
        template="Based on the provided call transcript between, fill the retrieved values, and leave the rest as None.\n{format_instructions}\n{transcript}\n",
        input_variables=["transcript"],
        partial_variables={
            "format_instructions": patient_data_parser.get_format_instructions()
        },
    )

    prompt_input = prompt.format_prompt(transcript=call_transcript)
    output = model(prompt_input.to_string())
    parsed_patient_data: PatientData = patient_data_parser.parse(output)
    return parsed_patient_data
