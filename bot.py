import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import os
from wordle import *
import numpy as np


# Sends word to wordle, saves response screenshot as png
def guess_word(driver, word, screenshot_dir="guesses"):
    # Guess word
    actions = ActionChains(driver)
    actions.send_keys(word)
    actions.send_keys(Keys.ENTER)
    actions.perform()
    time.sleep(3)
    # Save screenshot of response
    fname = os.path.join(screenshot_dir, f'{time.time()}.png')
    driver.get_screenshot_as_file(fname)
    time.sleep(1)


def clear_response(driver):
    actions = ActionChains(driver)
    for _ in range(5):
        actions.send_keys(Keys.BACK_SPACE)
    actions.perform()
    
    
# Call driver, get Wordle
driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get('https://www.nytimes.com/games/wordle/index.html')
time.sleep(3)


# Try clicking out of rules tile
try:
    # Try clicking on current mouse position
    actions = ActionChains(driver)
    actions.click()
    actions.perform()
    print("Successfully clicked!")
    time.sleep(3)
except:
    # Temporary workaround: manually close button
    print("Click the close button (auto-click failed)")
    time.sleep(5)


# Solving algorithm
solved = False
vocab = get_vocab()
valid_letters = set()

while not solved:
    # Pick a random word from the set
    selection = np.random.choice(list(vocab))
    print("Guessed:", selection)
    # Send guess to wordle
    guess_word(driver, selection)
    # Should type response as list of numbers separated
    # by commas, no spaces. Ex: 2,0,0,2,2
    response = input("Response:").lower().strip()
    if response == "na":
        clear_response(driver)
        continue
    if response == "done":
        print(":(")
        break
    response = [int(n) for n in response.split(',')]
    valid_letters = remove_words(vocab, valid_letters, selection, response)
    # Solved?
    if response == [2,2,2,2,2]:
        print("Huzza!")
        break


# Close after 5 seconds
print("Closing in 5 seconds...")
time.sleep(5)
driver.quit()
