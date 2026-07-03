# def make_chai_gen():
#   yield "chai"
# def make_coffee_gen():
#   yield "coffee"  

# def make_drink_gen():
#   yield from make_chai_gen()
#   yield from make_coffee_gen()
# for drink in make_drink_gen():
#   print(drink)

# print(list(make_drink_gen()))



# def _gen():
#   yield 100 
#   yield 200
#   yield 300
#   yield 400
#   yield 500

# lets = _gen()

# print(next(lets))
# print(next(lets))



def local_coffee():
  yield "Filter Coffee"
  yield "Sandwich Coffee"

def imported_coffee():
  yield "Cappuccino"
  yield "Mocha"
  yield "Macchiato"



def full_menu():
  yield from local_coffee()
  yield from imported_coffee()


# for coffee in full_menu():
#   print(coffee)


def coffee_stall():
  try:
    while True:
      order = yield "waiting for order"
  except :
    print("stall closed")


stall=coffee_stall()
print(next(stall))
stall.send("Cappuccino")
print(next(stall))
stall.close()