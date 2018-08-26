sentence = "I went to the store for fun"
sentence1 = "Shijit said hello the other day"
sentence2 = "I ran to the store"
sentence3 = "I went shopping"




def spanishTranslator(sentence):
    new_sentence = ""
    dictionary_key = {"store": "almacenar", "went":"fuimos","hello":"hola","bye":"adios","ran":"corre","i":"yo","why":"porque",
                      "to":"a", "today":"hoy", "the":"el"}
    for word in sentence.lower().split():
        if word not in dictionary_key:
            new_sentence = new_sentence + " " + word + " "
        else:
            new_sentence = new_sentence + " " + dictionary_key[word] + " "
    print(new_sentence)

spanishTranslator(sentence)
spanishTranslator(sentence1)
spanishTranslator(sentence2)
spanishTranslator(sentence3)
