import datetime

from pydantic import BaseModel, ConfigDict


class Question(BaseModel):

    id: int
    subject: str
    # email : str
    content: str
    create_date: datetime.datetime
    
    class Config:
        orm_mode = True
        # extra = "allow"