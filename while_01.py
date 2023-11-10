import random

"""a = random.randrange(1,11)
b = 0
while b < a:
  b += 1
  if b == a:
    print(b)
  else:
    print(str(b) + ",",end=" ")"""


a = random.randrange(1,11)
b = 0
s = ""
while b < a:
  s = s + str(b + 1) + ", "
  b += 1
print(s.removesuffix(", "))
# initiate $a as random INT (integer) from 1 to 10
# with the help of WHILE loop, create a concatinated string 1, 2,.. $a
# print this string at the end of the loop