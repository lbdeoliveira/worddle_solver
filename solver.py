from wordle import *
import numpy as np

solved = False
vocab = get_vocab()
valid_letters = set()

while not solved:
    # Pick a random word from the set
    selection = np.random.choice(list(vocab))
    print("Type:", selection)
    # Should type response as list of numbers separated
    # by commas, no spaces. Ex: 2,0,0,2,2
    response = input("Response:")
    if response.lower().strip() == "na":
        continue
    response = [int(n) for n in response.split(',')]
    valid_letters = remove_words(vocab, valid_letters, selection, response)
    # Solved?
    if response == [2,2,2,2,2]:
        solved = True
        print("Huzza!")
