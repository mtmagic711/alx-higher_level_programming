#!/usr/bin/python3
def search_replace(my_list, search, replace):
    fun = lambda x : replace if x == search else x
    new_list = list(map(fun, my_list))
    return new_list
