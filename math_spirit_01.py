import math

for x in range(1,):
  a = x ** 2
  b = x ** 2 + 12 * x + 72
  c = x ** 2 + 24 * x + 144
  if math.sqrt(b) == int(math.sqrt(b)):
    print(str(x) + ":",a,b,c)
    print("square")