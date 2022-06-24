#taking input of word
word = input("Please enter a word or zzz to quit: ")
#outerloop setting sentimental value
while word != "zzz":
    consonants = ("bcdfghjklmnpqrstvwxyz")
    newLetter = ''
    count = 0
#inner loop searching for consonants and replacing with ?
    for letter in word.lower():
        if letter in consonants:
            letter = "?"
            count = count + 1
        newLetter += letter
#Output
    print("The original word is: ", word.lower())    
    print("The word without consonants is: ", newLetter)
    print("The number of consonants in the word are: ", count)
    print()
#next input
    word = input("Please enter another word or zzz to quit: ")

