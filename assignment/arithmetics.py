def add(a, b):
    return a + b

def subtract(a, b):
    return abs(a - b)

def divide(a, b):
    larger, smaller = max(a, b), min(a, b)
    return larger // smaller if smaller != 0 else None

def multiply(a, b):
    return a * b

