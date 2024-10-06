class ValueTooHighError(Exception):
    pass

def check_value(number):
        if number > 100:
            raise ValueTooHighError(f"Error! '{number}' is too high.")
        else:
            print(f"'{number}' is correct.")

try:
    number = int(input("Input a number: "))
    check_value(number)
except ValueTooHighError as e:
    print(e)

