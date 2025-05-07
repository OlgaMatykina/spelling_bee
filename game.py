def greeting():
    print('Welcome to Spelling Bee!')

def conditions(dayword, dayletter):
    print(f"Today's letters are {dayword.upper()} and the letter of the day is {dayletter.upper()}")

def exit_cond():
    print("Feel free to press XXXXX when you're done playing")

def finish(score):
    print(f"Congrats! Your final score is {score}")

def check(word, score, used, correct, dayword, dayletter):
    word = word.lower()
    if word == 'xxxxx':
        return True, score

    if word.isalpha() == False:
        print("Sorry, those clearly aren't letters")
        return False, score
    
    for letter in word:
        if letter not in dayword:
            print(f"Sorry, {letter} isn't one of the today's letters")
            return False, score

    if dayletter not in word:
        print(f"Sorry, the letter of the day {dayletter} is missing. Try again")
        return False, score
    
    if word in used:
        print("Sorry, you've already used this word. Try another")
        return False, score

    if len(word) < 4:
        print('Sorry, this word is too short')
        return False, score

    if word not in correct:
        print("Sorry, the word doesn't seem correct")
        return False, score
    
    if len(word) == 4:
        ball = 1
    elif len(word) > 4 and len(word) < 8:
        ball = len(word)
    else:
        ball = 2 * len(word)
    score += ball
    print(f'Cool! You found the word "{word}" and earned {ball} points')
    used.append(word)
    return False, score

def play():
    dayword = 'ACILMTY'.lower()
    dayletter = 'T'.lower()
    correct = [
        'ALIT', 
        'AMITY', 
        'ATILT', 
        'ATTIC', 
        'CACTI', 
        'CALAMITY', 
        'CATALYTIC', 
        'CATALYTICALLY', 
        'CATCALL', 
        'CATTAIL', 
        'CATTILY', 
        'CATTY', 
        'CITY', 
        'CLIMACTIC', 
        'CLIMACTICALLY', 
        'CLIMATIC', 
        'CLIMATICALLY', 
        'ILLICIT', 
        'ILLICITLY', 
        'ITALIC', 
        'ITTY', 
        'LACTIC', 
        'LAITY', 
        'LICIT', 
        'LICITLY', 
        'LILT', 
        'LIMIT', 
        'MALT', 
        'MALTY', 
        'MILITIA', 
        'MITT', 
        'TACIT', 
        'TACITLY', 
        'TACT', 
        'TACTIC', 
        'TACTICAL', 
        'TACTICALLY', 
        'TACTILITY', 
        'TAIL', 
        'TALC', 
        'TALI', 
        'TALL', 
        'TALLIT', 
        'TALLY', 
        'TATAMI', 
        'TATTY', 
        'TILL', 
        'TILT'
    ]
    correct = [word.lower() for word in correct]

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