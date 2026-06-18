from fastapi import FastAPI
from routes import agent_routes, mission_routes
from database.db_connection import DBConnection

d1 = DBConnection()
d1.get_connection()
d1.create_database()
d1.create_tables()


app = FastAPI()

app.include_router(agent_routes.router)
app.include_router(mission_routes.router)