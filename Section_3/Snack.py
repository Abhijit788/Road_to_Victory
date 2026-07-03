snack =  input("What snack do you want to order? ").lower()
order_placed = False
samosa_count = 0
cookies_count = 0
total_samosa_sales = 0
total_cookies_sales = 0
smosa_price = 10
cookies_price = 20
while not order_placed:
  if snack == "cookies" or snack == "samosa":
    print(f"Order Confirmed of {snack}.")
    if snack == "cookies":
      cookies_count += 1
      total_cookies_sales += cookies_price
    else:
      samosa_count += 1
      total_samosa_sales += smosa_price
    
    order_placed = True
  else:
    check = input(f"Sorry, we don't have {snack}. Do you want to order something else? ").lower()
    if check == "yes":
      snack = input("What snack do you want to order? ").lower()
    else:
      print("Thank you for visiting!")
      print(f"Total Samosa Sales: {total_samosa_sales}")
      print(f"Total Cookies Sales: {total_cookies_sales}")
      print(f"Total Samosa Ordered: {samosa_count}")
      print(f"Total Cookies Ordered: {cookies_count}")
      break