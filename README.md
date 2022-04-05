# Wordle solver

This project stems from my profound mediocrity in word puzzles, namely Wordle. Luckily, I can program so I coded up a bot that solves Wordle for me! 

In this repo, you'll find all the functions and the Python script that drives the our little puzzle solver. During this process we'll explore:

* Puppeteering a Chrome browser using *Selenium*
* Error handling and driving the program from the terminal

As it stands, this is a command-line program that requires the user to input the responses from the webpage. In future updates of this repository, I will use machine learning techniques to fully-automate this process. I'm working on this in my infinite spare time between working and grad school, so expect a fully self-sufficient bot soon but not too soon.


## Algorithm

The algorithm for solving wordle is pretty straightforward. We start out by loading in all valid words from our local computer's built-in dictionary file. For Mac users, these words are usually found in $\texttt{"/usr/share/dict/words"}$.

The program runs as follows:

1. Load in all vocab words (filtered for only 5-letter words).
2. Select a random word from remaining vocab words.
3. Guess that word (send keys to Wordle site).
4. Extract a response for that guess. For now we will enter this response in the command line.
5. Filter out words from the vocab set according to the response.
6. Repeat 2-5 until puzzle is solved or we run out of guesses.


## Building the bot

I built this bot using Python and Selenium to drive a Chrome web browser. Make sure you have the latest *chromedriver* and Chrome browser for everything to run smoothly.

One big problem I ran into was wrestling with the shadow roots in the source code of the Wordle webpage. This made finding elements like the close button for the explainer window and the game tiles for sending keys and getting responses much more complicated than I initially anticipated. Unfortunately, it just so happens that pretty much everything that we need to interact with on the Wordle webpage falls under these shadow roots.

<p align="center">
<img src="https://github.com/lbdeoliveira/wordle_solver/static/source.png" width="800">
</p>

Luckily, instead of clicking or sending keys to a specific element, we can use Selenium *Actions* to "generally" click or type. When the page first opens, we simply tell the bot to "click" and this closes the instruction tile. Whenever we want to type in a word, we simply "send keys" as if we were typing on the keyboard without having to identify any webpage element in particular.

**Beware!** I'm collecting screenshots as training data for some machine learning models that will hopefully automate the entire process. For you, this means that you'll have to either comment out line 21 of *bot.py*, otherwise, create a folder in your working director called *guesses* to avoid any errors.


## Driving the bot

Now that we know how the algorithm and bot work, let talk about how we actually get the bot to solve Wordle.

We initialize the program by typing *python bot.py* in the terminal. This will launch a Chrome browser that will nagivate to the Wordle website, close the intro guide, and send the first guess.

Your job at this juncture is to provide feedback to the program in the as follows. If the bot guesses an invalid word (this happens often) type *na* in the terminal.

<p align="center">
<img src="https://github.com/lbdeoliveira/wordle_solver/static/na.png" width="800">
</p>

**Comments here**

For valid words, we will type a list of comma-separated numbers to denote the different colors:

* Grey: 0
* Yellow: 1
* Green: 2

<img src="https://github.com/lbdeoliveira/wordle_solver/static/ex1.png" width="800">
</p>

**Comments here**

<img src="https://github.com/lbdeoliveira/wordle_solver/static/ex2.png" width="800">
</p>
