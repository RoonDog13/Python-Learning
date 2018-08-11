############FIRST PROGRAM
from collections import Counter
names = ['bob', 'susan', 'shijit', 'connor', 'connor', 'shijit', 'bob', 'dan', 'susan','jimmy','jimmy']
nonduplicates = []
duplicates = []
for name in names:
    if name not in nonduplicates:
        nonduplicates.append(name)
        print(name)
        print("was added to nonduplicates")
    elif name in nonduplicates:
        duplicates.append(name)
        print(name)
        print("was added to duplicates")
print("The duplicates are ")
print(duplicates)
##############FIRST PROGRAM

    
