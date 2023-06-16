#!/usr/bin/python3

def roman_to_int(roman_string):

    if (roman_string is None or not isinstance(roman_string, str)):
        return (0)

    rom_dictionary = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
    }
    number = 0

    for j in range(len(roman_string)):
        if rom_dictionary.get(roman_string[j], 0) == 0:
            return (0)

        if (j != (len(roman_string) - 1) and
                rom_dictionary[roman_string[j]] < rom_dictionary[roman_string[j + 1]]):
                number += rom_dictionary[roman_string[j]] * -1

        else:
            number += rom_dictionary[roman_string[j]]
    return (number)
