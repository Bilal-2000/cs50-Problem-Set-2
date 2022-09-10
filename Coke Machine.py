def main():
    coins = [25, 10, 5]
    due = 50
    check_coins(coins, due)


def check_coins(coins, due):
    while True:
        coin = int(input("Insert Coin: "))
        for val in coins:
            if val == coin:
                due -= val
        if due > 0:
            print(f"Amount Due {due}")
        elif due == 0:
            print(f"Change Owned: {due}")
            break
        elif due < 0:
            print(f"Change Owned: {abs(due)}")
            break


main()
