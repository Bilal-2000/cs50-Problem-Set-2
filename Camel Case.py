def main():
    name_list = list(input("Camel Case: "))
    result = Snake_Case(name_list)
    print("Snake Case: ", *result, sep="")


def Snake_Case(temp_list):
    for index, val in enumerate(temp_list):
        if val.isupper():
            temp_list.insert(index, "_")
            temp_list[index + 1] = val.lower()
    return temp_list


main()
