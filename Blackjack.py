import random as rnd

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
numbers = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10,
         'Q':10, 'K':10, 'A':11}

playing = True

# Creating Cards #

class Card:
    
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number
    
    def __str__(self):
        return self.number + ' of ' + self.suit

# Creating the Deck that shuffles automatically and does single dealing #

class Deck:
    
    def __init__(self):
        self.deck = [] 
        for suit in suits:
            for number in numbers:
                self.deck.append(Card(suit, number))
    
    def __str__(self):
        deck_comp = '' 
        for card in self.deck:
            deck_comp += '\n' + card.__str__() 
        return 'The deck has' + deck_comp
            
    def shuffle(self):
        rnd.shuffle(self.deck)
        
    def deal(self):
        single_card = self.deck.pop()
        return single_card

# Creating a hand #

class Hand:
    def __init__(self):
        self.cards = []  
        self.value = 0   
        self.aces = 0    
    
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.number]
        if card.number == 'Ace':
            self.aces += 1
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
            
# Creating a betting system as well as money balance system for the player #           

class Money:
    
    def __init__(self):
        self.total = 1000  # User default value is set to a thousand dollars player can only bet wthin this amount initially
        self.bet = 0
        
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet
        

# Defining the bet taking aspect of the game #

def recieve_bet(Money):
    while True:
        try:
            Money.bet = int(input('How much money would you like to bet? $ '))
        except ValueError:
            print("Sorry, a bet must be an integer!")
        else:
            if Money.bet > Money.total:
                print('Sorry, your bet cannot exceed {} '.format(Money.total))
            else:
                break      

# Defining a hit #

def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()

# Defining decision to hit or stand #

def hit_or_stand(deck,hand):
    global playing
    
    while True:
        x = input("Would you like to Hit or Stand? Enter 'h' or 's'")
        
        if x[0].lower() == 'h':
            hit(deck,hand)  

        elif x[0].lower() == 's':
            print("Dealer is playing.")
            playing = False

        else:
            print("Sorry, please choose again.")
            continue
        break

# Defining the functions that will display the cards #

def show_some(player,dealer):
    print("\nDealer's Hand")
    print("")
    print(' ', dealer.cards[1])
    print("\nPlayer's Hand: ", *player.cards, sep= '\n')
        
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep="\n")
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand: ", *player.cards, sep= '\n')
    print("Player's Hand = ", player.value)

# Defining the functions that react to game scenarios #

def player_busts(player,dealer,money):
    print("It's a bust!")
    money.lose_bet()

def player_wins(player,dealer,money):
    print("You win!")
    money.win_bet()

def dealer_busts(player,dealer,money):
    print("Dealer busts!")
    money.win_bet()
    
def dealer_wins(player,dealer,money):
    print("Dealer wins!")
    money.lose_bet()
    
def push(player,dealer):
    print("You and the dealer have tied! It's a push.")    

# Creating the game #
while True:
    # Opening statement
    print("Welcome to the Blackjack game at the Foundations Casino!")
    
    # Creating & shuffling the deck as well as dealing two cards to each player
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    
    # Setting up the player's money
    player_money = Money()
        
    # Prompting the Player for their bet
    recieve_bet(player_money)
    
    # Shows player the cards but keeps one dealer card hidden 
    show_some(player_hand, dealer_hand)
    
    while playing: 
        
        # Prompting player to hit or stand
        hit_or_stand(deck, player_hand)
        
        show_some(player_hand,dealer_hand) 
        
        # If the player's hand exceeds 21, the player has lost and the loop breaks
        if player_hand.value >21:
            player_busts(player_hand, dealer_hand, player_money)

            break

    # If Player hasn't lost, play Dealer's hand until Dealer reaches 17
    if player_hand.value <= 21:
        
        while dealer_hand.value <17:
            hit(deck, dealer_hand)
    
        # Shows all the cards
        show_all(player_hand,dealer_hand)
        
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_money)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_money)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_money)

        else:
            push(player_hand,dealer_hand)
        
    
    # Inform Player of their money balance
    print("\nMoney Balance:", player_money.total)
    
    # Ask to play again
    new_game = input("Would you like to continue playing? Enter 'y' or 'n'")
    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print('Thank you for playing at the Foundations Casino! ')

        break