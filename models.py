from pydantic import BaseModel


class ScrappingResult(BaseModel):
    url: str
    status: int
    html: str