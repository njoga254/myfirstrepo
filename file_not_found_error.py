file = input("Input the file you wish to open: ")

try:
    with open(file, 'r') as file:
        content = file.read()
        print(content)

except FileNotFoundError:
    print("Error! The file '{file}' does not exist. Please check the file name and try again.")