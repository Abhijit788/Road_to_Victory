def order_chai(item,quantity):
  try:
    price = {"chai": 2.50, "coffee": 3.00}[item]
    total = price * quantity
    print(f"Total price for {quantity} {item} is {total}")
  except KeyError:
    print(f"{item} is currently not available on the menu.")
  except TypeError:
    print("Quantity must be a number")
  
order_chai("chai", 3)  # Returns "Total price for 3 chai(s) is $7.50"
order_chai("tea", 2)  # Returns "tea is currently not available on the menu."
order_chai("coffee", "two")  # Returns "Quantity must be a number"