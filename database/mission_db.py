from database.db_connection import DBConnection



class MissionDB:
    def __init__(self):
        self.db = DBConnection()
    

    def create_mission(self,data):
        try:
            self.db.get_connection()
            self.db.cursor.execute("INSERT INTO missions (title, description, location, difficulty, importance, risk_level) VALUES (%s, %s, %s, %s, %s, %s)",
                                    (data["title"], data["description"], data["location"], data["difficulty"], data["importance"], data["risk_level"]))
            self.db.connection.commit()
            self.db.cursor.execute("select * FROM missions ORDER BY id DESC LIMIT 1")
            return self.db.cursor.fetchone()
        except Exception as e:
            print(e)
        finally:
            self.db.cursor.close()
    

    def get_all_missions(self):
        try:
            self.db.get_connection()
            self.db.cursor.execute("select * from missions")
            return self.db.cursor.fetchall()
        except Exception as e:
            print(e)
        finally:
            self.db.cursor.close()
    

    def get_mission_by_id(self, id):
        try:
            self.db.get_connection()
            self.db.cursor.execute("select * from missions where id=%s", (id,))
            return self.db.cursor.fetchone()
        except Exception as e:
            print(e)
        finally:
            self.db.cursor.close()
    

    def assign_mission(self, m_id, a_id):
        try:
            self.db.get_connection()
            self.db.cursor.execute("UPDATE missions SET assigned_agent_id=%s, status='ASSIGNED' WHERE id=%s",
                                   (m_id, a_id))
            self.db.connection.commit()

            return True
        except Exception as e:
            print(e)
        finally:
            self.db.cursor.close()
    


    def update_mission_status(self, id, status):
        try:
            self.db.get_connection()
            self.db.cursor.execute("UPDATE missions SET status=%s WHERE id=%s",
                                   (status, id))
            self.db.connection.commit()
            return {"seuccess":True}
        except Exception as e:
            print(e)
        finally:
            self.db.cursor.close()



    def count_all_missions(self):
        try:
            self.db.get_connection()
            self.db.cursor.execute("SELECT COUNT(*) as total_missions FROM missions")
            return self.db.cursor.fetchone()
        except Exception as e:
            print(e)
        finally:
            self.db.cursor.close()
    

    def status_by_count(self,status):
        try:
            self.db.get_connection()
            self.db.cursor.execute("SELECT COUNT(status) FROM missions WHERE status=%s", (status,))
            return self.db.cursor.fetchone()
        except Exception as e:
            print(e)
        finally:
            self.db.cursor.close()
    

    def count_open_missions(self):
        try:
            self.db.get_connection()
            self.db.cursor.execute("SELECT COUNT(status) as sam_open_missions FROM missions WHERE status='NEW' OR status = 'ASSIGNED' OR status='PROGRESS_IN'")
            return self.db.cursor.fetchone()
        except Exception as e:
            print(e)
        finally:
            self.db.cursor.close()
    

    def count_critical_missions(self):
        try:
            self.db.get_connection()
            self.db.cursor.execute("SELECT COUNT(risk_level) FROM missions WHERE risk_level='CRITICAL';")
            return self.db.cursor.fetchone()
        except Exception as e:
            print(e)
        finally:
            self.db.cursor.close()
    

    # def get_top_agent(self):
    #     try:
    #         self.db.get_connection()
    #         self.db.cursor.execute("
        