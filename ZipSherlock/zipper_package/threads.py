import threading

from .unzipper import Unzipper


class myThreader(threading.Thread):
    """class which will handle creation of the threads"""
    # content="Static here"
    unzipperObject = Unzipper() #object responsible with unziiping
    number_of_threads = 0

    def __init__(self, threadId: int, threadName: str):
        """constructor"""
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.threadName = threadName
        self.numberOfBytesForRunnig = 0

    def SetNumberOfBytes(self, numberOfBytes:int):
        """setter
        numberOfBytes-> number of bytes for which thread will try to open and unzip the file
        """
        self.numberOfBytesForRunnig = numberOfBytes

    def GetNumberOfBytes(self):
        return self.numberOfBytesForRunnig

    def run(self):
        print(f"Thread {self.threadId} isworking")
        if Unzipper.monitorObject.getNumberOfBytesFound() == 0:
            myThreader.unzipperObject.createTempForFindingNeedBytes(self.GetNumberOfBytes(), self.threadId)
        else:
            # print(f"Start for {self.numberOfBytesForRunnig} bytes")
            myThreader.unzipperObject.workWithTempFiles(self.GetNumberOfBytes(), self.threadId, self.threadId,
                                                        myThreader.number_of_threads)
        print(f"Thread {self.threadId} should stop")
