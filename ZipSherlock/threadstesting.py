import threading
from unzipper import Unzipper
from monitor import Monitor
from bytesGenerator import RandomGenLengBytes
class myThreader(threading.Thread):
   #content="Static here"
   unzipperObject=Unzipper()
   all_posible=[]
   def __init__(self,threadId,threadName):
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
        myThreader.unzipperObject.workWithTempFiles(self.GetNumberOfBytes())
        print(f"Thread {self.threadId} should stop")
