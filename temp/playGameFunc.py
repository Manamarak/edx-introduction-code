# -*- coding: utf-8 -*-
"""
Created on Thu Apr  5 12:34:14 2018

@author: Evanderwalt
"""

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
      * If the user inputs 'n', let the user play a new (random) hand.
      * If the user inputs 'r', let the user play the last hand again.
      * If the user inputs 'e', exit the game.
      * If the user inputs anything else, tell them their input was invalid.
 
    2) When done playing the hand, repeat from step 1
    """
    
    firstHand=True
    gameRepeat = "b"
    validResponses = ["n", "r", "e"]
    while gameRepeat != "e":
        gameRepeat = input ("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        if gameRepeat not in validResponses:
            print ("Invalid command.")
        else:
            if gameRepeat == "n":
                thisHand = dealHand(HAND_SIZE)
                playHand(thisHand, wordList, HAND_SIZE)
                firstHand = False
            elif gameRepeat == "r":
                if firstHand == True:
                    print ("You have not played a hand yet. Please play a new hand first!")
                else:
                    playHand(thisHand, wordList, HAND_SIZE)
                    firstHand = False