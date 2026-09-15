import smtplib
import datetime as dt
import random
import os
from dotenv import load_dotenv

# Load variables from .env file (create this file locally, never commit it)
load_dotenv()

EMAIL = os.getenv("EMAIL_ADDRESS")
PASSWORD = os.getenv("EMAIL_APP_PASSWORD")
TO_ADDRESS = os.getenv("TO_ADDRESS")

def send_motivation_email():
    if not EMAIL or not PASSWORD or not TO_ADDRESS:
        raise ValueError(
            "Missing required environment variables. "
            "Make sure EMAIL_ADDRESS, EMAIL_APP_PASSWORD and TO_ADDRESS are set in your .env file."
        )

    with open("quotes.txt", "r") as file:
        quote = random.choice(file.readlines()).strip()

    connection = smtplib.SMTP("smtp.gmail.com", 587)
    connection.starttls()
    connection.login(EMAIL, PASSWORD)
    connection.sendmail(
        from_addr=EMAIL,
        to_addrs=TO_ADDRESS,
        msg=f"Subject: Monday Motivation\n\n{quote}",
    )
    connection.close()
    print("Motivation email sent successfully!")


if __name__ == "__main__":
    now = dt.datetime.now()
    weekday = now.weekday()  # Monday = 0, Tuesday = 1, ...

    if weekday == 0:
        send_motivation_email()
    else:
        print("Today is not the scheduled day. No email sent.")
