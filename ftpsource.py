import socket as s
import getopt,sys,os

#This will keep the file data
HOST=""
PORT=0
PATH: str=""
CONNECTION=None


def __init(HOST,PORT):
    ftp = s.socket(s.AF_INET, s.SOCK_STREAM)
    try:
        ftp.connect((HOST, PORT))
        pass
    except:
        print("connection refused")
        os._exit(0)
        pass
    return ftp
    pass
def __des():
    CONNECTION.close()



def ftpprep( HOST:str,PORT:int,PATH:str):
    File=""
    global CONNECTION
    CONNECTION=__init(HOST,PORT)
    try:
        with open(PATH,"r") as file:
            File=file.read()
            ftpsend(File)
            pass
        pass
    except FileNotFoundError as e:
        print(str(e))
        __des()
        os._exit(0)
        pass
    return


def ftpsend(file:str):

    try:
        CONNECTION.sendall(file.encode())

        pass
    except s.error as e:
        print(str(e))
        CONNECTION.close()
        os._exit(0)
        pass


def main():
    global HOST
    global PORT,PATH
    argv = sys.argv[1:]
    if len(argv) < 6 < len(argv):
        print("error!!")
        return
    try:
        opts,arg = getopt.getopt(argv,"i:p:o:",["ip","port"])
        pass
    except getopt.GetoptError as e:
        print(str(e))
        return
    for o,a in opts:
        if o in ("-i","--ip"):
            HOST=a
            pass
        elif o in ("-p","--port"):
            PORT=int(a)
            pass
        elif o in ("-o"):
            PATH=a
            pass
        pass
    ftpprep(HOST,PORT,PATH)
    __des()




if __name__ == '__main__':
    main()
