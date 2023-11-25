import datetime
from sqlite3 import Date

import day
from pydantic import BaseModel


class WeatherForecast(BaseModel):
    wf_date: datetime.date
    temp_c: float
    temp_f: float


class WeatherForecastIn(BaseModel):
    wf_date: datetime.date
    temp_c: float
    