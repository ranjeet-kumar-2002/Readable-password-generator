
# word+symbol+number

import random 

upper_char=['A','B','C','D','E']
special_char=['@','#','^','&','!']
lower_char=['a','b','c','d','e']
num =['1','2','3','4','5']


passw= random.choice(upper_char)+random.choice(lower_char)+random.choice(num)+random.choice(special_char)+random.choice(upper_char)+random.choice(lower_char)+random.choice(num)+random.choice(special_char)
print(passw)


