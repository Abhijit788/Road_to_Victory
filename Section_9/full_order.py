class InvalidChaiType(Exception):
  pass
class InvalidQuantity(Exception):
  pass
class OutOfStock(Exception):
  pass
class LessQuantity(Exception):
  pass

inventory={"masala":10,"ginger":20,"lemon":0}
def order(type,quantity):
  price={"masala":20,"ginger":30,"lemon":25}
  try:
    if type not in price:
      raise InvalidChaiType(f"The {type} chai is not available.")
    elif not isinstance(quantity,int):
      raise InvalidQuantity(f"The quantity should be a number.")
    elif quantity <=0:
      raise InvalidQuantity(f"The quantity should be a number greator than equal to 1.")
    elif inventory[type]==0:
      raise OutOfStock(f"The {type} chai is currently out of stock.")
    elif inventory[type]<quantity:
      raise LessQuantity(f"Only {inventory[type]} cups of {type} is available")
    amount = price[type]*quantity
    print(f"Total price for {quantity} {type} is ${amount}")
  except InvalidChaiType as e:
    print(str(e))
  except InvalidQuantity as e:
    print(str(e))
  except OutOfStock as e:
    print(str(e))
  except LessQuantity as e:
    print(str(e))

order("masala", int(3))  # Returns "Total price for 3 chai(s) is $7.50"
order("assam", int(2))  # Returns "tea is currently not available on the menu."
order("masala", "two")  # Returns "Quantity must be a number"
order("masala", int(-1))  # Returns "Quantity must be greater than or equal to 1"
order("masala", int(0))  # Returns "Quantity must be greater than or equal to 1"
order("lemon", int(3))  # Returns "Sorry, we are out of tea."
order("masala", int(15))  # Returns "Sorry, we only have 10 chai(s) available."
