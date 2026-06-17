from database.db_connection import DBConnection



class MissionDB:
    def __init__(self):
        self.db = DBConnection()
    

    def create_mission(self,data):
        try:
            data["risk_level"] = data["difficulty"] *2 + data["importance"]
            self.db.get_connection()
            self.db.cursor.execute("INSERT INTO missions (title, description, location, difficulty, importance, risk_level) VALUES (%s, %s, %s, %s, %s, %s)",
                                   (data["title"], data["description"], data["location"], data["difficulty"], data["importance"], data["risk_level"]))
            self.db.connection.commit()
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
        