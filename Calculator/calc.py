"""
Improvements:
1. Error like this: '5+' will proceed without error
2. - at the start example: -5+3 will see - as the operator
3. For future - 5+2+3+4, make this work
4. Use the typewriter less
"""

import os,sys
from time import sleep

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y == 0:
        return "undefined"
    return x/y

def find_operator(operation):
    operators = ['+', '-', '*', '/']

    for operator in operators:
        if operator in operation:
            return operator
        
    return None

def typewrite(string):
    for char in string:
        sleep(0.035)
        sys.stdout.write(char)
        sys.stdout.flush()
        
os.system('clear')
while True:
    print("Enter your problem\nDon't leave any spaces!! Enter STOP if you want to end the program...\n")
    problem = str(input("\n: ")).lower()
    if (problem == 'stop'):
        typewrite("\nEnding Program...")
        break
    operator = find_operator(problem)
    if operator:
        problem_list = list(problem)
        operator_location = problem_list.index(operator)
        x = float(''.join(problem_list[:operator_location]))
        y = float(''.join(problem_list[operator_location+1:]))

        if operator == '*':
            print('\n', problem, ' = ', multiply(x,y), '\n')
        elif operator == '/':
            print('\n', problem, ' = ', divide(x,y), '\n')
        elif operator == '+':
            print('\n', problem, ' = ', add(x,y), '\n')
        elif operator == '-':
            print('\n', problem, ' = ', subtract(x,y), '\n')
    else:
        typewrite("\nInvalid Input...")
        print("")

sleep(1)
os.system('clear')