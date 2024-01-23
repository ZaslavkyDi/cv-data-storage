import logging
from typing import ClassVar, Self

from confluent_kafka import Message
from cv_common_library.message_brokers.kafka.base.consumer import BaseKafkaConsumer
from cv_common_library.message_brokers.kafka.config import get_kafka_global_settings
from cv_common_library.registry import consumers
from cv_common_library.schemas.cv_data_storage.message import CandidateResultMessageSchema


logger = logging.getLogger(__name__)


@consumers.register("candidates_result_consumer_kafka")
class CandidatesStorageConsumer(BaseKafkaConsumer):
    _TOPICS: ClassVar[list[str]] = ["cv-scrapers.candidates.request.result"]
    _GROUP_ID = "cv-scrappers.candidates_result_producer"

    def __init__(self) -> None:
        super().__init__(
            group_id=self._GROUP_ID,
            topics_to_subscribe=self._TOPICS,
            bootstrap_servers=get_kafka_global_settings().bootstrap_servers,
        )

    @classmethod
    def create_instance(cls) -> Self:
        """Creates an instance of the consumer. Implementing Registry protocol."""
        return cls()

    async def process_message(self, message: Message) -> None:
        try:
            message_model = CandidateResultMessageSchema.model_validate_json(message.value())
            logger.info(f"Received message: {message_model.model_dump()}")
            await self._initiate_scraping(message_model)
        except Exception as e:
            logger.exception(f"Error in {self.topics}: {e!s}")

    async def _save_result_to_db(self, message: CandidateResultMessageSchema) -> None:
        pass
