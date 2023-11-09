import random
import calendar

lst = []
for x in range(1,21):
  a = random.randrange(1,16)
  lst.append(a)

print(lst)
print("")

lst_2 = lst.copy()
for x in lst_2:
  comp = x
  z = 0
  for y in lst:
    if ( y == comp ):
      z += 1
  if z > 1:
    lst.remove(x)

print(lst)
print("")
lst_2 = lst.copy()
for x in lst_2:
  print( "checking: " + str(x))
  if x > 11:
    print(lst)
    lst.remove(x)
    print(x)
    print(lst)
    print(lst_2)
lst_2 = []

print(lst)
print("")

months = calendar.month_name[1:]
print(months)
print("")
print(lst)
print("")
for x in lst:
  lst_2.append((x+1,months[x]))

dict = {k: v for k, v in lst_2}
print(dict)
print("")

lst_2 = []
days = calendar.day_name[0:]
print(days)
print("")

for x in lst:
  if x < 8:
    lst_2.append((x,days[x-1]))
  else:
    lst_2.append((x,"-"))

dict_1 = {k: v for k, v in lst_2}
print(dict_1)
# generate a list $lst, containing 20 members, each member a random INT, from 0 to 15; print it
# remove all duplicates from this list
# remove all list members bigger than 11
# create a list $months of month names, by using "calendar" library, here is how:
'''
from calendar import month_name
months = month_name[1:]
'''
# note that this is a different format of using import; previously we were using import function this way:
'''
import calendar
months = calendar.month_name[1:]
'''
# print $months list; try both ways of using import functionality
# print $months list; try both ways of using import functionality
# try to use calendar.month_name[0:] instead of calendar.month_name[1:], see the difference

# create a dictionary $dict, where indexes are numbers from $lst and dictionary members are corrsponding month names from $months list; print it

# create list of weekdays, as 
'''
days = calendar.day_name[0:]
'''
# create a dictionary $dict1, where indexes are numbers from $lst and dictionary members are respective weekday names from $days list - if they exist; if index is too big - dictionary member should be "-"
# print $dict1