from menu_data import MENU


def display_menu():
    print("\n════════════ MENU ════════════")
    print("             MENU CARD")
    print("══════════════════════════════")

    print("\nCOMBO :")
    print_item(1)

    print("\nSTARTERS :")
    for number in range(2, 12):
        print_item(number)

    print("\nRICE & BIRYANI :")
    for number in range(12, 14):
        print_item(number)

    print("\nBREADS :")
    for number in range(14, 16):
        print_item(number)

    print("\nSOUTH INDIAN :")
    for number in range(16, 18):
        print_item(number)

    print("\nDESSERTS :")
    for number in range(18, 20):
        print_item(number)

    print("\nBEVERAGES :")
    for number in range(20, 26):
        print_item(number)

    print("\nMORE STARTERS :")
    for number in range(26, 33):
        print_item(number)

    print("\nMORE MAIN COURSE :")
    for number in range(33, 43):
        print_item(number)

    print("\nSPECIAL ITEMS :")
    for number in range(43, 49):
        print_item(number)

    print("\nDESSERTS :")
    for number in range(49, 51):
        print_item(number)

    print("══════════════════════════════")


def print_item(number):
    food, price = MENU[number]
    print(f"{number:<3} {food:<25} : ₹{price}")
