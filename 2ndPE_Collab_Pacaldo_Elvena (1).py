# File: 2ndPE_Collab_Pacaldo_Elvena.py
# Developers: Pacaldo & Jaden Clark Elvena
# Repository: https://github.com/jaelvena-web/Grade9_POS_Ordering-System.git

STORE_NAME = "MINI STORE"

MENU = {
    1: {"name": "Burger", "price": 50.00},
    2: {"name": "Fries", "price": 35.00},
    3: {"name": "Soft Drink", "price": 25.00},
}


def display_menu(menu):
    print("=" * 45)
    print(f"{'WELCOME TO ' + STORE_NAME:^45}")
    print(f"{'POS ORDERING SYSTEM':^45}")
    print("=" * 45)
    print("\nPRODUCT MENU")
    print("-" * 25)
    for item_id, item in menu.items():
        print(f"[{item_id}] {item['name']:<12} - PHP {item['price']:.2f}")
    print("-" * 25)


def take_orders(menu):
    orders = []
    valid_choices = ", ".join(str(k) for k in menu.keys())

    while True:
        while True:
            try:
                choice = int(input(f"\nEnter product number ({valid_choices}): "))
                if choice in menu:
                    break
                print("Invalid product number. Please try again.")
            except ValueError:
                print("Please enter a valid number.")

        while True:
            try:
                quantity = int(input("Enter quantity: "))
                if quantity > 0:
                    break
                print("Quantity must be at least 1.")
            except ValueError:
                print("Please enter a valid whole number.")

        product = menu[choice]
        subtotal = product["price"] * quantity
        orders.append({
            "name": product["name"],
            "quantity": quantity,
            "price": product["price"],
            "subtotal": subtotal,
        })

        print(f"\nAdded: {product['name']} x {quantity}")

        while True:
            again = input("Order another product? (yes/no): ").strip().lower()
            if again in ("yes", "y"):
                keep_ordering = True
                break
            elif again in ("no", "n"):
                keep_ordering = False
                break
            print("Please enter 'yes' or 'no'.")

        if not keep_ordering:
            break

    return orders


def calculate_total(orders):
    return sum(item["subtotal"] for item in orders)


def print_receipt(store_name, orders):
    total_amount = calculate_total(orders)

    print("\n" + "=" * 45)
    print(f"{'RECEIPT':^45}")
    print(f"{store_name:^45}")
    print("=" * 45)
    print(f"{'Product':<14} {'Qty':>4} {'Price':>8} {'Subtotal':>10}")
    print("-" * 39)

    for item in orders:
        print(
            f"{item['name']:<14} "
            f"{item['quantity']:>4} "
            f"{item['price']:>8.2f} "
            f"{item['subtotal']:>10.2f}"
        )

    print("-" * 39)
    print(f"{'TOTAL AMOUNT:':<24} PHP {total_amount:>10.2f}")
    print("=" * 45)
    print(f"{'THANK YOU FOR YOUR ORDER!':^45}")
    print("=" * 45)


def main():
    display_menu(MENU)
    orders = take_orders(MENU)
    print_receipt(STORE_NAME, orders)


if __name__ == "__main__":
    main()
