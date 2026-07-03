temp = 0
threshold = 100
while temp <= threshold:
  if temp < threshold:
    print(f"Temperature is {temp}°C. It's safe to continue.")
    temp += 10
  else:
    print(f"Temperature is {temp}°C. It's too hot! Please stop.")
    break;
