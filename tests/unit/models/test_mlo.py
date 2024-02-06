from bson import ObjectId

from models.mlo import MLOIn


class TestMLO:
    def test_generate_web_app_id(self):
        first_name = "))Al %%  Pa Chino  ^:"
        last_name = "(('''__ Bibe ;"
        nmls_license = "33333"
        mlo_attributes = {
            "first_name": first_name,
            "last_name": last_name,
            "headshot": None,
            "phone_number": "123456",
            "website": "http://www.yololo.biz/",
            "email": "yololo@example.com",
            "nmls_license": nmls_license,
            "zip_code": "90210",
            "web_app_id": None,
            "app_deep_link": None,
            "status": "draft",
            "theme_id": str(ObjectId())
        }
        mlo = MLOIn(**mlo_attributes)

        assert mlo.generate_web_app_id() == "alpachinobibe-33333"
