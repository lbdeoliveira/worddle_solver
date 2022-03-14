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
        * vocab - set of all allowable words
        * input_word - word sent to worddle (str)
        * output - list of numbers indicating matches
            (0 = no match, 1 = wrong position, 2 = right position)
            (0 = grey, 1 = yellow, 2 = green)
    
    Function does not return anything, just removes invalid words
    from the vocab set.
    '''
    remove_words = set()
    for i in range(5):
        letter, match = input_word[i], output[i]
        # Remove words containing invalid letter
        if match == 0:
            [remove_words.add(word) for word in vocab if letter in word]
        # Remove words with valid letter in wrong position
        # and remove words without valid letter
        elif match == 1:
            [remove_words.add(word) for word in vocab if letter == word[i]]
            [remove_words.add(word) for word in vocab if letter not in word]
        # Remove words without valid letter in right position
        else:
            [remove_words.add(word) for word in vocab if letter != word[i]]
    for word in remove_words:
        vocab.remove(word)
        
        

