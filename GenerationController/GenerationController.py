import multiprocessing
from functools import partial

from MagicCube.MagicCube import MagicCube

from CubeORM.MagicORM import MagicORM
from GenerationController.MCMoves import MCubeMoves
from GenerationController.MCStep import MCStep


class GenerationController(object):
    def __init__(self,path,dbname):
        self.orm = MagicORM(path,dbname)
        self.initial_state = MagicCube()
        data = (
            str(self.initial_state),
            str(MCubeMoves.IDENTICAL),
            1,
            0,
            str(self.initial_state.distances())
        )
        self.initial_state_id = self.orm.save(data)

    def start_gen(self,gen):
        size=0
        states = self.orm.get_states(gen-1)
        while(len(states) > 0):
            size = states[-1]["id"]
            for state_dict in states:
                work_state = state_dict["state"]
                print("Generate childs of :",work_state)
                parent_id = state_dict["id"]
                #child_states_data = GenerationController.gen_child_state_data(work_state,parent_id,gen)

                child_states_data = list()
                for move in MCubeMoves:
                    step = MCStep(work_state)
                    step.move(move)
                    data = (
                        str(step.magicCube),
                        str(move),
                        parent_id,
                        gen,
                        str(step.magicCube.distances())
                    )
                    child_states_data.append(data)
                self.orm.save_group(child_states_data)
            states = self.orm.get_states(gen-1,parent_id)

        return size
    # def gen_child_state_data(work_state,parent_id,gen):
    #     f_p = partial(
    #         GenerationController.f,
    #         work_state= work_state,
    #         parent_id = parent_id,
    #         gen = gen
    #         )
    #
    #
    #     pool = multiprocessing.Pool(processes=46)
    #     child_states_data = pool.map(
    #         f_p, MCubeMoves
    #     )
    #
    #     return child_states_data
    #
    # def f(move_id,work_state,parent_id,gen):
    #         move = MCubeMoves(move_id)
    #         step = MCStep(work_state)
    #         step.move(move)
    #         data = (
    #                 str(step.magicCube),
    #                 str(move),
    #                 parent_id,
    #                 gen,
    #                 str(step.magicCube.distances())
    #                 )
    #         return data

