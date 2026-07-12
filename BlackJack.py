# to store the list of all cards
import random; #to shuffle the cards
class Card: 

    def __init__(self,suit , rank):
        # it will store suit and rank in variables
        self.suit = suit
        self.rank = rank

    def __str__(self):
        # it is the method to print a specific sentencce using f string to make it more readable and easy to understand
        return f"{self.rank['rank']} of { self.suit }"

# we created a deck class for instance of that class
class Deck:
    # constructor
    def __init__(self):
            # self.cards will store the combination of suits and rank meaning all cards
            self.cards = []
            # first we create a list of suits 
            suits = ["spades" , "clubs" , "hearts" , "diamonds"]
            # then we create a list of ranks
            ranks = [{"rank" : "A" , "value" : 11},
                    {"rank" : "2" , "value" : 2}, 
                    {"rank" : "3" , "value" : 3},
                    {"rank" : "4" , "value" : 4},
                    {"rank" : "5" , "value" : 5},
                    {"rank" : "6" , "value" : 6},
                    {"rank" : "7" , "value" : 7},
                    {"rank" : "8" , "value" : 8},
                    {"rank" : "9" , "value" : 9},
                    {"rank" : "10" , "value" : 10},
                    {"rank" : "J" , "value" : 10},
                    {"rank" : "K" , "value" : 10},
                    {"rank" : "Q" , "value" : 10}]
            # this loop will iterate through suits
            for suit in suits:
                # this will match each rank for each suit
                for rank in ranks:
                    # this will store the list of cards in cards list using card class to create a card object with suit and rank
                    self.cards.append(Card(suit,rank))
    # we create  a function that shuffle the cards
    def Shuffle(self):
        # agar card ki length 1 se jyada hai toh hi shuffle karna padega
        if len(self.cards) > 1:
            # using shuffle from random to shuffle cards
            random.shuffle(self.cards)
    # we create a function for the dealer which is computer that will pop two cards from the shufffled cards to provide the player
    def dealer(self,number):
        # we created an empty list to store the random two cards
        cards_dealt = []
    # this will pop a card from the list of cards
        for x in range(number):
            # agar cards ka length 0 se jyada hai toh hi card pop hoga
            if len(self.cards ) > 0:
                card = self.cards.pop()
                cards_dealt.append(card)
        return cards_dealt

class Hand:
    def __init__(self,dealer = False): #this will create a hand for the player and dealer and store the cards in a List and value of the hand in a variable. The dealer parameter is used to check if the hand is for the dealer or player. If dealer is True then it will be for dealer else for player.
        self.cards = []
        self.value = 0
        self.dealer = dealer
        
    def add_cards(self,card_list): #this will add the cards to the hand and calculate the value of the hand.
        self.cards.extend(card_list)

    def calculate_value(self): #this will calculate the value of the hand and return the value.
        self.value = 0
        has_ace = False #this will check if the hand has an ace or not
        for card in self.cards:
            card_value = int(card.rank["value"]) #this will get the value of the card from the rank dictionary and convert it to integer
            self.value += card_value #this will add the value of the card to the value of the hand 
            if card.rank["rank"] == "A":#this wiill check if the card is an ace or not
                has_ace = True

        if has_ace and self.value > 21:
            self.value -= 10 #this will subtract 10 from the value of the hand if the hand has an ace and the value is greater than 21 

    def get_value(self): 
        self.calculate_value()
        return self.value #this will return the value of the hand
    
    def is_blackjack(self):
        return self.get_value() == 21
    
    def display(self, show_all_dealer_cards = False): #this will display the cards in the hand and the value of the hand. If show

        print(f'''{"Dealer's " if self.dealer else "Your"}hand:''')
        for index, card in enumerate(self.cards):
            if index == 0 and self.dealer and show_all_dealer_cards == False and not  self.is_blackjack():
                print("hidden")
            else:
                print(card)
        
        if not self.dealer:
            print("Value:", self.get_value())
            print()

# deck = Deck() 
# deck.Shuffle() #this will shuffle the cards in the deck

# hand = Hand() #this will create a hand for the player
# hand.add_cards(deck.dealer(2)) #this will add two cards to the player's hand from the deck
# # print(hand.cards[0], hand.cards[1])#this will print the two cards in the player's  
# hand.display() #this will display the player's hand and value

class Game:
    def play(self):
        game_number = 0;
        games_to_play = 0;
        while games_to_play <= 0:
            try:
                games_to_play = int(input("How many games do you want to play ?" + "\n"))
            except :
                print("Invalid input. Please enter a valid number.")
        
        while game_number < games_to_play:
            game_number +=1

            deck = Deck()
            deck.Shuffle() #this will shuffle the cards in the deck


            player_hand = Hand() #this will create a hand for the player 
            dealer_hand = Hand(dealer = True) #this will create a hand for the dealer

            for i in range(2):
                player_hand.add_cards(deck.dealer(1)) #this will add two cards to the player's hand from the deck 
                dealer_hand.add_cards(deck.dealer(1)) #this will add two cards to the dealer's hand from the deck

            print()
            print("*" * 30)
            print(f"Game {game_number} of {games_to_play}")
            print ("*" * 30)
            player_hand.display()
            dealer_hand.display()

            if self.check_winner(player_hand, dealer_hand):
                continue

            choice = ""
            while player_hand.get_value() < 21 and choice not in ["s" , "stand"]:
                choice = input("Please choose 'Hit' or 'Stand' : ").lower()
                print()
                while choice not in ["h" , "hit" , "s" , "stand"]:
                    choice = input("Please enter 'Hit' or 'Stand' (or H/S) : ").lower()
                    print()

                    if choice in ["hit" , "h"]:
                        player_hand.add_cards(deck.dealer(1)) 
                        player_hand.display()

            if self.check_winner(player_hand, dealer_hand):
                continue

            player_hand_value = player_hand.get_value()
            dealer_hand_value = dealer_hand.get_value()

            while dealer_hand_value < 17:
                dealer_hand.add_cards(deck.dealer(1))
                dealer_hand_value = int (dealer_hand_value.get_value())

            dealer_hand.display(show_all_dealer_cards = True)

            
            if self.check_winner(player_hand, dealer_hand):
                continue

            print("Final Result : ")
            print("Your hand: " , player_hand_value)
            print("Dealer hand: " , dealer_hand_value)
            
            self.check_winner(player_hand , dealer_hand, True )
            print("\n Thanks for playing! ")



    def check_winner(self, player_hand , dealer_hand, game_over = False):
        if not game_over:
            if player_hand.get_value() > 21:
                print("You Busted. Dealer wins! ")
                return True
            elif dealer_hand.get_value() > 21:
                print("Dealer Busted. You wins! ")
                return True
            elif dealer_hand.is_blackjack() and player_hand.is_blackjack() :
                print("Its a Tie !")
                return True
            elif player_hand.is_blackjack():
                print("You hace BlackJack. You win! ")
                return True
            elif dealer_hand.is_blackjack():
                print("Dealer hace BlackJack. Dealer win! ")
                return True
                
        else:
            if player_hand.get_value() > dealer_hand.get_value():
                print("You win!")
                
            elif player_hand.get_value() == dealer_hand.get_value():
                print("its a Tie!")
            else : 
                print("Dealer Wins!") 
            return True
        return False


g = Game()
g.play()