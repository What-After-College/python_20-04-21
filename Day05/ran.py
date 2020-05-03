import random
"""
1 10
8
7
9
11 # it can't pick eleven because it's out of range

randint

"""
# k =  random.randint(1,100)
# print(k)

"""

Tanish --> 55
Rithic --> 22
Vanshika --> 30
Akanshu --> 74
Bhargavi --> 85

"""

names = ["Akanshu", "Bhargavi", "Rithic", "Joshna", "Tanish", "Vanshika", "Thor", "Captain America", "Wonder Woman"]
k = random.randint(0,len(names)-1)
print(names[k])


