from .bytesGenerator import getAllPosibbleCombinations
class Assigner:
    """class which will handle with assigning of a possible byte combination for thread"""
    all_possible_values=[]

    def assignValue(self,threadid,next_value):
        """Function which will return a value( byte combination) form a specicific index( nex_value)"""
        if next_value<len(self.all_possible_values):
            return self.all_possible_values[next_value]
        else:
            return ""
    def setAllPossibleValues(self,number_of_bytes_length):
        """Function which will generate all possible values when number of bytes is between 3 and 5"""
        Assigner.all_possible_values=getAllPosibbleCombinations(number_of_bytes_length)
