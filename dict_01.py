import random
from collections import Counter

lst_1 = []
lst_2 = []
z = 0
for x in range(1,21):
  x = random.randrange(1,11)
  lst_1.append(x)

print(lst_1)
lst_2 = lst_1
dict = {}
print("")
dict_1 = Counter(lst_1)
for x in lst_1:
  #lst_2[z] = (z,dict_1[x])
  #dict[z] = dict_1[x]
  z += 1

dict = {k: v for k, v in lst_2}
print(dict)

# generate a list $lst, containing 20 members, each member a random INT, from 1 to 10; 
# print this list 
# create a dictionary $dict, of the length of $lst, where index memebers correspond to indexes of $lst, and values are the number of times $lst member is found in $lst (number of it's duplicates) 
# i.e., if $lst = [ 1, 2, 2, 3, ], 
# then $dict = { 0: 1, 1: 2, 2: 2, 3: 1, }