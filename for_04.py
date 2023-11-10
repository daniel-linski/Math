import random

a = random.randrange(1,12)
s = ""

for b in range(1,(2 * a),2):
  #print(str(b) + ", ",end="") if b < (2 * a - 2) else print(b)
  s = s + ", " + str(b)
print(s.removesuffix(", ").removeprefix(", "))
c = b
s = ""
for b in range(c,(c + 3 * a),3):
  s = s + ", " + str(b)
print(s.removesuffix(", ").removeprefix(", "))
  #print(str(b) + ", ",end="") if b < ((c + 3 * a) - 3) else print(b)

# initiate $a as random INT (integer) from 1 to 11
# with the help of FOR loop, create a concatinated string starting from 1, 
# ", " as glue, with $a numbers, with step 2 (i.e. 1, 3, ..) 
# with the help of another FOR loop, create another concatinated string 
# which starts with the number at the end of the first string, glue ", ", 
# with $a numbers, step 1 (or step 3, your choice)