from pydantic import BaseModel
from pymongo import IndexModel


def create_mongo_index(columns: list) -> list:
    return [
        IndexModel([(column.name, column.sorting_order)],
                   background=True, name=column.name)
        for column in columns
    ]


def ascending(column_name: str):
    return MongoColumn(name=column_name, sorting_order=1)


def descending(column_name: str):
    return MongoColumn(name=column_name, sorting_order=-1)


def geo_2dsphere(colum_name):
    return MongoColumn(name=colum_name, sorting_order="2dsphere")


class MongoColumn(BaseModel):
    name: str
    sorting_order: int | str
