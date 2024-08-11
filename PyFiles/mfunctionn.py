import math

def performOperation(num1,num2,operation = 'sum', msg = 'This is default message!'):
    print(msg)
    if operation == 'sum':
        print(num1+num2)
    if operation == 'multiply':
        print(num1*num2)

def sumAndProductIt(*args,operation = 'sum'):
    if operation == 'sum':
        print(sum(args))
    
    if operation == 'prod':
        print(math.prod(args))

#sumAndProductIt(1,4,3, operation='prod')

def thisFunction(*args, operation = 'sum'):
    var = locals()
    if var['operation'] == 'sum':
        print(sum(var['args']))
    elif var['operation'] == 'prod':
        print(math.prod(var['args']))

thisFunction (2,3,operation='prod')
