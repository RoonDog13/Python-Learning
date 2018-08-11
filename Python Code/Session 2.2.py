# Find duplicates in a list and show counts.
names = ['bob', 'susan', 'bob', 'dan', 'susan']
seen_before = []
for name in names:
    if(name not in seen_before):
        seen_before.append(name)
    elif(name in seen_before):
        print(name + " is a duplicate")
    
