import sys 
import socket 
import json


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


def foo(par_1 : int) -> str:
	message = dict()
	message['procedure_name'] = 'foo'
	message['parameters'] = [ 
		{
			'parameter_name': par_1,
			'data_type': 'int'
		},
	]

	message['return_type'] = 'str'
	val = conToServer(message)
	if val is None:
		return
	return val

def foo2(par_1 : int, par_2 : float, par_3 : str, par_4 : float) -> str:
	message = dict()
	message['procedure_name'] = 'foo2'
	message['parameters'] = [ 
		{
			'parameter_name': par_1,
			'data_type': 'int'
		},
		{
			'parameter_name': par_2,
			'data_type': 'float'
		},
		{
			'parameter_name': par_3,
			'data_type': 'str'
		},
		{
			'parameter_name': par_4,
			'data_type': 'float'
		},
	]

	message['return_type'] = 'str'
	val = conToServer(message)
	if val is None:
		return
	return val

def foo3(par_1 : str) -> str:
	message = dict()
	message['procedure_name'] = 'foo3'
	message['parameters'] = [ 
		{
			'parameter_name': par_1,
			'data_type': 'str'
		},
	]

	message['return_type'] = 'str'
	val = conToServer(message)
	if val is None:
		return
	return val

def foo4(par_1 : float, par_2 : int) -> float:
	message = dict()
	message['procedure_name'] = 'foo4'
	message['parameters'] = [ 
		{
			'parameter_name': par_1,
			'data_type': 'float'
		},
		{
			'parameter_name': par_2,
			'data_type': 'int'
		},
	]

	message['return_type'] = 'float'
	val = conToServer(message)
	if val is None:
		return
	return val

def add(par_1 : int, par_2 : int) -> int:
	message = dict()
	message['procedure_name'] = 'add'
	message['parameters'] = [ 
		{
			'parameter_name': par_1,
			'data_type': 'int'
		},
		{
			'parameter_name': par_2,
			'data_type': 'int'
		},
	]

	message['return_type'] = 'int'
	val = conToServer(message)
	if val is None:
		return
	return val

def bar(par_1 : int, par_2 : str) -> int:
	message = dict()
	message['procedure_name'] = 'bar'
	message['parameters'] = [ 
		{
			'parameter_name': par_1,
			'data_type': 'int'
		},
		{
			'parameter_name': par_2,
			'data_type': 'str'
		},
	]

	message['return_type'] = 'int'
	val = conToServer(message)
	if val is None:
		return
	return val

def temp() -> int:
	message = dict()
	message['procedure_name'] = 'temp'
	message['parameters'] = [ 
	]

	message['return_type'] = 'int'
	val = conToServer(message)
	if val is None:
		return
	return val

def cprint():
	message = dict()
	message['procedure_name'] = 'cprint'
	message['parameters'] = [ 
	]

	message['return_type'] = 'NoneType'
	conToServer(message)
