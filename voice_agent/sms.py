import os
from twilio.rest import Client
from voice_agent.logger import logger


# TODO: IMPROVE ERROR HANDLING
def send_appointment_sms(to_number: str, to_name: str, appointment: dict):
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    twilio_client = Client(account_sid, auth_token)

    appt_provider = appointment.get("provider")
    appt_date = appointment.get("date")
    appt_time = appointment.get("time")

    # validate inputs
    if not to_number:
        logger.error("to_number is invalid")
        return
    if not to_name:
        logger.error("to_name is invalid")
        return
    if not appt_provider or not appt_date or not appt_time:
        logger.error("appointment data is invalid")
        return

    body = f"""Hi {to_name},\nYour appointment with {appt_provider} is confirmed for {appt_date} at {appt_time}."""

    try:
        message = twilio_client.messages.create(
            body=str(body),
            from_=os.getenv("TWILIO_SMS_FROM"),
            to=str(to_number),
        )
    except Exception as e:
        logger.error(f"Error in twilio_client.messages.create - {e}")
    else:
        logger.info(
            f"SMS event status:{message.status} to:{message.to} body:{message.body}"
        )
