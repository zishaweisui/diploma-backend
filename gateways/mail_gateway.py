import base64
from email.message import EmailMessage

from google.oauth2 import service_account
from googleapiclient.discovery import build


class GmailGateway:
    def __init__(self, credentials_file_path, scopes: list, sender_email: str):
        self.credentials = service_account.Credentials.from_service_account_file(
            filename=credentials_file_path,
            scopes=scopes,
            subject=sender_email
        )
        self.sender_email = sender_email
        self.service = self.__build_gmail_service()
        self.user_id = "me"

    def __build_gmail_service(self):
        return build("gmail", "v1", credentials=self.credentials)

    def send_email(self, email_message) -> None:
        message = self.__create_message(email_message)
        print(f"dat is {message = }")
        try:
            self.service.users().messages().send(
                userId=self.user_id, body=message).execute()
            print("Email sent successfully!")
        except Exception as error:
            print(type(error))
            print(f"An error occurred: {error}")

    def __create_message(self, email_message) -> dict:
        message = EmailMessage()
        message.set_content(email_message.body)
        message["To"] = email_message.to_email
        message["From"] = self.sender_email
        message["Subject"] = email_message.subject
        message = {"raw": base64.urlsafe_b64encode(message.as_bytes()).decode()}
        print(f"dat is {message = }")
        return message
