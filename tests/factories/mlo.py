import random

from bson.objectid import ObjectId
from faker import Faker

from models.mlo import MLO, MLOStatus


class MLOFactory:
    def __init__(self):
        self.faker = Faker()

    async def generic(
        self,
        status: MLOStatus | None = None,
        theme_id=None,
        zip_code=None,
        app_deep_link=None
    ):
        status = status or MLOStatus.DRAFT

        zip_codes = ["10001", "90001", "60601", "77001", "30301", "19101",
                     "97201", "02101", "94101", "48201", "89101", "84101",
                     "04662", "14738", "68023", "17563", "92704", "48637", "84003"]
        if zip_code:
            zip_codes = [zipcode for zipcode in zip_codes if zipcode != zip_code]
        return MLO(
            status=status,
            email=self.faker.email(),
            first_name=self.faker.first_name(),
            last_name=self.faker.last_name(),
            headshot=None,
            phone_number=str(self.faker.phone_number()),
            nmls_license=str(self.faker.random_number(digits=6)),
            web_app_id=self.faker.city(),
            app_deep_link=app_deep_link,
            website=self.faker.url(),
            zip_code=zip_code or random.choice(zip_codes),
            theme_id=theme_id or ObjectId()
        )
