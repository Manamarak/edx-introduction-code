# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 00:21:13 2018

@author: Manamarak
"""

 
playHand ={'h':1, 'i':1, 'c':1, 'z':1, 'm':2, 'a':1}
wordList = ["me", "my", "him"]


        
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    handAlt = hand
    if word =='':
        return False
    if word in wordList:
            for char in word:
                if char in handAlt:
                    handAlt [char] -=1
                    if handAlt [char] < 0:
                        return False
                else:
                    return False
    else:
        return False 
    return True        



    
score = 0    
howManyLettersInHand=0
for char2 in hand:
    howManyLettersInHand += hand[char2]
while howManyLettersInHand > 0:
    print ("Current Hand:   ", end='')
    for char in hand:
        counter = (hand[char])
        while counter > 0:
            print (char, ' ', end='')
            counter -=1
    userInput = input (str("Enter word, or a . to indicate that you are finished: ")) 
    
    if userInput == ".":
        break
    elif isValidWord (userInput, hand, wordList) == False:
        print ("Sorry, that's not a valid response")
        print (" ")
    else:  
        score += getWordScore(word, howManyLettersInHand) 
        print ("Your score is: ", score)
        print (" ")
        hand = (hand, word)
                
print ("Your score is: ", score)
