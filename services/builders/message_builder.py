from models.message import EmailMessage


class MessageBuilder:
    def build(self, webhook, mlo) -> EmailMessage:
        subject = "A prospect just completed a quiz in your VA Loan Educator app!"
        body = (
            f"Hey, {mlo.first_name}!\n"
            "Someone has just completed a quiz in your VA Loan Educator. "
            "You might want to contact that prospect directly. "
            "Here’s their contact information: \n"
            f"Name: {webhook.user_name}\n"
            f"Email: {webhook.user_email}\n"
            f"Score: {webhook.user_percent_marks}%\n\n"
            "--\n\n"
            "Best regards,\n\n"
            "VA Loan Educator team"
        )

        return EmailMessage(
            to_email=mlo.email,
            body=body,
            subject=subject
        )


