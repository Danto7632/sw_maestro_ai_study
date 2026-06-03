from pydantic import BaseModel, field_validator


class AnalyzeRequest(BaseModel):
    text: str
    senderRole: str
    receiverRole: str
    communicationType: str

    @field_validator("text")
    @classmethod
    def text_must_not_be_too_short(cls, v: str) -> str:
        if len(v.strip()) < 10:
            raise ValueError("분석할 텍스트와 필수 소통 정보를 입력해주세요.")
        return v.strip()
