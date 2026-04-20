#Food ordring system

print("----MENU----")
print("BURGER - 500")
print("PIZZA - 1000")
print("JUICE - 300")

item = input("Enter item name: ").lower()
quantity =int(input("Enter quantity: "))

price = 0

#price selection
if item == "burger":
  price = 500
elif item == "pizza":
  price = 1000
elif item == "juice":
  price = 300
else:
  print("Invalid choice")
  exit()

total = price*quantity

print("----BILL----")
print("Item : ", item)
print("Quentity :", quantity)
print("Total :", total)
