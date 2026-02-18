
from fastapi import Request

def call_api_gateway(request: Request):
    portal_id = request.path_params['portal_id']
    print(request.path_params)
    if portal_id == str(1):
        raise RedirectAlertsPortalException()
    elif portal_id == str(2):
        raise RedirectVehiclesPortalException()
    elif portal_id == str(3):
        raise RedirectRoutesPortalException()
    elif portal_id == str(4):
        raise RedirectLinesPortalException()


class RedirectAlertsPortalException(Exception):
    pass


class RedirectVehiclesPortalException(Exception):
    pass


class RedirectRoutesPortalException(Exception):
    pass


class RedirectLinesPortalException(Exception):
    pass