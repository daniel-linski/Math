top = 0
interval = 7
spacing = 5
delete = ""
s = "*"
for b in range(1,spacing + 1):
  delete = delete + " "
delete = delete + "*"
print("¯\_(ツ)_/¯")
if top == 0:
  s = ""
print(s)
for b in range(1,top):
  for b in range(1,interval + 1):
    for b in range(1,spacing + 1):
      s = s + " "
    s = s + "*"
  print(s)
for b in range(1,top):
  s = s.replace(delete,"",interval)
  print(s.removeprefix(" ").removesuffix(" "))

print("¯\_(ツ)_/¯")

# Write a code to print the following pattern using the for loop:
# ¯\_(ツ)_/¯
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * * 
# *
# ¯\_(ツ)_/¯