# receipt.py - Developer B
def print_receipt(orders):
    total = 0.0
    print("\n==========================================")
    print("            PYTHON MINI STORE             ")
    print("==========================================")
    print(f"{'Item':<15} {'Qty':<5} {'Price':<8} {'Subtotal':<10}")
    print("-" * 42)

    for name, qty, price, subtotal in orders:
        print(f"{name:<15} {qty:<5} P{price:<7.2f} P{subtotal:<9.2f}")
        total += subtotal

    print("-" * 42)
    print(f"TOTAL AMOUNT TO BE PAID:         P{total:.2f}")
    print("==========================================\n")