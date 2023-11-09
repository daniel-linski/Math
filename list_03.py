import random

a = random.randrange(10,17)
lst = []
max = 77
min = -19
lst_max = min - 1
lst_min = max + 1
print("a =",a)

for x in range(1,a + 1):
  b = random.randrange(min,max + 1)
  lst.append(b)

print(lst)

for x in lst:
  if x > lst_max:
    lst_max = x
    
for x in lst:
  if x < lst_min:
    lst_min = x

print("lst_max =",lst_max)
print("lst_min =",lst_min)

# generate a random INT $a, from 10 to 16
# print it as 'a = $a'
# generate a list, containing $a members, each member a random INT, from 1 to 20; print it
# find the biggest member of this list, $lst_max; print it as 'lst_max = $lst_max'
# find the smallest member of this list, $lst_min; print it as 'lst_min = $lst_min'