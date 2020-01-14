#!/usr/bin/python3
def text_indentation(text):
    text_list = list(text)
    length = len(text_list)
    punctuation = {'.': 1, '?': 2, ':': 3}

    if type(text) is not str:
        raise TypeError("text must be a string")

    for i in range(0, length):
        if text_list[i] in punctuation:
            print(text_list[i], end='')
            if i < length - 1:
                text_list[i+1] = "\n\n"
        else:
            print(text_list[i], end='')
