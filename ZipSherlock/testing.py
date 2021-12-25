import binascii
import collections
import zipfile, io, gzip
import zlib
import os
import hashlib,random,tempfile
import io


def function():
    return 0


# def unzipArchieve(path:str):
# print("ok")
# to_find = getSha("D:\\python\\proiect\\files\\aplicatii_c_cpp_patrut.pdf")
# try:
#     # import subprocess
#     # subprocess.getoutput('zip -FF ' + path)
#     z = zipfile.ZipFile(path)
#     print(z.infolist()[0])
#     for i in z.infolist():
#         if i.filename == "Tournaments _ CodeSignal.pdf":
#              print('am gasit fisierul cautat')
#         #     f = z.open(i.filename)
#         #     content = f.read()
#         #     f = open('file.pdf', 'wb')
#         #     f.write(content)
#         print(i.filename, i.file_size)
#     z.close()
# #     try:
# #         result= {name: z.read(name) for name in z.namelist()}
# #         print(len(result), result.keys())
# #         keyssha=[getSha2(key,result[key]) for key in result]
# #         if to_find in keyssha:
# #           index=keyssha.index(to_find)
# #           keys_list = list(result)
# #           key = keys_list[index]
# #           print("cheia este: ",key)
# #           full_path=path.split("\\")
# #           new_path=""
# #           for i in range(0, len(full_path)-1):
# #               if i>0:
# #                   new_path+="\\"+full_path[i]
# #               else:
# #                 new_path+=full_path[i]
# #           print(new_path)
# #           print(full_path)
# #           #z.write(z.read(key),new_path)
# #           z.extract(key,new_path)
# #         print(index)
# #
# #     except:
# #         print("error on reading")
# #         #z.extractall()
# #     z.close()
# except zipfile.BadZipfile:
#     print("error")
#


#     z = zipfile.ZipFile(path)
#     z.extractall()
# try:
# with open(path, 'rb') as compressed:
#     data = compressed.read()
#     file_no = 0
#     while data:
#         d = zlib.decompressobj(16+zlib.MAX_WBITS)
#         with open('{}_decompressed.{}'.format(path, file_no), 'wb') as f:
#             f.write(d.decompress(data,zlib.DEFLATED))
#         data = d.unused_data
#         file_no += 1
#     zip_archive=gzip.GzipFile(path,"r")
#     print(zip_archive.read())
#     files=zip_archive.open('Tournaments _ CodeSignal')
#     bytes_io = io.BytesIO(files.read())
#     print(bytes_io)
#     # with open("output.pdf", "wb") as f:
#     #     f.write(bytes_io.getbuffer())
#     # for item in zip_archive.filelist:
#     #     print(item)
#     # print(f'\nThere are {len(zip_archive.filelist)} ZipInfo objects present in archive')
#
# except zipfile.BadZipFile:
#     print("w", "Unable to retrieve metadata from {fname}: archive is corrupt.".format(fname=path))


# x=bytes(8)
# print(x)
# z.write(to_write)
# z.close()



def getSha(filepath: str):
    m = hashlib.sha1()
    m.update(open(filepath, "rb").read())
    return m.hexdigest()


def getSha2(file_name, content):
    m = hashlib.sha1()
    m.update(content)
    return m.hexdigest()


def ContentToHex(path: str):
    with open(path, 'rb') as z:
        content = z.read()
        #print(content)
        hexcontent = binascii.hexlify(content)
        with open("uot.txt", 'w') as f:
            f.write(hexcontent.decode("utf-8"))
        print(type(hexcontent))
        # slice k=0,k+1
        k = 0
        bytes_lit = [hexcontent[i:i + 4] for i in range(0, len(hexcontent), 2) if hexcontent[i:i + 2] == b'81']
        # frequency_table={b:bytes_lit.count(b) for b in bytes_lit}
        print(len(bytes_lit))
        print(len(set(bytes_lit)))
        #print(sorted(calculateFrequencies(bytes_lit).items(), key=lambda x: x[1]))
        return hexcontent

def calculateFrequencies(d: list):
    result = {}
    for b in d:
        # if len(result)==256:
        #     break
        if b in result:
            continue
        else:
            result[b] = d.count(b)
    return result


def PrintInfo(path: str):
    try:
        import subprocess
        print(subprocess.getoutput('zip -FF ' + path + ' --out fixed2.zip'))
        z = zipfile.ZipFile(path)
        print(z.infolist()[0])
        for i in z.infolist():
            print(i.filename, i.file_size)
    except zipfile.BadZipfile:
        print("error")
def RandomGenLengBytes(length:int):
    hex_list=['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
    first=random.choice(hex_list)
    second=random.choice(hex_list)
    print(first+second)
    return first+second

def TryToOpen(path:str):
   opened=False
   while not opened:
    try:
        z = zipfile.ZipFile(path)
        content=ContentToHex(path)
        print(content)
        opened=True
        for i in z.infolist():
            print(i.filename, i.file_size)
        z.close()
    except zipfile.BadZipFile:
        print("BadZip file")
        PutContent(path,content,byter)

def PutContent(path,content,byte:hex):
    content=content+byte
    return 0


def workWithTempFiles(path:str):
    content_original=b''
    x=0
    with open(path, 'r+b') as z:
        content_original= z.read()
        x = z.tell()
        print(z.tell(), ' ', x)
    list_files=[]
    print(content_original)
    for i in range(0,4):
     temp = tempfile.TemporaryFile()
     list_files.append(temp)
    for file in list_files:
        print("another file")
        try:
            random_byte=bytes.fromhex(RandomGenLengBytes(1))
            file.write(content_original+random_byte)
            file.seek(0)
            print(len(file.read()))
            file.seek(0)
            print(file.read(22222))
        finally:
            file.close()
    return 0
def playing_around(path):

       with open(path, 'r+b') as z:
           content = z.read()
           x = z.tell()
           hex = "01"
           bying = bytes.fromhex(hex)
           print(content)
           print(z.tell(), ' ', x)
           #print(binascii.hexlify(content))
           print(content+bying)
           print(bying)
           # z.write(content+bying)
           # z.truncate()
workWithTempFiles("D:\\python\\proiect\\files2.zip")
#playing_around("D:\\python\\proiect\\files2.zip")
# PrintInfo("D:\\python\\proiect\\files2.zip")
# unzipArchieve("D:\\python\\proiect\\files.zip")
print("second")
# print(print(getSha("D:\\python\\proiect\\aplicatii_c_cpp_patrut.pdf")))
# ContentToHex("D:\\python\\proiect\\signals.zip")
#print(TruncateManually("D:\\python\\proiect\\files2.zip", 5))
#TryToOpen("D:\\python\\proiect\\files.zip")