from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field
import requests
import os
from dotenv import load_dotenv
from typing import Optional
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load environment variables
load_dotenv()

app = FastAPI(
    title="Weather Microservice",
    description="Real-time weather data from OpenWeatherMap API",
    version="2.1.0",
    docs_url="/docs",
    redoc_url=None,
    openapi_tags=[{
        "name": "weather",
        "description": "Get current weather data for cities worldwide"
    }]
)

class WeatherResponse(BaseModel):
    city: str = Field(..., example="Nairobi")
    temperature: float = Field(..., example=15.5)
    conditions: str = Field(..., example="clear sky")
    humidity: Optional[int] = Field(None, example=67)
    wind_speed: Optional[float] = Field(None, example=3.2)
    pressure: Optional[int] = Field(None, example=1012)
    visibility: Optional[int] = Field(None, example=10000)

class ErrorResponse(BaseModel):
    detail: str = Field(..., example="City not found")

@app.get(
    "/weather/{city}",
    response_model=WeatherResponse,
    responses={
        404: {"model": ErrorResponse},
        429: {"model": ErrorResponse},
        500: {"model": ErrorResponse}
    },
    tags=["weather"],
    summary="Get current weather data",
    description="""Returns comprehensive weather information for the specified city.""",
    response_description="Successful weather data response"
)
async def get_weather(city: str, units: str = "metric", lang: str = "en"):
    owm_api_key = os.getenv("OPENWEATHER_API_KEY")
    if not owm_api_key:
        logger.error("OpenWeatherMap API key not configured")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Service configuration error"
        )

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={owm_api_key}&units={units}&lang={lang}"
    
    try:
        response = requests.get(url, timeout=10)
        data = response.json()
        
        if response.status_code == 401:
            logger.error("Invalid OpenWeatherMap API key")
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="Service configuration error"
            )
        if response.status_code == 404:
            logger.info(f"City not found: {city}")
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="City not found. Check spelling or try nearby cities."
            )
        if response.status_code == 429:
            logger.warning("OpenWeatherMap rate limit exceeded")
            raise HTTPException(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                detail="Weather service is currently overloaded. Please try again later."
            )

        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "conditions": data["weather"][0]["description"],
            "humidity": data["main"].get("humidity"),
            "wind_speed": data["wind"].get("speed"),
            "pressure": data["main"].get("pressure"),
            "visibility": data.get("visibility")
        }
        
    except requests.Timeout:
        logger.error("OpenWeatherMap API timeout")
        raise HTTPException(
            status_code=status.HTTP_504_GATEWAY_TIMEOUT,
            detail="Weather service timeout"
        )
    except Exception as e:
        logger.error(f"Weather data fetch failed: {str(e)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to fetch weather data"
        )

@app.get("/health", include_in_schema=False)
async def health_check():
    return {"status": "healthy"}
