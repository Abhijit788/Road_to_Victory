class OutOfStockError(Exception):
    """Custom exception for out of stock items."""
    pass
class LessStockError(Exception):
    """Custom exception for invalid quantity."""
    pass

ingredients = {
    "chai": 10,
    "coffee": 5,
    "tea": 0
}
def order(item,quantity):
  try:
    if quantity <=0:
      raise ValueError("Quantity must be greater than or equal to 1")
    
    if quantity > ingredients.get(item, 0):
      raise LessStockError(f"Sorry, we only have {ingredients.get(item, 0)} {item}(s) available.")
    
    if ingredients.get(item, 0) == 0:
      raise OutOfStockError(f"Sorry, we are out of {item}.")
    price = {"chai": 2.50, "coffee": 3.00}[item]
    total = price * quantity
    print(f"Total price for {quantity} {item} is {total}")
  except KeyError:
    print(f"{item} is currently not available on the menu.")
  except TypeError:
    print("Quantity must be a number")
  except ValueError as e:
    print(str(e))
  except OutOfStockError as e:
    print(str(e))
  except LessStockError as e:
    print(str(e))

order("chai", 3)  # Returns "Total price for 3 chai(s) is $7.50"
order("tea", 2)  # Returns "tea is currently not available on the menu."
order("coffee", "two")  # Returns "Quantity must be a number"
order("chai", -1)  # Returns "Quantity must be greater than or equal to 1"
order("chai", 0)  # Returns "Quantity must be greater than or equal to 1"
order("tea", 3)  # Returns "Sorry, we are out of tea."
order("chai", 15)  # Returns "Sorry, we only have 10 chai(s) available."
