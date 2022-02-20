import sys 
import socket
import json

dataType =  {"int":int, "string":str,"float": float,"complex" :complex, "list":list, "tuple" :tuple, 
            "range": range,"dict": dict,"set": set, "frozenset" : frozenset, "bool" : bool,
            "bytes": bytes, "bytearray": bytearray, "memoryview": memoryview}

def conToServer(message):
    host_ip = "127.0.0.1"
    host_port = 6070
    rcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    rcp_server.connect((host_ip, host_port))
    message = json.dumps(message)
    print(message)
    message = message.encode()
    rcp_server.sendall(message)
    response=""
    # while True:
    #     recv = rcp_server.recv(4096)
    #     if recv is NULL:
    #         break
    #     response += recv.decode()
    recv = rcp_server.recv(4096)
    response += recv.decode()

    rcp_server.close()
    return response

def foo(a,b):
    message = dict()
    message['procedure_name'] = "foo"
    message["parameters"] = [
        {
            "parameter_name":a,
            "data_type":"int"
        },
        {
            "parameter_name":b,
            "data_type":"int"
        } 
    ]

    message["return_type"] = "int"
    val = conToServer(message)
    print(val)


foo(2,5)