tweet = input('Please tweet here: ')
length = len(tweet)
remainder = 140 - length
if(length < 140):
    print("You have " + remainder + " characters remaining")
if(length == 140):
    print("You have no characters remaining")
