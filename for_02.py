import random

a = random.randrange(1,21)
s = ""

for b in range(1,(a + 1)):
  #print(str(b) + ", ",end="") if b < a else print(b)
  s = s + ", " + str(b)
print(s.removesuffix(", ").removeprefix(", "))
s = ""
for b in range((a + 1),(2 * a + 1)):
  s = s + ", " + str(b)
print(s.removesuffix(", ").removeprefix(", "))
  #print(str(b) + ", ",end="") if b < (2 *a) else print(b)

# initiate $a as random INT (integer) from 1 to 20
# with the help of FOR loop, create a concatinated string 1, 2,.. $a
# print this string at the end of the loop
# with the help of another FOR loop, create a concatinated string $a+1, $a+2,.. with the same $a numbers as the first string
# while still inside this loop, print a loop counter at every run of the loop
# print this string at the end of the loop