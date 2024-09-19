value = input("Enter a value (number or string): ")
value = int(value)
#matching data types

match value:
    case int() if isinstance(value, int):
        print("You entered an integer: ", value)
    case str():
        print("You entered a string: ", value)
    case _:
        print("Invalid data type entered.")