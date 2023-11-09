import random

uniquelst = []
z = 20
lst = []
for x in range(1,21):
  a = random.randrange(1,11)
  lst.append(a)

print(lst)

for x in lst:
  if x not in uniquelst:
    uniquelst.append(x)
    z -= 1
    
print(uniquelst)
print("number of found duplicates =", z)

# generate a list, containing 20 members, each member a random INT, from 1 to 10; 
# print this list 
# find and remove duplicates from the list; print the new list
# print the number of found duplicates