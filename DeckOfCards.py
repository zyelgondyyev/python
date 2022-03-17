#Name of the programmer: Zhandos Yelgondyyev

"""****************************************************************************
Overall notes (these notes do not replace in-code comments):
    
    This program is meant to create a deck of cards, shuffle the deck and cut it 
    at a random position; the top portion of the cut deck should be switched with 
    the bottom portion of the cut deck. Then, the deck should be dealt into 
    four hands each with 5 cards in the hand. Once a card is placed into a hand,
    it should be removed from the deck. The program reports to the screen each of 
    the hands with a list of the cards within the hands. 

    
****************************************************************************"""



# Your code begins here...
 
    
import random  

ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
suits = ["Hearts", "Diamonds", "Spades", "Clubs"] 

deck = []
for rank in ranks:
    for suit in suits:
        deck.append(rank + " of " + suit)
 
       
print (deck)


import random


class Deck: #A class with one attribute, Deck, which is a standard deck of 52 cards. 
  
   
   def __init__(self): #A constructor to create a deck of 52 cards
       
       ranks = ["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"] #creates a list which contains the possible ranks
       suits = ["Hearts", "Diamonds", "Spades", "Clubs"] #creates a list which contains the possible suits
       
       self._deck = [] #creates an empty deck
       
       for rank in ranks: #for loop to go through each possible rank
           for suit in suits: #nested for loop to go through each possible suit 
               self._deck.append(rank +" of "+suit) #appends the empty deck to populate with each of the possible card variations 
  
    
   
   def shuffle(self): #A function used to shuffle the deck.
       random.shuffle(self._deck) #Uses import random to randomly shuffle the deck created above. 
  
    
    
   def cut(self): #A function used to cut the deck randomly at any location and then puts the bottom cards on top of top cards.

       cut_location = random.randint(0,len(self._deck) - 1) #uses the import random to choose a random location in the deck to cut (from range 0 to the length of the deck -1). 

       top = self._deck[0: cut_location + 1] #Identifies the group of cards above the cut location
       
       bottom =self._deck[cut_location + 1:] #Identifies the group of cards below the cut location
      
       self._deck = bottom + top #Places the bottom pile above the top pile. 

  

   def dealem(self, n): #Function used to deal the cards and return a list of the top n cards from deck, with parameters n.

       cards_dealt = [] #Creates an empty list for the dealt cards

       if(len(self._deck) < n): #An if statement to check if the deck contains n cards
           n = len(self._deck) #else set n to the number of cards in the deck
      
        
       i = 0 #Initializes i to zero. 

       while(i < n): #A while loop to populate the cards_dealt with the top n cards from the deck.
           cards_dealt.append(self._deck.pop(0)) #This adds the first card of the deck to the end of cards_dealt, and removes it from the deck
           i += 1
           
       return cards_dealt #Returns the list of cards dealt  



def main(): #This is the client code, the main program. 

   deck = Deck() #Initializes the deck of cards function

   deck.shuffle() #Shuffles the deck

   deck.cut() #Cuts the deck
   
   # deal 4 hands of 5 cards each and display the hands
   for i in range(4): #For loop which creates 4 hands and goes through each of them
       print('Hand %d: '%(i+1)) #deals out and prints the each hand.
       
       hand = deck.dealem(5) #makes sure that each hand has 5 cards. 
       print(hand) #prints the hands
  
    
main() #Calls the main function  

  



# And ends here.




