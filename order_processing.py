from menu_data import get_food_name, get_price


def take_order():
    choice = input("\nWhat You Want! : ")

    items = choice.split()

    bill = 0
    ordered_items = []

    for item in items:

        n = int(item)

        # Keep asking until a valid item number is entered
        while get_price(n) == 0:
            print(n, "is NOT AVAILABLE. Try again.")
            n = int(input("Enter a valid item number: "))

        price = get_price(n)
        food = get_food_name(n)

        quantity = int(
            input("Enter quantity for " + food + " : ")
        )

        total = price * quantity

        bill += total

        ordered_items.append(
            [food, price, quantity, total]
        )

        print(
            food,
            "Quantity:", quantity,
            "Total: ₹", total
        )

    if bill == 0:
        print("\nNo valid items were ordered.")

    return ordered_items, bill
