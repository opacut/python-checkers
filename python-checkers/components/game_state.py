import pdb

def number_to_letter(n):
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
    else:
        return "X"

def letter_to_number(a):
    if a=="A":
        return 1
    elif a=="B":
        return 2
    elif a=="C":
        return 3
    elif a=="D":
        return 4
    elif a=="E":
        return 5
    elif a=="F":
        return 6
    elif a=="G":
        return 7
    elif a=="H":
        return 8
    else:
        return 0

class GameState:
    def __init__(self):
        self.loop = True
        #self.pieces = dict()
        #self.pieces["A"] = GamePiece(current_location="A1")
        self.game_board = GameBoard()
        self.pieces = dict()
        self.pieces["R1"] = GamePiece(current_location="A1", name="R1", player="R")
        self.pieces["R2"] = GamePiece(current_location="C1", name="R2", player="R")
        self.game_board.spaces["A1"].piece = self.pieces["R1"]
        self.game_board.spaces["C1"].piece = self.pieces["R2"] 

    def print_board(self):
        return self.game_board.print()

    def move_piece(self, piece, new_location):
        self.game_board.spaces[self.pieces[piece].current_location].piece = None
        self.pieces[piece].move(new_location)
        self.game_board.spaces[new_location].piece = self.pieces[piece]

    def quit_game(self):
        self.loop = False

class GameBoard:
    def __init__(self):
        self.spaces = dict()
        for i in range(1,9):
            for j in range(1,9):
                alphanumeric_code= number_to_letter(n=i)
                self.spaces[alphanumeric_code+str(j)] = GameBoardSpace(x=i,y=j,piece=None)
    
    def print(self):
        #left border
        print("---------------------------")
        for i in range(0,8):
            line = "|"
            #print("|")
            for space in self.spaces.values():
                #pdb.set_trace()
                if space.y == 8-i:
                    #print(space.draw())
                    line += " "
                    line += space.draw()
            line += " "
            line += "|"
            print(line)
        print("---------------------------")


class GameBoardSpace:
    def __init__(self,x,y, piece=None):
        self.x = x
        self.y = y
        self.piece = piece

    def draw(self):
        if not self.piece:
            return "--"
        else:
            return self.piece.name

class GamePiece:
    def __init__(self, name, current_location, player):
        self.current_location = current_location
        self.name = name
        self.player = player
    
    def move(self, new_location):
        self.current_location = new_location

    @property
    def possible_moves(self):
        #moves = list()
        if self.player == "R":
            loc_A_x = number_to_letter(letter_to_number(self.current_location[0])-1)
            loc_A_y = str(int(self.current_location[1])+1)
            loc_B_x = number_to_letter(letter_to_number(self.current_location[0])+1)
            loc_B_y = str(int(self.current_location[1])+1)
            locs = list()
            if loc_A_x != "X" and loc_A_y != 0:
                locs.append(str(loc_A_x)+str(loc_A_y))
            if loc_B_x != "X" and loc_B_y != 0:
                locs.append(str(loc_B_x)+str(loc_B_y))
            return locs
        else:
            loc_A_x = number_to_letter(letter_to_number(self.current_location[0])-1)
            loc_A_y = str(int(self.current_location[1])-1)
            loc_B_x = number_to_letter(letter_to_number(self.current_location[0])+1)
            loc_B_y = str(int(self.current_location[1])-1)
            locs = list()
            if loc_A_x != "X" and loc_A_y != 0:
                locs.append(str(loc_A_x)+str(loc_A_y))
            if loc_B_x != "X" and loc_B_y != 0:
                locs.append(str(loc_B_x)+str(loc_B_y))
            return locs
