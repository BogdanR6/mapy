from pydantic import BaseModel

class ConsentRequest(BaseModel):
    name: str | None = None
    shouldSave: bool
