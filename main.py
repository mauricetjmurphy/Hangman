# Import modules
import random

# Select a random word from a list
words = ['CandleStick', 'KitchenTable', 'SofaBed', 'SittingRoom']

def lowercaseList(l):
    for i in range(len(l)):
        l[i] = l[i].lower()
    return l


def listToString (l):
    strl = ''
    for i in l:
        strl += i
    return strl


def getRandomWord(l):
    word = random.choice(l)
    newWord = ''
    for e in word:
        newWord += e
    return newWord


# Split the word into letters
def split(w):
    return [i for i in w]

word = getRandomWord(words)

# Make a list that is the same length as splitWordList
def createEmptyWordList(l):
    EmptyWordList = []
    for i in l:
        i = '_'
        EmptyWordList.append(i)
    return EmptyWordList

splitWordList = split(word)
emptyWordList = createEmptyWordList(word)
lives = 5

print(splitWordList)

end_of_game = False

while not end_of_game:
#  Ask the user to guess a letter/letters in the word
    guess = [input('Please guess a letter!\n')]         
# Check to see if the letter exists
    for i in range(len(splitWordList)):
        if splitWordList[i].lower() in guess: 
            emptyWordList[i] = splitWordList[i]

    print(emptyWordList)
            
    strGuess = listToString(guess)
    splitWordList = lowercaseList(splitWordList)

    if strGuess not in splitWordList:
        lives -= 1
        print(f'You have {lives} lives left!')
        if lives < 1:
            end_od_game = True
            print('You lose!') 
            break


    if '_' not in emptyWordList:
        end_od_game = True
        print('You win!')
            
    