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

def decrypt(file,x,y):
partial_keys = get_all_partial_keys(['e', 't', 'a', 'o'], LetterCounter(file, y)) #use partial keys to generate dictionaries set, y is the # of letters to get, bigger the y, bigger the # of key dicts(more combos)
dict_key = partial_keys[x]  #x is the chosen set of dict keys out of all possible combos
print(dict_key)
with open(file) as word_list: #open example ciphertext file and put every word in a list
    words_list = word_list.read().split()
    print(words_list)
    result_list = []
    #for i in dict_key
    for word in words_list:
        new_word = ''
        for char in word:
            for i in dict_key:
                if char == dict_key[i]:
                    new_word += i
                else:
                    new_word += char
                    break
        result_list.append(new_word)
    print(result_list)



def decrypt(file,x,y):
    partial_keys = get_all_partial_keys(['e', 't', 'a', 'o'], LetterCounter(file, y)) #use partial keys to generate dictionaries set, y is the # of letters to get, bigger the y, bigger the # of key dicts(more combos)
    dict_key = partial_keys[x]  #x is the chosen set of dict keys out of all possible combos
    dict_key.items()
    dict_key = {v:k for k,v in dict_key.items()}
    print(dict_key)
    with open(file) as word_list: #open example ciphertext file and put every word in a list
        words_list = word_list.read().split()
        print(words_list)
        result_list = words_list[:] # create a copy of words_list to be decrypted, so the original list is preserved
        for i, word in enumerate(result_list): #enumerate the words (strings) as numbers so that it can be modified
            for key in dict_key:
                    result_list[i] = result_list[i].replace(key,dict_key.get(key))
        print(result_list)

decrypt('ciphertext_ex.txt',1,4)
