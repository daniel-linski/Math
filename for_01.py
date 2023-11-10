import random

a = random.randrange(1,16)
print(a)
b = 0
for c in range(1,(a + 2)):
  s = ""
  for b in range((b + c),(b + a * c + c),c):
    s = s + ", " + str(b)
  print(s.removesuffix(", ").removeprefix(", "))
# initiate $a as random INT (integer) from 1 to 15
# with the help of 2 (two) FOR loops, print $a + 1 number of concatinated strings, 
# first starts with 1, 2,.. $a (the step is 1), the second starts with $a+2, $a+4, .., the step is 2
# each string containing $a numbers
# to sum up: $a+1 rows of strings, $a numbers in each, glue ', ', step=1 for first row, step = 2 for the second row, and 1 more for each next row 