import random

unique_duplicate_lst = []
duplicate_lst = []
lst = []
for x in range(1,20):
  a = random.randrange(1,13)
  lst.append(a)

print(lst)

for x in lst:
  comp = x
  z = 0
  for y in lst:
    if ( y == comp ):
         z += 1
  if z > 1:
    duplicate_lst.append(x)

for x in duplicate_lst:
  if x not in unique_duplicate_lst:
    unique_duplicate_lst.append(x)

print(duplicate_lst)
print(unique_duplicate_lst)
# generate the list of random numbers, range from 1 to 21
# remove all the unique members from this list, print out the new list without those numbers
# form another list from this list of duplicates, where every duplicate number shows only once
# i.e. if the initial list lst = [ 1, 2, 2, 3, 4, 3 ]
# then lst1 = [ 2, 2, 3, 3, ] and lst2 =[ 2, 3, ]