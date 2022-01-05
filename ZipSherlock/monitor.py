import os
import sys


class Monitor():
    """Class responsible for creating objects which will monitorize
        finding number of bytes which will open the archive
        can_read->if it find the right combination of bytes which could read the archive
        path_of_found_file->path of the file if it's found
    """
    list_of_numbers_ofBytes = []
    def __init__(self, numberOfBytesFound=0, canRead=False, pathOfFoundFile=""):
        self.numbers_of_bytes_needed = numberOfBytesFound
        self.can_read = canRead
        self.path_of_foundFile = pathOfFoundFile
        self.createdNewArchieve=""
    def getPathOfNewCreatedArchieve(self):
        return  self.createdNewArchieve
    def setCreatedArchivePath(self,path):
        self.createdNewArchieve=path
    def appendNumberOfBytes(self,numberBytes:int):
        self.list_of_numbers_ofBytes.append(numberBytes)
    def getListOfPossibleBytes(self):
        return self.list_of_numbers_ofBytes
    def setNumberOfBytesNeed(self, numberOfBytes: int):
        if self.numbers_of_bytes_needed == 0 and numberOfBytes!=0:
            self.numbers_of_bytes_needed = numberOfBytes
        elif numberOfBytes<self.numbers_of_bytes_needed:
            self.numbers_of_bytes_needed
        else:
            pass

    def setCanOpenFlag(self, boolValue: bool):
        if self.can_read == True:
            pass
        else:
            self.cant_read = boolValue

    def getCanOpenFlag(self):
        return self.can_read

    def getNumberOfBytesFound(self):
        return self.numbers_of_bytes_needed

    def setFoundFilePath(self, path):
        if path == "" or path == os.path.dirname(sys.argv[0]):
            return "path is incorect. It does not contain name of a file"
        else:
            self.path_of_foundFile = path

    def getPathOfFoundedFile(self):
        return self.path_of_foundFile

    def __str__(self):
        return f"number of bytes needed for openening archieve: {self.numbers_of_bytes_needed} | could read? {self.can_read}"
