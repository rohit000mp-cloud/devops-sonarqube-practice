
def calculate_total(price, quantity):
    total = price * quantity
    return total


def main():
    price = 100
    quantity = 5

    result = calculate_total(price, quantity)

    print("Total amount:", result)


if __name__ == "__main__":
    main()
