import sqlite3

CREATE_QUIZ_TABLE= "CREATE TABLE IF NOT EXISTS question(id INTEGER PRIMARY KEY,question TEXT,level TEXT,topic TEXT,answer TEXT);"
INSERT_QUESTION = "INSERT INTO question(question,level,topic,answer) VALUES(?,?,?,?);"
GET_QUIZ_BY_TOPIC="SELECT * FROM question WHERE topic=?;"
GET_QUIZ_BY_LEVEL="SELECT * FROM question WHERE LEVEL=?;"
def connect():
    return sqlite3.connect("data.db")
def create_tables(connection):
    with connection:
        connection.execute(CREATE_QUIZ_TABLE)
    
def add_question(connection,question,level,topic,answer):
     with connection:
        connection.execute(INSERT_QUESTION,(question,level,topic,answer))

def get_quiz_by_topic(connection,question,level,topic,answer):
     with connection:
         return connection.execute(GET_QUIZ_BY_TOPIC,(topic,)).fetchall()

def get_quiz_by_level(connection,question,level,topic,answer):
     with connection:
         return connection.execute(GET_QUIZ_BY_LEVEL,(level,)).fetchall()


