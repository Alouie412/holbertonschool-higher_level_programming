#!/usr/bin/python3
def search_replace(my_list, search, replace):
    return ([i for i is not search else replace for i in my_list])
