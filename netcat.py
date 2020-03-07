import tclient as TCLIENT
import tcp_server as TCPSERVER
import ftpsource as FTPSOURCE
import ftpdest as FTPDEST
import portscanner as PS
import sys,getopt,os
import socket as s
import pty

Server=False
Client=True
Ftps=False
Ftpd=False
Ps=False

def help():
    help="-l                no of listeners\n" \
         "-p     --port     port number\n" \
         "-i     --ip       host ip\n" \
         "-o                path of file to be send\n" \
         "-O                path of the file to be recieved\n" \
         "-z                portscanner\n" \
         "-h     --help     help" \
         "-n                arp scan"\
         "\n" \
         "\n" \
         "usage:\n" \
         "1. python3 netcat.py -l 15 -p 2222         create a tcp server in localhost on port 2222 with 15 listeners\n" \
         "2. python3 netcat.py -i 0.0.0.0 -p 2222    create a tcp client to connect to host 0.0.0.0 at port 2222\n" \
         "3. python3 netcat.py -p 2222 -O test.ext   create a reciver at port 2222 and recive file \n" \
         "4. python3 netcat.py -i 0.0.0.0 -p 2222 -o test.txt send a file to the host \n" \
         "5. python3 netcat.py -z -i 0.0.0.0 -p 1-90 scans all the port from 1 to 90 for the host\n"
    print(help)
    os._exit(0)
    pass
def main():
    global Server
    global Client
    global Ftps
    global Ftpd
    global Ps
    port=0
    host=""
    path=""
    listener=0
    open_port_list=[]

    argv=sys.argv[1:]
    if len(argv)==0:
        help()
        return

    try:
        opts,agr = getopt.getopt(argv,"l:p:i:o:O:zh",["port","ip","help"])
        pass
    except getopt.error or ValueError as e:
        print(str(e)+"\n")
        help()
        return
    for o,a in opts:
        if o in ("-l"):
            listener=int(a)
            Server=True
            pass
        elif o in ("-p","--port"):
            port=a
            pass
        elif o in ("-i","--ip"):
            host=a
            pass
        elif o in ("-o",):
            path=a
            Ftps=True
            pass
        elif o in ("-O"):
            path=a
            Ftpd = True
            pass
        elif o in ("-z"):
            Ps=True
            pass
        elif o in ("-h","--help"):
            help()
            return
        elif o in ("-n"):
            pty.pty("sudo ./netdiscover.py")
            pass
        pass
    if Server==True and ( Ftpd==True or Ftps == True or Ps== True):
        help()
        return
    elif Ftpd==True and (Server==True or Ftps == True or Ps== True):
        help()
        return
    elif Ftps==True and (Server==True or Ftpd==True or Ps== True):
        help()
        return
    elif Ps==True and (Server==True or Ftpd==True or Ftps == True):
        help()
        return
    if Server:
        Client=False
        try:
            port=int(port)
            pass
        except ValueError as e:
            print(str(e))
            return
            pass
        TCPSERVER.CLS(port,listener)
        return
    elif Ftps:
        Client = False
        try:
            port = int(port)
            pass
        except ValueError as e:
            print(str(e))
            return
            pass
        FTPSOURCE.ftpprep(host,port,path)
        return
    elif Ftpd:
        Client = False
        try:
            port = int(port)
            return
            pass
        except ValueError as e:
            print(str(e))
            pass
        FTPDEST.ftpdest(port,path)
        return
    elif Ps:
        Client = False
        ports=["",""]
        i=0
        for prt in port:
            if prt == "-":
                i+=1
                pass
            else:
                ports[i]=ports[i]+prt

        open_port_list=PS.scan(host,int(ports[0]),int(ports[1]))
        flag=True
        for ports in open_port_list:
            flag=False
            print("[*] "+str(ports)+" open")

        if flag:
            print("No port open")
        os._exit(0)
    else:
        try:
            port = int(port)
            pass
        except ValueError as e:
            print(str(e))
            return
            pass
        TCLIENT.client(host, port)
        return
    pass

if __name__ == '__main__':
    main()



