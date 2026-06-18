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



@router.get("/")
def get_agents():
    return agent.get_all_agents()



@router.get("/{id}")
def get_agent(id):
    return chicke_id(id)



@router.put("/{id}")
def update_agent(id, data:Agent):
    id_chicke = chicke_id(id)
    if id_chicke:
        data = dict(data)
        agent_rank = data["agent_rank"]
        chicke_rank = chicke_agent_rank(agent_rank, data)
        if chicke_rank:
            return agent.update_agent(id, data)
        return chicke_rank
    return id_chicke




@router.put("/{id}/deactivate")
def deactivate_agent(id):
    id_chicke = chicke_id(id)
    if id_chicke:
        return agent.deactivate_agent(id)
    return id_chicke



@router.put("/{id}/performance")
def performance_agent(id):
    id_chicke = chicke_id(id)
    if id_chicke:
        return agent.get_agent_performance(id)
    return id_chicke