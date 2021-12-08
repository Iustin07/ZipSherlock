import zipfile,io,gzip
import zlib
import os
import hashlib
import io
def function():
    return 0
def unzipArchieve(path:str):
    print("ok")
    to_find = getSha("D:\\python\\proiect\\files\\aplicatii_c_cpp_patrut.pdf")
    try:
        # import subprocess
        # subprocess.getoutput('zip -FF ' + path)
        z = zipfile.ZipFile(path)
        for i in z.infolist():
            if i.filename == "Tournaments _ CodeSignal.pdf":
                 print('am gasit fisierul cautat')
            #     f = z.open(i.filename)
            #     content = f.read()
            #     f = open('file.pdf', 'wb')
            #     f.write(content)
            print(i.filename, i.file_size)
        try:
            result= {name: z.read(name) for name in z.namelist()}
            print(len(result), result.keys())
            keyssha=[getSha2(key,result[key]) for key in result]
            if to_find in keyssha:
              index=keyssha.index(to_find)
              keys_list = list(result)
              key = keys_list[index]
              print("cheia este: ",key)
              full_path=path.split("\\")
              new_path=""
              for i in range(0, len(full_path)-1):
                  if i>0:
                      new_path+="\\"+full_path[i]
                  else:
                    new_path+=full_path[i]
              print(new_path)
              print(full_path)
              #z.write(z.read(key),new_path)
              z.extract(key,new_path)
            print(index)

        except:
            print("error on reading")
            #z.extractall()
        z.close()
    except zipfile.BadZipfile:
        print("error")
    #     z = zipfile.ZipFile(path)
    #     z.extractall()
   #try:
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

    # with open(path, 'w+b') as z:
    #     content=z.read()
    #     hex="c97c0000"
    #     bying=bytes.fromhex(hex)
    #     print(content)
    #     print(content+bying)
    #     print(bying)
    #     z.write(content+bying)
    #     z.truncate()

    # x=bytes(8)
    # print(x)
    # z.write(to_write)
    # z.close()

def getSha(filepath:str):
    m=hashlib.sha1()
    m.update(open(filepath,"rb").read())
    return m.hexdigest()
def getSha2(file_name,content):
    m=hashlib.sha1()
    m.update(content)
    return m.hexdigest()



unzipArchieve("D:\\python\\proiect\\proiect_testing.zip")
print("second")
print(print(getSha("D:\\python\\proiect\\aplicatii_c_cpp_patrut.pdf")))

