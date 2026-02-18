from fastapi import FastAPI
import requests

#-------------------------------------------------------------- Beginning Added
from fastapi import FastAPI, Depends
import httpx




#---------------------------------------------------------------------------End of Assignment

API_KEY = "5df31c39b241470c89e862a1f041c735" # Fill in with your API Key
ENDPOINT_URL = "https://api-v3.mbta.com/" # DO NOT CHANGE THIS


app = FastAPI() # Initialize the end point

@app.get("/") # Create a default route
def read_root():
    return {"message": "Welcome to my FastAPI Application for lines!"}

#--------------------------------------------------------------------------------------------------------------------------------------Added
# Get information on a specific route
@app.get("/lines")
def get_lines():
    lines_list = list()
    response = requests.get(ENDPOINT_URL+f"/lines?&api_key={API_KEY}") # Send a request to the endpoint
    # Convert the response to json and extract the data key
    lines = response.json()["data"]
    for line in lines:
        # Loop through all routes extracting relevant information
        lines_list.append({
            "id": line["id"],
            "text_color": line["attributes"]["text_color"],
            "short_name": line["attributes"]["short_name"],
            "long_name": line["attributes"]["long_name"],
            "color": line["attributes"]["color"],
        })
    # Return the routes_list in JSON format
    return {"lines": lines_list}



@app.get("/lines/{line_id}")
def get_line_id(line_id: str):
    response = requests.get(ENDPOINT_URL + f"/lines/{line_id}?api_key={API_KEY}") # Send a request to the endpoint
    # Convert the response to json and extract the data key
    line_data = response.json()["data"]
    # Extract the relevant data
    line = {
        "id": line_data["id"],
        "text_color": line_data["attributes"]["text_color"],
        "short_name": line_data["attributes"]["short_name"],
        "long_name": line_data["attributes"]["long_name"],
        "color": line_data["attributes"]["color"],
    }
    # Return the data to the user
    return {"lines": line}

