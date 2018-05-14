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
        data = CubeORM.CubeCata(mcState,MCubeMoves.IDENTICAL,0,1)
        orm.save(data)
        step = MCStep(mcState)
        step.moves([MCubeMoves.UP_DOUBLE_DOWN_DOUBLE, MCubeMoves.FRONT_BACK_INVERS])
        data2 = CubeORM.CubeCata(mcState,MCubeMoves.IDENTICAL,0,1)
        id = orm.save(data2)
        orm.get(id)

    def test_save_group(self):
        from CubeORM.CubeORM import CubeORM
        orm = CubeORM("/work/MagicCubeLib/db","test_db")
        mcState = MagicCubeState()
        data = CubeORM.CubeCata(mcState,MCubeMoves.IDENTICAL,0,1)
        mcState2 = MagicCubeState()
        step = MCStep(mcState)
        step.moves([MCubeMoves.UP_DOUBLE_DOWN_INVERS, MCubeMoves.FRONT_BACK_INVERS])
        data2 = CubeORM.CubeCata(mcState,MCubeMoves.UP_DOUBLE_DOWN_INVERS,0,1)
        orm.save_group([data,data2])

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
