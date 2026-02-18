from fastapi import FastAPI
import requests

from fastapi import FastAPI, Depends, Request, Response
from fastapi.responses import RedirectResponse
from gateway.api_router import call_api_gateway,RedirectRoutesPortalException,RedirectVehiclesPortalException,RedirectLinesPortalException, RedirectAlertsPortalException
from Alerts import Alerts
from Lines import Lines
from Routes import Routes
from Vehicles import Vehicles
from controller import controller
import httpx

app = FastAPI()
app.include_router (controller.router,
                    dependencies=[Depends(call_api_gateway)])

@app.middleware("http")
async def middleware(request: Request, call_next):
    response = await call_next(request)
    return response


@app.exception_handler(RedirectAlertsPortalException)
def exception_handler_student(request: Request, exc: RedirectAlertsPortalException) -> Response:
    return RedirectResponse(url='http://localhost:8000/alerts')


@app.exception_handler(RedirectVehiclesPortalException)
def exception_handler_faculty(request: Request, exc: RedirectVehiclesPortalException) -> Response:
    return RedirectResponse(url='http://localhost:8000/vehicles')


@app.exception_handler(RedirectRoutesPortalException)
def exception_handler_library(request: Request, exc: RedirectRoutesPortalException) -> Response:
    return RedirectResponse(url='http://localhost:8000/routes')


@app.exception_handler(RedirectLinesPortalException)
def exception_handler_library(request: Request, exc: RedirectLinesPortalException) -> Response:
    return RedirectResponse(url='http://localhost:8000/lines')


#http://127.0.0.1:8000/Alerts/alerts
app.mount("/Alerts", Alerts.app)

#http://127.0.0.1:8000/Lines/lines
app.mount("/Lines", Lines.app)

#http://127.0.0.1:8000/Routes/routes
app.mount("/Routes", Routes.app)

#http://127.0.0.1:8000/Vehicles/vehicles/
app.mount("/Vehicles", Vehicles.app)


