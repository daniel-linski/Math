import random

a = random.randrange(1,12)
b = 1
s = ""

while b <= (2 * a):
  s = s + str(b) + ", "
  b += 2
print(s.removesuffix(", "))
c = b - 2
b -= 2
s = ""
while b < (c + a):
  s = s + str(b) + ", "
  b += 1
print(s.removesuffix(", "))
# initiate $a as random INT (integer) from 1 to 11
# with the help of WHILE loop, create a concatinated string starting from 1, 
# ", " as glue, with $a numbers, with step 2 (i.e. 1, 3, ..) 

# with the help of another WHILE loop, create another concatinated string 
# which starts with the number at the end of the first string, glue ", ", 
# with $a numbers, step 1