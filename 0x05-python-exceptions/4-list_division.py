#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):

    new_list = []
    type_err = 0
    index_err = 0
    zero_err = 0

    for num in range(0, list_length):
        try:
            division = my_list_1[num] / my_list_2[num]
        except IndexError:
            index_err = 1
            division = 0
        except ZeroDivisionError:
            division = 0
            zero_err = 1
        except TypeError:
            division = 0
            type_err = 1
        finally:
            new_list.append(division)
    if zero_err == 1:
        print("division by 0")
    if type_err == 1:
        print("wrong type")
    if index_err == 1:
        print("out of range")

    return new_list
