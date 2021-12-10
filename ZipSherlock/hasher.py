import hashlib
class Hasher:
    """Class used for instantiate objects which will calculate a specific hash:sha1,md5,sha256,sha125 of a file"""
    def __init__(self,method_of_hashing:str,content:bytes):
        self.hashingMethod=method_of_hashing
        self.content=content
    def getData(self):
        print(f'{self.hashingMethod}+{self.content}')
    def getHash(self):
        """method which will calculate hash of a file depending on desire hashing method"""
        if self.hashingMethod=='sha1':
                m = hashlib.sha1()
                m.update(self.content)
                return m.hexdigest()
        elif self.hashingMethod=='md5':
            m=hashlib.md5()
            m.update(self.content)
            return m.hexdigest()



