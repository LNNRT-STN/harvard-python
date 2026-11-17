name = str(input("what is your name? "))

match name:
    case "harry" | "lennart":
        print("gryffindor")
    case "draco":
        print("Slytherin")
    case _:
        print("who")

