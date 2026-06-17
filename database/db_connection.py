import mysql.connector


class DBConnection:
    def __init__(self):
        self.config = {
            "host": "127.0.0.1",
            "port":"3306",
            "user":"root",
            "password":"1234",
            "database":"Intelligence_db"
        }
        self.connection = None
        self.cursor = None
    
    def get_connection(self):
        self.connection = mysql.connector.connect(**self.config)
        self.cursor = self.connection.cursor(dictionary=True)
    
    def create_database(self):
        try:
            self.cursor.execute("""CREATE DATABASE IF NOT EXISTS Intelligence_db""")
        except Exception as e:
            print(e)
        finally:
            self.cursor.close()
    

    def create_tables(self):
        try:
            self.get_connection()
            self.cursor.execute("""CREATE TABLE agents(id INT AUTO_INCREMENT PRIMARY KEY,
                                name VARCHAR(50) not null,
                                specialty VARCHAR(100) not null,
                                is_active BOOLEAN DEFAULT TRUE,
                                completed_missions INT DEFAULT 0,
                                failed_missions INT DEFAULT 0,
                                agent_rank ENUM('Junior','Senior','Commander'))
                                ;""")
            

            self.cursor.execute("""CREATE TABLE missions(
                                id INT AUTO_INCREMENT PRIMARY KEY,
                                title VARCHAR(50) not null,
                                description TEXT not null,
                                location VARCHAR(50) not null,
                                difficulty INT(10) not null,
                                importance INT(10) not null,
                                status VARCHAR(50) DEFAULT 'NEW',
                                risk_level VARCHAR(50),
                                assigned_agent_id int DEFAULT NULL 
                                );""")
            
        except Exception as e:
            print(e)
        finally:
            self.cursor.close()


# d = DB_connection()
# d.get_connection()
# d.create_database()
# d.create_tables()