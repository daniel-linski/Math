import pprint

# below you are given 2 dictionaries, with info about 2 students
# generate another dictionary with the same structure, with info about both students in it
# use .update() function for the merge
# print the resulting dictionary
# print info about students marks by year
# format: 
# 2000: Joe Smuth - English: 1, Math: 1, Physics: 1 
#       Smoe Juth - English: 2, Math: 2, Physics: 2 
# 3000: Joe Smuth - English: 3, Math: 3, Physics: 3 
#       Smoe Juth - English: 4, Math: 4, Physics: 4

dict1 = {
    "class": {
        "student": {
            "Alex Linski": {
              "marks": { 
                  2022: {
                    "marks": {                
                       "Math": 95,
                       "English": 85,
                       "Science": 95,
                       "Music": 5,
                    }
                  },
                  2023: {
                    "marks": {                
                       "Math": 92,
                       "English": 80,
                       "Science": 100,
                       "Music": 25,
                  }
                }                  
            }
        }
    }  
  }
}

dict2 = {
    "class": {
        "student": {
            "Daniel Linski": {
              "marks": {
                  2022: {
                    "marks": {                
                       "Math": 100,
                       "English": 50,
                       "Science": 100,
                       "Music": 77,
                    }
                  },
                  2023: {
                    "marks": {                
                       "Math": 95,
                       "English": 88,
                       "Science": 70,
                       "Music": 67,
                  }
                }                  
            }
        }
    }  
  }
}

dict1["class"]["student"].update(dict2["class"]["student"])

s = ""
dict_final = {}
name = ""
for name, v in dict1["class"]["student"].items():
  for yer,val in v["marks"].items():
    
    s = ""
    for subj,mark in val["marks"].items():
      s += subj + ": " + str(mark) + ", "
      
    s.removesuffix(", ")
    
    if yer not in dict_final:
      dict_final[yer] = {name: s}
    else:
      dict_final[yer].update({name: s})

pprint.pprint(dict_final)

for k,v in dict_final.items():
  s = str(k) + ": "
  for k2, v2 in v.items():
    s += k2 + " - " + v2.removesuffix(", ") + "\n"
  print(s)