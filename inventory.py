# inventory dictionary
inventory = {}
def addproduct(item,quantity):
    if item in inventory:
      inventory[item] += quantity
    else:
      inventory[item] = quantity
def removeproduct(item, quantity):
    if item in inventory:
      if inventory[item] >= quantity:
          inventory[item] -= quantity
          if inventory[item] == 0:
              del inventory[item]
      else:
          print(f"Not enough {item} in stock.")
    else:
      print(f"{item} not found in inventory.")
def totalitems():
  print("Items in Inventory:")
  for item, quantity in inventory.items():
      print(f"{item}: {quantity}")
addproduct("Apples", 10)
addproduct("Bananas", 15)
addproduct("Oranges", 20)
removeproduct("Bananas", 5)
totalitems()