import random
#print(12%6


"""x%y means divide x by y and take the remainder"""
x = 0
a = random.randrange(1,51)

if not a % 2:
  print(a,"is divisible by 2")
  x = 1

if a % 3 == 0:
  print(a,"is divisible by 3")
  x = 1

if a % 5 == 0:
  print(a,"is divisible by 5")
  x = 1

if a % 7 == 0:
  print(a,"is divisible by 7")
  x = 1

if a % 9 == 0:
  print(a,"is divisible by 9")
  x = 1

if a % 11 == 0:
  print(a,"is divisible by 11")
  x = 1

if a % 13 == 0:
  print(a,"is divisible by 13")
  x = 1

if x == 0:
  print(a,"is not divisible by 2,3,5,7,9,11 or 13")
# try to Run the following: print(12%5); print(12%6); print(12%7); print(12%8); 
# guess what is the meaning of operator '%' 
 
# initiate $a as random INT (integer) from 1 to 50 
# check if $a id divisible by: 2,3,5,7,9,11,13
# print eaach time '$a is divisible by' INT above if it is true 
# after all checks, print '$a is not divisible by 2,3,5,7,9,11 or 13' if you have found that it is NOT divisible to anything