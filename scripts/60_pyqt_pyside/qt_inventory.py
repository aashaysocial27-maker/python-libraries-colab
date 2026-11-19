import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit,
                               QCheckBox, QTableWidget, QTableWidgetItem, QHeaderView, QLabel)
from PySide6.QtGui import QColor

PRODUCTS = [("Steel Bottle", "Kitchen", 499, 40), ("Yoga Mat", "Fitness", 1299, 3), ("Desk Lamp", "Home", 899, 7),
            ("Notebook", "Stationery", 149, 200), ("Headphones", "Electronics", 2499, 2), ("Dumbbells", "Fitness", 1999, 15)]

class Inventory(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ShopEasy inventory")
        self.resize(620, 360)
        self.search = QLineEdit(placeholderText="Search products...")
        self.low = QCheckBox("Low stock only (< 10)")
        self.table = QTableWidget(0, 4)
        self.table.setHorizontalHeaderLabels(["Product", "Category", "Price", "Stock"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        top = QHBoxLayout(); top.addWidget(self.search); top.addWidget(self.low)
        box = QVBoxLayout(); box.addLayout(top); box.addWidget(self.table)
        central = QWidget(); central.setLayout(box); self.setCentralWidget(central)
        self.search.textChanged.connect(self.refresh)     # signal -> slot
        self.low.toggled.connect(self.refresh)
        self.refresh()

    def visible_products(self):
        q = self.search.text().lower()
        return [p for p in PRODUCTS if q in p[0].lower() and (not self.low.isChecked() or p[3] < 10)]

    def refresh(self):
        rows = self.visible_products()
        self.table.setRowCount(len(rows))
        for r, (name, cat, price, stock) in enumerate(rows):
            for c, val in enumerate([name, cat, f"Rs. {price:,}", str(stock)]):
                item = QTableWidgetItem(val)
                if stock < 10:
                    item.setBackground(QColor("#FFE3E3"))
                self.table.setItem(r, c, item)
        self.statusBar().showMessage(f"{len(rows)} of {len(PRODUCTS)} products")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Inventory(); win.show()
    sys.exit(app.exec())