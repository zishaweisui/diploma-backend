from pydantic import BaseModel, EmailStr


class EmailMessage(BaseModel):
    to_email: EmailStr | None
    body: str
    subject: str
