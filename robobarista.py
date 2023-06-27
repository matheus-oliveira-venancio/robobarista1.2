print("Welcome to Robo Barista Cafe!")

name = input("What is your name? ")

print(f"Hello, {name}! What do you want to order?")

menu = input("We have Java coffee, coffee with milk, and normal coffee. What do you want to order? ")
price = 8

quantity = int(input("How many coffees would you like? "))

total = price * quantity 

print("Thank you, your total is $:", total)
print("Sounds good, " + name + "! We'll have your " + str(quantity) + " coffee(s) ready for you in a moment.") 
print ("Do you want more one thing?")

reply = input ("Type here: ") 

if reply == "no" or reply=="No":
        print ("Ok sir have a nice day" )

if reply == "yes" or reply== "Yes":
        print ("Okay what do you want more" )
        print("Thank you for coming to Robo Barista Cafe, " + name + "! We hope to see you again soon!")

        more = input ("we also have water and pizza") 
        print ("Ok sir, we have " + more + " in our menu")
