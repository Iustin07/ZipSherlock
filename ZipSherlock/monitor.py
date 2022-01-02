import os
import sys

class Monitor():
    """Class responsible for creating objects which will monitorize
        finding number of bytes which will open the archive
        can_read->if it's find the right combination of bytes which could read the archive
        path_of_found_file->path of the file if it's found
    """
    def __init__(self,numberOfBytesFound=0,canRead=False,pathOfFoundFile=""):
        self.numbers_of_bytes_needed=numberOfBytesFound
        self.can_read=canRead
        self.path_of_foundFile=pathOfFoundFile
    def setNumberOfBytesNeed(self,numberOfBytes:int):
        if self.numbers_of_bytes_needed==0:
            self.numbers_of_bytes_neede=numberOfBytes
        else:
            pass
    def setCanOpenFlag(self,boolValue:bool):
        if self.can_read==True:
            pass
        else:
            self.cant_read=boolValue
    def getCanOpenFlag(self):
        return self.can_read
    def getNumberOfBytesFound(self):
        return self.numbers_of_bytes_needed
    def setFoundFilePath(self,path):
        if path=="" or path==os.path.dirname(sys.argv[0]):
           return "path is incoorect. It does not contain name of a file"
        else:
            self.path_of_foundFile=path
    def getPathOfFoundedFile(self):
        return self.path_of_foundFile
    def printMonitorData(self):
        return f"number of bytes needed for openening archieve: {self.numbers_of_bytes_needed} | could read? {self.can_read}"
