import typing

from aio_pika.abc import AbstractIncomingMessage
from cv_common_library.message_broker.base.consumer import BaseAsyncConsumer

from cv_data_storage.consumers.schemas import CandidatesStorageRequestMessageSchema


class CandidatesStorageConsumer(BaseAsyncConsumer[CandidatesStorageRequestMessageSchema]):
    def __init__(self) -> None:
        super().__init__(
            queue_name="cv-data-storage.candidates.storage",
            routing_keys=("candidates.resume.store.v1",),
        )

    async def _map_message_to_schema(
        self, message: AbstractIncomingMessage
    ) -> CandidatesStorageRequestMessageSchema:
        pass

    async def _do_staff(
        self, message_schema: CandidatesStorageRequestMessageSchema, **kwargs: typing.Any
    ) -> typing.Any:
        pass
