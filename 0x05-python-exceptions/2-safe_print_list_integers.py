#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count = 0 
    try:
        for num in range(0, x):
            print("{:d}".format(my_list[num]), end="")
            count += 1
    except ValueError:
        pass
    finally:
        print()
        return count
