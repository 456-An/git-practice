def add(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Arguments must be numbers")
    result = a + b
    print(f"Adding {a} + {b} = {result}")
    return result

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Nan"
    else:        
        return a / b

def power(base, exponent):
    return base ** exponent

if __name__ == "__main__":
    print(f"3 + 5 = {add(3, 5)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    print(f"2 * 3 = {multiply(2, 3)}")
    print(f"6 / 3 = {divide(6, 3)}")
    print(f"2 ^ 8 = {power(2, 8)}")
