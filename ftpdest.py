import socket as s
import getopt,os,sys


def __init(host,port):
    reciever = s.socket(s.AF_INET,s.SOCK_STREAM)
    reciever.setsockopt(s.SOL_SOCKET,s.SO_REUSEADDR,1)
    reciever.bind((host,port))
    reciever.listen(1)
    print("[*]Listening...\n")
    return reciever

def __dest(reciever):
    reciever.close()
    os._exit(0)


def recvall(reciever):
    try:
        client, addr = reciever.accept()
        pass
    except:
        __dest(reciever)
        return
    Filecontents=""
    while True:
        try:
            chunk=client.recv(4096).decode()
            pass
        except s.error as e:
            print(str(e))
            return
        if not chunk:
            break
        Filecontents+=chunk
        pass
    client.close()
    return Filecontents
    pass

def writeout(reciever,path):
    file=open(path,"w")
    try:
        file.write(recvall(reciever))
        pass
    except:
        print("some error occured While writing the file!")
        file.close()
        __dest(reciever)
        return
    print("writing done!!")
    file.close()
    return

def ftpdest(port,path):
    reciever = __init("0.0.0.0", port)
    writeout(reciever, path)
    __dest(reciever)

def main():
    port=0
    path=""
    argv=sys.argv[1:]
    if len(argv)<4 or len(argv)>4:
        print("arguemnts count!!")
        return
    try:
        opts,args = getopt.getopt(argv,"p:O:",["--port"])
        pass
    except getopt.GetoptError as e:
        print(str(e))
        return
    for o,a in opts:
        if o in ("-p","--port"):
            port=int(a)
            pass
        elif o in ("-O"):
            path=a
            pass
        pass
    ftpdest(port,path)

    return

if __name__ == '__main__':
    main()




