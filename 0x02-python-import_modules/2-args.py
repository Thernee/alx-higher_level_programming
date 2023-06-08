#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    lenght = len(argv)

    if lenght == 1:
        print(lenght - 1, "arguments.")

    elif lenght == 2:
        print(lenght - 1, "argument:")
        print("{}: {}".format(lenght - 1, argv[1]))

    elif lenght > 2:
        print(lenght - 1, "arguments:")
        for n in range(1, lenght):
            print("{}: {}".format(n, argv[n]))
