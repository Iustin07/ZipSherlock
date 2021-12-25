import threading
import time
import random
class myThreader(threading.Thread):
   content="Static here"
   def __init__(self,threadId,threadName):
    threading.Thread.__init__(self)
    self.threadId=threadId
    self.threadName=threadName
   def run(self):
        print(f"thread with id {self.threadId}")
        x=GetCombination(self.name)
        print(x)
        print(f"Thread stop {self.threadId}")
def GetCombination(name):
        hex_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
        first = random.choice(hex_list)
        second = random.choice(hex_list)
        print(first + second)
        print(f"{name} choose {first+second}")
        return first + second
def createThreds():
    threadslist=[]
    for i in range(0,4):
        threadslist.append(myThreader(i,f"Thread {i}"))
    for threadi in threadslist:
        threadi.start()
        print(threadi.getName(),threadi.content)
createThreds()