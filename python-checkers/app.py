from components.game_state import GameState

def run():
    game_state = GameState()
    print("Welcome to python/ checkers!")
    while game_state.loop:
        game_state.print_board()
        piece = input("Pick a piece: ")
        if piece == "exit" or piece == "quit":
            break
        print("Possible moves: "+str(game_state.pieces[piece].possible_moves))
        new_location = input("Pick a location to move the piece to: ")
        if new_location == "exit" or new_location == "quit":
            break
        game_state.move_piece(piece=piece, new_location=new_location)