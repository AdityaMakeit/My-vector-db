from pydantic import BaseModel


class TextUploadRequest(BaseModel):
    text: str


class SearchRequest(BaseModel):
    query: str
    k: int = 3