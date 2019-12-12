import socket as s
import sys
import threading as t

'''
*this is create a group chat over a local server
'''

client_list=[]

def server_setup(host,port,listener):
    server=s.socket(s.AF_INET,s.SOCK_STREAM)
    server.setsockopt(s.SOL_SOCKET,s.SO_REUSEADDR,1)
    server.bind((host,port))
    server.listen(listener)
    print("[*]Server started at"+host+":"+str(port)+"\n")
    return server

def handle_client(client,addr):
    try:
        while True:
            try:
                req=client.recv(5000)
                if req:
                    broadcast(client,req,addr)
                    pass
                else:

                    remove(client, addr)
                    client.close()
                    break
                    pass
                pass
            except :
                continue

            pass
    except :
        remove(client,addr)
        client.close()

        pass
    return

def broadcast(client,req,addr):
    global client_list
    client_list.remove(client)
    msg="\n<"+addr+">"+req.decode()+" \n"
    for cl in client_list:

            try:
                cl.send(msg.encode("utf-8"))
                pass
            except:
                print("{} dissconnected!".format(addr))
                remove(cl, addr)
                cl.close()
                pass


            pass
    client_list.append(client)
    return

def remove(client,addr):
    global client_list
    client_list.remove(client)
    msg="\n<client"+addr+"is closed>\n"
    for cl in client_list:

            try:
                cl.send(msg.encode("utf-8"))
                pass
            except:
                pass
    pass
    return

def main():
    argv = sys.argv[1:]
    global client_list
    host=argv[0]
    port=int(argv[1])
    listener=int(argv[2])
    server=None
    try:
            server = server_setup(host, port, listener)
            while True:
                client,addr=server.accept()
                client_list.append(client)
                client.send("Welcome!\n\n".encode("utf-8"))
                print("[*]"+addr[0]+" connected")
                t.Lock().acquire()
                client_handler=t.Thread(target=handle_client,args=(client,addr[0]))
                client_handler.start()
                pass
            pass
    except:
            server.shutdown(s.SHUT_RDWR)
            server.close()
            pass
    pass



main()

0