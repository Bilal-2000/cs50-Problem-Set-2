def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    counter = 0
    length = len(s)
    notZero = False
    for index, val in enumerate(s):
        if val.isspace() or val == "!" or val == ".":
            return False
        elif val.isalpha() and index == 0:
            counter += 1
        elif val.isalpha() and index == 1:
            counter += 1
            if counter == length:
                return True
        elif val.isalnum() and index == 2:
            counter += 1
            if val == '0':
                return False
            elif counter == length:
                return True
            elif val.isdigit():
                notZero = True
                continue
        elif val.isalnum() and index == 3:
            counter += 1
            if val == '0' and not notZero:
                return False
            elif val.isalpha() and notZero:
                return False
            elif counter == length:
                return True
            elif val.isdigit():
                notZero = True
                continue
            elif val.isdigit() and notZero:
                continue
        elif val.isalnum() and index == 4:
            counter += 1
            if val == '0' and not notZero:
                return False
            elif val.isalpha() and notZero:
                return False
            elif counter == length:
                return True
            elif val.isdigit():
                notZero = True
                continue
            elif val.isdigit() and notZero:
                continue
        elif val.isalnum() and index == 5:
            counter += 1
            if val == '0' and not notZero:
                return False
            elif val.isalpha() and notZero:
                return False
            elif counter == length:
                return True
            elif val.isdigit():
                notZero = True
                continue
            elif val.isdigit() and notZero:
                continue
        else:
            return False


main()
