# Wordle solver

If you're anything like me then you're not very good at Wordle. If you're like me then not being good at Wordle bothers you. Luckily, we don't have to settle for mediocre performance when it comes to word puzzles because we can program!

In this repo, you'll find all the functions I used to build a bot to solve Wordle. During this process we'll explore:


* Puppeteering a Chrome browser using *Selenium*
* Extracting a response from an image using machine learning (*sklearn*) and deep learning (*PyTorch*)
* Error handling and driving the program from the terminal


## Finding candidate words

The process of finding candidate words for a guess is pretty straightforward:

1. Load in all vocab words (filtered for only 5-letter words)
2. Select a random word from remaining vocab words
3. Guess that word (send keys to Wordle site)
4. Extract a response for that guess: 
	* V1: manually enter the response in the terminal
	* V2: create a machine learning model that can extract the answer from the screenshot
5. Filter out words from the vocab set according to the response


## Building a bot

