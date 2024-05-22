import random

# Class for creating a chessboard with a random set of pieces:
class RandomChessBoard:
    def __init__(self):
        self.integers = '12345678'
        self.letters = 'abcdefgh'
        self.fields = [f'{integer}{letter}' for integer in self.integers for letter in self.letters]
        self.pieces = ['bking', 'wking', 'bqueen', 'wqueen', 'brook', 'wrook', 'bbishop', 'wbishop', 'bknight', 'wknight', 'bpawn', 'wpawn']

# Method that uses RandomChessBoard to generate a random chessboard dictionary:
    def generate_board(self, num_pieces):

        # Initialize an empty dictionary:
        board = {}

        selected_fields = random.sample(self.fields, num_pieces)
        for field in selected_fields:
            piece = random.choice(self.pieces)
            board[field] = piece
            
        return board

# Function that checks if the board is valid:
def isValidChessBoard(board):

    try:

        # make a dictionary to keep count of the players' pieces:
        piece_count = {}
        for piece in board.values():
            if piece in piece_count:
                piece_count[piece] += 1
            else:
                piece_count[piece] = 1

        # make a validator variable:
        validator = True

        # Check the total number of pieces does not exceed 32:
        if len(board) > 32:
            print("There are more than 32 pieces on the board")
            validator = False
            
        # check if the two kings are on the board:
        if not ('bking' in piece_count and 'wking' in piece_count):
            print("There must be two kings on the board")
            validator = False

        # check if there's no more than 16 pieces starting with w and 16 starting with b:
        for piece in piece_count:
            if piece[0] == 'w' and piece_count[piece] > 16:
                print("Too many white pieces")
                validator = False
            if piece[0] == 'b' and piece_count[piece] > 16:
                print("Too many black pieces")
                validator = False
            
        # check for pawns if there are maximum 8 for each color:
        for piece in piece_count:
            if piece[1:] == 'pawn' and piece_count[piece] > 8:
                print("Too many pawns")
                validator = False
            
        # check if the integer version of first character of each field is between 1 and 8:
        for field in board:
            if int(field[0]) < 1 or int(field[0]) > 8:
                print("Field numbers must be between 1 and 8")
                validator = False
            
        # check if the 2nd character of the key is in the range 'abcdefgh':
        for field in board:
            if field[1] not in 'abcdefgh':
                print("Field letters must be between a and h")
                validator = False

    except ValueError:
        print("Invalid input")
        return False
    
    return validator


chess_board_generator = RandomChessBoard()
players_board = chess_board_generator.generate_board(num_pieces=40)
print(players_board)
print(isValidChessBoard(players_board))



