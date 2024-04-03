from fastapi import FastAPI
from fastapi import APIRouter
import requests
import httpx

router = APIRouter(
    prefix='/openweatherapi',
    tags=['Open weathermap a third-party API’s']
)

@router.get('/')
def ExternalApi():
    api_url = 'https://api.openweathermap.org/data/2.5/weather?q=London&units=metric&appid=5e9e52d2d35442f9762b296ff8bac9f7'
    data = requests.get(api_url).json()
    city=str(data['name'])
    temp= str(data['main']['temp'])
    humidity= str(data['main']['humidity'])+'%'
    speed= data['wind']['speed']
    description= str(data['weather'][0]['description'])
    print(speed)
    print(temp)
    return {'city':city, 'Temperature':temp, 'Humidity':humidity, 'Wind Speed': speed, 'Description':description}

