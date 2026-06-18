from fastapi import APIRouter
from service.missions_service import *
from service.agent_service import chicke_id
from database.mission_db import MissionDB
from database.agent_db import AgentDB

mis = MissionDB()
agent = AgentDB()

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



@router.put("/{id}/assign/{agent_id}")
def assign_mission(id, agent_id):
    id_checke = checke_id(id)
    if id_checke:
        chicke_id_agent = chicke_id(agent_id)
        if chicke_id_agent:
            status_checke = checke_status(id)
            if status_checke:
                is_active = checke_is_active(id)
                if is_active:
                    open_mission = mis.count_open_missions()
                    if open_mission["sam_open_missions"] >= 3:
                        rank = checke_rank(id, agent_id)
                        if rank:
                            return mis.assign_mission(id, agent_id)
                        return rank
                    return HTTPException(400, "You cannot enter more than 3 open tasks.")
                return is_active
            return status_checke
        return chicke_id_agent
    return id_checke





@router.put("/{id}/start")
def update_mission_status(id):
    id_checke = checke_id(id)
    if id_checke:
        assu = checks_associated(id)
        if assu:
            status = is_assigned(id)
            if status:
                return mis.update_mission_status(id, "IN_PROGRESS")
            return status
        return assu
    return id_checke



@router.put("/{id}/complete")
def update_mission_status_to_complete(id):
    id_checke = checke_id(id)
    if id_checke:
        status = is_in_progress(id)
        if status:
            id_agent = mis.get_mission_by_id(id)["assigned_agent_id"]
            agent.increment_completed(id_agent)
            return mis.update_mission_status(id, "COMPLETED")
        return status
    return id_checke



@router.put("/{id}/fail")
def update_mission_status_to_failed(id):
    id_checke = checke_id(id)
    if id_checke:
        status = is_in_progress(id)
        if status:
            id_agent = mis.get_mission_by_id(id)["assigned_agent_id"]
            agent.increment_failed(id_agent)
            return mis.update_mission_status(id, "FAILED")
        return status
    return id_checke





@router.put("/{id}/cancel")
def update_mission_status_to_cancel(id):
    id_checke = checke_id(id)
    if id_checke:
        status = to_cancel(id)
        if status:
            return mis.update_mission_status(id, "CANCELLED")
        return status
    return id_checke