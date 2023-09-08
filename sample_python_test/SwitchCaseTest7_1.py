def number_to_string(argument):
    match argument:
        case 0:
            return "zero"
        case 1:
            return "one"
        case 2:
            return "two"
        case default:
            return "something"

def numbers_to_strings(argument):
    switcher = {
        0: "zero",
        1: "one",
        2: "two",
    }
    return switcher.get(argument, "nothing")

class SwitchCaseTest:
    print("Start")
    print(number_to_string(2))
    print("Test Other Way--")
    print(numbers_to_strings(1))

# Output will be - Supported above python 10 Version
# Start
# two
