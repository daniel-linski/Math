import random

a = random.randrange(1,21)
b = 0
s = ""

while b < a:
  s = s + str(b + 1) + ", "
  b += 1
print(s.removesuffix(", "))

s = ""
b = 1
while b <= a:
  s = s + str(a + b) + ", "
  b += 1
print(s.removesuffix(", "))
# initiate $a as random INT (integer) from 1 to 20
# with the help of WHILE loop, create a concatinated string 1, 2,.. $a
# print this string at the end of the loop
# with the help of another WHILE loop, create a concatinated string $a+1, $a+2,.. with the same $a numbers as the first string
# while still inside this loop, print a loop counter at every run of the loop
# print this string at the end of the loop