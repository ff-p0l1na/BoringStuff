# Write a function named isValidChessBoard() that takes a dictionary argument 
# and returns True or False depending on if the board is valid.
# This function should detect when a bug has resulted in an improper chess board.

# maximum number of pieces for each player
max_chess_pieces = {
    'b': {'pawn': 8, 'knight': 2, 'bishop': 2, 'rook': 2, 'queen': 1, 'king': 1},
    'w': {'pawn': 8, 'knight': 2, 'bishop': 2, 'rook': 2, 'queen': 1, 'king': 1}
}

# chessboard fields
chessboard_fields = [
    '1a', '1b', '1c', '1d', '1e', '1f', '1g', '1h',
    '2a', '2b', '2c', '2d', '2e', '2f', '2g', '2h',
    '3a', '3b', '3c', '3d', '3e', '3f', '3g', '3h',
    '4a', '4b', '4c', '4d', '4e', '4f', '4g', '4h',
    '5a', '5b', '5c', '5d', '5e', '5f', '5g', '5h',
    '6a', '6b', '6c', '6d', '6e', '6f', '6g', '6h',
    '7a', '7b', '7c', '7d', '7e', '7f', '7g', '7h',
    '8a', '8b', '8c', '8d', '8e', '8f', '8g', '8h'
]

# Example board:
players_board = {
    '1a': 'bking',
    '2b': 'wqueen',
}

def isValidChessBoard(players_board):
    #  Dictionary to keep track of counts for each player:
    piece_counts = {
        'b': {'pawn': 0, 'knight': 0, 'bishop': 0, 'rook': 0, 'queen': 0, 'king': 0},
        'w': {'pawn': 0, 'knight': 0, 'bishop': 0, 'rook': 0, 'queen': 0, 'king': 0}
        }
    # 1) Validate the players board by checking if the input is alphanumeric

    # 2) Check if the current number of pieces doesn't exceed the max number of each player by
    # comparing players_board to the max_chess_pieces dictionary:

    # 3) Return True if the board is valid, and False if it is invalid


