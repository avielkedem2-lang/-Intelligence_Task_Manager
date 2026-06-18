from fastapi import APIRouter
from service.missions_service import *
from database.mission_db import MissionDB

mis = MissionDB()

router = APIRouter(prefix="/missions", tags=["missions"])


@router.post("/")
def create_mission(data:Mission):
    return checks_difficulty_and_importance(data)



@router.get("/")
def get_all_missions():
    return mis.get_all_missions()



@router.get("/{id}")
def get_mission(id):
    id_checke = checke_id(id)
    if id_checke:
        return mis.get_mission_by_id(id)
    return id_checke