PATIENT_DATA_TO_COLLECT = {
    "first_name": None,
    "last_name": None,
    "insurance": {
        "payer_name": None,
        "member_id": None,
    },
    "referral": {
        "has_referral": None,
        "to_provider": None,
    },
    "chief_complaint": None,
    "address": {
        "street": None,
        "unit": None,
        "city": None,
        "state": None,
        "zip": None,
    },
    "contact": {
        "phone": None,
        "email": None,
    },
}

AVAILABLE_APPOINTMENTS = [
    {
        "provider": "John Doe",
        "date": "2023-09-01",
        "time": "10:00 AM",
    },
    {
        "provider": "Jane Doe",
        "date": "2023-09-01",
        "time": "11:00 AM",
    },
]

PATIENT_DATA_WITH_APPOINTMENT = {
    **PATIENT_DATA_TO_COLLECT,
    "appointment": {
        "provider": None,
        "date": None,
        "time": None,
    },
}

# TODO: derive programmatically from PATIENT_DATA_TO_COLLECT
PATIENT_DATA_FIELDS = [
    "first_name",
    "last_name",
    "insurance_payer_name",
    "insurance_member_id",
    "referral_has_referral",
    "referral_to_provider",
    "chief_complaint",
    "address_street",
    "address_unit",
    "address_city",
    "address_state",
    "address_zip",
    "contact_phone",
    "contact_email",
]


INITIAL_MESSAGE = "Hello! I am Vardaan, your intake agent. \
  To help you get the care you need, I will be asking you a series of questions to process your registration. \
    Once you are registered, I will help you schedule an appointment with a doctor. To begin, please say ok."

AGENT_GOAL_DESCRIPTION = f"""Retrieve patient information by going through the provided fields. Do not stop until you 
have collected information about all the fields Once all fields are retrieved,
help the patient schedule an appointment with a doctor."""

# preamble based on vocode InformationRetrievalAgent
PROMPT_PREAMBLE = f"""
    You are a friendly phone bot built for information intake via inbound calls from patients.
    Step 1: You will go through a list of fields and collect information about each field from the user.
    Step 2: Once all fields have been collected, help the user schedule an appointment with a doctor.
    You will not stop until you have collected information about all the fields and scheduled an appointment. After each response by the user,
    you will ask the next question in the list until all fields have been collected.

    Here is the context for the call:
    Intended goal: {AGENT_GOAL_DESCRIPTION}
    Information to be collected in order sequentially: {PATIENT_DATA_TO_COLLECT}
    Available appointments with doctors: {AVAILABLE_APPOINTMENTS}

    Do not answer questions that are not relevant to the  intended goal. If the caller is not cooperative, 
    gently bring them back on track.
"""
