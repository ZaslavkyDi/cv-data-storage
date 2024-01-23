import asyncio

from cv_common_library.registry import consumers

from cv_data_storage.consumers.candidates_result_consumer import CandidatesStorageConsumer


async def main() -> None:
    candidates_consumer: CandidatesStorageConsumer = consumers.get(
        "candidates_result_consumer_kafka"
    )
    await candidates_consumer.start_consuming()


if __name__ == "__main__":
    asyncio.run(main())
