from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional



class EventResponse(BaseModel):
    event_id: int
    venue_id: int
    venue_name: str
    venue_postcode: str
    venue_city: str
    event_title: str
    event_description: str
    event_date_start: datetime
    event_created_at: datetime
    image_url: Optional[str] = None
    organizer_name: Optional[str] = None
    event_type: Optional[str] = None
    genre_type: Optional[str] = None
    venue_type: Optional[str] = None
    space_name: Optional[str] = None
    space_type: Optional[str] = None
