import random

a = random.randrange(1,16)
b = 0
c = 1

while c <= a:
  s = ""
  while b < (c * a):
    s = s + str(b + 1) + ", "
    b += 1
  print(s.removesuffix(", "))
  c +=1
# initiate $a as random INT (integer) from 1 to 15
# with the help of WHILE loops, print $a number of concatinated strings, 
# first starts with 1, 2,.. $a, the second starts with $a+1, $a+2,.. $a+$a, 
# each string containing $a numbers
# to sum up: $a rows of strings, glue ', ', step 1 for every next number in every string