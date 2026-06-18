from pydantic import BaseModel, Field
from database.mission_db import MissionDB
from database.agent_db import AgentDB
from fastapi import HTTPException

mission = MissionDB()
agent = AgentDB()



class Mission(BaseModel):
    title: str
    description: str
    location: str
    difficulty: int
    importance: int



def checks_difficulty_and_importance(data):
    data = dict(data)
    importance = data["importance"]
    difficulty = data["difficulty"]
    if 10 >= importance > 0 and  10 >= difficulty > 0:
        return create_risk_level(data)
    raise HTTPException(400, "The difficulty and importance most to be 1-10")




def create_risk_level(data):
    risk_level = data["difficulty"] *2 + data["importance"]
    if risk_level >= 25:
        data["risk_level"] = "CRITICAL"
    
    elif 18 <= risk_level <= 24:
        data["risk_level"] = "HIGH"

    elif 10 <= risk_level <= 17:
        data["risk_level"] = "MEDIUM"
    
    elif 1 <= risk_level <= 9:
        data["risk_level"] = "LOW"
    
    return mission.create_mission(data)



def checke_id(id):
    try:
        id = int(id)
    except:
        raise HTTPException(422, "The id most to be int")
    mission_data = mission.get_mission_by_id(id)
    if mission_data:
        return True
    raise HTTPException(404,f"id= {id} not fond")




def checke_status(id):
    if mission.get_mission_by_id(id)["status"] == "NEW":
        return True
    raise HTTPException(400, "The status most to be NEW")


def checke_is_active(id):
    if agent.get_agent_by_id(id)["is_active"] == 1:
        return True
    raise HTTPException(400, "The agent mast to be active")



def checke_rank(id, agent_id):
    if mission.get_mission_by_id(id)["risk_level"] == "CRITICAL":
        if agent.get_agent_by_id(agent_id)["agent_rank"] == "Commander":
            return True
        return HTTPException(400, "The agent nost to be Commander becase it is CRITICAL")
    return True




def checks_associated(id):
    if mission.get_mission_by_id(id)["assigned_agent_id"]:
        return True
    raise HTTPException(400, "The mission not associat to no bady")

def is_assigned(id):
    if mission.get_mission_by_id(id)["status"] == "ASSIGNED":
        return True
    raise HTTPException(400, "The mission not on ASSIGNED")




def is_in_progress(id):
    if mission.get_mission_by_id(id)["status"] == "IN_PROGRESS":
        return True
    raise HTTPException(400, "The mission not on IN_PROGRESS")




def to_cancel(id):
    if mission.get_mission_by_id(id)["status"] == "NEW" or mission.get_mission_by_id(id)["status"] == "ASSIGNED":
        return True
    raise HTTPException(400, "The mission not on NEW OR ASSIGNED")