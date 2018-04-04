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



    
score=0
    
howManyLettersInHand=0
for char2 in playHand:
    howManyLettersInHand += playHand[char]
while howManyLettersInHand > 0:
    print ("Current Hand:   ", end='')
    for char in playHand:
        counter = (playHand[char])
        while counter > 0:
            print (char, ' ', end='')
            counter -=1
    userInput = input (str("Enter word, or a . to indicate that you are finished: ")) 
    
    if userInput == ".":
        break
    elif isValidWord (userInput, playHand, wordList) == True:
        print ("yay")
        # If the input is a single period:
        
            # End the game (break out of the loop)

            
        # Otherwise (the input is not a single period):
        
            # If the word is not valid:
            
                # Reject invalid word (print a message followed by a blank line)

            # Otherwise (the word is valid):

                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line
                
                # Update the hand 
                

    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
