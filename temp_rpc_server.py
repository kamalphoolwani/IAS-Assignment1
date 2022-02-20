import sys 
import socket
import json
from server_procedures import *

dataType =  {"int":int, "str":str,"float": float,"complex" :complex, "list":list, "tuple" :tuple, 
            "range": range,"dict": dict,"set": set, "frozenset" : frozenset, "bool" : bool,
            "bytes": bytes, "bytearray": bytearray, "memoryview": memoryview}

# def foo(a,b):
#     c = a+b
#     return c

def handleConn(conn,addr):
    response = ""
    print("Client Connected")
    # while True:
    recv = conn.recv(4096)
    # print(recv.decode())
        # if len(recv)<=0:
        #     break
    response += recv.decode()
    data = json.loads(response)
    # print(data)
    # for data in res:
    fName = data['procedure_name']
    p = ""
    f = 0
    for para in data['parameters']:
        var = para['parameter_name']
        type = para['data_type']
        if f==0:
            p += str(dataType[type](var))
            f=1
        else:
            p += ", " + str(dataType[type](var))
    
    return_type = data['return_type']
    res = eval(fName + "(" + p + ")")
    print("Value Sent Successfully!!")
    conn.send(str(res).encode())




host_ip = "127.0.0.1"
host_port = 6070

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket Created Successsfully!!")
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((host_ip, host_port))
 
sock.listen(5)

while True:
    conn, addr = sock.accept()
    handleConn(conn,addr)


