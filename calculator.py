def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def divide(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b

def power(base: float, exponent: float) -> float:
    return base ** exponent

if __name__ == "__main__":
    print(f"3 + 5 = {add(3, 5)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    print(f"2 * 3 = {multiply(2, 3)}")
    print(f"6 / 3 = {divide(6, 3)}")
    print(f"2 ^ 8 = {power(2, 8)}")
