import random,os
import zipfile
from hasher import Hasher

class Truncator:
    """class from where create objects responsable with making data for input"""
    def __init__(self,path:str,numberOfBytes:int):
        self.path=path
        self.bytesToDelete=numberOfBytes
    def GenerateInputData(self,method_of_hashing:str):
        """Main function for generate truncate archive with missing x bytes.
        Will return a path for truncate archive and hash for choosen file"""
        file_hash=self.GetFileHashFromArchive(method_of_hashing)
        self.TruncateArchive()
        return self.path,file_hash

    def TruncateArchive(self):
     """function which delete x bytes from the end of archieve"""
     if self.bytesToDelete<=0:
         print("you can't delete 0 or less tha 0 bytes")
     else:
        with open(self.path, 'r+b') as z:
            z.read()
            x=z.tell()
            print(f"number of bytes from archieve is : {x}")
            z.truncate(z.tell()-self.bytesToDelete)
            z.seek(0)
            content=z.read()
            print(content)
            print(z.tell(),' ',x)
     return self.path

    def TruncateWithoutSpecificFunction(self, bytesToDelete: int):
        """function which truncate archive withou using truncate() explicity"""
        size = os.path.getsize(self.path)
        print(size)
        content = b''
        with open(self.path, 'r+b') as z:
            newsize = size - bytesToDelete
            content = z.read(newsize)
            print(content)
            print(size, ' ', newsize)
        with open(self.path, "w+b") as myarchive:
            myarchive.write(content)
        return self.path
    def GetFileHashFromArchive(self,typeOfHashing:str):
        """Function which takes a random file from archive and calculate hash for it"""
        try:
            zipObject = zipfile.ZipFile(self.path)
            listOfFiles=zipObject.infolist()
            numberOfFilesInArchive=len(listOfFiles)
            randomIndexOfaFile=random.randrange(numberOfFilesInArchive)
            choosenFileName=listOfFiles[randomIndexOfaFile]
            content=zipObject.read(choosenFileName.filename)
            hasherObject=Hasher("sha1",content)
            #print(content)
            # print(choosenFileName.filename)
            # print(hasherObject.getHash())
            zipObject.close()
            return hasherObject.getHash()
        except (zipfile.BadZipfile):
            print("error zip is corrupt")
        finally:
            zipObject.close()
            print("file close succesfully")


