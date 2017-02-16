#CS323
#Author: Curtis Turner, Billy Giang
#Assignment 2
#Postfix Calculations

def addition(x, y):
    return y + x

def subtract(x, y):
    return y - x

def multiply(x, y):
    return y * x

def divide(x, y):
    return y / x


cont = False
while not cont:
    name = []
    value = []
    stack = []
    
    print('enter a postfix expression >> ')

    postfix = input()

    newpostfix = postfix.split()

    
    for i in newpostfix:
        if i not in name and i !='+' and i!= '-' and i != '*' and i!= '/' and i != '$':
            if i.isdigit():
                name.append(i)
                value.append(int(i))
            else:
                print("what is the value of ", i)
                v = int(input('>> '))
                name.append(i)
                value.append(v)
    
    unique = dict(zip(name, value))
    
    index = ''
    
    while index != '$':
        for i in newpostfix:
            index = i
            if i == '+':
                x = stack.pop()
                y = stack.pop()
                result = addition(x, y)
                stack.append(result)
                #print(stack)
            elif i == '-':
                x = stack.pop()
                y = stack.pop()
                result = subtract(x, y)
                stack.append(result)
                #print(stack)
            elif i == '*':
                x = stack.pop()
                y = stack.pop()
                result = multiply(x, y)
                stack.append(result)
                #print(stack)
            elif i == '/':
                x = stack.pop()
                y = stack.pop()
                result = divide(x, y)
                stack.append(result)
                #print(stack)
            elif i == '$':
                break
            else:
                stack.append(unique[i])
                #print(stack)

    print('Final Value = ')
    print(stack[0])

    print('Continue (y/n) ?')
    choice = input()
    if choice == 'y' or choice == 'Y':
        cont = False

    elif choice == 'n' or choice == 'N':
        cont = True

    else:
        print('invalid input closing program')
        cont = True

