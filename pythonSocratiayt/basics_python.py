# #There are some ways to write strings code with quotes in python:
# print("This is an example without quotes")
# print("This is anoter 'example' with quotes")
# print("""This is "another" 'example'""")
# #
# #This is because the interpretator need the same pattern to recognize a begin and a end of the string. 
# #These example will evaluate an error:
# #"This is "an" example"
# #'This is 'an example' 
# #
# #There are three types of numbers in python: int, float, and complex numbers
# #
# #numbers of type int are integer values: 
# a = 496 
# b = 593
# #
# #we can check the type of a number with function type(x)
# print(type(a))
# #
# #float numbers have a decimal point: 
# a = 2.5 
# e = 2.71828128
# print(type(e))
# #
# #complex numbers: 
# a = (2 - 6.1j)
# print(a)
# #
# #python uses 'j' to identify the imaginary part of a complex number
# #to acess the first value:
# print(a.real)
# print(a.imag)
# #and to imaginary 
# #both numbers of a complex variable are floats
# #
# #in python the number types are int, float and complex
# #a int value are narrower than float and a float is narrower than a complex number
# #this means that you can't convert a narrower type number to a wider:
# a = 25
# print(float(a))
# #
# #int(a) # this cause an error
# print(complex(a))
#float(a) # this cause another error
#
#The math operations in python are: + - * /
#We can evaluate a exponenciation by doing a ** b
#Division can be made in 3 ways: 
# a = 10
# b = 5
# print(a / b) # always returns a float number
# print(a % b) # returns the reminder
# print(a // b) # returns the quotient
# #
# #In multiplicantion and in the others operations, an operation will return its wider type
# #like: 
# print(a * b) #the result: 4.0
# #
# #python help can be used to lear more about functions of python modules:
# dir() # shows the modules that are built-in python
#help('modules') # shows all python modules that can be imported
# #
# #use '.' to navigate the module, like:
# import math as m
# m.pow(a, b)
#help(m.radians)
#
# boolen values are True and False
# you can convert True or False to str or number:
# print(str(True))
# print(int(True))
# print(1 + True)
# print(1 + False)
# print(bool(25))
# print(bool(0))
# print(bool(' '))
# print(bool(''))

#Exercice =  make a calculator with + * - / exponential, squareroot and fatorial
#programa que calcula operações básicas e expoentes, raiz quadrada e fatorial
import math
x = int(input("insira o primeiro número ou -1 para sair: "))

while(x != -1):
    op = input("Insira a operação: + (soma), -(sub), *(mult), /(div), e(expo), r(squareroot), f(fatorial)\n")
    y = int(input("Insira o segundo número: "))
    
    if(op == '+'):
        print(f'Resultado = {x + y}')
    elif(op == '-'):
        print(f'Resultado = {x - y}')
    elif(op == '*'):
        print(f'Resultado = {x * y}')
    elif(op == '/'):
        print(f'Resultado = {x / y}')
    elif(op == 'e'):
        print(f'Resultado = {math.pow(x, y)}')
    elif(op == 'r'):
        print(f'Resultado da raiz do primeiro número = {math.sqrt(x)}\nResultado da raiz do segundo número = {math.sqrt(y)}')
    elif(op == 'f'):
        def fat(fatorial):
            if(fatorial == 1):
                return fatorial
            else:
                return fatorial * fat(fatorial -1)
        print(f"Fatorial do primeiro número = {fat(x)}\nFatorial do segundo número = {fat(y)}")
    else:
        print("Operação inválida!")
    
    x = int(input("Insira o primeiro número ou -1 para sair: "))
