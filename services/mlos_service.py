import asyncio

from bson.objectid import ObjectId

from infrastructure_exceptions import (
    InvalidRequestException,
    NotFoundException,
    ThirdPartyServiceException,
)
from log import logger
from models.filtering import MLOFiltering
from models.mlo import (
    MLO,
    MLOCount,
    MLOIn,
    MLOProspect,
    MLOStatus,
    MLOStatusIn,
    MLOUpdate,
    PublicMLOWebAppInfo,
    QRcodeMLO,
)
from models.page import MLOPaging, Page
from models.uploaded_file import SharedUploadedFile


class MLOsService:
    ...
    # def __init__(
    #         self,
    #         mlos_geolocation_service,
    #         qrcode_service,
    #         themes_service,
    #         files_service,
    #         page_service,
    #         locations_service,
    #         repository,
    #         web_app_url_builder,
    #         app_deep_links_gateway,
    #         cache_gateway
    # ):
    #     self.qrcode_service = qrcode_service
    #     self.files_service = files_service
    #     self.page_service = page_service
    #     self.locations_service = locations_service
    #     self.repository = repository
    #     self.mlos_geolocation_service = mlos_geolocation_service
    #     self.themes_service = themes_service
    #     self.web_app_url_builder = web_app_url_builder
    #     self.app_deep_links_gateway = app_deep_links_gateway
    #     self.cache_gateway = cache_gateway
    #
    # async def change_headshot(self, mlo_id: ObjectId, file, principal=None):
    #     mlo = await self.__get_mlo(mlo_id)
    #     uploaded_file = await self.files_service.upload_public_file(file)
    #     await self.files_service.delete_public_orphan_file(mlo.headshot)
    #     await self.repository.change_headshot(mlo_id, uploaded_file)
    #     if mlo.status == MLOStatus.PUBLISHED:
    #         mlo.headshot = uploaded_file
    #     return uploaded_file
    #
    # async def get_headshot(self, mlo_id: ObjectId, principal=None) -> MLO:
    #     mlo = await self.repository.get(mlo_id)
    #     if not mlo:
    #         raise NotFoundException
    #     mlo.headshot = self.share_headshot(mlo.headshot)
    #     return mlo
    #
    # async def get_headshot_by_web_app_id(self, web_app_id: str, principal=None) -> MLO:
    #     mlo = await self.repository.find_by_web_app_id(web_app_id)
    #     if not mlo or mlo.status != MLOStatus.PUBLISHED:
    #         raise NotFoundException
    #     mlo.headshot = self.share_headshot(mlo.headshot)
    #     return mlo
    #
    # async def create_mlo(self, model: MLOIn, principal=None) -> MLO:
    #     exists_email_mlo = await self.repository.find_strict_by_email(model.email)
    #     await self.__check_in_collisions(model, exists_email_mlo)
    #     mlo = MLO.model_validate(model)
    #     mlo.web_app_id = model.generate_web_app_id()
    #     mlo.status = MLOStatus.PROSPECT
    #     if not exists_email_mlo:
    #         mlo.id = await self.repository.create(mlo)
    #     else:
    #         mlo.id = exists_email_mlo.id
    #         await self.repository.update(mlo)
    #
    #     self.cache_gateway.book(mlo.email, mlo.zip_code)
    #     mlo.headshot = self.share_headshot(mlo.headshot)
    #     await self.assemble_theme(mlo)
    #     return mlo
    #
    # async def count(self, filtering: MLOFiltering, principal=None) -> MLOCount:
    #     return MLOCount(count=await self.repository.count(filtering))
    #
    # async def get_mlo(self, mlo_id: ObjectId, principal=None) -> MLO:
    #     mlo = await self.repository.get(mlo_id)
    #     mlo.headshot = self.share_headshot(mlo.headshot)
    #     await self.assemble_theme(mlo)
    #     return mlo
    #
    # async def get_mlo_by_web_app_id(self, web_app_id: str, principal=None) -> QRcodeMLO:
    #     mlo = await self.repository.find_by_web_app_id(web_app_id)
    #     if not mlo or mlo.status not in (MLOStatus.PUBLISHED,) or mlo.web_app_id is None:
    #         raise NotFoundException
    #     mlo.qrcode = await self.qrcode_service.get_qrcode(mlo.app_deep_link)
    #     mlo.headshot = self.share_headshot(mlo.headshot)
    #     return mlo
    #
    # async def __create_qrcode(self, mlo):
    #     if not mlo.app_deep_link:
    #         return None
    #     logo = mlo.headshot.link if (mlo.headshot and mlo.headshot.link) else None
    #     link = mlo.app_deep_link
    #     color = mlo.theme.name if mlo.theme else None
    #     return await self.qrcode_service.create_qrcode(
    #         logo, link, color
    #     )
    #
    # async def update_mlo(self, mlo_id: ObjectId, updated_mlo: MLOUpdate, principal=None) -> MLO:
    #     mlo = await self.__get_mlo(mlo_id)
    #     old_theme_id = mlo.theme_id
    #     old_first_name = mlo.first_name
    #     old_last_name = mlo.last_name
    #     await self.__check_update_collisions(mlo, updated_mlo)
    #     if mlo.zip_code != updated_mlo.zip_code:
    #         await self.locations_service.change_location(mlo.zip_code, updated_mlo.zip_code, mlo.id)
    #         await self.mlos_geolocation_service.change_mlo_geolocation(updated_mlo.zip_code, mlo.id)
    #     mlo.assign_request(updated_mlo)
    #     mlo.headshot = self.share_headshot(mlo.headshot)
    #     tasks = [
    #         self.repository.update(mlo),
    #         self.assemble_theme(mlo)
    #     ]
    #     await asyncio.gather(*tasks)
    #
    #     if old_theme_id != updated_mlo.theme_id:
    #         await self.qrcode_service.delete_qrcode(mlo.app_deep_link)
    #         await self.__create_qrcode(mlo)
    #
    #     if (mlo.first_name != old_first_name) or (mlo.last_name != old_last_name):
    #         await self.__upsert_app_deep_link(mlo)
    #     return mlo
    #
    # async def change_status(
    #         self, mlo_id: ObjectId, status_model: MLOStatusIn, principal=None) -> MLO:
    #     status = status_model.status
    #
    #     mlo = await self.__get_mlo(mlo_id)
    #     await self.__check_status_collisions(mlo, status)
    #
    #     match status:
    #         case MLOStatus.UNPUBLISHED:
    #             await self.locations_service.un_claim_location(mlo.zip_code)
    #             await self.mlos_geolocation_service.delete_mlo_geolocation(mlo.id)
    #             mlo.zip_code = None
    #             await self.__invalidate_app_deep_link(mlo)
    #             mlo.app_deep_link = None
    #             await self.qrcode_service.delete_qrcode(mlo.app_deep_link)
    #
    #         case MLOStatus.PUBLISHED:
    #             if mlo.app_deep_link is None:
    #                 link = await self.__upsert_app_deep_link(mlo)
    #                 mlo.app_deep_link = link
    #                 await self.__soft_create_mlo_geolocation(mlo.zip_code, mlo.id)
    #         case _:
    #             errors = {
    #                 "mlo_status": [
    #                     {
    #                         "message": "Unsupported status",
    #                         "key": "error_cannot_change_mlo_status"
    #                     }
    #                 ]
    #             }
    #             raise InvalidRequestException(errors)
    #
    #     mlo.status = status
    #     mlo.headshot = self.share_headshot(mlo.headshot)
    #     tasks = [
    #         self.repository.update(mlo),
    #         self.assemble_theme(mlo)
    #     ]
    #     await asyncio.gather(*tasks)
    #     if status == MLOStatus.PUBLISHED:
    #         await self.__create_qrcode(mlo)
    #     return mlo
    #
    # async def __soft_create_mlo_geolocation(self, zip_code: str, mlo_id: ObjectId):
    #     async with asyncio.TaskGroup() as tg:
    #         mlo_geolocation_task = tg.create_task(
    #             self.mlos_geolocation_service.find_by_mlo_id(mlo_id)
    #         )
    #         zip_code_geolocation_task = tg.create_task(
    #             self.mlos_geolocation_service.find_by_zip_code(zip_code)
    #         )
    #     mlo_geolocation = mlo_geolocation_task.result()
    #     zip_code_geolocation = zip_code_geolocation_task.result()
    #
    #     if not (mlo_geolocation or zip_code_geolocation):
    #         return await self.mlos_geolocation_service.create_mlo_geolocation(zip_code, mlo_id)
    #     if zip_code_geolocation.mlo_id != mlo_id or mlo_geolocation.zip_code != zip_code:
    #         errors = {
    #             "mlo_geolocation": [
    #                 {
    #                     "message": "Geolocation already taken",
    #                     "key": "error_already_taken"
    #                 }
    #             ]
    #         }
    #         raise InvalidRequestException(errors)
    #     return mlo_geolocation
    #
    # async def delete_mlo(self, mlo_id: ObjectId, principal=None) -> None:
    #     mlo = await self.__get_mlo(mlo_id)
    #     if mlo.status in {MLOStatus.PUBLISHED}:
    #         error = {
    #             "mlo_delete": [
    #                 {"message": "MLO cannot be deleted", "key": "error_cannot_delete"}
    #             ]
    #         }
    #         raise InvalidRequestException(error)
    #
    #     tasks = [
    #         self.locations_service.un_claim_location(mlo.zip_code),
    #         self.repository.delete(mlo.id),
    #         self.__remove_mlo_headshot(mlo)
    #     ]
    #     await asyncio.gather(*tasks)
    #
    # async def get_web_app_info(self, mlo_id: ObjectId, principal=None) -> PublicMLOWebAppInfo:
    #     mlo = await self.__get_mlo(mlo_id)
    #     if mlo.status not in {MLOStatus.PUBLISHED} or mlo.web_app_id is None:
    #         error = {
    #             "mlo_web_app_info": [
    #                 {"message": "Can't get MLO web app info", "key": "error_web_app_info"}
    #             ]
    #         }
    #         raise InvalidRequestException(error)
    #
    #     await self.assemble_theme(mlo)
    #     url = self.web_app_url_builder.build(mlo.web_app_id)
    #     return PublicMLOWebAppInfo(url=url, theme=mlo.theme)
    #
    # async def __upsert_app_deep_link(self, mlo) -> str:
    #     shared_image = self.files_service.share_public_file(mlo.headshot)
    #     try:
    #         return await self.app_deep_links_gateway.upsert_deep_link(mlo, shared_image)
    #     except (DeepLinkServiceException, DeepLinkValidationException) as e:
    #         logger.critical(
    #             "Unable to create app deep link for MLO %s", mlo.id, exc_info=e
    #         )
    #
    #         # We don't really care about exception type for now because
    #         # any exception is a show stopper and MLO can't be published.
    #         raise ThirdPartyServiceException({
    #             "app_deep_link": [
    #                 {"message": "Can't upsert deep link",
    #                  "key": "error_upsert_deep_link"}
    #             ]
    #         }) from e
    #
    # async def __invalidate_app_deep_link(self, mlo) -> str:
    #     try:
    #         return await self.app_deep_links_gateway.invalidate_deep_link(mlo)
    #     except Exception as e:
    #         # We don't really care if something went wrong while invalidating a deep link.
    #         # Reasons:
    #         # - if we try to create a deep link with the same parameters again then existing
    #         #   one will be returned
    #         # - dangling deep link don't really make any harm because app won't be able to
    #         #   get any info with dangling deep link as backend is aware of `published` status.
    #         logger.error(
    #             f"Unable to invalidate app deep link for MLO {mlo.id}", exc_info=e
    #         )
    #
    # async def __remove_mlo_headshot(self, mlo):
    #     if not mlo.headshot:
    #         return
    #     await self.files_service.delete_public_orphan_file(mlo.headshot)
    #
    # async def __get_mlo(self, mlo_id: ObjectId):
    #     mlo = await self.repository.get(mlo_id)
    #     if not mlo:
    #         raise NotFoundException
    #     return mlo
    #
    # async def get_page(self, paging: MLOPaging, principal=None) -> Page:
    #     mlos_page = await self.page_service.get_page(
    #         paging,
    #         self.repository.get_page,
    #         self.repository.count,
    #         paging.filtering
    #     )
    #     for mlo in mlos_page.items:
    #         mlo.headshot = self.share_headshot(mlo.headshot)
    #     return mlos_page
    #
    # def share_headshot(self, headshot) -> None | SharedUploadedFile:
    #     if not headshot:
    #         return None
    #     return self.files_service.share_public_file(headshot)
    #
    # async def share_qrcode(self, mlo) -> None:
    #     if mlo.qrcode and mlo.qrcode.uploaded_file:
    #         mlo.qrcode = await self.files_service.share_file(mlo.qrcode.uploaded_file)
    #
    # async def assemble_theme(self, mlo) -> None:
    #     mlo.theme = await self.themes_service.get_theme(mlo.theme_id)
    #
    # async def __check_in_collisions(self, mlo: MLOIn, taken_email_mlo: MLO):
    #     tasks = [
    #         self.repository.find_by_nmls(mlo.nmls_license),
    #         self.locations_service.get_location_by_zip_code(mlo.zip_code)
    #     ]
    #     collisions = await asyncio.gather(*tasks)
    #     booked_zip_code = self.cache_gateway.is_booked(mlo.email, mlo.zip_code)
    #     taken_nmls_mlo = collisions[0]
    #     zip_code = collisions[1]
    #
    #     if (taken_email_mlo and taken_email_mlo.status == MLOStatus.PROSPECT
    #             and taken_nmls_mlo and taken_nmls_mlo.status == MLOStatus.PROSPECT
    #             and not booked_zip_code):
    #         return
    #     errors = {}
    #     if taken_email_mlo and taken_email_mlo.status != MLOStatus.PROSPECT:
    #         errors["email"] = [
    #             {"message": "Email is already taken", "key": "error_belongs_to_another"}
    #         ]
    #     if taken_nmls_mlo and taken_nmls_mlo.status != MLOStatus.PROSPECT:
    #         errors["nmls_license"] = [
    #             {"message": "NMLS license is already taken", "key": "error_belongs_to_another"}
    #         ]
    #     if booked_zip_code:
    #         errors["zip_code"] = [
    #             {
    #                 "message": "ZipCode is already booked by another",
    #                 "key": "error_booked_by_another"
    #             }
    #         ]
    #     if zip_code and zip_code.is_claimed:
    #         errors["zip_code"] = [
    #             {"message": "ZipCode is already taken", "key": "error_belongs_to_another"}
    #         ]
    #     if not zip_code:
    #         errors["zip_code"] = [
    #             {"message": "ZipCode is not valid", "key": "error_invalid_input"}
    #         ]
    #     if errors:
    #         raise InvalidRequestException(errors)
    #
    # async def validate_prospect(self, mlo_prospect: MLOProspect, principal=None) -> None:
    #     tasks = [
    #         self.repository.find_strict_by_email(mlo_prospect.email),
    #         self.repository.find_by_nmls(mlo_prospect.nmls_license),
    #         self.locations_service.get_location_by_zip_code(mlo_prospect.zip_code)
    #     ]
    #     collisions = await asyncio.gather(*tasks)
    #     email_collision = collisions[0]
    #     nmls_collision = collisions[1]
    #     zip_code = collisions[2]
    #     booked_zip_code = self.cache_gateway.is_booked(
    #         mlo_prospect.email, mlo_prospect.zip_code)
    #     errors = {}
    #
    #     if email_collision and email_collision.status != MLOStatus.PROSPECT:
    #         errors["email"] = [
    #             {"message": "Email is already taken", "key": "error_belongs_to_another"}
    #         ]
    #     if nmls_collision and nmls_collision.status != MLOStatus.PROSPECT:
    #         errors["nmls_license"] = [
    #             {"message": "NMLS license is already taken", "key": "error_belongs_to_another"}
    #         ]
    #     if zip_code and zip_code.is_claimed:
    #         errors["zip_code"] = [
    #             {"message": "ZipCode is already taken", "key": "error_belongs_to_another"}
    #         ]
    #     if not zip_code:
    #         errors["zip_code"] = [
    #             {"message": "ZipCode is not valid", "key": "error_invalid_input"}
    #         ]
    #     if booked_zip_code:
    #         errors["zip_code"] = [
    #             {
    #                 "message": "ZipCode is already booked by another",
    #                 "key": "error_booked_by_another"
    #             }
    #         ]
    #     if errors:
    #         raise InvalidRequestException(errors)
    #
    # async def __check_update_collisions(self, mlo: MLO, update_mlo: MLOUpdate):
    #     tasks = [
    #         self.repository.find_strict_by_email(update_mlo.email),
    #         self.repository.find_by_nmls(update_mlo.nmls_license),
    #         self.locations_service.get_location_by_zip_code(update_mlo.zip_code),
    #         self.repository.find_by_web_app_id(update_mlo.web_app_id)
    #     ]
    #     collisions = await asyncio.gather(*tasks)
    #     booked_zip_code = self.cache_gateway.is_booked(
    #         update_mlo.email, update_mlo.zip_code)
    #
    #     email_collision = collisions[0]
    #     nmls_collision = collisions[1]
    #     zip_code_collision = collisions[2]
    #     web_app_id_collision = collisions[3]
    #     errors = {}
    #
    #     if email_collision and email_collision.id != mlo.id:
    #         errors["email"] = [
    #             {"message": "Email is already taken", "key": "error_belongs_to_another"}
    #         ]
    #     if nmls_collision and nmls_collision.id != mlo.id:
    #         errors["nmls_license"] = [
    #             {"message": "NMLS license is already taken", "key": "error_belongs_to_another"}
    #         ]
    #     if not zip_code_collision and mlo.status != MLOStatus.UNPUBLISHED:
    #         errors["zip_code"] = [
    #             {"message": "ZipCode is not valid", "key": "error_invalid_input"}
    #         ]
    #     if not zip_code_collision and mlo.status == MLOStatus.UNPUBLISHED and update_mlo.zip_code:
    #         errors["zip_code"] = [
    #             {"message": "ZipCode is not valid", "key": "error_invalid_input"}
    #         ]
    #     if (zip_code_collision and zip_code_collision.is_claimed
    #             and mlo.zip_code != update_mlo.zip_code):
    #         errors["zip_code"] = [
    #             {"message": "ZipCode is already taken", "key": "error_belongs_to_another"}
    #         ]
    #
    #     if web_app_id_collision and mlo.web_app_id != update_mlo.web_app_id:
    #         errors["web_app_id"] = [
    #             {"message": "Web app id is already taken", "key": "error_belongs_to_another"}
    #         ]
    #     if booked_zip_code:
    #         errors["zip_code"] = [
    #             {
    #                 "message": "ZipCode is already booked by another",
    #                 "key": "error_booked_by_another"
    #             }
    #         ]
    #     if errors:
    #         raise InvalidRequestException(errors)
    #
    # async def __check_status_collisions(self, mlo: MLO, status: MLOStatus):
    #     errors = {}
    #     match status:
    #         case MLOStatus.UNPUBLISHED:
    #             if mlo.status in {MLOStatus.DRAFT, MLOStatus.UNPUBLISHED}:
    #                 errors["mlo_status"] = [
    #                     {
    #                         "message": "Status cannot be changed",
    #                         "key": "error_cannot_change_mlo_status"
    #                     }
    #                 ]
    #         case MLOStatus.PUBLISHED:
    #             if mlo.status in {MLOStatus.PUBLISHED} or not mlo.zip_code:
    #                 errors["mlo_status"] = [
    #                     {
    #                         "message": "Status cannot be changed",
    #                         "key": "error_cannot_change_mlo_status"
    #                     }
    #                 ]
    #         case MLOStatus.DRAFT:
    #             errors["mlo_status"] = [
    #                 {
    #                     "message": "Setting 'draft' status is not supported",
    #                     "key": "error_cannot_change_mlo_status"
    #                 }
    #             ]
    #
    #     if errors:
    #         raise InvalidRequestException(errors)
