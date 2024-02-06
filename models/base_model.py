from bson.objectid import ObjectId as BsonObjectId
from pydantic_core import core_schema


class PyObjectId(BsonObjectId):
    @classmethod
    def __get_pydantic_json_schema__(cls, core_schema, handler):
        json_schema = {}
        json_schema.update(type="string")
        return json_schema

    @classmethod
    def validate(cls, v, *args):
        if isinstance(v, BsonObjectId):
            return v
        if not BsonObjectId.is_valid(v):
            error = "ObjectId required"
            raise ValueError(error)
        return BsonObjectId(v)

    @classmethod
    def __get_pydantic_core_schema__(cls, source, handler):
        return core_schema.general_plain_validator_function(cls.validate)


class PydanticObjectId(BsonObjectId):
    @classmethod
    def __get_pydantic_json_schema__(cls, core_schema, handler):
        json_schema = {}
        json_schema.update(type="string")
        return json_schema

    @classmethod
    def validate(cls, v, *args):
        if not isinstance(v, BsonObjectId):
            error = "ObjectId required"
            raise ValueError(error)
        return v

    @classmethod
    def __get_pydantic_core_schema__(cls, source, handler):
        return core_schema.general_plain_validator_function(cls.validate)


class PyObjectIdOut(BsonObjectId):
    @classmethod
    def __get_pydantic_json_schema__(cls, core_schema, handler):
        json_schema = {}
        json_schema.update(type="string")
        return json_schema

    @classmethod
    def validate(cls, v, *args):
        if not isinstance(v, BsonObjectId):
            error = "ObjectId required"
            raise ValueError(error)
        return str(v)

    @classmethod
    def __get_pydantic_core_schema__(cls, source, handler):
        return core_schema.general_after_validator_function(
            cls.validate,
            core_schema.str_schema(),
        )
