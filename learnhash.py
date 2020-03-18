import hashlib

def main():
    digester = hashlib.md5()
    with open('G:\CS001\R-3.6.3-win.exe','rb') as file_stream:
        
        # data=file_stream.read(1024)
        # while data:
        #     digester.update(data)
        #     data=file_stream.read(1024)

        file_iter = iter(lambda : file_stream.read(1024),b'')
        for data in file_iter:
            digester.update(data)
    print(digester.hexdigest())

if __name__ == "__main__":
    main()