from truncator import Truncator
import os,sys
from threadstesting import myThreader
from unzipper import Unzipper
from openFile import FileOpener
# Press the green button in the gutter to run the script.
def createThreds():
    threadslist=[]
    for i in range(0,30):
        threadslist.append(myThreader(i,f"Thread {i}"))
    k=1
    for threadi in threadslist:
            threadi.SetNumberOfBytes(k)
            k+=1
            threadi.start()
    for th in threadslist:
        th.join()
    threadslist.clear()
    # if k==3:
    #     for i in range(0,256):
    #         threadslist.append(myThreader(i,f"Thread{i}"))

if __name__ == '__main__':
     # tr=Truncator("D:\\python\\proiect\\files.zip",5)
     # #tr.GetFileHashFromArchive("sha1")
     # path,hasher=tr.GenerateInputData("sha1")
     # print(path,hasher)
     hash="c4529b8193aabed1c8d2cac33oadjfaoi4909"
     #hash = "c4529b8193aabed1c8d2cac3302b8a7b46c2e04c"
     path="D:\\python\\proiect\\files2.zip"
     myUnzipObject=Unzipper(path,hash)
     myThreader.unzipperObject=myUnzipObject
     createThreds()
     FileOpener(myThreader.unzipperObject.monitorObject.getPathOfFoundedFile()).open()
