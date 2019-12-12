import socket as s
import threading as t
import sys,getopt
import os

def client(HOST,PORT):
    CLIENT = s.socket(s.AF_INET,s.SOCK_STREAM)
    try:
        CLIENT.connect((HOST,PORT))
        pass
    except s.error as e:
        print("Connection Refused!!")
        return
    try:
        while True:
            try:
                try:
                    sendmsg=t.Thread(target=send_msg,args=(CLIENT,))
                    sendmsg.start()
                    pass
                except t.ThreadError as e:
                    print("\n"+str(e)+"\n")
                    os._exit(0)
                    pass
                try:
                    msg=CLIENT.recv(4095).decode()

                    pass
                except :
                    print("server closed!")
                    CLIENT.close()
                    os._exit(0)
                    pass
                if msg:
                    print("<Server>" + msg + "\n")
                    pass
                else:
                    print("server closed!")
                    CLIENT.close()
                    os._exit(0)

                pass
            except:
                os._exit(0)
        pass
    except:
        os._exit(0)
    pass

def send_msg(CLIENT):
    while True:
        msg=input("\n")
        try:
            CLIENT.send(msg.encode("utf-8"))
            pass
        except:
            os._exit(0)
            pass
        pass



def main():
    global HOST
    global PORT
    argv=sys.argv[1:]
    if len(argv) < 4:
        print("Error!")
        return
    try:
        opts,gets= getopt.getopt(argv,"i:p:",["--ip","--port"])
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
        pass
    try:
        client(HOST,PORT)
        pass
    except:
        os._exit(0)
        pass
    os._exit(0)
    return




if __name__ == '__main__':
    try:
        main()
        pass
    except:
        os._exit(0)
