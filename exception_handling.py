def divide(x, y):
    if y == 0:
        raise ZeroDivisionError("Division by zero is not allowed.")

    return x / y

#example
result = divide(10, 2)
print(result)
