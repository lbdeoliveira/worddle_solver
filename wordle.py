def get_vocab(dictionary_file="/usr/share/dict/words"):
    '''
    Input:  filepath to built-in dictionary file
            (for unix/mac this will usually be 
            "/usr/share/dict/words")
    Output: set of all 5-letter words in dictionary
    '''
    words = set()
    with open(dictionary_file, 'r') as f:
        for word in f.readlines():
            word = word.strip()
            if len(word) == 5:
                words.add(word.lower())
    return words


def remove_words(vocab, input_word, output):
    '''
    Inputs:
        * set
        * input_word - word sent to worddle (str)
        * output - list of numbers indicating matches
            (-1 = no match, 0 = wrong position, 1 = right position)
            (-1 = grey, 0 = yellow, 1 = green)
    
    Function does not return anything, just removes invalid words
    from the vocab set.
    '''
    remove_words = set()
    for i in range(5):
        letter, match = input_word[i], output[i]
        if match == -1:
            [remove_words.add(word) for word in vocab if letter in word]
        elif match == 0:
            [remove_words.add(word) for word in vocab if letter == word[i]]
        else:
            [remove_words.add(word) for word in vocab if letter != word[i]]
    for word in remove_words:
        vocab.remove(word)
