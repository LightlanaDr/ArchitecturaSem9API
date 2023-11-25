import datetime

from models import WeatherForecast, WeatherForecastIn


class WeatherForecastController:

    def __init__(self):
        self.__weatherForecastArchive: list[WeatherForecast] = []

    def get_all(self) -> list[WeatherForecast]:
        return self.__weatherForecastArchive

    def get_weather_for_day(self, date: datetime.date):
        for weather_for_day in self.__weatherForecastArchive:
            if weather_for_day.wf_date == date:
                return weather_for_day
            return print("Данных за указанный день нет")

    def forecast_for_period(self, from_date: datetime.date, to_date: datetime.date):
        forecast_weather_for_period = []
        for fwp in self.__weatherForecastArchive:
            if from_date <= fwp.wf_date <= to_date:
                forecast_weather_for_period.append(fwp)
            return forecast_weather_for_period
        return None

    def add_weather_for_day(self, wf: WeatherForecastIn):
        for info_day in self.__weatherForecastArchive:
            if info_day.wf_date == wf.wf_date:
                return None
        new_forecast = WeatherForecast(id=len(self.__weatherForecastArchive) + 1,
                                       wf_date=wf.wf_date,
                                       temp_c=wf.temp_c,
                                       temp_f=wf.temp_c * 9 / 5 + 32)

        self.__weatherForecastArchive.append(new_forecast)
        return new_forecast

    def update_weather_for_day(self, date_day: datetime.date, temp_c: int):
        for wfd in self.__weatherForecastArchive:
            if wfd.wf_date == date_day:
                wfd.temp_c = temp_c
                wfd.temp_f = temp_c * 9 / 5 + 32
                return wfd
        return None

    def delete_weather_for_day(self, date_day: datetime.date):
        for wfd in self.__weatherForecastArchive:
            if wfd.wf_date == date_day:
                self.__weatherForecastArchive.remove(wfd)
                return True
        return False
