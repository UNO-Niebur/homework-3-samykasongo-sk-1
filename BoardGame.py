# Homework 3 - Board Game System
# Name:
# Date:

def loadGameData(filename):
    """Reads game data from a file and returns it as a list."""
    data = []
    with open(filename, "r") as file:
        for line in file:
            data.append(line.strip())
    return data


def displayGame(data):
    """Displays the current game state."""
    print("\nCurrent Game State:")
    
    turn = ""
    board = {}

    
    # Parse the data
    for item in data:
        if item.startswith("Turn"):
            turn = item
        else:
            pos, value = item.split(": ")
            board[int(pos)] = value

    print(turn)
    print("\nBoard:")

    # Display positions in order
    for pos in sorted(board.keys()):
        print(f"{pos}: {board[pos]}")

def movePlayer(data):
    """Example function to simulate moving a player."""
    print("\nMove player function not fully implemented.")
    # Students will modify this
    
    turn_index = 0
    current_player = ""
    board = {}

    for i in range(len(data)):
        if data[i].startswith("Turn"):
            turn_index = i
            current_player = data[i].split(": ")[1]
        else:
            pos, value = data[i].split(": ")
            board[int(pos)] = value

    print("Current turn:", current_player)

    # Find player position
    player_pos = None
    for pos, value in board.items():
        if value == current_player:
            player_pos = pos
            break

    if player_pos is None:
        print("Player not found!")
        return

    # Ask how far to move
    move = int(input("Enter spaces to move: "))

    new_pos = player_pos + move

    # Remove player from old position
    del board[player_pos]

    # Check for event
    if new_pos in board:
        print("Event triggered:", board[new_pos])

    # Place player in new position
    board[new_pos] = current_player

    # Update data list
    new_data = []
    new_data.append(f"Turn: {current_player}")

    for pos in sorted(board.keys()):
        new_data.append(f"{pos}: {board[pos]}")

    # Replace original data
    data.clear()
    data.extend(new_data)

    print(f"{current_player} moved to {new_pos}")


def main():
    filename = "events.txt"   # Students can rename if needed

    gameData = loadGameData(filename)
    displayGame(gameData)

    # Example interaction
    choice = input("\nMove player? (y/n): ")
    if choice.lower() == "y":
        movePlayer(gameData)
        displayGame(gameData)


if __name__ == "__main__":
    main()
