from enum import Enum

class Weather(str, Enum):
    sun = 'sun'
    cloud = 'cloud'
    rain = 'rain'
    snow = 'snow'