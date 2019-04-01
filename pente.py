''' 
Adam Pumphrey, CMPUT 497, ID: 1469319 

Random Pente Player
'''
import sys, random

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
    board.append(3)
    move_history = []
    return board, move_history

def show_board(board, boardsize):
    column_list = []
    for x in range(0, (boardsize)):
        column_list.append(chr(97 + x))
    column_str = '   '
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
        tempcount = 1
        for i in row_list:
            if tempcount == 1 and count < 10:
                row_str += '  '
            else:
                row_str += ' '
            row_str += i
            row_str += ' '
            tempcount += 1
        #print(board[(((boardsize + 1) * count) + 1):((boardsize + 1) * (count + 1))])
        count += 1
        print(row_str)
        
def quit():
    print("\nShutting down...")
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

def boardloc_to_point(boardloc, boardsize):
    col = boardloc[0:1]
    if not col.isalpha():
        print("\nError: board location syntax incorrect")
        return "error"
    col = col.lower()
    row = boardloc[1:]
    if not row.isdigit():
        print("\nError: board location syntax incorrect")
        return "error"
    row = int(row)
    if row > boardsize:
        print("\nError: board location out of bounds")
        return "error"
    cols = "abcdefghijklmnopqrs"
    if col not in cols:
        print("\nError: board location out of bounds")
        return "error"
    if cols.index(col) > (boardsize - 1):
        print("\nError: board location out of bounds")
        return "error"
    coord_col = (cols.index(col)) + 1
    point = (((boardsize + 1) * row) + coord_col)
    return point
    #coord = (coord_col, row)
    #return coord

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
        print("\nError: Boardsize must be an odd integer between 7 and 19")
        return 1
    else:
        new_boardsize = int(new_size)
        if new_boardsize < 7 or new_boardsize > 19:
            print("\nError: Boardsize must be an odd integer between 7 and 19")
            return 1
        elif new_boardsize % 2 == 0:
            print("\nError: Boardsize must be an odd integer between 7 and 19")
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

def play_move(move, board, boardsize, player, opponent):
    point = boardloc_to_point(move, boardsize)
    if point == "error":
        return False, None, None, None
    # no need to deep check if move legal
    # every empty space is a legal move
    # only need to check for capture
    if board[point] != 0:
        print("\nError: Illegal move - position already occupied")
        return False, None, None, None
    board[point] = player
    # check for capture
    # capture can only be in form of O-X-X-O as per rules
    capture_status, capture_list, capture_count = capture_check(board, boardsize, player, opponent, point)
    if capture_status:
        for i in capture_list:
            board[i] = 0
    # check for win
    # need to implement calling 4 in a row (tessera) and 3 in a row (tria)
    win_status = check_win(board, boardsize, player, point)
        
    return True, capture_status, capture_count, win_status

def check_win(board, boardsize, player, point):
    win = False
    blocks = []
    # vertical check
    win, block1 = check_win_directions(board, point, win, (boardsize + 1), player)
    blocks.append(block1)
    if not win:
        # horizontal check
        win, block2 = check_win_directions(board, point, win, 1, player)
        blocks.append(block2)
        if not win:
            # diagonal up/left, down/right check
            win, block3 = check_win_directions(board, point, win, (boardsize + 2), player)
            blocks.append(block3)
            if not win:
                # diagonal up/right, down/left check
                win, block4 = check_win_directions(board, point, win, (boardsize), player)
                blocks.append(block4)
    if player == 1:
        p1 = "black"
    elif player == 2:
        p1 = "bhite"
    for i in blocks:
        if i == 3:
            print("\nTria!", p1, "has made 3 in a row!")
        elif i == 4:
            print("\nTessera!", p1, "has made 4 in a row!")
    return win

def check_win_directions(board, point, found, increment, player):
    count = 1
    posi_check = True
    negi_check = True
    index1 = point
    index2 = point
    while not found:
        if posi_check:
            index1 += increment
            if board[index1] == player:
                count += 1
            else:
                posi_check = False
        if negi_check:
            index2 -= increment
            if board[index2] == player:
                count += 1
            else:
                negi_check = False
        if count >= 5:
            found = True
            return found, count
        if not posi_check and not negi_check:
            return found, count
        
def capture_check_direction(board, index, pos_list, status, increment, player, opponent, mode):
    if board[index] == opponent:
        pos1 = index
        if mode == 1:
            # positive increment
            index += increment
            if board[index] == opponent:
                pos2 = index
                index += increment
                if board[index] == player:
                    status = True
                    pos_list.extend([pos1, pos2])
        else:
            index -= increment
            if board[index] == opponent:
                pos2 = index
                index -= increment
                if board[index] == player:
                    status = True
                    pos_list.extend([pos1, pos2])
    return status, pos_list

def capture_check(board, boardsize, player, opponent, point):
    capture = False
    capture_list = []
    count = 0
    # vertical - check
    index = point - (boardsize + 1)
    capture, capture_list = capture_check_direction(board, index, capture_list, capture, (boardsize + 1), player, opponent, 2)
    if capture:
        count += 1
    # vertical + check
    capture = False
    index = point + (boardsize + 1)
    capture, capture_list = capture_check_direction(board, index, capture_list, capture, (boardsize + 1), player, opponent, 1)
    if capture:
        count += 1
    capture = False    
    # horizontal - check
    index = point - 1
    capture, capture_list = capture_check_direction(board, index, capture_list, capture, 1, player, opponent, 2)
    if capture:
        count += 1
    capture = False    
    # horizontal + check
    index = point + 1
    capture, capture_list = capture_check_direction(board, index, capture_list, capture, 1, player, opponent, 1)
    if capture:
        count += 1
    capture = False    
    # diagonal up/left check
    index = point + (boardsize + 2)
    capture, capture_list = capture_check_direction(board, index, capture_list, capture, (boardsize + 2), player, opponent, 1)
    if capture:
        count += 1
    capture = False    
    # diagonal down/right check
    index = point - (boardsize + 2)
    capture, capture_list = capture_check_direction(board, index, capture_list, capture, (boardsize + 2), player, opponent, 2)
    if capture:
        count += 1
    capture = False    
    # diagonal up/right check
    index = point + boardsize
    capture, capture_list = capture_check_direction(board, index, capture_list, capture, boardsize, player, opponent, 1)
    if capture:
        count += 1
    capture = False    
    # diagonal down/left check
    index = point - boardsize
    capture, capture_list = capture_check_direction(board, index, capture_list, capture, boardsize, player, opponent, 2)
    if capture:
        count += 1
    if count > 0:
        capture = True
    return capture, capture_list, count

def check_draw(board, boardsize, status):
    empty_spaces = get_empty_spaces(board, boardsize)
    if len(empty_spaces) == 0:
        status = True
    return status

def check_game_status(black_status, white_status, draw_status):
    if black_status or white_status or draw_status:
        return True
    else:
        return False
    
def generate_random_move(board, boardsize, player, opponent, move_history, ruleset):
    if ruleset == 1 and player == 1 and len(move_history) == 0:
        pos = (len(board) - 1) // 2
        move = point_to_boardloc(pos, boardsize)
    elif ruleset == 1 and player == 1 and len(move_history) == 2:
        available_moves = get_empty_spaces(board, boardsize)
        center = (len(board) - 1) // 2
        center = point_to_boardloc(center, boardsize)
        center_ord = ord(center[0])
        legal_moves = []
        for move in available_moves:
            move_ord = ord(move[0])
            ord_diff = abs(center_ord - move_ord)
            if ord_diff < 3:
                center_coord = int(center[1])
                move_coord = int(move[1])
                coord_diff = abs(center_coord - move_coord)
                if coord_diff >= 3:
                    legal_moves.append(move)
            else:
                legal_moves.append(move)
        random.shuffle(legal_moves)
        move = legal_moves[0]
    else:
        available_moves = get_empty_spaces(board, boardsize)
        random.shuffle(available_moves)
        move = available_moves[0]
    move_status, capture, capture_count, win = play_move(move, board, boardsize, player, opponent)
    return move_status, capture, capture_count, win, move

def tournament_rule_check(board, boardsize, player, move_history, move):
    if player == 1 and len(move_history) == 0:
        pos = (len(board) - 1) // 2
        center = point_to_boardloc(pos, boardsize)
        if move != center:
            print("\nError: Black's first move must be the center point")
            return False
        else:
            return True
    elif player == 1 and len(move_history) == 2:
        available_moves = get_empty_spaces(board, boardsize)
        center = (len(board) - 1) // 2
        center = point_to_boardloc(center, boardsize)
        center_ord = ord(center[0])
        legal_moves = []
        for i in available_moves:
            move_ord = ord(i[0])
            ord_diff = abs(center_ord - move_ord)
            if ord_diff < 3:
                center_coord = int(center[1])
                move_coord = int(i[1])
                coord_diff = abs(center_coord - move_coord)
                if coord_diff >= 3:
                    legal_moves.append(i)
            else:
                legal_moves.append(i)
        if move not in legal_moves:
            print("\nError: Black's second move must be at least 3 spaces away from the center point")
            return False
        else:
            return True
    else:
        return True

def display_move(move_status, player, move, board, boardsize):
    if move_status:
        if player == 1:
            p1 = "black"
            p2 = "white"
        else:
            p1 = "white"
            p2 = "black"
        print("")
        print(p1, "played", move)
        show_board(board, boardsize)
        # implement 4 in a row/3 in a row announcing here
    else:
        print("Move was not played")

def display_capture(capture, player, black_capture_count, white_capture_count, capture_count, black_win, white_win, p1, p2):
    capture_win = False
    if capture:
        if player == 1:
            black_capture_count += capture_count
            if black_capture_count >= 5:
                capture_win = True
                black_win = True
        else:
            white_capture_count += capture_count
            if white_capture_count >= 5:
                capture_win = True
                white_win = True
        if capture_count == 1:
            print("")
            print(p1, "made 1 capture")
        elif capture_count > 1:
            print("")
            print(p1, "made", capture_count, "captures")
        if capture_win:
            if black_win:
                print("\nBlack made 5 or more captures - black wins!")
            elif white_win:
                print("\nWhite made 5 or more captures - white wins!")
    return black_capture_count, white_capture_count, black_win, white_win

def display_win(win, player, black_win, white_win, draw, board, boardsize, move_status, opponent):
    if win:
        if player == 1:
            black_win = True
        else:
            white_win = True
        if black_win:
            print("\nBlack wins via 5 in a row!")
        elif white_win:
            print("\nWhite wins via 5 in a row!")
    else:
        draw = check_draw(board, boardsize, draw)
        if draw:
            print("\nGame has ended in a draw")
        else:
            # game continues, switch internal current-player values
            if move_status:
                if player == 1:
                    player = 2
                    opponent = 1
                else:
                    player = 1
                    opponent = 2
    return black_win, white_win, draw, player, opponent

def boardsize_cmd(command, board, boardsize, move_history):
    if len(command) != 2:
        print("\nError: Command requires additional input. Consult README for more info")
        show_board(board, boardsize)
        return board, boardsize, move_history, False
    else:
        new_boardsize = boardsize_change(command[1])
        if new_boardsize == 1:
            return board, boardsize, move_history, False
        else:
            boardsize = new_boardsize                
            board, move_history = build_board(boardsize)
            show_board(board, boardsize)
            return board, boardsize, move_history, True

def reset_win_status():
    b_win = False
    w_win = False
    draw_win = False
    return b_win, w_win, draw_win

def reset_players():
    p1 = 1
    p2 = 2
    return p1, p2
        
def reset_cap_counts():
    bcc = 0
    wcc = 0
    return bcc, wcc

def genmove_cmd(board, boardsize, player, opponent, b_cap_count, w_cap_count, b_win, w_win, draw, move_history, ruleset):
    move_status, capture, capture_count, win, move = generate_random_move(board, boardsize, player, opponent, move_history, ruleset)
    if player == 1:
        p1 = "black"
        p2 = "white"
    else:
        p1 = "white"
        p2 = "black"
    return format_move(board, boardsize, player, opponent, b_cap_count, w_cap_count, b_win, w_win, draw, move_status, 
                       capture, capture_count, move, p1, p2, win, move_history)

def format_move(board, boardsize, player, opponent, b_cap_count, w_cap_count, b_win, 
                w_win, draw, move_status, capture, capture_count, move, p1, p2, win, move_history):
    display_move(move_status, player, move, board, boardsize)
    b_cap_count, w_cap_count, b_win, w_win \
        = display_capture(capture, player, b_cap_count, w_cap_count, capture_count, b_win, w_win, p1, p2)
    b_win, w_win, draw, player, opponent \
        = display_win(win, player, b_win, w_win, draw, board, boardsize, move_status, opponent)
    move_history.append((p1[0], move))
    return board, boardsize, player, opponent, b_cap_count, w_cap_count, b_win, w_win, draw

def play_cmd(board, boardsize, player, opponent, b_cap_count, w_cap_count, b_win, w_win, draw, move, move_history):
    move_status, capture, capture_count, win = play_move(move, board, boardsize, player, opponent)
    if player == 1:
        p1 = "black"
        p2 = "white"
    else:
        p1 = "white"
        p2 = "black"
    return format_move(board, boardsize, player, opponent, b_cap_count, w_cap_count, b_win, 
                       w_win, draw, move_status, capture, capture_count, move, p1, p2, win, move_history)

def emptyspaces_cmd(board, boardsize):
    empty_spaces = get_empty_spaces(board, boardsize)
    empty_spaces.sort()
    count = 1
    print("")
    for i in empty_spaces:
        print(i, end =' ')
        if count == 10:
            print("")
            count = 1
        else:
            count += 1
    print("")

def capturecounts_cmd(b_cap_count, w_cap_count):
    print("\n5 or more captures are needed for a capture win")
    print("Black has made", b_cap_count, "capture(s)")
    print("White has made", w_cap_count, "capture(s)")
    
def winner_cmd(b_win, w_win, draw):
    if b_win:
        print("\nBlack is the winner!")
    elif w_win:
        print("\nWhite is the winner!")
    elif draw:
        print("\nThe game is a draw")
    else:
        print("\nGame is still ongoing") 

def ptm_cmd(player):
    if player == 1:
        print("\nIt is black's turn")
    else:
        print("\nIt is white's turn")    
    
def changeptm_cmd(inp, player, opponent):
    inp = inp.lower()
    if inp == "b":
        player = 1
        opponent = 2
        print("\nPlayer to move is now Black")
    elif inp == "w":
        player = 2
        opponent = 1
        print("\nPlayer to move is now White")
    else:
        print("\nError: Incorrect input for command. Consult README for more info") 
    return player, opponent

def movehistory_cmd(inp, move_history):
    if len(inp) > 1:
        if len(inp) > 2:
            print("\nError: Incorrect amount of input for command. Consult README for more info.")
        else:
            if not inp[1].isalpha():
                print("\nError: Incorrect input for command. Consult README for more info.")
            else:
                if inp[1].lower() == "b":
                    if len(move_history) < 1:
                        print("\nBlack has not made a move yet")
                    else:
                        count = 1
                        for move in move_history:
                            if move[0] == "b":
                                print(str(count)+".", move[0].upper(), move[1])
                                count += 1
                elif inp[1].lower() == "w":
                    if len(move_history) < 1:
                        print("\nWhite has not made a move yet")
                    else:
                        count = 1
                        for move in move_history:
                            if move[0] == "w":
                                print(str(count)+".", move[0].upper(), move[1])
                                count += 1
                else:
                    print("\nError: Incorrect input for command. Consult README for more info.")
    else:
        if len(move_history) < 1:
            print("\nNo moves have been made yet")
        else:
            count = 1
            for move in move_history:
                print(str(count)+".", move[0].upper(), move[1])
                count += 1    
                
def check_ruleset(ruleset):
    if ruleset == 1:
        print("\nThe current ruleset is: Tournament")
    elif ruleset == 2:
        print("\nThe current ruleset is: Casual")    

def main():
    
    commandlist = ["boardsize", "reset", "quit", "genmove", "play", "commands", "emptyspaces", 
                   "ptm", "winner", "showboard", "capturecounts", "playgame", "changeptm", "movehistory",
                   "rules", "changerules"]

    boardsize = 7
    board = [0] * ((boardsize + 1) ** 2)
    
    # build board
    board, move_history = build_board(boardsize)
    
    # show board
    print("Pente random player, by Adam Pumphrey")
    print("\nBlack = 1")
    print("White = 2")
    print("Empty space = 0")
    show_board(board, boardsize)
    
    player = 1
    opponent = 2
    ruleset = 1
    black_capture_count = 0
    white_capture_count = 0
    black_win = False
    white_win = False
    draw = False
    user_inp = input("\nPlease enter a command: ")
    while user_inp:
        command = user_inp.split(" ")
        check_result = check_inp_command(command, commandlist)
        if check_result == 1:
            error = True
            print("\nError: Command does not exist. Use 'commands' to list existing commands")
        elif check_result == 0:
            # execute command
            if command[0] == "boardsize":
                board, boardsize, move_history, success = boardsize_cmd(command, board, boardsize, move_history)
                if success:
                    player, opponent = reset_players()
                    black_capture_count, white_capture_count = reset_cap_counts()
                    black_win, white_win, draw = reset_win_status()                        
            elif command[0] == "reset":
                if len(command) > 1:
                    print("\nError: Command does not require additional input. Consult README for more info")
                else:
                    player, opponent = reset_players()
                    black_capture_count, white_capture_count = reset_cap_counts()
                    black_win, white_win, draw = reset_win_status()
                    board, move_history = build_board(boardsize)
                    show_board(board, boardsize)
            elif command[0] == "quit":
                if len(command) > 1:
                    print("\nError: Command does not require additional input. Consult README for more info")
                else:                
                    quit()
            elif command[0] == "genmove":
                if len(command) > 1:
                    print("\nError: Command does not require additional input. Consult README for more info")
                elif check_game_status(black_win, white_win, draw):
                    print("\nGame is over. To start a new game, please use the 'reset' command")
                else:
                    board, boardsize, player, opponent, black_cap_count, white_cap_count,\
                    black_win, white_win, draw \
                    = genmove_cmd(board, boardsize, player, opponent, black_capture_count, 
                                  white_capture_count, black_win, white_win, draw, move_history, ruleset)                  
            elif command[0] == "play":
                if len(command) < 2:
                    print("\nError: Command requires additional input. Consult README for more info")
                elif len(command) > 2:
                    print("\nError: Incorrect amount of input for command. Consult README for more info")
                elif check_game_status(black_win, white_win, draw):
                    print("\nGame is over. To start a new game, please use the 'reset' command")
                else:
                    if ruleset == 1:
                        check = tournament_rule_check(board, boardsize, player, move_history, command[1])
                        if check:
                            board, boardsize, player, opponent, black_capture_count, white_capture_count,\
                                black_win, white_win, draw \
                                = play_cmd(board, boardsize, player, opponent, black_capture_count, 
                                           white_capture_count, black_win, white_win, draw, command[1], move_history)
                        else:
                            show_board(board, boardsize)
                    else:
                        board, boardsize, player, opponent, black_capture_count, white_capture_count,\
                            black_win, white_win, draw \
                            = play_cmd(board, boardsize, player, opponent, black_capture_count, 
                                       white_capture_count, black_win, white_win, draw, command[1], move_history)                        
            elif command[0] == "commands":
                if len(command) > 1:
                    print("\nError: Command does not require additional input. Consult README for more info")
                else:
                    print("\nCommands:")
                    for i in commandlist:
                        print(" ", i)
            elif command[0] == "emptyspaces":
                if len(command) > 1:
                    print("\nError: Command does not require additional input. Consult README for more info")
                else:
                    emptyspaces_cmd(board, boardsize)
            elif command[0] == "ptm":
                if len(command) > 1:
                    print("\nError: Command does not require additional input. Consult README for more info")
                else:
                    if check_game_status(black_win, white_win, draw):
                        print("\nThe game has ended. To start a new game, please use the 'reset' command")
                    else: 
                        ptm_cmd(player)
            elif command[0] == "changeptm":
                if len(command) < 2:
                    print("\nError: Command requires additional input. Consult README for more info")
                elif len(command) > 2:
                    print("\nError: Incorrect amount of input for command. Consult README for more info")                
                elif check_game_status(black_win, white_win, draw):
                    print("\nThe game has ended. To start a new game, please use the 'reset' command")
                else:
                    inp = command[1]
                    if not inp.isalpha():
                        print("\nError: Incorrect input for command. Consult README for more info")
                    else:
                        player, opponent = changeptm_cmd(inp, player, opponent)
            elif command[0] == "winner":
                if len(command) > 1:
                    print("\nError: Command does not require additional input. Consult README for more info")
                else:
                    winner_cmd(black_win, white_win, draw)
            elif command[0] == "showboard":
                if len(command) > 1:
                    print("\nError: Command does not require additional input. Consult README for more info")
                else:
                    show_board(board, boardsize)
            elif command[0] == "capturecounts":
                if len(command) > 1:
                    print("\nError: Command does not require additional input. Consult README for more info")
                else:
                    capturecounts_cmd(black_capture_count, white_capture_count)
            elif command[0] == "playgame":
                if len(command) > 1:
                    print("\nError: Command does not require additional input. Consult README for more info")
                else:
                    if check_game_status(black_win, white_win, draw):
                        print("\nThe game has ended. To start a new game, please use the 'reset' command") 
                    else:
                        while not black_win and not white_win and not draw:
                            board, boardsize, player, opponent, black_capture_count, white_capture_count,\
                                black_win, white_win, draw \
                                = genmove_cmd(board, boardsize, player, opponent, black_capture_count, 
                                      white_capture_count, black_win, white_win, draw, move_history, ruleset)
            elif command[0] == "movehistory":
                movehistory_cmd(command, move_history)
            elif command[0] == "changerules":
                arg = input("\nEnter 1 for Tournament Rules, enter 2 for Casual Rules, enter c to cancel: ")
                argcheck = False
                while not argcheck:
                    if arg != "1" and arg != "2" and arg != "c":
                        print("\nError: Incorrect input for command. Consult README for more info")
                        check_ruleset(ruleset)
                        arg = input("\nEnter 1 for Tournament Rules, enter 2 for Casual Rules: ")
                    else:
                        argcheck = True
                if arg == "c":
                    check_ruleset(ruleset)
                    show_board(board, boardsize)
                else:
                    ruleset = int(arg)
                    check_ruleset(ruleset)
                    player, opponent = reset_players()
                    black_capture_count, white_capture_count = reset_cap_counts()
                    black_win, white_win, draw = reset_win_status()
                    board, move_history = build_board(boardsize)
                    show_board(board, boardsize)
            elif command[0] == "rules":
                check_ruleset(ruleset)
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