from Enumerations.facet import Facet
from MagicCube.MagicCube import MagicCube

from GenerationController.MCMoves import MCubeMoves


class MCStep(object):
    def __init__(self , magicCubeState = None):
        if magicCubeState is None:
            self.magicCube = MagicCube()
        else:
            self.magicCube = MagicCube(magicCubeState)

    def move(self,move_type = MCubeMoves.IDENTICAL):
        if move_type is MCubeMoves.IDENTICAL:
            pass
        #Simple Moves
        elif move_type is MCubeMoves.FRONT:
            self.magicCube.rotate(Facet.FRONT)
        elif move_type is MCubeMoves.RIGHT:
            self.magicCube.rotate(Facet.RIGHT)
        elif move_type is MCubeMoves.DOWN:
            self.magicCube.rotate(Facet.DOWN)
        elif move_type is MCubeMoves.UP:
            self.magicCube.rotate(Facet.UP)
        elif move_type is MCubeMoves.LEFT:
            self.magicCube.rotate(Facet.LEFT)
        elif move_type is MCubeMoves.BACK:
            self.magicCube.rotate(Facet.BACK)
        #Revers of simple moves
        elif move_type is MCubeMoves.FRONT_INVERS:
            self.magicCube.rotate(Facet.FRONT,True)
        elif move_type is MCubeMoves.RIGHT_INVERS:
            self.magicCube.rotate(Facet.RIGHT,True)
        elif move_type is MCubeMoves.DOWN_INVERS:
            self.magicCube.rotate(Facet.DOWN,True)
        elif move_type is MCubeMoves.UP_INVERS:
            self.magicCube.rotate(Facet.UP,True)
        elif move_type is MCubeMoves.LEFT_INVERS:
            self.magicCube.rotate(Facet.LEFT,True)
        elif move_type is MCubeMoves.BACK_INVERS:
            self.magicCube.rotate(Facet.BACK,True)
        #Double Moves
        elif move_type is MCubeMoves.FRONT_DOUBLE:
            self.magicCube.rotate(Facet.FRONT)
            self.magicCube.rotate(Facet.FRONT)
        elif move_type is MCubeMoves.RIGHT_DOUBLE:
            self.magicCube.rotate(Facet.RIGHT)
            self.magicCube.rotate(Facet.RIGHT)
        elif move_type is MCubeMoves.DOWN_DOUBLE:
            self.magicCube.rotate(Facet.DOWN)
            self.magicCube.rotate(Facet.DOWN)
        elif move_type is MCubeMoves.UP_DOUBLE:
            self.magicCube.rotate(Facet.UP)
            self.magicCube.rotate(Facet.UP)
        elif move_type is MCubeMoves.LEFT_DOUBLE:
            self.magicCube.rotate(Facet.LEFT)
            self.magicCube.rotate(Facet.LEFT)
        elif move_type is MCubeMoves.BACK_DOUBLE:
            self.magicCube.rotate(Facet.BACK)
            self.magicCube.rotate(Facet.BACK)
        #Hard Moves
        elif move_type is MCubeMoves.FRONT_BACK:
            self.magicCube.rotate(Facet.FRONT)
            self.magicCube.rotate(Facet.BACK)
        elif move_type is MCubeMoves.FRONT_BACK_INVERS:
            self.magicCube.rotate(Facet.FRONT)
            self.magicCube.rotate(Facet.BACK,True)
        elif move_type is MCubeMoves.FRONT_BACK_DOUBLE:
            self.magicCube.rotate(Facet.FRONT)
            self.magicCube.rotate(Facet.BACK)
            self.magicCube.rotate(Facet.BACK)
        elif move_type is MCubeMoves.RIGHT_LEFT:
            self.magicCube.rotate(Facet.RIGHT)
            self.magicCube.rotate(Facet.LEFT)
        elif move_type is MCubeMoves.RIGHT_LEFT_INVERS:
            self.magicCube.rotate(Facet.RIGHT)
            self.magicCube.rotate(Facet.LEFT,True)
        elif move_type is MCubeMoves.RIGHT_LEFT_DOUBLE:
            self.magicCube.rotate(Facet.RIGHT)
            self.magicCube.rotate(Facet.LEFT)
            self.magicCube.rotate(Facet.LEFT)
        elif move_type is MCubeMoves.UP_DOWN:
            self.magicCube.rotate(Facet.UP)
            self.magicCube.rotate(Facet.DOWN)
        elif move_type is MCubeMoves.UP_DOWN_INVERS:
            self.magicCube.rotate(Facet.UP)
            self.magicCube.rotate(Facet.DOWN,True)
        elif move_type is MCubeMoves.UP_DOWN_DOUBLE:
            self.magicCube.rotate(Facet.UP)
            self.magicCube.rotate(Facet.DOWN)
            self.magicCube.rotate(Facet.DOWN)

        elif move_type is MCubeMoves.FRONT_INVERS_BACK:
            self.magicCube.rotate(Facet.FRONT,True)
            self.magicCube.rotate(Facet.BACK)
        elif move_type is MCubeMoves.FRONT_INVERS_BACK_INVERS:
            self.magicCube.rotate(Facet.FRONT,True)
            self.magicCube.rotate(Facet.BACK,True)
        elif move_type is MCubeMoves.FRONT_INVERS_BACK_DOUBLE:
            self.magicCube.rotate(Facet.FRONT,True)
            self.magicCube.rotate(Facet.BACK)
            self.magicCube.rotate(Facet.BACK)
        elif move_type is MCubeMoves.RIGHT_INVERS_LEFT:
            self.magicCube.rotate(Facet.RIGHT,True)
            self.magicCube.rotate(Facet.LEFT)
        elif move_type is MCubeMoves.RIGHT_INVERS_LEFT_INVERS:
            self.magicCube.rotate(Facet.RIGHT,True)
            self.magicCube.rotate(Facet.LEFT,True)
        elif move_type is MCubeMoves.RIGHT_INVERS_LEFT_DOUBLE:
            self.magicCube.rotate(Facet.RIGHT,True)
            self.magicCube.rotate(Facet.LEFT)
            self.magicCube.rotate(Facet.LEFT)
        elif move_type is MCubeMoves.UP_INVERS_DOWN:
            self.magicCube.rotate(Facet.UP,True)
            self.magicCube.rotate(Facet.DOWN)
        elif move_type is MCubeMoves.UP_INVERS_DOWN_INVERS:
            self.magicCube.rotate(Facet.UP,True)
            self.magicCube.rotate(Facet.DOWN,True)
        elif move_type is MCubeMoves.UP_INVERS_DOWN_DOUBLE:
            self.magicCube.rotate(Facet.UP,True)
            self.magicCube.rotate(Facet.DOWN)
            self.magicCube.rotate(Facet.DOWN)

        elif move_type is MCubeMoves.FRONT_DOUBLE_BACK:
            self.magicCube.rotate(Facet.FRONT)
            self.magicCube.rotate(Facet.FRONT)
            self.magicCube.rotate(Facet.BACK)
        elif move_type is MCubeMoves.FRONT_DOUBLE_BACK_INVERS:
            self.magicCube.rotate(Facet.FRONT)
            self.magicCube.rotate(Facet.FRONT)
            self.magicCube.rotate(Facet.BACK,True)
        elif move_type is MCubeMoves.FRONT_DOUBLE_BACK_DOUBLE:
            self.magicCube.rotate(Facet.FRONT)
            self.magicCube.rotate(Facet.FRONT)
            self.magicCube.rotate(Facet.BACK)
            self.magicCube.rotate(Facet.BACK)
        elif move_type is MCubeMoves.RIGHT_DOUBLE_LEFT:
            self.magicCube.rotate(Facet.RIGHT)
            self.magicCube.rotate(Facet.RIGHT)
            self.magicCube.rotate(Facet.LEFT)
        elif move_type is MCubeMoves.RIGHT_DOUBLE_LEFT_INVERS:
            self.magicCube.rotate(Facet.RIGHT)
            self.magicCube.rotate(Facet.RIGHT)
            self.magicCube.rotate(Facet.LEFT,True)
        elif move_type is MCubeMoves.RIGHT_DOUBLE_LEFT_DOUBLE:
            self.magicCube.rotate(Facet.RIGHT)
            self.magicCube.rotate(Facet.RIGHT)
            self.magicCube.rotate(Facet.LEFT)
            self.magicCube.rotate(Facet.LEFT)
        elif move_type is MCubeMoves.UP_DOUBLE_DOWN:
            self.magicCube.rotate(Facet.UP)
            self.magicCube.rotate(Facet.UP)
            self.magicCube.rotate(Facet.DOWN)
        elif move_type is MCubeMoves.UP_DOUBLE_DOWN_INVERS:
            self.magicCube.rotate(Facet.UP)
            self.magicCube.rotate(Facet.UP)
            self.magicCube.rotate(Facet.DOWN,True)
        elif move_type is MCubeMoves.UP_DOUBLE_DOWN_DOUBLE:
            self.magicCube.rotate(Facet.UP)
            self.magicCube.rotate(Facet.UP)
            self.magicCube.rotate(Facet.DOWN)
            self.magicCube.rotate(Facet.DOWN)
