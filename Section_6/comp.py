beverages=["coffee", "tea", "juice", "soda", "water","iced tea" , "iced coffee", "lemonade","water", "smoothie", "milkshake" ,"milkshake", "iced latte", "iced mocha", "iced cappuccino", "iced espresso", "iced americano", "iced caramel macchiato", "iced vanilla latte", "iced chai latte", "iced matcha latte", "iced hot chocolate", "iced green tea", "iced tea", "iced herbal tea", "iced tea", "iced bubble tea", "iced boba tea", "iced milk tea", "iced Thai tea", "iced Vietnamese coffee", "iced affogato", "iced frappuccino", "iced blended coffee drink"]
# key_t = []
# def filter_beverage(beverage,key):
#   res = [key_t.append(key_b) for key_b in beverage if key in key_b]
#   return res
# filter_beverage(beverages,"iced")
# print(key_t)

# def unique_bev(beverages):
#   unique_beverages = {bev for bev in beverages}
#   return unique_beverages

# def count(set):
#   return len(set)

# print(unique_bev(beverages))
# print(count(beverages))
# print(count(unique_bev(beverages)))

dict_bev = {
  'hot':[bev_h for bev_h in beverages if "iced" not in bev_h],
  'iced':[bev_i for bev_i in beverages if "iced" in bev_i]
}

dict_bev={
  "iced latte": 40,
  "iced mocha": 35,
  "iced cappuccino": 90
}


dict_bev_dollar= {f"{bev}": f"{price / 80 :.0f}$ and {price % 80}cents"  for bev, price in dict_bev.items()}

print(dict_bev_dollar)