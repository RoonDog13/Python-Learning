name_count = {} # declare empty dictionary
for name in names:
    if name not in name_count:
        name_count[name] = 1
    else:
        name_count[name] += 1
print('name_count', name_count.items())
