from email.mime import message
import json
import sys

header = ["import sys \n", "import socket \n","import json\n","\n"]
static_code = '''
dataType =  {"int":int, "str":str,"float": float,"complex" :complex, "list":list, "tuple" :tuple, 
            "range": range,"dict": dict,"set": set, "frozenset" : frozenset, "bool" : bool,
            "bytes": bytes, "bytearray": bytearray, "memoryview": memoryview}

def conToServer(message):
    host_ip = "127.0.0.1"
    host_port = 6070
    rcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    rcp_server.connect((host_ip, host_port))
    message = json.dumps(message)
    # print(message)
    message = message.encode()
    rcp_server.sendall(message)
    response=""
    recv = rcp_server.recv(4096)
    response += recv.decode()

    rcp_server.close()
    return response


'''
def writeHeaders(fName):
    file_rpc = open(fName, 'w')
    file_rpc.writelines(header)
    file_rpc.write(static_code)
    file_rpc.close()
    print("Done")

def generateFunc(fileName,procName,para_list,return_type):
    lines = list()
    funcName = "def " +  str(procName)  + "("
    f = 0
    for i in para_list:
        if(i[1]=="string"):
            i[1]="str"
        if f==0:
            funcName += str(i[0]) + " : " +   str(i[1]) 
            f=1
        else:
            funcName += ", " + str(i[0]) + " : " +  str(i[1])
    if(return_type=="string"):
        return_type="str"
    if(return_type=="NoneType"):
        funcName += "):\n"
    else:
        funcName += ") -> " + str(return_type) + ":\n"
    funcName += "\tmessage = dict()\n"
    funcName += "\tmessage['procedure_name'] = " + "'" + procName + "'" + "\n"
    funcName  += "\tmessage['parameters'] = [ \n"
    for i in para_list:
        funcName += "\t\t{\n\t\t\t"
        funcName += "'parameter_name': " +  str(i[0]) +",\n\t\t\t"
        funcName += "'data_type': " + "'" +str(i[1])+ "'" +"\n\t\t},\n"
    funcName += "\t]\n\n"
    funcName += "\tmessage['return_type'] = " + "'" +  str(return_type) +"'" +"\n"
    if(return_type=="NoneType"):
        funcName+="\tconToServer(message)\n"
    else:
        funcName += "\tval = conToServer(message)\n"
        funcName += "\tif val is None:\n"
        funcName += "\t\treturn\n"
        funcName += "\treturn val\n\n"
    return funcName

if __name__ == "__main__":
    file_to_write = "rpc_client.py"
    writeHeaders(file_to_write)
    jsonFName = sys.argv[1]
    jsonFile = open(jsonFName)
    # returns JSON object as
    # a dictionary
    data = json.load(jsonFile)
    lines = list()
    for i in data['remote_procedures']:
        para_list = list()
        funcName = i['procedure_name']
        for para in i['parameters']:
            name = para['parameter_name']
            type = para['data_type']
            para_list.append([name,type])
        return_type = i['return_type']
        gen_func = generateFunc(file_to_write,funcName,para_list,return_type)
        lines.append(gen_func)
        
    file_rpc = open(file_to_write, 'a')
    file_rpc.writelines(lines)
    file_rpc.close()
    print("Done")
        
        