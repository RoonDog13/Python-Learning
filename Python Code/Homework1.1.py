while True:
    name = input("Enter a name to check for duplicates: ").lower()
    length_of_name = len(name)
    seen_before = []
    double =[]
    for x in range (0,length_of_name):
        if(name[x] not in seen_before()):
            seen_before.append(name[x])
        else:
            duplicate_array.append(name[x])
            
    print("The duplicate characters are..")
    print(duplicate_array)

        

