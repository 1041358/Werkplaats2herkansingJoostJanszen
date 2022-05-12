import random
import sqlite3


class HighScores:
    def __init__(self, database_file_name):
        self.database_file_name = database_file_name
        self.init_database()

    def init_database(self):
        conn = sqlite3.connect(self.database_file_name)
        cur = conn.cursor()
        sql = "CREATE TABLE IF NOT EXISTS highscores " \
              "(id INTEGER PRIMARY KEY AUTOINCREMENT , name TEXT NOT NULL, score INTEGER NOT NULL)"
        cur.execute(sql)
        conn.commit()
        conn.close()

    def insert_score(self, name, score):
        conn = sqlite3.connect(self.database_file_name)
        cur = conn.cursor()
        sql = "INSERT INTO highscores VALUES (?, ?, ?)"
        cur.execute(sql, [None, name, score])
        print("Inserted " + name + " into highscores with a score of " + str(score))
        conn.commit()
        conn.close()


highscores = HighScores("scores.db")
highscores.insert_score("Jelle", 170000)
highscores.insert_score("Eva", 150000)
highscores.insert_score("Tjidde", 150000)
highscores.insert_score("Mark", 100000)
highscores.insert_score("Robert", 90000)
highscores.insert_score("Clifton", random.randint(0, 100000))
highscores.insert_score("Horacio", random.randint(0, 100000))
highscores.insert_score("Hyman", random.randint(0, 100000))
highscores.insert_score("Tom", random.randint(0, 100000))
highscores.insert_score("Franklin", random.randint(0, 100000))
highscores.insert_score("Arturo", random.randint(0, 100000))
highscores.insert_score("Sammie", random.randint(0, 100000))
highscores.insert_score("Percy", random.randint(0, 100000))
highscores.insert_score("Erick", random.randint(0, 100000))
highscores.insert_score("Mel", random.randint(0, 100000))
highscores.insert_score("Harrison", random.randint(0, 100000))
highscores.insert_score("Mohamed", random.randint(0, 100000))
highscores.insert_score("Homer", random.randint(0, 100000))
highscores.insert_score("Dorsey", random.randint(0, 100000))
highscores.insert_score("Christian", random.randint(0, 100000))
highscores.insert_score("Alton", random.randint(0, 100000))
highscores.insert_score("Heriberto", random.randint(0, 100000))
highscores.insert_score("Dustin", random.randint(0, 100000))
highscores.insert_score("Sheldon", random.randint(0, 100000))
highscores.insert_score("Willie", random.randint(0, 100000))
highscores.insert_score("Jody", random.randint(0, 100000))
highscores.insert_score("Santos", random.randint(0, 100000))
highscores.insert_score("Jeffery", random.randint(0, 100000))
highscores.insert_score("Allan", random.randint(0, 100000))
highscores.insert_score("Rodrick", random.randint(0, 100000))
highscores.insert_score("Merlin", random.randint(0, 100000))
highscores.insert_score("Linwood", random.randint(0, 100000))
highscores.insert_score("Judson", random.randint(0, 100000))
highscores.insert_score("Alexander", random.randint(0, 100000))
highscores.insert_score("Logan", random.randint(0, 100000))
highscores.insert_score("Genaro", random.randint(0, 100000))
highscores.insert_score("Amado", random.randint(0, 100000))
highscores.insert_score("Raul", random.randint(0, 100000))
highscores.insert_score("Irving", random.randint(0, 100000))
highscores.insert_score("Roscoe", random.randint(0, 100000))
highscores.insert_score("Hollis", random.randint(0, 100000))
highscores.insert_score("Titus", random.randint(0, 100000))
highscores.insert_score("Miguel", random.randint(0, 100000))
highscores.insert_score("Florencio", random.randint(0, 100000))
highscores.insert_score("Marcellus", random.randint(0, 100000))
highscores.insert_score("Jordan", random.randint(0, 100000))
highscores.insert_score("Rusty", random.randint(0, 100000))
highscores.insert_score("Tristan", random.randint(0, 100000))
highscores.insert_score("Leonardo", random.randint(0, 100000))
highscores.insert_score("Lawerence", random.randint(0, 100000))
highscores.insert_score("Jeff", random.randint(0, 100000))
highscores.insert_score("Rayford", random.randint(0, 100000))
highscores.insert_score("Abram", random.randint(0, 100000))
highscores.insert_score("Zachary", random.randint(0, 100000))
highscores.insert_score("Domingo", random.randint(0, 100000))
