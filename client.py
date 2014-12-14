import socket
import timeit
import os
def Main():
    so=socket.socket()
    ad="127.0.0.1"
    po=5000
    ad="jointedace"
    print("connecting")
    so.connect((ad,po))
    print("connected")
    ext=so.recv(2048).decode()
    i=0;
    for c in ext:
        if c=='.':
            break
        i=i+1
    ext="b"+ext[i:]
    #file=open("b.png",encoding='latin-1')
    file=open(ext,'wb')
    strt=timeit.timeit()
    print(strt)
    while True:
        data=so.recv(512)
        #print(data)
        
        if not data:
            break
        file.write(data)
    stp=timeit.timeit()
    #print(stp)
    print((stp-strt))
    input()
    file.close()
    exit()
if __name__=="__main__":
    Main()
    
    
