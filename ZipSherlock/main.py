from truncator import Truncator
import os,sys
from threadstesting import myThreader
from unzipper import Unzipper
from colorama import Fore, Back, Style
from openFile import FileOpener
# Press the green button in the gutter to run the script.
NUMBER_OF_THREADS = 4
def createThreds(number_of_bytes:int):
    threadslist=[]
    if number_of_bytes<3 or number_of_bytes>=6:
        th = myThreader(1, f"Thread{1}")
        th.SetNumberOfBytes(number_of_bytes)
        th.start()
        th.join()
    elif number_of_bytes>=3 and number_of_bytes<=5:
        myThreader.unzipperObject.assingerObject.setAllPossibleValues(number_of_bytes)
        #print(myThreader.unzipperObject.assingerObject.all_possible_values)
        myThreader.number_of_threads=NUMBER_OF_THREADS
        for i in range(0,NUMBER_OF_THREADS):
            threadslist.append(myThreader(i, f"Thread{i}"))
        for threadi in threadslist:
            threadi.SetNumberOfBytes(number_of_bytes)
            threadi.start()
        joinThreds(threds_list=threadslist)
        #threadslist.clear()
def checkiffound():
    return myThreader.unzipperObject.monitorObject.getPathOfFoundedFile()!=""
def joinThreds(threds_list:list):
    for th in threds_list:
        th.join()
def checkBytes():
    return myThreader.unzipperObject.monitorObject.getNumberOfBytesFound()
def solveBsedOnBytesNumber():
    threadslist=[]
    for i in range(1,NUMBER_OF_THREADS+1):
        threadslist.append(myThreader(i, f"Thread {i}"))
    k=0
    while checkBytes()==0:
            for threadi in threadslist:
                threadi.SetNumberOfBytes(threadi.threadId)
                threadi.start()
            joinThreds(threds_list=threadslist)
            if checkBytes()==0:
                if k==0:
                    k=threadslist[len(threadslist)-1].threadId+1
                    threadslist.clear()
                    for i in range(k, NUMBER_OF_THREADS + k):
                        threadslist.append(myThreader(i, f"Thread {i}"))
                else:
                    k = threadslist[len(threadslist) - 1].threadId + 1
                    threadslist.clear()
                    for i in range(k, NUMBER_OF_THREADS+k):
                        threadslist.append(myThreader(i, f"Thread {i}"))
    number_of_bytes=min(myThreader.unzipperObject.monitorObject.getListOfPossibleBytes())
    return number_of_bytes

if __name__ == '__main__':
     # tr=Truncator("D:\\python\\proiect\\files.zip",5)
     # #tr.GetFileHashFromArchive("sha1")
     # path,hasher=tr.GenerateInputData("sha1")
     # print(path,hasher)
     #hash="c4529b8193aabed1c8d2cac33oadjfaoi4909"
     hash = "c4529b8193aabed1c8d2cac3302b8a7b46c2e04c"
     path="D:\\python\\proiect\\morefiles6.zip"
     myUnzipObject=Unzipper(path,hash)
     myThreader.unzipperObject=myUnzipObject
     number_of_bytes_needed_for_opening_archive=solveBsedOnBytesNumber()
     print(Fore.BLUE+str(number_of_bytes_needed_for_opening_archive))
     print(Fore.WHITE+"")
     createThreds(number_of_bytes_needed_for_opening_archive)
     FileOpener(myThreader.unzipperObject.monitorObject.getPathOfFoundedFile()).open()
     if number_of_bytes_needed_for_opening_archive>=6:
        os.remove(myThreader.unzipperObject.monitorObject.getPathOfNewCreatedArchieve())

