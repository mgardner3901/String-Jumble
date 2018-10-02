"""
stringjumble.py
Author: <your name>
Credit: <sources>

Assignment:

The purpose of this challenge is to gain proficiency with 
manipulating lists.

Write and submit a Python program that accepts a string from 
the user and prints it back in three different ways:

* With all letters in reverse.
* With words in reverse order, but letters within each word in 
  the correct order.
* With all words in correct order, but letters reversed within 
  the words.

Output of your program should look like this:

Please enter a string of text (the bigger the better): There are a few techniques or tricks that you may find handy
You entered "There are a few techniques or tricks that you may find handy". Now jumble it:
ydnah dnif yam uoy taht skcirt ro seuqinhcet wef a era erehT
handy find may you that tricks or techniques few a are There
erehT era a wef seuqinhcet ro skcirt taht uoy yam dnif ydnah
"""

userInput = input("Please enter a string of text (the bigger the better): ")

print("You entered " +'"' + userInput +'"'+ ". Now jumble it:")

word= ""
words = []
wordsBackwards=[]

for s in userInput:
        if s == " ":
            words.append(word)
            word=""
        else:
            word = word + s
              
words.append(word)



for i in range(len(words)-1, -1, -1):
    wordsBackwards.append(words[i])

rev= "" 
for s in userInput:
    rev = s + rev
            
print(rev)

print(' '.join(wordsBackwards))

characterRev = words

for t in range(0, len(characterRev), 1):
    wordRev = ""
    for r in (characterRev[t]):
        wordRev= r + wordRev
    characterRev[t] = wordRev

print(' '.join(characterRev))