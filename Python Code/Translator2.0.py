sentence = "I went to the store today."
new_sentence = ""

for word.lower() in sentence.split():
    if word == "store":
        new_sentence = new_sentence + " almacenar "
    elif word == "went":
        new_sentence = new_sentence + " fuimos "
    else:
        new_sentence = new_sentence +  " " + word +" "
        
print(new_sentence)
        
