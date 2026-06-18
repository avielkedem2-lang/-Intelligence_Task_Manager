from fastapi import APIRouter
from service.missions_service import *


router1 = APIRouter(prefix="/missions", tags=["missions"])


@router1.post("/")
def create_mission(data:Mission):
    return checks_difficulty_and_importance(data)