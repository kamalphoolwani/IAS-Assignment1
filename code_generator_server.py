import json
import sys

header = ["import sys \n", "import socket \n","import json\n","from server_procedures import *\n","from _thread import *\n","\n"]
static_code = '''
dataType =  {"int":int, "str":str,"float": float,"complex" :complex, "list":list, "tuple" :tuple, 
            "range": range,"dict": dict,"set": set, "frozenset" : frozenset, "bool" : bool,
            "bytes": bytes, "bytearray": bytearray, "memoryview": memoryview}

def handleConn(conn,addr):
    response = ""
    print("Client Connected")
    recv = conn.recv(4096)
    response += recv.decode()
    data = json.loads(response)

    fName = data['procedure_name']
    p = ""
    f = 0
    for para in data['parameters']:
        var = para['parameter_name']
        type = para['data_type']
        if f==0:
            if type == "str":
                var = "'" + str(var) + "'"
            p += str(dataType[type](var))
            f=1
        else:
            if type == "str":
                var = "'" + str(var) + "'"
            p += ", " + str(dataType[type](var))
    
    return_type = data['return_type']
    try:
        res = eval(fName + "(" + p + ")")
        print("Value Sent Successfully!!")
        conn.send(str(res).encode())
    except:
        res = "Error"
        print("Value Sent Successfully!!")
        conn.send(str(res).encode())




if __name__ == "__main__":
    host_ip = "127.0.0.1"
    host_port = 6070

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print("Socket Created Successsfully!!")
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((host_ip, host_port))
    
    sock.listen(5)

    while True:
        conn, addr = sock.accept()
        start_new_thread(handleConn,(conn,addr))

'''

def writeHeaders(fName):
    file_rpc = open(fName, 'w')
    file_rpc.writelines(header)
    file_rpc.write(static_code)
    file_rpc.close()
    print("Done")

if __name__ == "__main__":
    jsonFName = sys.argv[1]
    file_to_write = "rpc_server.py"

    writeHeaders(file_to_write)