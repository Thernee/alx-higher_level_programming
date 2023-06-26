#!/usr/python3

def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for num in range(0, x):
            print(my_list[num], end="")
            count += 1
    except IndexError:
        pass
    finally:
        print()
        return count
