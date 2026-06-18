from pydantic import BaseModel, Field
from typing import Literal, Protocol
from fastapi import HTTPException
from database.agent_db import AgentDB

agent = AgentDB()


class Agent(BaseModel):
    name: str = Field(max_length=50)
    specialty: str = Field(max_length=50)
    agent_rank: str




def chicke_agent_rank(agent_rank, data):
    if agent_rank not in ["Junior", "Senior", "Commander"]:
        raise HTTPException(400,f"The agent_rank={agent_rank} not good!")
    return agent.create_agent(data)




def chicke_id(id):
    try:
        id = int(id)
    except:
        raise HTTPException(422, "The id most to be int")
    agent_data = agent.get_agent_by_id(id)
    if agent_data:
        return agent_data
    raise HTTPException(404,f"id= {id} not fond")
    