from cv_common_library.message_broker.schemas import BaseMessageSchema
from pydantic import BaseModel


class CandidateDetailsSchema(BaseModel):
    cv_url: str
    position: str
    name: str
    compensation: str | None = None
    age: int | None = None
    location: str | None = None


class CandidatesStorageRequestBody(BaseModel):
    scraping_source: str
    candidates: list[CandidateDetailsSchema]


class CandidatesStorageRequestMessageSchema(BaseMessageSchema):
    body: CandidatesStorageRequestBody
