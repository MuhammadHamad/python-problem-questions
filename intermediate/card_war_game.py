import random

def create_deck():
    """Create a standard deck of 52 cards without jokers."""
    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
    
    # Create deck as list of tuples (rank, suit)
    deck = [(rank, suit) for suit in suits for rank in ranks]
    return deck

def get_card_value(card):
    """Return the numerical value of a card based on its rank."""
    rank_values = {
        '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
        'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14
    }
    return rank_values[card[0]]

def deal_cards(deck):
    """Shuffle deck and deal cards to two players."""
    random.shuffle(deck)
    midpoint = len(deck) // 2
    return deck[:midpoint], deck[midpoint:]

def display_player_cards(player_deck, player_num):
    """Display available cards for a player."""
    print(f"\nPlayer {player_num}'s cards:")
    for i, card in enumerate(player_deck, 1):
        print(f"{i}. {card[0]} of {card[1]}")

def get_player_choice(player_deck, player_num):
    """Get player's choice of card to play."""
    while True:
        try:
            display_player_cards(player_deck, player_num)
            choice = int(input(f"Player {player_num}, choose a card number to play (1-{len(player_deck)}): "))
            if 1 <= choice <= len(player_deck):
                return player_deck.pop(choice - 1)
            print("Invalid choice. Please select a valid card number.")
        except ValueError:
            print("Please enter a valid number.")

def play_round(player1_deck, player2_deck, player1_score, player2_score, round_num):
    """Play a single round of the game with user interaction."""
    print(f"\n=== ROUND {round_num} ===")
    
    # Players choose their cards
    print("\nPlayer 1's turn:")
    card1 = get_player_choice(player1_deck, 1)
    
    print("\nPlayer 2's turn:")
    card2 = get_player_choice(player2_deck, 2)
    
    # Get card values
    value1 = get_card_value(card1)
    value2 = get_card_value(card2)
    
    # Display played cards
    print(f"\nPlayer 1 played: {card1[0]} of {card1[1]}")
    print(f"Player 2 played: {card2[0]} of {card2[1]}")
    
    # Determine round winner and update scores
    round_points = value1 + value2
    if value1 > value2:
        player1_score += round_points
        print(f"\nPlayer 1 wins the round and scores {round_points} points ({value1} + {value2})!")
    elif value2 > value1:
        player2_score += round_points
        print(f"\nPlayer 2 wins the round and scores {round_points} points ({value1} + {value2})!")
    else:
        print("\nIt's a tie! No points awarded.")
    
    print(f"\nCurrent scores - Player 1: {player1_score}, Player 2: {player2_score}")
    input("\nPress Enter to continue...")
    return player1_score, player2_score

def play_game():
    """Main game function to manage the complete interactive card war game."""
    # Initialize game
    deck = create_deck()
    player1_deck, player2_deck = deal_cards(deck)
    player1_score = 0
    player2_score = 0
    
    print("=== Welcome to Card War Game ===")
    print("Each player will take turns choosing a card to play.")
    print("The player with the higher card wins the round and collects points.")
    print("The game will last 7 rounds.")
    input("\nPress Enter to start the game...")
    
    # Play 7 rounds
    for round_num in range(1, 8):
        player1_score, player2_score = play_round(
            player1_deck, player2_deck, 
            player1_score, player2_score, 
            round_num
        )
    
    # Determine and announce winner
    print("\n=== Game Over ===")
    print(f"Final Scores - Player 1: {player1_score}, Player 2: {player2_score}")
    
    if player1_score > player2_score:
        print("Player 1 wins the game!")
    elif player2_score > player1_score:
        print("Player 2 wins the game!")
    else:
        print("The game is a tie!")

# Start the game
if __name__ == "__main__":
    play_game()