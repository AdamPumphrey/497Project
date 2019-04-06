import utility as u
import heuristic as heur
import random

def boardsize_cmd(command, board, boardsize, move_history):
    if len(command) != 2:
        print("\nError: Command requires additional input. Consult README for more info")
        u.show_board(board, boardsize)
        return board, boardsize, move_history, False
    else:
        new_boardsize = u.boardsize_change(command[1])
        if new_boardsize == 1:
            return board, boardsize, move_history, False
        else:
            boardsize = new_boardsize                
            board, move_history = u.build_board(boardsize)
            u.show_board(board, boardsize)
            return board, boardsize, move_history, True

def genmove_cmd(board, boardsize, player, opponent, b_cap_count, w_cap_count, b_win, w_win, draw, move_history, ruleset):
    move_status, capture, capture_count, win, move, blocks = u.generate_random_move(board, boardsize, player, opponent, move_history, ruleset)
    if player == 1:
        p1 = "black"
        p2 = "white"
    else:
        p1 = "white"
        p2 = "black"
    return u.format_move(board, boardsize, player, opponent, b_cap_count, w_cap_count, b_win, w_win, draw, move_status, 
                       capture, capture_count, move, p1, p2, win, move_history, blocks)

def play_cmd(board, boardsize, player, opponent, b_cap_count, w_cap_count, b_win, w_win, draw, move, move_history):
    move_status, capture, capture_count, win, blocks = u.play_move(move, board, boardsize, player, opponent)
    if player == 1:
        p1 = "black"
        p2 = "white"
    else:
        p1 = "white"
        p2 = "black"
    return u.format_move(board, boardsize, player, opponent, b_cap_count, w_cap_count, b_win, 
                       w_win, draw, move_status, capture, capture_count, move, p1, p2, win, move_history, blocks)

def emptyspaces_cmd(board, boardsize):
    empty_spaces = u.get_empty_spaces(board, boardsize)
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

def startgame_cmd(boardsize, ruleset):
    player, opponent = u.reset_players()
    black_capture_count, white_capture_count = u.reset_cap_counts()
    black_win, white_win, draw = u.reset_win_status()
    board, move_history = u.build_board(boardsize)
    u.show_board(board, boardsize)                
    arg = input("\nChoose your colour (b for black, w for white, c to cancel): ")
    argcheck = False
    while not argcheck:
        arg = arg.lower()
        if arg != "b" and arg != "w" and arg != "c":
            print("\nError: Incorrect input for command. Consult README for more info")
            arg = input("\nChoose your colour (b for black, w for white, c to cancel): ")
        else:
            argcheck = True
    if arg == "c":
        print("\nGame has been cancelled")
        u.show_board(board, boardsize)
    elif arg == "b":
        player = 1
    elif arg == "w":
        opponent = 1
    arg2 = input("\nChoose the player for your opponent. 1 for Random, 2 for Heuristic: ")
    argcheck2 = False
    while not argcheck2:
        if arg2 != "1" and arg2 != "2":
            print("\nError: Incorrect input for command. Consult README for more info")
            arg2 = input("\nChose the player for your opponent. 1 for Random, 2 for Heuristic: ")
        else:
            argcheck2 = True
    if opponent == 1:
        while not black_win and not white_win and not draw:
            if arg2 == "1":
                board, player, opponent, black_capture_count, white_capture_count,\
                    black_win, white_win, draw \
                    = genmove_cmd(board, boardsize, 1, 2, black_capture_count, 
                                  white_capture_count, black_win, white_win, draw, move_history, ruleset)
            elif arg2 == "2":
                black_move = current_position_evaluation(player, opponent, board, boardsize, move_history, ruleset, 1)
                board, player, opponent, black_capture_count, white_capture_count,\
                    black_win, white_win, draw \
                    = play_cmd(board, boardsize, player, opponent, black_capture_count, 
                               white_capture_count, black_win, white_win, draw, black_move, move_history)                
            if black_win or white_win or draw:
                break
            else:
                move_arg = input("\nPlease enter your move, or enter 'quit' to exit: ")
                move_arg = move_arg.lower()
                if move_arg == "quit":
                    print("\nGame cancelled")
                    break
                board, player, opponent, black_capture_count, white_capture_count,\
                    black_win, white_win, draw \
                    = play_cmd(board, boardsize, 2, 1, black_capture_count, 
                               white_capture_count, black_win, white_win, draw, move_arg, move_history)
    elif player == 1:
        while not black_win and not white_win and not draw:
            move_arg = input("\nPlease enter your move, or enter 'quit' to exit: ")
            move_arg = move_arg.lower()
            if move_arg == "quit":
                print("\nGame cancelled")
                break
            movecheck = False
            while not movecheck:
                if len(move_history) == 0:
                    pos = (len(board) - 1) // 2
                    center = u.point_to_boardloc(pos, boardsize)
                    if move_arg != center:
                        print("\nError: Black's first move must be the center point")
                        u.show_board(board, boardsize)
                        move_arg = input("\nPlease enter your move, or enter 'quit' to exit: ")
                        move_arg = move_arg.lower()
                        if move_arg == "quit":
                            print("\nGame cancelled")
                            break
                    else:
                        movecheck = True
                        board, player, opponent, black_capture_count, white_capture_count,\
                            black_win, white_win, draw \
                            = play_cmd(board, boardsize, 1, 2, black_capture_count, 
                                       white_capture_count, black_win, white_win, draw, move_arg, move_history)                             
                elif ruleset == 1:
                    check = u.tournament_rule_check(board, boardsize, player, move_history, move_arg)
                    if check:
                        movecheck = True
                        board, player, opponent, black_capture_count, white_capture_count,\
                            black_win, white_win, draw \
                            = play_cmd(board, boardsize, 1, 2, black_capture_count, 
                                       white_capture_count, black_win, white_win, draw, move_arg, move_history)
                    else:
                        u.show_board(board, boardsize)
                        move_arg = input("\nPlease enter your move, or enter 'quit' to exit: ")
                        move_arg = move_arg.lower()
                        if move_arg == "quit":
                            print("\nGame cancelled")
                            break
                else:
                    movecheck = True
                    board, player, opponent, black_capture_count, white_capture_count,\
                        black_win, white_win, draw \
                        = play_cmd(board, boardsize, 1, 2, black_capture_count, 
                                   white_capture_count, black_win, white_win, draw, move_arg, move_history)
            if black_win or white_win or draw:
                break
            else:
                if arg2 == "1":
                    board, player, opponent, black_capture_count, white_capture_count,\
                        black_win, white_win, draw \
                        = genmove_cmd(board, boardsize, 2, 1, black_capture_count, 
                                      white_capture_count, black_win, white_win, draw, move_history, ruleset)
                elif arg2 == "2":
                    white_move = current_position_evaluation(player, opponent, board, boardsize, move_history, ruleset, 1)
                    board, player, opponent, black_capture_count, white_capture_count,\
                        black_win, white_win, draw \
                        = play_cmd(board, boardsize, player, opponent, black_capture_count, 
                                   white_capture_count, black_win, white_win, draw, white_move, move_history)
                    
def current_position_evaluation(player, opponent, board, boardsize, move_history, ruleset, mode=0):
    if player == 1:
        playercolour = 'black'
    elif player == 2:
        playercolour = 'white'
    if len(move_history) == 0:
        pos = (len(board) - 1) // 2
        move = u.point_to_boardloc(pos, boardsize)
        if mode == 0:
            print("\nblack must play", move, "to start the game")
        else:
            return move
    elif player == 1 and ruleset == 1 and len(move_history) == 2:
        available_moves = u.get_empty_spaces(board, boardsize)
        center = (len(board) - 1) // 2
        center = u.point_to_boardloc(center, boardsize)
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
        if mode == 0:
            count = 1
            print('\nblack must play in one of the following spaces as per tournament rules:')
            for i in legal_moves:
                print(i, end =' ')
                if count == 10:
                    print('')
                    count = 1
                else:
                    count += 1
            print('')            
        else:
            random.shuffle(legal_moves)
            move = legal_moves[0]
            return move
    else:
        last_move = move_history[-1]
        last_move_index = u.boardloc_to_point(last_move[1], boardsize)
        player_move_history = heur.parse_move_history(player, move_history)
        win_moves = heur.win_heuristic(player_move_history, board, player, opponent, boardsize)
        if win_moves:
            if mode == 0:
                print("\nwinning moves for", playercolour, "are: ", end='')
                for move in win_moves:
                    move = move + ' '
                    print(move, end='')
                print('')
            else:
                random.shuffle(win_moves)
                move = win_moves[0]
                return move
        else:
            def_moves = heur.def_heuristic(board, player, opponent, last_move_index, boardsize)
            if def_moves:
                if mode == 0:
                    if len(def_moves) > 1:
                        print("\na", playercolour, "loss is inevitable. blocking moves would be: ", end='')
                    else:
                        print("\nmove that will prevent a", playercolour, "loss is: ", end='')
                    for move in def_moves:
                        move = move + ' '
                        print(move, end='')
                    print('')
                else:
                    random.shuffle(def_moves)
                    move = def_moves[0]
                    return move
            else:
                four_moves = heur.win_heuristic(player_move_history, board, player, opponent, boardsize, 4)
                if four_moves:
                    if mode == 0:
                        print('')
                        print(playercolour, "can make an open four with: ", end='')
                        for move in four_moves:
                            move = move + ' '
                            print(move, end='')
                        print('')
                    else:
                        random.shuffle(four_moves)
                        move = four_moves[0]
                        return move
                else:
                    def_moves = heur.def_heuristic(board, player, opponent, last_move_index, boardsize, 4)
                    if def_moves:
                        if mode == 0:
                            print('')
                            print(playercolour, "can block an open four with: ", end='')
                            for move in def_moves:
                                move = move + ' '
                                print(move, end='')
                            print('')
                        else:
                            random.shuffle(def_moves)
                            move = def_moves[0]
                            return move
                    else:
                        if mode == 0:
                            print("\nthere are no specific moves to play at this time")
                        else:
                            legal_moves = u.get_empty_spaces(board, boardsize)
                            random.shuffle(legal_moves)
                            move = legal_moves[0]
                            return move
