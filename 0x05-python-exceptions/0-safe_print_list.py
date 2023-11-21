#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    su_total = 0
    for l in range(x):
        try:
            print(f"{my_list[l]}", end="")
            su_total += 1
        except IndexError:
            break
    print()
    return(su_total)
