import copy

from MCState.MCState import MagicCubeState
from MCStep.MCMoves import MCubeMoves
from MCStep.MCStep import MCStep
from CubeORM.CubeORM import CubeORM


class GControl(object):
    def __init__(self,path):
        self.orm = CubeORM(path)
        self.initial_state = MagicCubeState()
        self.initial_state_id = self.orm.save(self.initial_state,MCubeMoves.IDENTICAL,1,0)

    def start_fisrt_gen(self):
        self.fisrt_gen_dict = {}

        for move in MCubeMoves:
            print("Move is :"+str(move))
            initial_state = MagicCubeState()
            step = MCStep(initial_state)
            step.move(move)
            parent_id_1 = self.orm.save(initial_state,move,self.initial_state_id,1)
            self.fisrt_gen_dict[initial_state]=parent_id_1

        print("Done first gen")

    def start_second_gen(self):
        self.fisrt_second_dict = {}
        for state in self.fisrt_gen_dict.keys():
            parent_state_id =  self.fisrt_gen_dict[state]
            for move in MCubeMoves:
                print("Move is :" + str(move))
                new_state = copy.deepcopy(state)
                step = MCStep(new_state)
                step.move(move)
                parent_id = self.orm.save(new_state, move,parent_state_id, 2)
                self.fisrt_second_dict[new_state] = parent_id

        print("Done first gen")

    def start_third_gen(self):
        self.the_3_dict = {}
        for state in self.fisrt_second_dict.keys():
            parent_state_id =  self.fisrt_second_dict[state]
            for move in MCubeMoves:
                print("Move is :" + str(move))
                new_state = copy.deepcopy(state)
                step = MCStep(new_state)
                step.move(move)
                parent_id = self.orm.save(new_state, move,parent_state_id,3)
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
