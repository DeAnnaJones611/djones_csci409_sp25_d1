from fastapi import FastAPI, Depends
import httpx
from fastapi import FastAPI
import requests

API_KEY = "5df31c39b241470c89e862a1f041c735" # Fill in with your API Key
ENDPOINT_URL = "https://api-v3.mbta.com/" # DO NOT CHANGE THIS
app = FastAPI() # Initialize the end point

async def get_all_vehicles():
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{ENDPOINT_URL}/vehicles?api_key={API_KEY}")
        response.raise_for_status()
        return response.json()

    # Dependency to fetch a specific alert by ID
async def get_vehicles_by_id(vehicles_id: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{ENDPOINT_URL}/vehicles/{vehicles_id}?api_key={API_KEY}")
        response.raise_for_status()
        return response.json()


#---------------------------------------------------------------------------End of Assignment


@app.get("/") # Create a default route
def read_root():
    return {"message": "Welcome to my FastAPI Application vehicles!"}

@app.get("/vehicles")
async def read_alerts(alerts=Depends(get_all_vehicles)):
    return alerts


@app.get("/vehicles/{vehicles_id}")
async def read_alert(vehicles_id: str, alert=Depends(get_vehicles_by_id)):
    return alert