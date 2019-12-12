import socket as s
import sys, getopt,os

HOST=""
PORT=0


def scan(HOST,PORT1,PORT):
    i=PORT1
    port_list=[]
    flag=True

    while i<=PORT:
        client = s.socket(s.AF_INET, s.SOCK_STREAM)
        try:
            client.connect((HOST,i))
            port_list.append(i)
            flag=False
            pass
        except s.error as er:
            pass
        except KeyboardInterrupt:
            for port in port_list:
                flag = False
                print("[*] port" + str(port) + " is open\n")
                pass
            if flag:
                print("no port is open")
            os._exit(0)
            pass
        i+=1
        client.close()

        pass

    return port_list

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
    flag=True
    port_list=scan(HOST,0,PORT)
    for port in port_list:
        flag=False
        print("[*] port"+str(port)+" is open\n")
        pass
    if flag:
        print("no port is open")




if __name__ == '__main__':
    main()
