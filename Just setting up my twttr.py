def main():
    str = input("Input: ")
    str = Removing_Vowels(str)
    print(f"Output: {str}")


def Removing_Vowels(str):
    Vowels = "AEIOUaeiou"
    for val in str:
        if val in Vowels:
            str = str.replace(val, "")
    return str


main()
