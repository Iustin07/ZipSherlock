import random,os
import zipfile
from .hasher import Hasher

class Truncator:
    """class from where create objects responsable with making data for input"""
    def __init__(self,path:str,numberOfBytes:int):
        """Constructor
        :param path: path of the archive
        :param numberOfBytes: number of bytes wanted to be deleted from the end of archive
        """
        self.path=path
        self.bytes_to_delete=numberOfBytes
    def GenerateInputData(self,method_of_hashing:str):
        """Main function for generate truncate archive with missing x bytes.
        :param method_of_hashing: which method will be used for hashing the file
        :return: a path for truncate archive and hash for choosen file as str both"""
        file_hash=self.GetFileHashFromArchive(method_of_hashing)
        self.TruncateArchive()
        return self.path,file_hash

    def TruncateArchive(self):
     """function which delete x bytes from the end of archieve"""
     if self.bytes_to_delete<=0:
         print("you can't delete 0 or less tha 0 bytes")
     else:
        with open(self.path, 'r+b') as z:
            z.read()
            x=z.tell()
            print(f"number of bytes from archieve is : {x}")
            z.truncate(z.tell()-self.bytes_to_delete)
            z.seek(0)
            content=z.read()
            #print(content)
            print(z.tell(),' ',x)
     return self.path

    def TruncateWithoutSpecificFunction(self, bytesToDelete: int):
        """function which truncate archive without using truncate() explicity"""
        size = os.path.getsize(self.path)
        print(size)
        content = b''
        with open(self.path, 'r+b') as z:
            newsize = size - bytesToDelete
            content = z.read(newsize)
            #print(content)
            print(size, ' ', newsize)
        with open(self.path, "w+b") as myarchive:
            myarchive.write(content)
        return self.path
    def GetFileHashFromArchive(self,typeOfHashing:str):
        """Function which takes a random file from archive and calculate hash for it
        :param typeOfHashing:method which is used for hashing the file
        :return: string-representing hash of choosen file
        """
        try:
            zipObject = zipfile.ZipFile(self.path)
            list_of_file_files=zipObject.infolist()
            numberOfFilesInArchive=len(list_of_file_files)
            random_index_of_afile=random.randrange(numberOfFilesInArchive)
            choosen_file_name=list_of_file_files[random_index_of_afile]
            content=zipObject.read(choosen_file_name.filename)
            hasherObject=Hasher(typeOfHashing,content)
            #print(content)
            # print(choosen_file_name.filename)
            # print(hasherObject.getHash())
            zipObject.close()
            return hasherObject.getHash()
        except (zipfile.BadZipfile):
            print("error zip is corrupt")
        finally:
            zipObject.close()
            print("file close succesfully")


