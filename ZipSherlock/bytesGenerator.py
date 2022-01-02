import random
import itertools

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
def GenerateThreeFormStringBytes(length:int):
    all_posiible=[]
    blist=GenerateBytes(1)
    for bt in blist:
        sequence=bt
        sequence+=RandomGenLengBytes(2)
        all_posiible.append(sequence)
    return all_posiible
def GetCartesianProduct(number):
    l1=l2=GenerateBytes(1)
    p = itertools.product(l1, l2)
    all_possible=[]
    for x,y in p:
        sequence=str(x)+str(y)
        sequence+=RandomGenLengBytes(2)
        all_possible.append(sequence)
    return all_possible
#numberBytes=int(input("Insert number of bytes to generate"))
#print(GenerateBytes(1))
# print(RandomGenLengBytes(numberBytes:int))
#print(GenerateMyStringBytes(3))
#print(GetCartesianProduct(4))