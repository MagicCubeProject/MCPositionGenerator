#from GenerationController.GenControl import GControl
from GenerationController.GenerationController import GenerationController


def main():


    g = GenerationController("/work/MagicCubeLib/db","TestDB002")
    for x in range(5):
        g.start_gen(x)


if __name__ == "__main__":
    main()
locals()
