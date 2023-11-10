import random
a = random.randrange(1,100)
b = random.randrange(1,100)
x = "category_a"
y = "category_b"
if a < 26:
  x = "category 1"
elif a > 25 and a < 51:
  x = "category 2"
elif a > 50 and a < 76:
  x = "category 3"
elif a > 75:
  x = "category 4"
else:
  x = "category ???"

if b < 26:
  y = "category 1"
elif b > 25 and b < 51:
  y = "category 2"
elif b > 50 and b < 76:
  y = "category 3"
elif b > 75:
  y = "category 4"
else:
  y = "category ???"

print("a =",a,"-",x)
print("")
print("b =",b,"-",y)
print("")
if x == y:
  print("a and b are in the same category","-",x)
else:
  print("a and b are in different categories","-",x,"and",y)
# generate 2 random numbers, a and b, from 1 to 100, and initialize $a and $b with it
# find out in which range both variables land: 
# if it is < 26 - category 1; 
# if it's > 25 but less than < 51  - category 2 
# if it's > 50 but less than < 76  - category 3 
# if it's > 75 but less than < 101 - category 4 
# print 'a = ' + $a + ' - category $x'
# print 'b = ' + $b + ' - category $y'
# if a and b are in the same category - print "a and b are in the same category $x"
# if not - print "a and b are in different categories, $x and $y"