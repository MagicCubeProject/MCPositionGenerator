import base64
import sqlite3
import os
import pickle


class CubeORM(object):
    class CubeCata(object):
        def __init__(self,state,move,parent_state_id,generation):
            self.state = state
            self.move = move
            self.parent_state_id =parent_state_id
            self.generation = generation

        def tuple(self):
            obj = pickle.dumps(self.state,3)
            bobj = sqlite3.Binary(obj)
            data = (
                self.state.numeric(),
                str(self.move),
                self.parent_state_id,
                self.generation,
                bobj
            )
            return data

    def __init__(self,path,name="cube"):
        suffix = ".db"
        db_path = os.path.join(path, name + suffix)
        self.connection = sqlite3.connect(db_path)
        self.cursor = self.connection.cursor()
        self.__crate_table()

    def __crate_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS states (
         state_id INTEGER PRIMARY KEY,
         parent_state_id INTEGER,
         state VARCHAR NOT NULL UNIQUE,
         objetc BLOB NOT NULL,
         move VARCHAR NOT NULL,
         generation INTEGER NOT NULL
        );
        """
        self.cursor.execute(query)


    def save(self,data):
        query ="""
        INSERT INTO states (state,move,parent_state_id,generation,objetc)
        VALUES (?,?,?,?,?)
        """
        print("Executing >")
        try:
            self.cursor.execute(query,data.tuple())
            self.connection.commit()
            print("State saved :"+data.state.numeric())
        except sqlite3.IntegrityError:
            print("this state already exist :"+data.state.numeric())
        return self.cursor.lastrowid

    def save_group(self,datas):
        query ="""
        INSERT INTO states (state,move,parent_state_id,generation,objetc)
        VALUES (?,?,?,?,?)
        """
        print("Executing >")
        for data in datas:
            try:
                self.cursor.execute(query,data.tuple())
                self.connection.commit()
                print("State saved :"+data.state.numeric())
            except sqlite3.IntegrityError:
                print("this state already exist :"+data.state.numeric())
        return self.cursor.lastrowid

    def get(self,state_id):
        query_temp ="""
        SELECT objetc
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
        return pickle.loads(obj)

    def update(self,state_id,state,move,parent_state_id,generation):
        query_temp ="""
        UPDATE states
        SET state = "{state}", move = "{move}", parent_state_id = {parent_state_id},generation={generation}
        WHERE state_id = {state_id};
        """
        query = query_temp.format(
            state = state.numeric(),
            move = str(move),
            parent_state_id = parent_state_id,
            state_id = state_id,
            generation=generation
        )
        print("Executing >")
        print(query)
        try:
            self.cursor.execute(query)
            self.connection.commit()
            print("State updated :"+state.numeric())
            return state_id
        except sqlite3.IntegrityError:
            print("this state already exist :"+state.numeric())
        return None

    def delete(self,state_id):
        query_temp ="""
        DELETE FROM states
        WHERE state_id = {state_id};
        """
        query = query_temp.format(
            state_id = state_id
        )
        print("Executing >")
        print(query)
        self.cursor.execute(query)
        self.connection.commit()
