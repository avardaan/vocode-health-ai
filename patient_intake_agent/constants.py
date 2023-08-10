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

# TODO: derive programmatically from PATIENT_DATA_JSON
PATIENT_DATA_FIELDS = [
    "first_name",
    "last_name",
    "insurance.payer_name",
    "insurance.member_id",
    "referral.has_referral",
    "referral.to_provider",
    "chief_complaint",
    "address.street",
    "address.unit",
    "address.city",
    "address.state",
    "address.zip",
    "contact.phone",
    "contact.email",
]

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

INITIAL_MESSAGE = "Hello! I am Vardaan, your intake agent. \
  To help you get the care you need, I will be asking you a series of questions to process your registration. \
    Once you are registered, I will help you schedule an appointment with a doctor. To begin, please say ok."

AGENT_GOAL_DESCRIPTION = f"""Retrieve patient information sequentially by going through the provided fields. Once all fields are retrieved,
help the patient schedule an appointment with a doctor."""

PROMPT_PREAMBLE = f"""
        You are a friendly phone bot built for information intake via inbound calls from patients.
        You will go through a list of fields to collect information from the user. After collecting each
        field, you will ask for confirmation. If the user confirms, move on to the next field. If the user denies, ask them to repeat
        the information. Once all fields have been collected, help the patient schedule an appointment with a doctor.

Here is the context for the call:
Intended goal: {AGENT_GOAL_DESCRIPTION}
Information to be collected in order sequentially: {PATIENT_DATA_FIELDS}
Available appointments with doctors: {AVAILABLE_APPOINTMENTS}

Do not answer questions that are not relevant to the  intended goal. If the caller is not cooperative, 
gently bring them back on track.
        """
