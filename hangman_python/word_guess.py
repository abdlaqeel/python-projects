#remove aeestrics where word is guessed right
def asterisker(word, word_encod, idx, guess):
        return word[:idx] + guess + word_encod[idx+1:]

def guess_letter(wordLst):
    from random import randint
    restart = 'y'
    while restart == "y": #while loop for contiuation of game
        x = randint(0, len(wordLst)-1) #randomly picks a random word from provided list
        wrong = 0
        right = 0
        word = wordLst[x]
        word_encod = "*" * len(word) #produces aestrics for lenght of word 
        while right <= len(word)-1: #asks for a new guess till the word is guessed completely
            guess = input("Guess a letter in the word " + word_encod + " >").strip().lower()
            if len(guess)>1:
                print("Enter one letter at a time: ")
                guess = input("Guess a letter in the word " + word_encod + " >").strip().lower()
            else:
                if guess in word:
                    idx = word.find(guess)
                    word_encod = asterisker(word,word_encod, idx, guess) #if guessed right aestricker called and increment in right
                    right += 1
                if guess not in word:
                    print("         ",guess, "is not in word") #if guessed wrong, told its wrong and increment in wrong
                    wrong += 1
        print("The word is", word, "You missed", wrong, "times.")
        restart = input("Do you want to guess for another word? Enter y or n> ").strip().lower()

def main():
    wordLst = ["brown", "amazon", "change", "computer"] #defines a list for the game
    guess_letter(wordLst)

main()
