import datetime

from fastapi import FastAPI, HTTPException
from starlette import status
from starlette.responses import RedirectResponse
from WeatherForecastController import WeatherForecastController
from models import WeatherForecast, WeatherForecastIn

app = FastAPI()

db = WeatherForecastController()


@app.get("/")
async def root():
    return RedirectResponse(url="/docs", status_code=status.HTTP_302_FOUND)


@app.get("/forecast/")
async def get_all():
    return db.get_all()


@app.get("/forecast/period", response_model=list[WeatherForecast])
async def find_forecast_for_period(from_day: datetime.date, to_day: datetime.date):
    result = db.forecast_for_period(from_day, to_day)
    if result is not None:
        return result
    raise HTTPException(status_code=404, detail='Данных за указанный период не найдено')


@app.get("/forecast/{wf_day}", response_model=list[WeatherForecast])
async def get_weather_for_day(wf_day: datetime.date):
    result = db.get_weather_for_day(wf_day)
    if result is not None:
        return result
    raise HTTPException(status_code=404, detail='Данных за указанный день нет')


@app.post("/forecast/add/", response_model=WeatherForecast)
async def add(wfc: WeatherForecastIn):
    result = db.add_weather_for_day(wfc)
    if result is not None:
        return result

    raise HTTPException(status_code=500, detail='Данные за этот день уже внесены')


@app.put("/forecasts/update/{wf_date}", response_model=WeatherForecast)
async def update(wf_date: datetime.date, new_temp_c: int):
    result = db.update_weather_for_day(wf_date, new_temp_c)
    if result is not None:
        return result

    raise HTTPException(status_code=404, detail='Данные за указанный день не найдены')


@app.delete("/forecasts/{wf_date}")
async def delete(wf_date: datetime.date):
    if db.delete_weather_for_day(wf_date):
        return {'message': 'Данные за указанный день удалены'}

    raise HTTPException(status_code=404, detail='Данные за указанный день не найдены')
