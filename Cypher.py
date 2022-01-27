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
                
