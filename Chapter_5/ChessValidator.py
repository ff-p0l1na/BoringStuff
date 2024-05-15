# Example board:
players_board = {
    '1a': 'bking',
    '2b': 'wqueen',
}

def isValidChessBoard(board):

    # make a dictionary to keep count of the players' pieces:
    piece_count = {}
    for piece in board.values():
        if piece in piece_count:
            piece_count[piece] += 1
        else:
            piece_count[piece] = 1
    
    # example piece_count after that: {'bking': 1, 'wqueen': 1}
 
    # check if the two kings are on the board:
    if not ('bking' in piece_count and 'wking' in piece_count):
        return False

    # check if there's no more than 16 pieces starting with w and 16 starting with b:
    for piece in piece_count:
        if piece[0] == 'w' and piece_count[piece] > 16:
            return False
        if piece[0] == 'b' and piece_count[piece] > 16:
            return False
        
    # check for pawns if there are maximum 8 for each color:
    for piece in piece_count:
        if piece[1:] == 'pawn' and piece_count[piece] > 8:
            return False
        
   # check if the integer version of first character of each field is between 1 and 8:
    for field in board:
        if int(field[0]) < 1 or int(field[0]) > 8:
            return False
        
    # check if the 2nd character of the key is in the range 'abcdefgh':
    for field in board:
        if field[1] not in 'abcdefgh':
            return False
        
    return True

test = isValidChessBoard(players_board)
print(test)



