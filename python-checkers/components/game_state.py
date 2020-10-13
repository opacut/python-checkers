class GameState:
    def __init__(self):
        #self.pieces = dict()
        #self.pieces["A"] = GamePiece(current_location="A1")
        self.game_board = GameBoard()
        self.game_board.spaces["A1"].piece = GamePiece(current_location="A1", name="A", player="R")
        self.game_board.spaces["C1"].piece = GamePiece(current_location="C1", name="B", player="R")

    def move_piece(self, piece, new_location):
        piece.move(new_location)

    def quit_game(self):
        self.loop = False

class GameBoard:
    def __init__(self):
        self.spaces = dict()
        for i in range(1,9):
            for j in range(1,9):
                alphanumeric_code= self.number_to_letter(n=i)
                self.spaces[alphanumeric_code+str(j)] = GameBoardSpace(x=i,y=j,piece=None)

    def number_to_letter(self, n):
        if n == 1:
            return "A"
        elif n==2:
            return "B"
        elif n==3:
            return "C"
        elif n==4:
            return "D"
        elif n==5:
            return "E"
        elif n==6:
            return "F"
        elif n==7:
            return "G"
        elif n==8:
            return "H"

class GameBoardSpace:
    def __init__(self,x,y, piece=None):
        self.x = x
        self.y = y
        self.piece = piece

class GamePiece:
    def __init__(self, name, current_location, player):
        self.current_location = current_location
        self.name = name
        self.player = player
    
    @property
    def move(self, new_location):
        self.current_location = new_location

    @property
    def possible_moves(self):
        pass