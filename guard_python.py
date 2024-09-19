age = int(input("Enter your age: "))
has_id = True       

match age:
    case 18 | 19: #match multiple valuees with pipe (|)
        if age >= 18 and has_id: #Guard using a functional call
            print("You're eligible to vote.")
        else:
            print("You need a valid ID to vote.")
    case _:
        print("You're not eligible to vote.")

    