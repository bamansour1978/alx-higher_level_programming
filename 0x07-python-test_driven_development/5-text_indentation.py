#!/usr/bin/
# 5-text_indentation.py
""" A text_indentation """


def text_indentation(text):
    """
    This function takes in one argument, 
    which should be the inputted paragraph of text and returns it

    args:
        - `text`: The given paragraph 
    raise:
        if text isn't str
    
    """
    if type(text) is not str:
        raise TypeError('text must be a string')
    re_t = text.replace('.', '.\n\n')
    re_t = re_t.replace(':', ':\n\n')
    re_t = re_t.replace('?', '?\n\n')
    re_t = re_t.replace('\n', '\n')
    print(re_t)
