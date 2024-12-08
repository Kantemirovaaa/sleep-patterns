from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional

from .data_processing import get_data_slice, add_record

app = FastAPI()


@app.get("/data")
def get_data(start: int = 0, limit: int = 10):
    return get_data_slice(start, limit)


class NewRecord(BaseModel):
    Sleep_Duration: Optional[float] = None
    Study_Time: Optional[float] = None
    Screen_Time: Optional[float] = None
    Caffeine_Intake: Optional[float] = None
    Physical_Activity: Optional[float] = None
    Sleep_Quality: Optional[float] = None
    Free_Time: Optional[float] = None


@app.post("/data")
def post_data(record: NewRecord):
    result = add_record(record.model_dump())
    return {"status": "success", "record": result}
