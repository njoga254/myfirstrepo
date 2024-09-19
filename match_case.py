day = input("Enter a day of the week (monday-sunday): ").lower()
#match case statements
match day:
    case "monday":
        print("Ugh, Mondays are boring.")
    case "tuesday":
        print("Just a normal working day!")
    case "wednesday":
        print("ALx PLD day.")
    case "thursday":
        print("Huh! My cooking day.")
    case "friday":
        print("Closing on the tasks.")
    case "saturday" | "sunday":
        print("Aaaw! Weekend's are for unwinding")
    case _:
        print("Invalid name entered")