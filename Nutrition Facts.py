def main():
    fruits = {
        "apple": 130,
        "avocado": 50,
        "banana": 110,
        "cantaloupe": 50,
        "grapefruit": 60,
        "grapes": 90,
        "honeydew melon": 50,
        "kiwi fruit": 90,
        "lemon": 15,
        "lime": 20,
        "nectarine": 60,
        "orange": 80,
        "pear": 100,
        "peach": 60,
        "pineapple": 50,
        "plums": 70,
        "strawberries": 50,
        "sweet cherries": 100,
        "tangerine": 50,
        "watermelon": 80
    }
    store = (check_calories(fruits))
    if store == 0:
        return 0
    else:
        print(f"Calories: {store}")


def check_calories(fruits):
    str = input("Item: ").lower()
    keys = fruits.keys()
    if str in keys:
        return fruits.get(str)
    else:
        return 0


main()
