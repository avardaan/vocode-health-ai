from pydantic import BaseModel
from typing import Optional


class _Insurance(BaseModel):
    payer_name: Optional[str]
    member_id: Optional[str]


class _Referral(BaseModel):
    has_referral: Optional[bool]
    to_provider: Optional[str]


class PatientData(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    insurance: Optional[_Insurance]
    referral: Optional[_Referral]
    chief_complaint: Optional[str]


INITIAL_MESSAGE = "Hello! I am Vardaan, your intake agent. \
  To help you get the care you need, I will be asking you a series of questions to process your registration. \
    Once you are registered, I will help you schedule an appointment with a doctor. To begin, please say ok."

AGENT_GOAL_DESCRIPTION = (
    "Retrieve patient information and schedule an appointment with a doctor."
)

PROMPT_PREAMBLE = f"""
        The AI is a friendly phone bot built for information intake via inbound calls from patients.

Here is the context for the call:
Intended goal: {AGENT_GOAL_DESCRIPTION}
Information to be collected: {PatientData().dict()}
        """
