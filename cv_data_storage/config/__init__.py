from functools import cache

from cv_data_storage.config.settings import MongoDBSettings


@cache
def get_mongodb_settings() -> MongoDBSettings:
    return MongoDBSettings()
