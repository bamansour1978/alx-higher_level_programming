#!/usr/bin/python3

def roman_to_int(roman_string):

    a = roman_string
    if (a is None or not isinstance(a, str)):
        return (0)

    rom_dic = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
    }
    number = 0

    for j in range(len(a)):
        if rom_dic.get(a[j], 0) == 0:
            return (0)

        if (j != (len(a) - 1) and rom_dic[a[j]] < rom_dic[a[j + 1]]):
            number += rom_dic[a[j]] * -1

        else:
            number += rom_dic[a[j]]
    return (number)
