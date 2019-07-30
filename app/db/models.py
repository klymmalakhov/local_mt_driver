from pydantic import BaseModel


class Event(BaseModel):
    id_event: int
    event_request: str
    event_response: str
