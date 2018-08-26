sentence = "I went to the store today."
new_sentence = ""
dictionary_key = {"store": "almacenar", "went":"fuimos"}

for word in sentence.lower().split():
    if word not in dictionary_key:
        new_sentence = new_sentence + " " + word + " "
    else:
        new_sentence = new_sentence + " " + dictionary_key[word] + " "
print(new_sentence)
