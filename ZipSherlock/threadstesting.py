import threading
from unzipper import Unzipper
from monitor import Monitor
from bytesGenerator import RandomGenLengBytes
class myThreader(threading.Thread):
    """class which will handle creation of the threads"""
   #content="Static here"
    unzipperObject=Unzipper()
    number_of_threads=0
    def __init__(self,threadId:int,threadName:str):
        threading.Thread.__init__(self)
        self.threadId=threadId
        self.threadName=threadName
        self.numberOfBytesForRunnig=0

    def SetNumberOfBytes(self,numberOfBytes):
        self.numberOfBytesForRunnig=numberOfBytes
    def GetNumberOfBytes(self):
        return  self.numberOfBytesForRunnig
    def run(self):
        print(f"Thread {self.threadId} isworking")
        if Unzipper.monitorObject.getNumberOfBytesFound()==0:
            myThreader.unzipperObject.createTempForFindingNeedBytes(self.GetNumberOfBytes(),self.threadId)
        else:
            #print(f"Start for {self.numberOfBytesForRunnig} bytes")
            myThreader.unzipperObject.workWithTempFiles(self.GetNumberOfBytes(),self.threadId,self.threadId,myThreader.number_of_threads)
        print(f"Thread {self.threadId} should stop")
