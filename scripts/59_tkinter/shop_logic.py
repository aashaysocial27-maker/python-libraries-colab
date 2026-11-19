PRODUCTS = {"Steel Bottle": 499, "Yoga Mat": 1299, "Desk Lamp": 899, "Notebook": 149}
COUPONS = {"SAVE10": 0.10, "FEST25": 0.25}

def order_total(product, qty, coupon=""):
    if product not in PRODUCTS:
        raise ValueError("Unknown product")
    if qty < 1:
        raise ValueError("Quantity must be at least 1")
    subtotal = PRODUCTS[product] * qty
    discount = COUPONS.get(coupon.strip().upper(), 0)
    return round(subtotal * (1 - discount), 2)