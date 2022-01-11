import random
import itertools
from itertools import product


def generateBytes(numberOfWAntedBytes: int):
    """calculate all possible bytes of length 1 in hex"""
    hex_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    all_possible_combinations = [i + j for i in hex_list for j in hex_list]
    return all_possible_combinations


def RandomGenLengBytes(length: int):
    """
    Function which will calculate a random hexbytes string of specified length
    :param length: int
    :return: hexstring
    """
    hex_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
    sequence = ""
    for i in range(0, length):
        first = random.choice(hex_list)
        second = random.choice(hex_list)
        hex_byte = first + second
        sequence += hex_byte
    return sequence


def getAllPosibbleCombinations(number_of_bytes):
    """
    Function which will generare all possible values( hex strings reprezenting number of bytes) for a given number of bytes
    :param number_of_bytes:
    :return: list of hex strings
    """
    general_lists = []
    created_list = []
    number_of_lists = number_of_bytes - 2
    for index in range(0, number_of_lists):
        general_lists.append(generateBytes(1))
    if number_of_lists == 1:
        return [var1 + RandomGenLengBytes(2) for var1 in general_lists[0]]
    elif number_of_lists == 2:
        created_list = [var1 + var2 + RandomGenLengBytes(2) for var1, var2 in
                        product(general_lists[index - 1], general_lists[index])]
        return created_list
    else:
        for index in range(1, number_of_lists):
            if index == 1:
                created_list = [var1 + var2 for var1, var2 in product(general_lists[index - 1], general_lists[index])]
            else:
                created_list = [var1 + var2 + RandomGenLengBytes(2) for var1, var2 in
                                product(created_list, general_lists[index])]
    return list(created_list)
