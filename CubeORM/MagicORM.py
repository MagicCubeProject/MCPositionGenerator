import sqlite3
import os


class MagicORM(object):
    def __init__(self,path,name="cube"):
        suffix = ".db"
        db_path = os.path.join(path, name + suffix)
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()
        self.__crate_table()


    def __crate_table(self):
        # query = """
        # CREATE TABLE IF NOT EXISTS states (
        #  state_id INTEGER PRIMARY KEY,
        #  parent_state_id INTEGER,
        #  state VARCHAR NOT NULL,
        #  distances VARCHAR NOT NULL,
        #  move VARCHAR NOT NULL,
        #  generation INTEGER NOT NULL
        # );
        # """

        # query = """
        # CREATE TABLE IF NOT EXISTS states (
        #  state_id INTEGER PRIMARY KEY,
        #  parent_state_id INTEGER,
        #  state VARCHAR NOT NULL UNIQUE,
        #  distances VARCHAR NOT NULL,
        #  move VARCHAR NOT NULL,
        #  generation INTEGER NOT NULL
        # );
        # """

        query = """
        CREATE TABLE IF NOT EXISTS states (
         state_id INTEGER PRIMARY KEY,
         parent_state_id INTEGER,
         state VARCHAR NOT NULL UNIQUE,
         distances VARCHAR NOT NULL UNIQUE,
         move VARCHAR NOT NULL,
         generation INTEGER NOT NULL
        );
        """
        self.cursor.execute(query)

    def save(self,data):
        query ="""
        INSERT INTO states (state,move,parent_state_id,generation,distances)
        VALUES (?,?,?,?,?)
        """
        print("Executing >")
        try:
            self.cursor.execute(query,data)
            self.connection.commit()
            print("State saved :"+data[0])
        except sqlite3.IntegrityError:
            print("this state already exist :"+data[0])
        return self.cursor.lastrowid

    def save_group(self,datas):
        query ="""
        INSERT INTO states (state,move,parent_state_id,generation,distances)
        VALUES (?,?,?,?,?)
        """
        print("Executing >")
        for data in datas:
            try:
                self.cursor.execute(query,data)
                self.connection.commit()
                print("State saved :"+data[0])
            except sqlite3.IntegrityError:
                print("this state already exist :"+data[0])
        return self.cursor.lastrowid

    def get(self,state_id):
        query_temp ="""
        SELECT state,
        FROM states
        WHERE state_id = {state_id};
        """
        query = query_temp.format(
            state_id = state_id
        )
        print("Executing >")
        print(query)
        self.cursor.execute(query)
        self.connection.commit()
        obj = self.cursor.fetchall()[0][0]
        return str(obj)

    def get_states(self,generation,start=0,count = 50):
        query = """
        SELECT state_id,state FROM states
        WHERE generation=? and state_id >?
        LIMIT ?;
        """
        data=(generation,start,count)
        self.cursor.execute(query,data)
        self.connection.commit()
        obj = self.cursor.fetchall()
        states = list(map(lambda x: {"id":x[0],"state":x[1]},obj))
        return states
