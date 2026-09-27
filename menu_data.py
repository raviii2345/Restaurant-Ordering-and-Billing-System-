# Restaurant Menu Data

MENU = {
    1: ("Combo Shahi Thali", 1200),
    2: ("Samosa", 55),
    3: ("Vada Pav", 60),
    4: ("Achari Paneer", 380),
    5: ("Paneer Butter Masala", 250),
    6: ("Chole Bhature", 650),
    7: ("Rajma", 120),
    8: ("Pav Bhaji", 350),
    9: ("Dal Makhani", 220),
    10: ("Malai Kofta", 300),
    11: ("Palak Paneer", 270),
    12: ("Veg Biryani", 280),
    13: ("Veg Fried Rice", 200),
    14: ("Tandoor Roti", 180),
    15: ("Aloo Paratha", 120),
    16: ("Masala Dosa", 350),
    17: ("Idli Sambhar", 150),
    18: ("Gulab Jamun", 50),
    19: ("Rasmalai", 90),
    20: ("Juice", 100),
    21: ("Mango Lassi", 120),
    22: ("Cold Coffee", 150),
    23: ("Masala Chai", 50),
    24: ("Fresh Lime Soda", 80),
    25: ("Sweet Lassi", 100),
    26: ("Hara Bhara Kabab", 180),
    27: ("Paneer Tikka", 280),
    28: ("Veg Spring Roll", 160),
    29: ("French Fries", 140),
    30: ("Chilli Paneer", 260),
    31: ("Veg Manchurian", 220),
    32: ("Honey Chilli Potato", 200),
    33: ("Kadhai Paneer", 280),
    34: ("Shahi Paneer", 300),
    35: ("Mix Veg", 220),
    36: ("Butter Naan", 70),
    37: ("Garlic Naan", 90),
    38: ("Plain Naan", 50),
    39: ("Laccha Paratha", 80),
    40: ("Jeera Rice", 180),
    41: ("Dal Tadka", 190),
    42: ("Veg Pulao", 200),
    43: ("Hyderabadi Biryani", 350),
    44: ("Tandoori Platter", 550),
    45: ("Paneer Roll", 180),
    46: ("Veg Sandwich", 150),
    47: ("Veg Burger", 180),
    48: ("Pizza", 350),
    49: ("Ice Cream", 100),
    50: ("Brownie", 180)
}


def get_food_name(item_number):
    """Return the food name for a menu item."""
    if item_number in MENU:
        return MENU[item_number][0]
    return "NOT AVAILABLE"


def get_price(item_number):
    """Return the price for a menu item."""
    if item_number in MENU:
        return MENU[item_number][1]
    return 0
