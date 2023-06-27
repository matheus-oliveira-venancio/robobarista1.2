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

welcome_label = tk.Label(window, text="Bem vindo a cafeteria robo barista!", font=("Helvetica", 16))
welcome_label.pack(pady=10)

name_label = tk.Label(window, text="Qual o seu nome")
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack()

menu_label = tk.Label(window, text="O que voce deseja pedir hoje?")
menu_label.pack()

menu_var = tk.StringVar()
menu_var.set("1")

menu_options = [
    ("Java coffee", "1"),
    ("Café com leite", "2"),
    ("Café preto", "3"),
    ("Café", "4")
]

# Menu_options  vai listar as opçoes com o numeral 1 2 3 4, ira listar o numero exato do pedido 

for text, value in menu_options:
    menu_radio = tk.Radiobutton(window, text=text, variable=menu_var, value=value)
    menu_radio.pack() 

quantity_label = tk.Label(window, text="Quantos cafes voce gostaria?")
quantity_label.pack() 
quantity_entry = tk.Entry(window)
quantity_entry.pack()

order_button = tk.Button(window, text="Fazer pedido", command=display_order)
order_button.pack(pady=10) 

order_label = tk.Label(window, text="")
order_label.pack()

clear_button = tk.Button(window, text="Limpar campos", command=clear_fields)
clear_button.pack(pady=10)

window.mainloop()
