import random
a = 3
b = 4
if a > b:
  print("big(a):",a)
  print("small(b):",b)
elif a == b:
  print("a equals b:",a)
else:
  print("big(b):",b)
  print("small(a):",a)

print("")

x = random.randrange(1,10)
y = random.randrange(1,10)
if x > y:
  print("big(x):",x)
  print("small(y):",y)
elif x == y:
  print("x equals y:",x)
else:
  print("big(y):",y)
  print("small(x):",x)
# initialize 'a' as a number from 1 to 10
# initialize 'b' as a number from 1 to 10
# if $a is bigger than 'b' - print 'small: $a' then 'big: $b'
# if $b is bigger than 'a' - print 'small: $b' then 'big: $a'
# if $a equals $b - print 'a equals b: $a'
# 
# now, find the way how, in PYTHON, to randomly generate number from 
# 1 to 10
# generate random number twice and initialize a and b with it
# print 'random a = ' + $a
# print 'random b = ' + $b
# and implement IF structure written above to this $a and $b