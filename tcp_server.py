import socket as s
import threading as t
import sys,os
import getopt

# client list
client_list = []


# this is to create a server on local host of aa given port

def Create_tcp_server(port=12345, listener=1):
    host = "0.0.0.0"
    server = s.socket(s.AF_INET, s.SOCK_STREAM)
    server.setsockopt(s.SOL_SOCKET, s.SO_REUSEADDR, 1)
    server.bind((host, port))
    server.listen(listener)
    print("[*]listening to " + host + ":" + str(port) + "\n")

    return server


# this is the tread function which will be used to manage multiple users

def broadcast():
    while True:
        msg = str(input())
        msg="\n"+msg+"\n"
        for client in client_list:
            try:
                client.send(msg.encode("utf-8"))
                pass
            except s.error as e:
                print(str(e))
                client_list.remove(client)
                client.close()


def client_handler(client, addr):
    try:
        while True:
            try:
                msg = client.recv(4096)
                pass
            except:
                continue
                pass
            if msg:
                print("\n<" + addr + ">" + msg.decode() + "\n")

                pass
            else:
                print("<" + addr + "> is down!")
                client_list.remove(client)
                client.close()
                pass
            pass
        pass
    except s.error as e:
        print(str(e))
        client_list.remove(client)
        client.close()
        pass
    return

def CLS(port:int=2222, listener:int=15):
    try:
        server = Create_tcp_server(port, listener)
        bcast = t.Thread(target=broadcast)
        while True:
            try:
                bcast.start()
                pass
            except:
                pass
            client, addr = server.accept()
            client_list.append(client)
            client.send("\nWelcome\n".encode("utf-8"))
            print("[*] " + addr[0] + " is connected")
            try:
                client_handle = t.Thread(target=client_handler, args=(client, addr[0]))
                client_handle.start()
                pass
            except t.ThreadError as e:
                print(e)
                break
                pass
            pass
        pass
    except:
        print("End")
        os._exit(0)


def main():
    listener=0
    port=0
    argv=sys.argv[1:]
    if len(argv) <4:
        print("too less argument")
        return
        pass
    else:
        try:
            opts,args = getopt.getopt(argv,"l:p:",["port","listeners"])
            pass
        except getopt.GetoptError as e:
            print(str(e))
            return
        for o,a in opts:
            if o in ("-l","--listeners"):
                listener=int(a)
                pass
            elif o in ("-p","--port"):
                port=int(a)
                print(port)
                pass
            pass
        CLS(port,listener)




if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
