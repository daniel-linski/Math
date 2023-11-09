import random

lst = []
for x in range(1,21):
  x = random.randrange(1,11)
  lst.append(x)


print(lst)
dict = {}
print("")
for x in lst:
  comp = x
  z = 0
  for y in lst:
    if ( y == comp ):
       z += 1
  dict[x] = z

print(dict)
# generate a list $lst, containing 20 members, each member a random INT, from 1 to 10; 
# print this list 
# create a dictionary $dict, of the length of $lst, where index memebers correspond to indexes of $lst, and values are the number of times $lst member is found in $lst (number of it's duplicates)
# do that through 2 FOR nested loops, WITHOUT using Counter() function