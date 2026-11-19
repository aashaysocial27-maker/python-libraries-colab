MENU = {"Steel Bottle": 499, "Yoga Mat": 1299, "Notebook": 149, "Desk Lamp": 899}

class Basket:
    def __init__(self):
        self.qty = {name: 0 for name in MENU}
    def add(self, name, n=1):
        self.qty[name] = max(0, self.qty[name] + n)
    def total(self):
        return sum(MENU[n] * q for n, q in self.qty.items())
    def summary(self):
        return ", ".join(f"{q} x {n}" for n, q in self.qty.items() if q) or "Basket is empty"