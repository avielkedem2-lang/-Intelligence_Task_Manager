from pydantic import BaseModel, Field
from database.mission_db import MissionDB
from fastapi import HTTPException

mission = MissionDB()




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
