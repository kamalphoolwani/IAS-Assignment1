def add(a,b):
    c = a + b
    return c

def bar(par_1,par_2):
    l=len(par_2)
    while(l>0):
        par_1+=par_1
        l-=1
    return par_1

def foo(par_1):
    return "Your birth date is "+str(par_1)+" !"

def temp():
    return 100

def foo2(a,b,c,d):
    return a+b

def foo3(a):
    return "andha"

def cprint():
    print ("Called Inside Server")

def foo4(a:float,b:int):
    c = a+b
    return c


    