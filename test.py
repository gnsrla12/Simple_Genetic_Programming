from math import *
import sys

# Evaluate Mean Square Error of the expression
def evaluate_mse(dataset, expression):
    sum = 0
    for x in xrange(0,747):
        output = dataset[x][57]
        sum = sum + pow(parse_rpn(expression,dataset[x])-output,2)
    return sum/747

# Evaluate a expression in reverse polish notation 
def parse_rpn(expression,data): 
    stack = []

    for val in expression.split(' '):
        if val in ['-','+','*','/','^']:
            op1 = stack.pop()
            op2 = stack.pop()
            if val=='-': result = op2 - op1
            if val=='+': result = op2 + op1
            if val=='*': result = op2 * op1
            if val=='/': result = op2 / op1
            if val=='^': result = pow(int(op2),int(op1))
            stack.append(result)
        elif val in ['~', 'abs', 'sin', 'cos', 'tan', 'asin', 'acos', 'atan', 'sinh', 'cosh', 'tanh', 'exp', 'sqrt', 'log']:
            op = stack.pop()
            if val=='~': result = -op
            if val=='abs': result = abs(op)
            if val=='sin': result = sin(op)
            if val=='cos': result = cos(op)
            if val=='tan': result = tan(op)
            if val=='asin': result = asin(op)
            if val=='acos': result = acos(op)
            if val=='atan': result = atan(op)
            if val=='sinh': result = sinh(op)
            if val=='cosh': result = cosh(op)
            if val=='tanh': result = tanh(op)
            if val=='exp': result = exp(op)
            if val=='sqrt': result = sqrt(op)
            if val=='log': result = log(op)
            stack.append(result)
        elif val[0] == 'x':
            variable_index = int(val.split('x')[1]) - 1
            stack.append(data[variable_index])
        else:
            stack.append(float(val))
 
    return stack.pop()

if __name__ == "__main__":
    # save rpn expression as expression
    expression = sys.argv[1]

    #open test.csv file that is passed as argument as read only
    f = open(sys.argv[2],'r')

    #ignore first 1 line  
    for x in xrange(1,2):
    	f.readline()

    #acquire data from test.csv line by line, and store it in dataset
    dataset = []
    for x in xrange(0,747):
        dataset.append(
            map(float,(f.readline().split(","))))

    #evaluate mean square erroor 
    mean_square_error = evaluate_mse(dataset, expression)
    print mean_square_error

    #close file
    f.close()