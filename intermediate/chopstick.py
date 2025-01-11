import sys

def display_instructions():
    """Display game instructions with improved formatting."""
    print("""
╔════════════════════════════════════════╗
║           Welcome to Chopsticks!       ║
╚════════════════════════════════════════╝

Rules:
1. Each player starts with one finger on each hand.
2. On your turn, you can:
   a. Attack: Add your fingers to opponent's hand
   b. Split: Redistribute your own fingers

Commands:
- Attack: attack <your_hand> <opponent_hand>
  Example: attack left right
- Split: split <hand1_fingers> <hand2_fingers>
  Example: split 2 0

Note: A hand with 5 or more fingers becomes dead (0)
""")

def create_player(name):
    """Create a new player dictionary."""
    return {
        "name": name,
        "left": 1,
        "right": 1
    }

def display_state(player1, player2):
    """Display current game state with ASCII art."""
    print("\n" + "="*40)
    for player in [player1, player2]:
        print(f"{player['name']}'s hands:")
        print(f"Left: {'|' * player['left'] or '✗'} ({player['left']})")
        print(f"Right: {'|' * player['right'] or '✗'} ({player['right']})")
    print("="*40 + "\n")

def is_game_over(player):
    """Check if a player has lost (both hands dead)."""
    return player['left'] == 0 and player['right'] == 0

def validate_attack(player, opponent, your_hand, opponent_hand):
    """Validate attack move with detailed error messages."""
    if your_hand not in ('left', 'right') or opponent_hand not in ('left', 'right'):
        return False, "Invalid hand selection. Use 'left' or 'right'."
    if player[your_hand] == 0:
        return False, f"Your {your_hand} hand is dead!"
    if opponent[opponent_hand] == 0:
        return False, f"Opponent's {opponent_hand} hand is already dead!"
    return True, ""

def validate_split(player, hand1_fingers, hand2_fingers):
    """Validate split move with detailed error messages."""
    total_fingers = player['left'] + player['right']
    if hand1_fingers < 0 or hand2_fingers < 0:
        return False, "Cannot have negative fingers!"
    if hand1_fingers + hand2_fingers != total_fingers:
        return False, f"Total fingers must equal {total_fingers}!"
    if hand1_fingers >= 5 or hand2_fingers >= 5:
        return False, "Cannot split to 5 or more fingers!"
    return True, ""

def execute_attack(player, opponent, your_hand, opponent_hand):
    """Execute attack move and handle overflow."""
    opponent[opponent_hand] += player[your_hand]
    if opponent[opponent_hand] >= 5:
        opponent[opponent_hand] = 0
        print(f"{opponent['name']}'s {opponent_hand} hand is now dead!")

def execute_split(player, hand1_fingers, hand2_fingers):
    """Execute split move."""
    player['left'] = hand1_fingers
    player['right'] = hand2_fingers

def get_player_input(player):
    """Get and validate player input with improved error handling."""
    try:
        move = input(f"\n{player['name']}'s turn > ").strip().lower()
        if move == "help":
            display_instructions()
            return None
        
        move_parts = move.split()
        if not move_parts:
            print("Please enter a move.")
            return None

        if move_parts[0] not in ("attack", "split"):
            print("Invalid move type. Use 'attack' or 'split'.")
            return None

        if len(move_parts) != 3:
            print(f"Invalid format. Use: {move_parts[0]} <hand1> <hand2>")
            return None

        return move_parts
    except EOFError:
        print("\nGame terminated by user.")
        sys.exit(0)

def initialize_game():
    """Initialize the game by getting player names."""
    display_instructions()
    
    # Get player names with validation
    player1_name = ""
    while not player1_name:
        player1_name = input("Enter Player 1's name: ").strip()
    
    player2_name = ""
    while not player2_name:
        player2_name = input("Enter Player 2's name: ").strip()
    
    return create_player(player1_name), create_player(player2_name)

def play_game():
    """Main game loop."""
    player1, player2 = initialize_game()
    players = [player1, player2]
    turn = 0

    while True:
        current_player = players[turn % 2]
        opponent = players[(turn + 1) % 2]

        display_state(player1, player2)
        move = get_player_input(current_player)

        if not move:
            continue

        if move[0] == "attack":
            _, your_hand, opponent_hand = move
            valid, error_msg = validate_attack(current_player, opponent, your_hand, opponent_hand)
            if valid:
                execute_attack(current_player, opponent, your_hand, opponent_hand)
                if is_game_over(opponent):
                    display_state(player1, player2)
                    print(f"\n🎉 {current_player['name']} wins! 🎉")
                    break
                turn += 1
            else:
                print(error_msg)

        elif move[0] == "split":
            try:
                _, hand1_fingers, hand2_fingers = move
                hand1_fingers = int(hand1_fingers)
                hand2_fingers = int(hand2_fingers)
                valid, error_msg = validate_split(current_player, hand1_fingers, hand2_fingers)
                if valid:
                    execute_split(current_player, hand1_fingers, hand2_fingers)
                    turn += 1
                else:
                    print(error_msg)
            except ValueError:
                print("Invalid input. Fingers must be numbers.")

if __name__ == "__main__":
    try:
        play_game()
    except KeyboardInterrupt:
        print("\nGame terminated by user.")
        sys.exit(0)