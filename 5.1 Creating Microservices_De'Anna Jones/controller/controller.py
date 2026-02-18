from fastapi import APIRouter

router = APIRouter()

@router.get("/controller/{portal_id}")
def access_portal(portal_id:int):
    return {'message': 'Made it to Transportation System'}
