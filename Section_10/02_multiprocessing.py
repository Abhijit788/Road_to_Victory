from multiprocessing import Process
import time


def preparePizza(name):
  print(f"Start of preparing {name} Pizza")
  time.sleep(3)
  print(f"End of preparing {name} Pizza")

if __name__=="__main__":
  
  pizza_makers=[
    Process(target=preparePizza,args=(f"Veg #{i+1}",))
    for i in range(3)
  ]

  for p in pizza_makers:
    p.start()

  for p in pizza_makers:
    p.join()

  print("All pizzas prepared.........")
# def brew_chai(name):
#     print(f"Start of {name} chai brewing")
#     time.sleep(3)
#     print(f"End of {name} chai brewing")

# if __name__ == "__main__":
#     chai_makers = [
#         Process(target=brew_chai, args=(f"Chai Maker #{i+1}", ))
#         for i in range(3)
#     ]

#     # Start all process
#     for p in chai_makers:
#         p.start()

#     # wait for all to complete
#     for p in chai_makers:
#         p.join()

#     print("All chai served")