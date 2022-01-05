import hashlib


class Hasher:
    """Class used for instantiate objects which will calculate a specific hash:sha1,md5 of a file"""

    def __init__(self, method_of_hashing: str, content: bytes):
        """cosntructor
        method_of_hashing->indicate which method of hashing will be used
        content-> represent content which will be hashed
        """
        self.hashingMethod = method_of_hashing
        self.content = content

    def __str__(self):
        print(f'{self.hashingMethod}+{self.content}')

    def getHash(self):
        """method which will calculate hash of a file depending on desired hashing method"""
        if self.hashingMethod == 'sha1':
            m = hashlib.sha1()
            m.update(self.content)
            return m.hexdigest()
        elif self.hashingMethod == 'md5':
            m = hashlib.md5()
            m.update(self.content)
            return m.hexdigest()
