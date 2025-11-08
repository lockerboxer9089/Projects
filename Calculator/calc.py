def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

def find_operator(operation):
    operators = ['+', '-', '*', '/']

    for operator in operators:
        if operator in operation:
            return operator

def find_operator_location(operator, operation):
    return operation.index(operator)

problem = str(input("Enter your problem\n"))
operator = find_operator(problem)
print(operator)
print(find_operator_location(operator, problem))