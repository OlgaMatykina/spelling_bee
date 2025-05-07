from .game import *
import nltk
import os
import random
import string

try:
    from nltk.corpus import words
    words.words()
except LookupError:
    nltk.download('words')
    from nltk.corpus import words

def finish(score):
    print(f"Congrats! Your final score is {score}")
    if os.path.exists('spelling_bee/best_score'):
        with open('spelling_bee/best_score') as file:
            best_score = int(file.readline())
    else:
        best_score = score
    if best_score < score or os.path.exists('spelling_bee/best_score') is False:
        best_score = score
        with open('spelling_bee/best_score', 'w') as file:
            file.write(str(best_score))
    print(f"Your best score is {best_score}")

def play():
    dayword = ''.join(random.sample(string.ascii_lowercase, 7))
    dayletter = random.choice(dayword)
    
    correct = set(words.words())
    used = []
    score = 0

    greeting()
    conditions(dayword, dayletter)
    exit_cond()

    exit_flag = False
    while not exit_flag:
        word = input("Please enter a word: ")
        exit_flag, score = check(word, score, used, correct, dayword, dayletter)

    finish(score)


if __name__=='__main__':
    play()