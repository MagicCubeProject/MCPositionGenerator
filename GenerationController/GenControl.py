import copy
import pickle

from MCState.MCState import MagicCubeState
from MCStep.MCMoves import MCubeMoves
from MCStep.MCStep import MCStep
from CubeORM.CubeORM import CubeORM


class GControl(object):
    def __init__(self,path):
        self.orm = CubeORM(path,"test2")
        self.initial_state = MagicCubeState()
        data = CubeORM.CubeCata(self.initial_state,MCubeMoves.IDENTICAL,1,0)
        self.initial_state_id = self.orm.save(data)

    def start_fisrt_gen(self):
        self.fisrt_gen_dict = {}

        for move in MCubeMoves:
            print("Move is :"+str(move))
            initial_state = MagicCubeState()
            step = MCStep(initial_state)
            step.move(move)
            data = CubeORM.CubeCata(initial_state,move,self.initial_state_id,1)
            parent_id_1 = self.orm.save(data)
            self.fisrt_gen_dict[initial_state]=parent_id_1

        print("Done first gen")


    def start_gen(self,gen):
        states = self.orm.get_states(gen)
        while(len(states) > 0):
            for state_dict in states:
                work_state = pickle.loads(state_dict["object"])
                print("Generate childs of :",work_state.numeric())
                work_id = state_dict["id"]
                child_states_data = list()
                for move in MCubeMoves:
                    initial_state = copy.deepcopy(work_state)
                    step = MCStep(initial_state)
                    step.move(move)
                    data = CubeORM.CubeCata(initial_state,move,work_id,gen+1)
                    child_states_data.append(data)
                self.orm.save_group(child_states_data)
            states = self.orm.get_states(gen,work_id)

    def start_second_gen(self):
        self.fisrt_second_dict = {}
        for state in self.fisrt_gen_dict.keys():
            parent_state_id =  self.fisrt_gen_dict[state]
            for move in MCubeMoves:
                print("Move is :" + str(move))
                new_state = copy.deepcopy(state)
                step = MCStep(new_state)
                step.move(move)
                data = CubeORM.CubeCata(new_state, move,parent_state_id, 2)
                parent_id = self.orm.save(data)
                self.fisrt_second_dict[new_state] = parent_id

        print("Done Second gen")

    def start_third_gen(self):
        self.the_3_dict = {}
        for state in self.fisrt_second_dict.keys():
            parent_state_id =  self.fisrt_second_dict[state]
            for move in MCubeMoves:
                print("Move is :" + str(move))
                new_state = copy.deepcopy(state)
                step = MCStep(new_state)
                step.move(move)
                data = CubeORM.CubeCata(new_state, move,parent_state_id,3)
                parent_id = self.orm.save(data)
                self.the_3_dict[new_state] = parent_id
        print("Done first gen")

    def start_4_gen(self):
        self.the_4_dict = {}
        for state in self.the_3_dict.keys():
            parent_state_id =  self.the_3_dict[state]
            for move in MCubeMoves:
                print("Move is :" + str(move))
                new_state = copy.deepcopy(state)
                step = MCStep(new_state)
                step.move(move)
                parent_id = self.orm.save(new_state, move,parent_state_id,4)
                self.the_4_dict[new_state] = parent_id
        print("Done first gen")

    def start_5_gen(self):
        #self.the_4_dict = {}
        for state in self.the_4_dict.keys():
            parent_state_id =  self.the_4_dict[state]
            for move in MCubeMoves:
                print("Move is :" + str(move))
                new_state = copy.deepcopy(state)
                step = MCStep(new_state)
                step.move(move)
                parent_id = self.orm.save(new_state, move,parent_state_id,5)
                #self.the_4_dict[new_state] = parent_id
        print("Done first gen")
