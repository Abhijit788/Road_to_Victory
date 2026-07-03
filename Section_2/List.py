strong_brew = ["Espresso", "Americano", "Cappuccino", "Latte"]*2

print(strong_brew)
print(type(strong_brew))
print(f"Is Espresso in strong brew? {'Espresso' in strong_brew}")
print(f"Is Mocha in strong brew? {'Mocha' in strong_brew}") 


raw_spieces=bytearray(b"cardamom, cinnamon, clove")
print(raw_spieces)
print(type(raw_spieces))
raw_spieces=raw_spieces.replace(b"card",b"elaichi")
print(raw_spieces)
