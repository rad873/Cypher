
def histogram(string):
    word_dict = dict()
    for letter in string:
        if letter not in word_dict:
            word_dict[letter]= 1
        else:
            word_dict[letter] += 1
    return word_dict
histogram('banana')
