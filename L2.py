def number(value):
    match value:
        case 2:
            return "WRONG"
        case 3:
            return "NEARLY"
        case 4:
            return "Congrats"


print(number(4))