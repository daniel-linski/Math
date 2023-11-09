import random

a = random.randrange(3,10)
s = ""
lst = [1,2,3,4,5,6,7,8,9,10]
print(len(lst))
print("a =",a)
print(str(lst).removeprefix("[").removesuffix("]"))

for x in lst:
  s = s + str(x * a) + ", "
print(s.removesuffix(", "))

# you are given a list lst = [1,2,3,4,5,6,7,8,9,10,]
# calculate and print the LENGTH of this list
# initiate $a as random INT from 3 to 9; print it, as 'a = $a'
# print 2 lines of numbers, first row is list members 
#(divided by ', ', no comma in the end) 
# second line is a result of multiplication of a respective list number 
# and $a - i.e. if $a = 2, second line will be like 2, 4, 6, ...