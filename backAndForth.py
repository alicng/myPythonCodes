def calculate_arrowhead(lst):
    
    a, b = "".join(lst).count("<"), "".join(lst).count(">")
    return "<" * (a - b) if a - b > 0 else ">" * (b - a)

a=calculate_arrowhead([">>>>", "<", "<", "<"])
print(a)