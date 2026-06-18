from database.db_connection import DBConnection
from database.mission_db import MissionDB

mis = MissionDB()


class AgentDB:
    def __init__(self):
        self.db = DBConnection()

    def create_agent(self, data):
        try:
            self.db.get_connection()
            self.db.cursor.execute("insert into agents(name, specialty, agent_rank) values (%s, %s, %s)",
                                   (data["name"], data["specialty"], data["agent_rank"]))
            self.db.connection.commit()
            self.db.cursor.execute("select * FROM agents ORDER BY id DESC LIMIT 1")
            return self.db.cursor.fetchone()
        except Exception as e:
            print(e)
        finally:
            self.db.cursor.close()



    def get_all_agents(self):
        try:
            self.db.get_connection()
            self.db.cursor.execute("SELECT * FROM agents")
            return self.db.cursor.fetchall()
        except Exception as e:
            print(e)
        finally:
            self.db.cursor.close()
    


    def get_agent_by_id(self, id):
        try:
            self.db.get_connection()
            self.db.cursor.execute("SELECT * FROM agents where id=%s",(id,))
            return self.db.cursor.fetchone()
        except Exception as e:
            print(e)
        finally:
            self.db.cursor.close()



    def update_agent(self, id, data):
        try:
            self.db.get_connection()
            self.db.cursor.execute("UPDATE agents SET name=%s, specialty=%s , agent_rank=%s WHERE id=%s",
                                   (data["name"], data["specialty"], data["agent_rank"], id))
            self.db.connection.commit()
            return {"seuccess": True}
        except Exception as e:
            print(e)
        finally:
            self.db.cursor.close()
    


    def deactivate_agent(self, id):
        try:
            self.db.get_connection()
            self.db.cursor.execute("UPDATE agents set is_active=FALSE WHERE id=%s", (id,))
            self.db.connection.commit()
            return True
        except Exception as e:
            print(e)
        finally:
            self.db.cursor.close()
    


    def increment_completed(self, id):
        try:
            self.db.get_connection()
            self.db.cursor.execute("UPDATE agents set completed_missions=completed_missions +1 WHERE id=%s",(id,))
            self.db.connection.commit()
            return True
        except Exception as e:
            print(e)
        finally:
            self.db.cursor.close()
    


    def increment_failed(self, id):
        try:
            self.db.get_connection()
            self.db.cursor.execute("UPDATE agents set failed_missions=failed_missions +1 WHERE id=%s",(id,))
            self.db.connection.commit()
            return True
        except Exception as e:
            print(e)
        finally:
            self.db.cursor.close()



    def get_agent_performance(self, id):
        try:
            conclusion_missions = {}
            self.db.get_connection()
            self.db.cursor.execute("SELECT completed_missions, failed_missions FROM agents WHERE id=%s",(id,))
            missions = self.db.cursor.fetchone()
            self.db.cursor.execute("SELECT COUNT(assigned_agent_id) FROM missions WHERE id=%s", (id,))
            conclusion_missions["total"] = self.db.cursor.fetchone()
            conclusion_missions["failed"] = missions["failed_missions"]
            conclusion_missions["completed"] = missions["completed_missions"]
            conclusion_missions["success_rate"] = (missions["completed_missions"] / conclusion_missions["total"]) * 100
            return conclusion_missions
        except ZeroDivisionError:
            conclusion_missions["success_rate"] = 0
            return conclusion_missions 
        except Exception as e:
            print(e)
        finally:
            self.db.cursor.close() 


    def count_active_agent(self):
        try:
            self.db.get_connection()
            self.db.cursor.execute("SELECT COUNT(*) as active_agents FROM agents WHERE is_active=1")
            return self.db.cursor.fetchone()
        except Exception as e:
            print(e)
        finally:
            self.db.cursor.close()

