def letter_counter(file, x):
    '''
    :param file: fully unciphered code
    :param x: the number of letters to be assigned from the file
    :return: the x most popular letters in order
    '''
    dictionary = dict()
    the_list = []
    read_file = open(file)
    for line in read_file:                                                          # loops over each line in the file
        for letter in line:                                                         # loops over each letter in the line
            if letter not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":                          # check for lowercase letter
                pass
            else:
                if letter not in dictionary:                                        # if letter is lowercase, it will be added to the dictionary
                    dictionary[letter] = 1
                else:
                    dictionary[
                        letter] += 1                                                # if that letter already exists in the dict, its count will be increased by 1
    dictionary_descending = sorted(dictionary, key=dictionary.get, reverse=True)    # sort the library so that the most common letters is up top.
    for r in dictionary_descending:
        the_list.append(r)                                                          # this loop append the sorted letters to an empty list
        if len(the_list) > x - 1:
            return (the_list)


def get_all_dictionaries(domain, codomain):
    """
    Set domain to be the most frequent plaintext characters (in descending order).
    Set comain to be the most frequent ciphertext characters (in descending order).
    You may have more successful decryptions if the size of domain is strictly less than the size of codomain.
    :param domain: domain of map as a list
    :param codomain: codomain of map as a list, must be at least as large as domain
    :return: list of all injective maps (as dictionaries) from domain into codomain
    """

    global dictionary_list
    dictionary_list = list()

    if len(domain) <= len(codomain):
        generate_all_dictionaries(domain, codomain, dict())

    return dictionary_list


def generate_all_dictionaries(domain, codomain, partial_map):
    """ Used by get_all_dictionaries to recursively generate all injective maps (as dictionaries) from domain
    into codomain. Dictionaries are stored in global variable dictionary_list and returned by get_all_dictionaries.
    :param domain: domain of map as a list
    :param codomain: codomain of map as a list, must be at least as large as domain
    :param partial_map: partial injection that is built recursively
    :return: None"""

    global dictionary_list

    if len(domain) == 0:
        dictionary_list.append(partial_map)
    else:
        for target_elt in codomain:
            new_partial_map = partial_map.copy()
            new_domain = domain.copy()
            new_codomain = codomain.copy()

            new_partial_map[domain[0]] = target_elt
            new_domain.remove(domain[0])
            new_codomain.remove(target_elt)

            generate_all_dictionaries(new_domain, new_codomain, new_partial_map)


def scrap(result_list):
    '''
    :param result_list: possible decoded ciphers
    :return: remaining valid decoded ciphers
    '''
    all_words = open('words.txt')
    all_words = all_words.read().split()    # open plainwords dictionary and get all words in a list
    for item in result_list:
        if item.islower() == True:          # check for fully decrypted word by seeing if it is all lowercase
            if item not in all_words:
                result_list = []            # if a match can't be found the entire decrypted list is deleted
    return (result_list)


def decrypt(file, y):
    '''
    :param file: input text to be decoded
    :return: partially decoded and valid ciphers
    '''
    partial_keys = get_all_dictionaries(['e', 't', 'a', 'o', 'i', 'n', 's', 'h'], letter_counter(file,y))
    #use partial keys to generate dictionaries set, y is the # of letters to get, bigger the y, bigger the # of key dicts(more combos)
    for x in partial_keys:
        dict_key = x                                                                    # x is the chosen set of dict keys out of all possible combos
        dict_key.items()
        dict_key = {v: k for k, v in
                    dict_key.items()}                                                   # swap key and value in a key set dictionary for easier replacement
        with open(file) as word_list:                                                   # open example ciphertext file and put every word in a list
            words_list = word_list.read().split()
            result_list = words_list[:]                                                 # create a copy of words_list to be decrypted, so the original list is preserved
            for i, word in enumerate(
                    result_list):                                                       # enumerate the words (strings) as numbers so that it can be modified
                for key in dict_key:                                                    # for every key in a selected key set
                    result_list[i] = result_list[i].replace(key, dict_key.get(key))     # begin decoding by replacing the encrypted letters with its key from the key set
            result_list = scrap(result_list)                                            # check to see if decrytped message is valid
            print(result_list)  # print out the decrypted message, an empty list will be printed if the decrypted message is invalid
                                # if a valid message is found, the list will be filled with fully decrypted and correct words making up the original message


decrypt('ciphertext_ex.txt', 8)
