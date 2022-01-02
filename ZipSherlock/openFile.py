import os


class FileOpener:
    """class for which will open founded file"""
    def __init__(self,path:str):
        """constructor
        path-indicate path of the file after unzip it"""
        self.path=path
    def open(self):
        """function which will open the file using default programs of computer"""
        os.system(self.path)