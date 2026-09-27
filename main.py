from menu_display import display_menu
from order_processing import take_order
from billing_and_payment import generate_bill


def main():

    print("============================================")
    print("     RESTAURANT ORDERING AND BILLING SYSTEM")
    print("============================================")

    # Get customer name
    name = input("Name Please : ")

    # Display restaurant menu
    display_menu()

    # Take customer order
    ordered_items, bill = take_order()

    # Generate bill and handle payment
    generate_bill(name, ordered_items, bill)


if __name__ == "__main__":
    main()
