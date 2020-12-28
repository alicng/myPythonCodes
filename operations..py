def operation(a, b, op):

    d={'subtract':'-', 'add':'+', 'multiply':'*', 'divide':'//'}
    return "undefined" if b == "0" and op == "divide" else str(eval('{}{}{}'.format(a,d[op],b)))

a=operation("0", "1", "divide")
print(a)