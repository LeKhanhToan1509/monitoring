from typing import Optional
from pydantic import BaseModel

class TenderPayload(BaseModel):
    id: Optional[int] = None
    tender_name: str
    project_name: str
    msc_field: str
    inviting_party: Optional[str] = None
    investor: Optional[str] = None
    scope_of_work: Optional[str] = None
    other_details: Optional[str] = None
