#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        prd = a / b
    except ZeroDivisionError:
        prd = None
        return prd
    finally:
        print("Inside result:{}".format(prd))
    return prd
