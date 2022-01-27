def decrypt(file,x):
    partial_keys = get_all_partial_keys(['e', 't', 'a', 'o'], LetterCounter(file, 4)) #use partial keys to generate dictionaries set
    key = partial_keys[x]  #x is the set of keys out of all the possible dictonary, use as testing
    print(key)
    with open(file) as word_list:  
        words_list = word_list.read().split()
    print(words_list)

    open('cypher_output.txt', 'w').close()
    #for word in words_list:
        #for letter in word:
           # if letter == key[key]:
            
                
def decrypt(file, x): #this prints the set of all partial decryptions
    partial_keys = get_all_dictionaries(['e','i','a'],LetterCounter(file,x))  # use partial keys to generate dictionaries set
    key = partial_keys[x]  # x is the set of keys out of all the possible dictonary, use as testing
    letters = []
    partial = []
    with open(file) as words_list:
        words_list = words_list.read().split()
        for key in partial_keys:#{}
            for item in key: #eta
                for word in words_list: #VQVXGVW
                    for letter in word: #V
                        if key[item] == letter:
                            letter = item
                        letters.append(letter)
                    partial.append(letters)
                    letters = []
            print(partial)

    open(file).close()
