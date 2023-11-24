import pprint
# there is a $dict with data on 3 cars 
# print data from $dict in 2 formats:

# 1. print data in 2 lines per car brand: 
    # car brand  
    # specs, in one string, format "$key1: $value1, $key2: $value2" 
    # line brake 

# 2. print data in a column: 
# year 
# specs, in a column, format "car brand: $car_name
#                             $key1: $value1"
#                             $key2: $value2"

dict = {
  "Maserati Quattroporte": {
    "year": 2021,
    "color": "white",
    "price": "$142,400",
    "engine": "3.0 liter",
  },
  "Mercedes-Benz S-Class": {
    "year": 2020,
    "color": "lunar blue",
    "price": "$115,900",
    "engine": "4.0 liter",
  },
  "Genesis G90": {
    "year": 2023,
    "color": "black",
    "price": "$95,000",
    "engine": "3.5 liter",
  },
}
pprint.pprint(dict)
for k,v in dict.items():
  s = ""
  s += k + "\n"
  for k2,v2 in v.items():
    s += str(k2) + ": " + str(v2) + ", "
  print(s.removesuffix(", "))
  print("")

for k,v in dict.items():
  s = ""
  for k2,v2 in v.items():
    if k2 == "year":
      print(v2)
    else:
      s += str(k2) + ": " + str(v2) + "\n"
  print("car brand: " + str(k))
  print(s.removesuffix(", "))
  print("")