from pydantic import BaseModel

class featured(BaseModel):
    title: str
    image: str
    url: str