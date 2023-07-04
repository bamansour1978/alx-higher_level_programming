#!/usr/bin/python3

def text_identation(text):

    if type(text) is not str:
        raise TypeError('text must be a string')
    re_t = text.replace('.', '.\n\n')
    re_t = re_t.replace(':', ':\n\n')
    re_t = re_t.replace('?', '?\n\n')
    re_t = re_t.replace('\n', '\n')
    print(re_t)
