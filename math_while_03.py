import random
import math

a = 0
b = 0
while a < 100:
  #b = (int(a * (a + 1) / 2))
  b += a + 1
  a += 1
  print("Sum of 1-" + str(a) + ": " + str(b))
print("Total Sum: " + str(b))
# part 1
# write a while loop that adds all numbers from 1 up to 100 (inclusive)
# inside the loop, print $i (counter) and current $total_sum (i.e. 'step 6: 21')
# print $total_sum at the end of the loop

print("")

a = random.randrange(2,23)
b = 0
c = 1
while b < a:
  #c = math.factorial((b + 1))
  c *= (b + 1)
  b += 1
  print(str(b) + "!: " + str(c))

print("Final Factorial: " + str(c))

# part 2
# generate INT $a between 2 and 22
# write a while loop that multiliplies all numbers from 1 up to $a (inclusive)
# inside the loop, print $i (counter) and current $factorial (i.e. '4: 24')
# print $factorial at the end of the loop