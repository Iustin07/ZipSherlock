import tempfile
import zipfile
from hasher import Hasher
from bytesGenerator import RandomGenLengBytes
import sys, os
from monitor import Monitor
from assinger import Assigner
from colorama import Fore, Back, Style
import tempfile as tfile
import subprocess
class Unzipper:
    """class which will handle unzipping archive"""
    monitorObject = Monitor()
    assingerObject = Assigner()

    def __init__(self, path="", fileHash=""):
        """constructor
        path->path of the archive in which we will search for file arfter "fixing" it
        file_hash->hash of the file we want to search for
        """
        self.path = path
        self.file_hash = fileHash

    def readContent(self):
        content_original = b''
        with open(self.path, 'r+b') as z:
            content_original = z.read()
            # x = z.tell()
            # print(z.tell(), ' ', x)
        return content_original

    def checkParameters(self):
        if self.path == "" or self.file_hash == "":
            return 0
        return 1

    def unzipArchieve(self, new_path: str, number_of_bytes: int, threadId: int, next_value: int,number_of_threads:int):
        to_find = self.file_hash
        try:
            if Unzipper.monitorObject.getCanOpenFlag():
                print(f"passed with value {Unzipper.monitorObject.getCanOpenFlag()}")
                pass
            else:
                if number_of_bytes>=6:
                    subprocess.getoutput('zip -FF ' + new_path+" --out fixedzip.zip")
                    mod_path=f"{os.path.dirname(sys.argv[0])}\\fixedzip.zip"
                    print("aaaaaaaaaaaaaaaaa "+new_path)
                    Unzipper.monitorObject.setCreatedArchivePath(mod_path)
                    z = zipfile.ZipFile(mod_path)
                else:
                    z=zipfile.ZipFile(new_path)
                #Unzipper.monitorObject.setNumberOfBytesNeed(number_of_bytes)
                try:
                    result = {name: z.read(name) for name in z.namelist()}
                    Unzipper.monitorObject.setCanOpenFlag(True)
                    print(len(result), result.keys())
                    keyssha = [Hasher("sha1", result[key]).getHash() for key in result]
                    print(keyssha)
                    if to_find in keyssha:
                        index = keyssha.index(to_find)
                    else:
                        index = -1
                    if index == -1:
                        print("File not found")
                    else:
                        keys_list = list(result)
                        key = keys_list[index]
                        print("key is: ", key)
                        # words_from_key = key.split()
                        pathname = os.path.dirname(sys.argv[0])
                        z.extract(key, pathname)
                        Unzipper.monitorObject.setFoundFilePath(f"{pathname}\\{key}")
                        print(Fore.GREEN + Unzipper.monitorObject.getPathOfFoundedFile())
                        if number_of_bytes>=6:
                            os.remove(Unzipper.monitorObject.getPathOfNewCreatedArchieve())
                        return (1, 0)
                except:
                    print("error on reading")
                    Unzipper.monitorObject.setCanOpenFlag(False)
                    # os.remove(new_path)
                    if 3 <= number_of_bytes <= 5:
                        return (0, next_value + number_of_threads)#4-represent number of threads
                    elif number_of_bytes>=6:
                        return (0,0)
                    #     print(f"thread with id {threadId} will continue with {next_value+256}")
                    #     self.workWithTempFiles(number_of_bytes,threadId,next_value+256)#256->number of threads created
                z.close()
        except zipfile.BadZipfile:
            print("error zip is corrupt ")
            return (-1, 0)

    def workWithTempFiles(self, number_of_bytes: int, threadId: int, next_value: int,number_of_threads:int):
        if self.checkParameters() == 0:
            return "providing wrong parameters"
        if Unzipper.monitorObject.getPathOfFoundedFile() == "":
            content_original = self.readContent()#?????????
            try:
                ##########################################
                if 3>number_of_bytes or number_of_bytes>=6:
                    random_byte = bytes.fromhex(RandomGenLengBytes(number_of_bytes))
                elif 3<= number_of_bytes <= 5:
                    random_byte = bytes.fromhex(Unzipper.assingerObject.assignValue(threadId, next_value))
                if random_byte == "":
                    return 0
                #######################################
                # tmpfile.write(content_original + random_byte)
                # tmpfile.seek(0)
                # new_content = tmpfile.read()
                #print(random_byte)
                new_content = content_original + random_byte
                fd, path_temp = tfile.mkstemp(suffix=".zip", prefix=f"my{number_of_bytes+next_value}")  # can use anything
                try:
                    import  os
                    with os.fdopen(fd, 'wb') as tmpo:
                        tmpo.write(new_content)
                    answer_tuple = self.unzipArchieve(path_temp, number_of_bytes, threadId, next_value,number_of_threads)
                    print(answer_tuple)
                    if answer_tuple[0] == 0:
                        os.remove(path_temp)
                        self.workWithTempFiles(number_of_bytes, threadId, answer_tuple[1],number_of_threads)
                    if  answer_tuple[0] == -1 or answer_tuple[0]==1:
                        os.remove(path_temp)
                # finally:
                #      os.remove(path_temp)
                except:
                     print("somenthing ewnt wrong with removing path")
            except:
                print("issues with creation of temp file")
        return 0


    def findNeedBytes(self,path,number_of_bytes,threadId:int):
        #if Unzipper.monitorObject.getNumberOfBytesFound()==0:
            try:
                z = zipfile.ZipFile(path)
                Unzipper.monitorObject.setNumberOfBytesNeed(number_of_bytes)
                Unzipper.monitorObject.appendNumberOfBytes(number_of_bytes)
                z.close()
                return 1
                #os.remove(path)
            except zipfile.BadZipfile:
                print("error zip is corrupt ")
                return 0
                #os.remove(path)
    def createTempForFindingNeedBytes(self, number_of_bytes: int,threadId:int):
        if self.checkParameters() == 0:
            return "providing wrong parameters"
        if Unzipper.monitorObject.getNumberOfBytesFound()==0:
                content_original = self.readContent()
                random_byte = bytes.fromhex(RandomGenLengBytes(number_of_bytes))
                new_content = content_original + random_byte
                fd, path_temp = tfile.mkstemp(suffix=".zip", prefix=f"my{number_of_bytes}")  # can use anything
                try:
                        with os.fdopen(fd, 'wb') as tmpo:
                            tmpo.write(new_content)
                        result=self.findNeedBytes(path_temp,number_of_bytes,threadId)
                        # if result==1 or result==0:
                        #   os.remove(path_temp)
                finally:
                    os.remove(path_temp)
                # except:
                #     print("smtg went wrong")

        return 0