chai_menu = {
  "masala chai": 2.5,
  "herbal chai": 3.0,
  "ginger chai": 2.75,
}

def get_chai_price(chai_type):
  try:
    if(chai_type =="unknown"):
      raise ValueError("We dont know the flavour of chai you are looking for")
    price = chai_menu[chai_type]
  except KeyError:
    return f"Sorry, we don't have {chai_type} on the menu."
  except ValueError as e:
    return str(e)
  return f"Masala Chai Price : {price}"

print(get_chai_price("masala chai"))  # Returns 2.5
print(get_chai_price("green tea"))  # Prints "Sorry, we don't have green tea on the menu." and returns None
print(get_chai_price("unknown"))  # Prints "We dont know the flavour of chai you are looking for" and returns None