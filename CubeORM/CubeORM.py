import sqlite3
import os

from MCState.MCState import MagicCubeState
from MCStep.MCMoves import MCubeMoves

class CubeORM(object):
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
         move VARCHAR NOT NULL,
         generation INTEGER NOT NULL
        );
        """
        self.cursor.execute(query)


    def save(self,state,move,parent_state_id,generation):
        query_temp ="""
        INSERT INTO states (state,move,parent_state_id,generation)
        VALUES ("{state}","{move}",{parent_state_id},{generation})
        """
        query = query_temp.format(
            state = state.numeric(),
            move = str(move),
            parent_state_id = parent_state_id,
            generation = generation
        )
        print("Executing >")
        print(query)
        try:
            self.cursor.execute(query)
            self.connection.commit()
            print("State saved :"+state.numeric())
        except sqlite3.IntegrityError:
            print("this state already exist :"+state.numeric())
        return self.cursor.lastrowid

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
