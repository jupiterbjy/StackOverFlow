from os import path


function_template = '''
def {0}():
    print({0})
    
'''

with open(path.abspath(__file__), 'a') as fp:
    for name, arg in zip('abcde', range(5)):
        fp.write(function_template.format(name, arg))

def a():
    print(a)
    

def b():
    print(b)
    

def c():
    print(c)
    

def d():
    print(d)
    

def e():
    print(e)
    
