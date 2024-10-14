def calc(x, y, sign):
    match sign:
        case "+":
            return x + y

        case "-":
            return x - y

        case "*":
            return x * y

        case "/":
            if y == 0:
                return "Error"
            else:
                return x / y

        case "%":
            if y == 0:
                return "Error"
            else:
                return x % y

        case _:
            return "Invalid operator"



