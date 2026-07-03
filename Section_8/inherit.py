# class Base_Pizza:
#   def __init__(self,type_):
#     self.type = type_
  
#   def prepare(self):
#     print(f"Preparing {self.type} pizza")

# class Paneer_Pizza(Base_Pizza):
#   def add_toppings(self):
#     print(f"Preparing {self.type} pizza with paneer topping")

# class Pizza_Shop:
#   pizza_cls=Base_Pizza

#   def __init__(self,):
#     self.pizza = self.pizza_cls("Margherita")

#   def serve(self):
#     print(f"Serving {self.pizza.type} pizza")

# class Paneer_Pizza_Shop(Pizza_Shop):
#   pizza_cls=Paneer_Pizza



# shop = Pizza_Shop()
# shop.serve()

# paneer_shop = Paneer_Pizza_Shop()
# paneer_shop.pizza.add_toppings()



#MRO(Method Resolution Order) - It is the order in which the base classes are searched when executing a method.

# class A:
#   label = "Class A"

# class B(A):
#   label = "Class B: Masala Chai"


# class C(A):
#   label = "Class C: Herbal Chai"

# class D(B,C):
#   pass

# cup = D()
# print(cup.label)
# print(D.__mro__)


#staticmethod - A static method is a method that knows nothing about the class or instance

# class Pizza:
#   @staticmethod
#   def prepare(type_):
#     print(f"Preparing {type_} pizza")
  
# Pizza.prepare("Margherita")

#classmethod - A class method is a method that is bound to the class and not the object of the class. It can modify a class state that applies across all instances of the class. It takes cls as the first parameter while a regular method takes self.

# class pizzaOrder:
#   def __init__(self, type_, size):
#     self.type = type_
#     self.size = size
  
#   @classmethod
#   def get_order_from_dict(cls,orderData):
#     return cls(orderData["type"], orderData["size"])
  
#   @classmethod
#   def getOrderFromString(cls,orderString):
#     type_,size =orderString.split(",")
#     return cls(type_,size)
  
# order = pizzaOrder.get_order_from_dict({"type": "Margherita", "size": "Medium"})
# print(order.type)

# order2 = pizzaOrder.getOrderFromString("Pepperoni,Large")
# print(f"Order 2 a {order2.size} {order2.type} pizza")

#property decorator - The property() function in Python is used to get the property of a class. It is used to customize getters and setters for class attributes. It allows you to define methods in a class that can be accessed like attributes.

# class Student:
#   def __init__(self,name,age):
#     self.name = name
#     self.age = age

#   @property
#   def name(self):
#     return self._name
  
#   @name.setter
#   def name(self,value):
#     if not value:
#       raise ValueError("Name cannot be empty")
#     self._name = value

#   @property
#   def age(self):
#     return self._age

#   @age.setter
#   def age(self,value):
#     if value < 0:
#       raise ValueError("Age cannot be negative")
#     elif value > 16:
#       raise ValueError("Age cannot be greater than 16")
#     else:
#       self._age = value

# A = Student("John", 15)
# print(A.name)
# print(A.age)

# B=Student("Alice", 17)  # This will raise a ValueError: Age cannot be greater than 16
# print(B.name)
# print(B.age)