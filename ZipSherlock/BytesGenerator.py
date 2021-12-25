import random


def GenerateBytes(numberOfWAntedBytes:int):
    hex_list=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    #pentru number of bytes wanted=1
    #lsit=[i+j for i,j in zip(hex_list,hex_list.copy())]
    all_possible_combinations=[i+j for i in hex_list for j in hex_list]
    return all_possible_combinations

def RandomGenLengBytes(length:int):
    hex_list=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    sequence=""
    for i in range(length):
        first=random.choice(hex_list)
        second=random.choice(hex_list)
        hexbyte=first+second
        sequence+=hexbyte
    return sequence
numberBytes=int(input("Insert number of bytes to generate"))
print(GenerateBytes(1))
print(RandomGenLengBytes(numberBytes))