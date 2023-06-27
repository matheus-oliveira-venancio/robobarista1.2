import tkinter as tk

def display_order():
    name = name_entry.get()
    menu = menu_var.get()
    quantity = int(quantity_entry.get())
    price = 8
    total = price * quantity
    order_text = f"Name: {name}\n"
    order_text += f"Menu: {menu}\n"
    order_text += f"Quantity: {quantity}\n"
    order_text += f"Total: ${total}"
    order_label.config(text=order_text)

def clear_fields():
    name_entry.delete(0, tk.END)
    menu_var.set("1")
    quantity_entry.delete(0, tk.END)

window = tk.Tk()
window.title("Robo Barista Cafe")

welcome_label = tk.Label(window, text="Welcome to Robo Barista Cafe!", font=("Helvetica", 16))
welcome_label.pack(pady=10)

name_label = tk.Label(window, text="What is your name?")
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack()

menu_label = tk.Label(window, text="What do you want to order?")
menu_label.pack()

menu_var = tk.StringVar()
menu_var.set("1")

menu_options = [
    ("Java coffee", "1"),
    ("Coffee with milk", "2"),
    ("Normal coffee", "3"),
    ("Strong coffee", "4")
]

for text, value in menu_options:
    menu_radio = tk.Radiobutton(window, text=text, variable=menu_var, value=value)
    menu_radio.pack()

quantity_label = tk.Label(window, text="How many coffees would you like?")
quantity_label.pack()
quantity_entry = tk.Entry(window)
quantity_entry.pack()

order_button = tk.Button(window, text="Place Order", command=display_order)
order_button.pack(pady=10)

order_label = tk.Label(window, text="")
order_label.pack()

clear_button = tk.Button(window, text="Clear Fields", command=clear_fields)
clear_button.pack(pady=10)

window.mainloop()
