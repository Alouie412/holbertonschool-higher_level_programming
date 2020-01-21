#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    count = 0

    with open(filename, 'r', encoding='utf-8') as f:
        if nb_lines <= 0:
            print(f.read(), end='')
        else:
            for i in f:
                if count < nb_lines:
                    print(i, end='')
                count += 1
