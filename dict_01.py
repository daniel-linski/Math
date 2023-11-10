from random import randrange
from collections import Counter
from pprint import pprint

lst = []
for x in range(1,21):
  x = randrange(1,11)
  lst.append(x)

print(lst)
print("")

dict_count = Counter(lst)
print(dict_count) 

#z = 0
#for val in lst:
dict = {}
for ind, val in enumerate(lst):
  dict[ ind ] = dict_count[ val ]
  #z += 1

pprint(dict)

# generate a list $lst, containing 20 members, each member a random INT, from 1 to 10; 
# print this list 
# create a dictionary $dict, of the length of $lst, where index memebers correspond to indexes of $lst, and values are the number of times $lst member is found in $lst (number of it's duplicates) 
# i.e., if $lst = [ 1, 2, 2, 3, ], 
# then $dict = { 0: 1, 1: 2, 2: 2, 3: 1, }