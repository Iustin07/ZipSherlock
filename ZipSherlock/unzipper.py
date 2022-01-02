import tempfile
import zipfile
from hasher import Hasher
from bytesGenerator import RandomGenLengBytes
import sys,os
from monitor import Monitor
class Unzipper:
    monitorObject = Monitor()
    def __init__(self,path="",fileHash=""):
        self.path=path
        self.file_hash=fileHash
    def readContent(self):
        content_original = b''
        with open(self.path, 'r+b') as z:
            content_original = z.read()
            # x = z.tell()
            # print(z.tell(), ' ', x)
        return content_original
    def checkParameters(self):
        if self.path=="" or self.file_hash=="":
            return 0
        return 1
    def unzipArchieve(self,new_path:str,number_of_bytes:int):
        print("ok")
        to_find =self.file_hash
        try:
            if Unzipper.monitorObject.getCanOpenFlag():
                print(f"passed with value {Unzipper.monitorObject.getCanOpenFlag()}")
                pass
            else:
                z = zipfile.ZipFile(new_path)
                Unzipper.monitorObject.setNumberOfBytesNeed(number_of_bytes)

                try:
                    result = {name: z.read(name) for name in z.namelist()}
                    Unzipper.monitorObject.setCanOpenFlag(True)
                    print(len(result), result.keys())
                    keyssha = [Hasher("sha1", result[key]).getHash() for key in result]
                    print(keyssha)
                    if to_find in keyssha:
                        index = keyssha.index(to_find)
                    else:
                        index=-1
                    if index==-1:
                        print("File not found")
                    else:
                        keys_list = list(result)
                        key = keys_list[index]
                        print("key is: ", key)
                        #words_from_key = key.split()
                        pathname = os.path.dirname(sys.argv[0])
                        z.extract(key, pathname)
                        Unzipper.monitorObject.setFoundFilePath(f"{pathname}\\{key}")
                except:
                    print("error on reading")
                    Unzipper.monitorObject.setCanOpenFlag(False)
                z.close()
        except zipfile.BadZipfile:
            print("error zip is corrupt ")

    def workWithTempFiles(self,number_of_bytes:int):
        if self.checkParameters()==0:
            return "providing wrong parameters"
        content_original = self.readContent()
        tmpfile=tempfile.TemporaryFile()
        try:
            random_byte = bytes.fromhex(RandomGenLengBytes(number_of_bytes))
            tmpfile.write(content_original + random_byte)
            tmpfile.seek(0)
            new_content = tmpfile.read()
            import os
            import tempfile as tfile
            fd, path_temp = tfile.mkstemp(suffix=".zip", prefix=f"my{number_of_bytes}")  # can use anything
            try:
                print(path_temp)
                print(fd)
                with os.fdopen(fd, 'wb') as tmpo:
                        # do stuff with temp file
                    tmpo.write(new_content)
                    # TryToOpen(path)
                self.unzipArchieve(path_temp,number_of_bytes)
            finally:
                os.remove(path_temp)
        finally:
            tmpfile.close()
        return 0