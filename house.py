name = input("What's your name? ")

match name:
    case "Harry" | "Ariba" | "Hermoine" | "Ron":
        print("!GRYFFINDOR!")
    case "Draco":
        print("!SLYTHERIN!")
    case _:
        print(" U R TOO DUMB TO BELONG TO HOGWARTS U DUMB MUGGLE ")

