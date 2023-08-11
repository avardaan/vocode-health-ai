import os
from twilio.rest import Client
from patient_intake_agent.logger import logger

# TODO: IMPROVE ERROR HANDLING
def send_appointment_sms(to_number: str, to_name: str, appointment: dict):
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    twilio_client = Client(account_sid, auth_token)

    body = f"""Hi {to_name},\nYour appointment with Dr. {appointment.get("provider")} is confirmed for {appointment.get("date")} at {appointment.get("time")}."""

    try:
        message = twilio_client.messages.create(
            body=str(body),
            from_=os.getenv("TWILIO_SMS_FROM"),
            to=str(to_number),
        )
    except Exception as e:
        logger.error(f"Error in twilio_client.messages.create - {e}")
    finally:
        logger.info(
            f"SMS event status:{message.status} to:{message.to} body:{message.body}"
        )
