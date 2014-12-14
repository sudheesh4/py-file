import socket
def Main():
    so=socket.socket()
    "ad- address po-port"
    ad=socket.gethostname()
    #ad="127.0.0.1"
    po=5000
    filna=input()
    img=open(filna,'rb')
    so.bind((ad,po))
    so.listen(1)
    print("waiting for connecction..")
    c,addr=so.accept()
    print("connected!!")
    #img=open('a.png',encoding='latin-1')

    c.send(filna.encode())
    while True:
        imdata=img.read(512)
        if not imdata:
            break
       # print(imdata)
        c.send(imdata)
       # open("b.png",'w').write(imdata)
    imdata="\n Regards From Server"
    #c.send(imdata.encode())
    img.close()
    
    exit()
if __name__=="__main__":
    Main()
    
