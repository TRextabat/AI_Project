import random
import time

def random_board():
    return [random.randint(0, 7) for _ in range(8)]

def calculate_attacks(board):
    attacks = 0
    for i in range(8):
        for j in range(i + 1, 8):
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                attacks += 1
    return attacks

def get_best_move(board):
    min_attacks = calculate_attacks(board)
    best_board = board[:]
    for col in range(8):
        original_row = board[col]
        for row in range(8):
            if row != original_row:
                board[col] = row
                attacks = calculate_attacks(board)
                if attacks < min_attacks:
                    min_attacks = attacks
                    best_board = board[:]
        board[col] = original_row
    return best_board, min_attacks

def hill_climbing():
    board = random_board()
    moves = 0
    restarts = 0
    start_time = time.time()

    while calculate_attacks(board) != 0:
        new_board, new_attacks = get_best_move(board)
        if new_board == board:  # No better neighbors, restart
            board = random_board()
            restarts += 1
        else:
            board = new_board
            moves += 1

    end_time = time.time()
    elapsed_time = (end_time - start_time) * 1000  # in milliseconds
    return board, moves, restarts, elapsed_time

# Running 20 times
results = []
def print_board(board):
    print("  +---+---+---+---+---+---+---+---+")
    for row in range(8):
        line = str(8 - row) + " |"  # Row number
        for col in range(8):
            if board[col] == row:
                line += " Q |"
            else:
                line += " _ |"
        print(line)
        print("  +---+---+---+---+---+---+---+---+")
    print("    a   b   c   d   e   f   g   h")  # Column labels
    print("\n")


for i in range(20):
    board, moves, restarts, elapsed_time = hill_climbing()
    results.append((moves, restarts, elapsed_time))
    print(f"Trial {i+1}: Moves={moves}, Restarts={restarts}, Time={elapsed_time:.2f} ms")
    print("Final Board:")
    print_board(board)

# Example: Save results to a table later
