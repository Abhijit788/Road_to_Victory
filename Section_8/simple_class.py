class Chai:
  origin = "India"

  def __init__(self, flavor):
    self.flavor = flavor
  def __str__(self):
    return f"{self.flavor} chai from {self.origin}"
  
masala_chai = Chai("Masala")
print(masala_chai)  
masala_chai.origin = "Sri Lanka"
print(masala_chai)


class Coffee:
  pass

class Cappuccino(Coffee):
  pass


orange_coffee = Coffee()

print(type(orange_coffee))
print(type(orange_coffee) is Coffee)
print(type(orange_coffee) is Cappuccino)