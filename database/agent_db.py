from database.db_connection import DBConnection


class AgentDB:
    def __init__(self):
        self.db = DBConnection()

    def create_agent(self, data):
        try:
            self.db.get_connection()
            self.db.cursor.execute("insert into agents(name, specialty, agent_rank) values (%s, %s, %s)",
                                   (data["name"], data["specialty"], data["agent_rank"]))
            self.db.connection.commit()
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
            return self.db.cursor.fetchone()
        except Exception as e:
            print(e)
        finally:
            self.db.cursor.close()