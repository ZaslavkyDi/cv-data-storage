from typing import Any

from motor import motor_asyncio

from cv_data_storage.config import get_mongodb_settings


class MongoClient:
    def __init__(
        self, database_name: str,
        collection_name: str,
        url: str | None = None,
    ) -> None:
        mongodb_url = url or get_mongodb_settings().url

        self._client = motor_asyncio.AsyncIOMotorClient(mongodb_url)
        self._database = self._client[database_name]
        self._collection = self._database[collection_name]

    @property
    def database(self):
        return self._database

    @property
    def collection(self):
        return self._database

    async def get_collections_names(self) -> list[str]:
        return await self._database.list_collection_names()

    async def insert_one(self, document: dict[str, Any]) -> None:
        await self._collection.insert_one(document)

    async def insert_many(self, documents: list[dict[str, Any]]) -> None:
        await self._collection.insert_many(documents)

    async def find_one(self, query: dict[str, Any]) -> dict[str, Any]:
        return await self._collection.find_one(query)

    async def find_many(self, query: dict[str, Any]) -> list[dict[str, Any]]:
        return await self._collection.find(query).to_list(length=None)

    async def delete_one(self, query: dict[str, Any]) -> None:
        await self._collection.delete_one(query)

    async def delete_many(self, query: dict[str, Any]) -> None:
        await self._collection.delete_many(query)


async def main() -> None:
    client = MongoClient(database_name="cv_data_storage", collection_name="test")
    await client.insert_many(
        documents=[
            {"test": "test"},
            {"test": "test2"},
            {"hello": "world"}
        ]
    )
    await client.delete_one(query={"hello": None})

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())