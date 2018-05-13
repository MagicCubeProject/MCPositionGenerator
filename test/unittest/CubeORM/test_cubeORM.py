from unittest import TestCase
from MCState.MCState import MagicCubeState
from MCStep.MCMoves import MCubeMoves
from MCStep.MCStep import MCStep

class TestCubeORM(TestCase):
    def test_init(self):
        from CubeORM.CubeORM import CubeORM
        orm = CubeORM("/work/MagicCubeLib/db","test_db")

    def test_save(self):
        from CubeORM.CubeORM import CubeORM
        orm = CubeORM("/work/MagicCubeLib/db","test_db")

        mcState = MagicCubeState()
        orm.save(mcState,MCubeMoves.IDENTICAL,0,1)
        step = MCStep(mcState)
        step.moves([MCubeMoves.UP_DOUBLE_DOWN_DOUBLE, MCubeMoves.FRONT_BACK_INVERS])
        id = orm.save(mcState,MCubeMoves.IDENTICAL,0,1)
        orm.get(id)


    def test_update(self):
        from CubeORM.CubeORM import CubeORM
        orm = CubeORM("/work/MagicCubeLib/db","test_db")
        mcState = MagicCubeState()
        step = MCStep(mcState)
        step.moves([MCubeMoves.UP_DOUBLE_DOWN_DOUBLE])
        id = orm.save(mcState,MCubeMoves.UP_DOUBLE_DOWN_DOUBLE,0,1)
        step.moves([MCubeMoves.FRONT_BACK_INVERS])
        id = orm.update(id,mcState,MCubeMoves.FRONT_BACK_INVERS,0,1)

    def test_delete(self):
        from CubeORM.CubeORM import CubeORM
        orm = CubeORM("/work/MagicCubeLib/db","test_db")
        mcState = MagicCubeState()
        step = MCStep(mcState)
        step.moves([MCubeMoves.UP_DOUBLE_DOWN])
        id = orm.save(mcState,MCubeMoves.UP_DOUBLE_DOWN,0,2)
        orm.delete(id)
