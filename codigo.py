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
welcome_label.grid(row=0, column=0, columnspan=2, pady=10)

name_label = tk.Label(window, text="Qual o seu nome")
name_label.grid(row=1, column=0)
name_entry = tk.Entry(window)
name_entry.grid(row=1, column=1)

menu_label = tk.Label(window, text="O que voce deseja beber hoje?")
menu_label.grid(row=2, column=0)

menu_var = tk.StringVar()
menu_var.set("1")

menu_options = [ 
    ("Café Filtrado", "1"),
    ("Café Americano", "2"),
    ("Café com Leite", "3"),
    ("Café Latte", "4"),
    ("Flat White", "5"),
    ("Café Mocha", "6"),
    ("Café Mocha Branco", "7"),
    ("Doce de Leite Latte", "8"),
    ("Baunilha Latte", "9"),
    ("Caramelo Macchiato", "10"),
    ("Brigadeiro Latte", "11"),
    ("suco de pessego", "12"),
    ("Leite c/achocolatado", "13"),
    ("Chocolate quente", "14"), 
]   #parte de bebidas finalizada 

menu_row = 3
for text, value in menu_options:
    menu_radio = tk.Radiobutton(window, text=text, variable=menu_var, value=value)
    menu_radio.grid(row=menu_row, column=0, sticky="w")
    menu_row += 1

quantity_label = tk.Label(window, text="Qual a quantidade o senhor (a) gostaria?")
quantity_label.grid(row=menu_row, column=0)
quantity_entry = tk.Entry(window)
quantity_entry.grid(row=menu_row, column=1)

order_button = tk.Button(window, text="Fazer pedido", command=display_order)
order_button.grid(row=menu_row+1, column=0, pady=10)

order_label = tk.Label(window, text="")
order_label.grid(row=menu_row+2, column=0, columnspan=2)

menu_label = tk.Label(window, text="Voce deseja mais alguma coisa para comer?")
menu_label.grid(row=menu_row+3, column=0)

# Opções de comida
food_options = [
    ("Pizza", "15"),
    ("Hambúrguer", "16"),
    ("Salada", "17"),
    ("Pao", "18"),
    ("Bolo de cenoura", "19"),
    ("Rosca", "20"),
    #Opçoes de comida finalizada
]

food_row = menu_row + 4
for text, value in food_options:
    food_radio = tk.Radiobutton(window, text=text, variable=menu_var, value=value)
    food_radio.grid(row=food_row, column=0, sticky="w")
    food_row += 1

clear_button = tk.Button(window, text="Limpar campos", command=clear_fields)
clear_button.grid(row=food_row, column=0, pady=10)

window.mainloop()
