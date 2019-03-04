''' 
Adam Pumphrey, CMPUT 497, ID: 1469319 

Random Pente Player
'''
import sys

def build_board(boardsize):
    board = [0] * ((boardsize + 1) ** 2)
    top_border = [3] * (boardsize + 1)
    board[0:(boardsize + 1)] = top_border
    count = 1
    while count <= boardsize:
        board[((boardsize + 1) * count):(((boardsize + 1) * count) + 1)] = [3]
        count += 1
    #board.append(0)
    board.extend(top_border)
    return board

def show_board(board, boardsize):
    column_list = []
    for x in range(0, (boardsize)):
        column_list.append(chr(97 + x))
    column_str = '  '
    for i in column_list:
        column_str += i
        column_str += '  '
    print("\nCurrent Board:")
    print(column_str)
    count = 1
    while count < (boardsize + 1):
        row_list = []
        for i in board[(((boardsize + 1) * count) + 1):((boardsize + 1) * (count + 1))]:
            row_list.append(str(i))
        row_str = ''
        row_str += str(count)
        for i in row_list:
            row_str += ' '
            row_str += i
            row_str += ' '        
        #print(board[(((boardsize + 1) * count) + 1):((boardsize + 1) * (count + 1))])
        count += 1
        print(row_str)
        
def quit():
    print("Program shutting down...")
    sys.exit()
        
def point_to_boardloc(point, boardsize):
    # eg) 9 --> c1
    if point > ((boardsize * 2) + 1):
        temp_point = point - (boardsize + 1)
        while temp_point > ((boardsize * 2) + 1):
            temp_point -= (boardsize + 1)
        boardloc_0 = chr((temp_point - (boardsize + 2)) + 97)
    else:
        boardloc_0 = chr((point - (boardsize + 2)) + 97)
    boardloc_1 = point//(boardsize + 1)
    boardloc = boardloc_0 + str(boardloc_1)
    return boardloc

def boardloc_to_coord(boardloc, boardsize):
    col = boardloc[0:1]
    if not col.isalpha():
        print("Error: board location syntax incorrect")
        return "error"
    row = boardloc[1:]
    if not row.isdigit():
        print("Error: board location syntax incorrect")
        return "error"
    row = int(row)
    if row > boardsize:
        print("Error: board location out of bounds")
        return "error"
    cols = "abcdefghijklmnopqrs"
    if col not in cols:
        print("Error: board location out of bounds")
        return "error"
    coord_col = (cols.index(col)) + 1
    coord = (coord_col, row)
    return coord

def check_inp_command(command, commandlist):
    if not command[0].isalpha():
        return 1
    else:
        command[0] = command[0].lower()
    if command[0] not in commandlist:
        return 1
    else:
        return 0

def boardsize_change(new_size):
    if not new_size.isdigit():
        print("\nError: Boardsize must be an integer between 5 and 19")
        return 1
    else:
        new_boardsize = int(new_size)
        if new_boardsize < 5 or new_boardsize > 19:
            print("\nError: Boardsize must be an integer between 5 and 19")
            return 1
        else:
            return new_boardsize
        
def get_empty_spaces(board, boardsize):
    empty_space_list = []
    count = (boardsize + 2)
    for i in board[(boardsize + 2):((boardsize + 1) ** 2)]:
        if i == 0:
            space = point_to_boardloc(count, boardsize)
            empty_space_list.append(space)
        count += 1
    return empty_space_list
    
def main():
    
    commandlist = ["boardsize", "reset", "quit", "genmove", "play", "commands", "emptyspaces", "playertomove", "winner"]

    boardsize = 5
    board = [0] * ((boardsize + 1) ** 2)
    
    # build board
    board = build_board(boardsize)
    
    # show board
    show_board(board, boardsize)
    
    user_inp = input("\nPlease enter a command: ")
    while user_inp:
        command = user_inp.split(" ")
        check_result = check_inp_command(command, commandlist)
        if check_result == 1:
            error = True
            print("Error: Command does not exist. Use 'commands' to list existing commands")
        elif check_result == 2:
            pass
        elif check_result == 0:
            # execute command
            if command[0] == "boardsize":
                if len(command) != 2:
                    print("\nError: Command requires additional input. Consult README for more info")
                else:
                    new_boardsize = boardsize_change(command[1])
                    if new_boardsize == 1:
                        pass
                    else:
                        boardsize = new_boardsize
                        board = build_board(boardsize)
                        show_board(board, boardsize)
            elif command[0] == "reset":
                board = build_board(boardsize)
                show_board(board, boardsize)
            elif command[0] == "quit":
                quit()
            elif command[0] == "genmove":
                pass
            elif command[0] == "play":
                pass
            elif command[0] == "commands":
                print("\nCommands:")
                for i in commandlist:
                    print(" ", i)
            elif command[0] == "emptyspaces":
                empty_spaces = get_empty_spaces(board, boardsize)
                count = 1
                for i in empty_spaces:
                    print(i, end =' ')
                    if count == 10:
                        print("")
                        count = 1
                    else:
                        count += 1
            elif command[0] == "player-to-move":
                pass
            elif command[0] == "winner":
                pass
        user_inp = input("\nPlease enter a command: ")
        
    # point to boardloc
    # eg) 9 = c1
    boardloc = point_to_boardloc(28, boardsize)
    
    # boardloc to coord
    # eg) c1 = (3,1)
    coord = boardloc_to_coord(boardloc, boardsize)
    
    # coord to point
    # eg) (3,1) = 9
    coord_0 = 3
    coord_1 = 1
    newpoint = (((boardsize + 1) * coord_1) + coord_0)
    
    # point to coord
    # eg) 9 = (3, 1)
    test1 = 9
    
main()