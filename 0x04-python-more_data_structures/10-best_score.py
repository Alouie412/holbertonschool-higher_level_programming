#!/usr/bin/python3
def best_score(a_dictionary):
    best_score = 0
    best_name = ""

    if a_dictionary is None or a_dictionary is []:
        return None

    for key, value in a_dictionary.items():
        if value > best_score:
            best_score = value
            best_name = key

    return best_name
