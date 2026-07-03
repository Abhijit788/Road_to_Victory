def tempalert():
    temp = int(input("Enter the current temperature in Celsius: "))
    if temp > 30:
        return "It's hot outside!"
    elif temp < 0:
        return "It's freezing outside!"
    else:
        return "The temperature is moderate."

# print(tempalert())


def prepare_chai(chai_type=input("Enter the type of chai")):
    if chai_type == "":
        return "No chai type entered. Please enter Masala, Ginger, or Cardamom."
    if chai_type.lower() == "masala":
        return "Preparing Masala Chai"
    elif chai_type.lower() == "ginger":
        return "Preparing Ginger Chai"
    elif chai_type.lower() == "cardamom":
        return "Preparing Cardamom Chai"
    else:
        return "Chai type not recognized. Please choose Masala, Ginger, or Cardamom."
    
print(prepare_chai())