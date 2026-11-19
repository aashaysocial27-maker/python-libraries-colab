import csv
import tkinter as tk
from tkinter import ttk, messagebox
from shop_logic import PRODUCTS, order_total

root = tk.Tk()
root.title("ShopEasy order calculator")
root.geometry("420x380")
frm = ttk.Frame(root, padding=16)
frm.pack(fill="both", expand=True)

product = tk.StringVar(value="Steel Bottle")
qty = tk.IntVar(value=1)
coupon = tk.StringVar()
total = tk.StringVar()

ttk.Label(frm, text="Product").grid(row=0, column=0, sticky="w", pady=4)
ttk.Combobox(frm, textvariable=product, values=list(PRODUCTS), state="readonly").grid(row=0, column=1, sticky="ew")
ttk.Label(frm, text="Quantity").grid(row=1, column=0, sticky="w", pady=4)
ttk.Spinbox(frm, from_=1, to=20, textvariable=qty, width=6).grid(row=1, column=1, sticky="w")
ttk.Label(frm, text="Coupon").grid(row=2, column=0, sticky="w", pady=4)
ttk.Entry(frm, textvariable=coupon).grid(row=2, column=1, sticky="ew")
ttk.Label(frm, textvariable=total, font=("Segoe UI", 14, "bold")).grid(row=3, column=0, columnspan=2, pady=10)
orders = tk.Listbox(frm, height=6)
orders.grid(row=5, column=0, columnspan=2, sticky="nsew", pady=6)
frm.columnconfigure(1, weight=1); frm.rowconfigure(5, weight=1)

def refresh(*_):
    try:
        total.set(f"Total: Rs. {order_total(product.get(), qty.get(), coupon.get()):,.2f}")
    except (ValueError, tk.TclError):
        total.set("Total: -")

def add_order():
    refresh()
    orders.insert("end", f"{qty.get()} x {product.get()}  ->  {total.get().split(': ')[1]}")

def save_csv():
    with open("orders.csv", "w", newline="") as f:
        csv.writer(f).writerows([[line] for line in orders.get(0, "end")])
    messagebox.showinfo("Saved", f"Saved {orders.size()} orders to orders.csv")

for var in (product, qty, coupon):
    var.trace_add("write", refresh)
ttk.Button(frm, text="Add to list", command=add_order).grid(row=4, column=0, pady=4, sticky="w")
ttk.Button(frm, text="Save CSV", command=save_csv).grid(row=4, column=1, pady=4, sticky="e")
refresh()
root.mainloop()