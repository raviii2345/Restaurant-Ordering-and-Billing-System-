def generate_bill(name, ordered_items, bill):

    if bill == 0:
        print("No valid items were ordered.")
        print("Thank you for visiting!")
        return

    # Billing calculations
    gst = bill * 0.05
    delivery = 40
    grand_total = bill + gst + delivery

    # Restaurant Bill
    print("\n")
    print("════════════════════════════════════════════")
    print("              RESTAURANT BILL")
    print("════════════════════════════════════════════")

    print("Customer Name :", name)
    print("--------------------------------------------")
    print("Food Name                 Qty     Price     Total")
    print("--------------------------------------------")

    for item in ordered_items:
        food = item[0]
        price = item[1]
        quantity = item[2]
        total = item[3]

        print(
            food,
            " " * max(1, 25 - len(food)),
            quantity,
            "     ₹",
            price,
            "    ₹",
            total
        )

    print("--------------------------------------------")
    print("Subtotal                         : ₹", bill)
    print("GST (5%)                         : ₹", round(gst, 2))
    print("Delivery Charge                  : ₹", delivery)
    print("--------------------------------------------")

    print(
        "GRAND TOTAL                      : ₹",
        round(grand_total, 2)
    )

    print("════════════════════════════════════════════")

    # Payment Method
    print("\nPAYMENT METHOD")
    print("1. Cash")
    print("2. UPI")
    print("3. Card")

    payment = input("Choose Payment Method : ")

    if payment == "1":

        method = "Cash"

        amount = float(
            input("Enter Cash Amount : ₹")
        )

        if amount >= grand_total:

            change = amount - grand_total

            print(
                "Change to Return : ₹",
                round(change, 2)
            )

        else:

            remaining = grand_total - amount

            print(
                "Remaining Amount : ₹",
                round(remaining, 2)
            )

    elif payment == "2":

        method = "UPI"

        print("UPI Payment Selected.")
        print("Please complete the payment.")
        print("Payment Successful!")

    elif payment == "3":

        method = "Card"

        print("Card Payment Selected.")
        print("Please complete the payment.")
        print("Payment Successful!")

    else:

        method = "Not Selected"

        print("Invalid Payment Method")

    # Final Receipt
    print("\n")
    print("════════════════════════════════════════════")
    print("               FINAL RECEIPT")
    print("════════════════════════════════════════════")

    print("Customer :", name)

    print("\nORDER DETAILS")

    for item in ordered_items:

        print(
            item[0],
            "x",
            item[2],
            "= ₹",
            item[3]
        )

    print("\nSubtotal       : ₹", bill)
    print("GST            : ₹", round(gst, 2))
    print("Delivery       : ₹", delivery)
    print("--------------------------------------------")
    print("TOTAL          : ₹", round(grand_total, 2))
    print("Payment Method :", method)

    print("════════════════════════════════════════════")
    print("       THANK YOU FOR YOUR ORDER!")
    print("       Your food will reach you soon.")
    print("════════════════════════════════════════════")

    input("\nPress Enter to exit...")
