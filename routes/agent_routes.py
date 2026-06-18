from fastapi import APIRouter
from service.agent_service import *
from database.agent_db import AgentDB


agent = AgentDB()

router = APIRouter(prefix="/agents",tags=["agents"])


@router.post("/")
def create_agent(data:Agent):
    data = dict(data)
    agent_rank = data["agent_rank"]
    return chicke_agent_rank(agent_rank,data)



