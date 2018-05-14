from GenerationController.GenControl import GControl


def main():
    g = GControl("/work/MagicCubeLib/db")
    # g.start_fisrt_gen()
    # g.start_second_gen()
    g.start_gen(3)
    #g.start_third_gen()
    # g.start_4_gen()
    # g.start_5_gen()

if __name__ == "__main__":
    main()
