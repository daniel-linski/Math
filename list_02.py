import random

lst = [1,3,5,7,9,11,13,15,17,19]
print( lst )

a = random.randrange(4,11)
b = random.randrange(2,6)
s = ""

print("a =",a)
print("b =",b)

lst[0], lst[-1] = lst[-1], lst[0]
print( lst )
print( "" )

for y in range(1,(a + 1)):
  for x in lst:
    s = s + str(x * b ** y) + ", "
  print(s.removesuffix(", "))
  s = ""

# you are given a list lst = [1,3,5,7,9,11,13,15,17,19]
# initiate $a as random INT from 4 to 10; print it, as 'a = $a'
# initiate $b as random INT from 2 to 5; print it, as 'b = $b'

# swap first and last members of the list
# print a lines of numbers, first row is list members multiplied by b each
#(divided by ', ', no comma in the end) 
# every next line is a result of multiplication of a respective number from the previous row