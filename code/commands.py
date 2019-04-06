import utility as u
import heuristic as heur
import random

def boardsize_cmd(command, board, boardsize, move_history):
    # if improper amount of arguments
    if len(command) != 2:
        print("\nError: Command requires additional input. Consult README for more info")
        # display current board
        u.show_board(board, boardsize)
        # return old values + False status
        return board, boardsize, move_history, False
    
    else:
        # try changing boardsize
        new_boardsize = u.boardsize_change(command[1])
        
        # if change unsuccessful
        if new_boardsize == 1:
            # return old values + False status
            return board, boardsize, move_history, False
        
        else:
            # change boardsize
            boardsize = new_boardsize
            # build new board
            board, move_history = u.build_board(boardsize)
            u.show_board(board, boardsize)
            # return new values + True status
            return board, boardsize, move_history, True

def genmove_cmd(board, boardsize, player, opponent, b_cap_count, w_cap_count, b_win, w_win, draw, move_history, ruleset):
    # generate and play random move
    move_status, capture, capture_count, win, move, blocks = u.generate_random_move(board, boardsize, player, opponent, move_history, ruleset)
    
    # if current player is black
    if player == 1:
        p1 = "black"
        p2 = "white"
    
    # if current player is white
    else:
        p1 = "white"
        p2 = "black"
        
    # return values obtained from utility.format_move
    return u.format_move(board, boardsize, player, opponent, b_cap_count, w_cap_count, b_win, w_win, draw, move_status, 
                       capture, capture_count, move, p1, p2, win, move_history, blocks)

def play_cmd(board, boardsize, player, opponent, b_cap_count, w_cap_count, b_win, w_win, draw, move, move_history):
    # play specified move
    move_status, capture, capture_count, win, blocks = u.play_move(move, board, boardsize, player, opponent)
    
    # if current player is black
    if player == 1:
        p1 = "black"
        p2 = "white"
    
    # if current player is white
    else:
        p1 = "white"
        p2 = "black"
        
    # return values obtained from utility.format_move
    return u.format_move(board, boardsize, player, opponent, b_cap_count, w_cap_count, b_win, 
                       w_win, draw, move_status, capture, capture_count, move, p1, p2, win, move_history, blocks)

def emptyspaces_cmd(board, boardsize):
    # get list of empty spaces on board
    empty_spaces = u.get_empty_spaces(board, boardsize)
    # sort list
    empty_spaces.sort()
    # display list
    count = 1
    print("")
    for i in empty_spaces:
        print(i, end =' ')
        # max row of 10 for readability
        if count == 10:
            print("")
            count = 1
        else:
            count += 1
    print("")

def capturecounts_cmd(b_cap_count, w_cap_count):
    # display capture counts for each player
    print("\n5 or more captures are needed for a capture win")
    print("Black has made", b_cap_count, "capture(s)")
    print("White has made", w_cap_count, "capture(s)")
    
def winner_cmd(b_win, w_win, draw):
    
    # if black has won
    if b_win:
        print("\nBlack is the winner!")
        
    # if white has won
    elif w_win:
        print("\nWhite is the winner!")
        
    # if the game is a draw
    elif draw:
        print("\nThe game is a draw")
        
    # if the game has not ended
    else:
        print("\nGame is still ongoing") 

def ptm_cmd(player):
    
    # if current player is black
    if player == 1:
        print("\nIt is black's turn")
        
    # if current player is white
    else:
        print("\nIt is white's turn")    
    
def changeptm_cmd(inp, player, opponent):
    # change input to lowercase
    inp = inp.lower()
    
    # change player-to-move to black
    if inp == "b":
        player = 1
        opponent = 2
        print("\nPlayer to move is now Black")
        
    # change player-to-move to white
    elif inp == "w":
        player = 2
        opponent = 1
        print("\nPlayer to move is now White")
    
    # if input is invalid
    else:
        print("\nError: Incorrect input for command. Consult README for more info")
        
    # return new values
    return player, opponent

def movehistory_cmd(inp, move_history):
    
    # if additional arguments
    if len(inp) > 1:
        
        # if too many arguments
        if len(inp) > 2:
            print("\nError: Incorrect amount of input for command. Consult README for more info.")
            
        else:
            
            # if invalid argument
            if not inp[1].isalpha():
                print("\nError: Incorrect input for command. Consult README for more info.")
                
            else:
                
                # move history for black
                if inp[1].lower() == "b":
                    
                    # if black has not played
                    if len(move_history) < 1:
                        print("\nBlack has not made a move yet")
                        
                    else:
                        count = 1
                        # list black's previous moves
                        for move in move_history:
                            if move[0] == "b":
                                print(str(count)+".", move[0].upper(), move[1])
                                count += 1
                                
                # move history for white
                elif inp[1].lower() == "w":
                    
                    # if white has not played
                    if len(move_history) < 1:
                        print("\nWhite has not made a move yet")
                        
                    else:
                        count = 1
                        # list white's previous moves
                        for move in move_history:
                            if move[0] == "w":
                                print(str(count)+".", move[0].upper(), move[1])
                                count += 1
                else:
                    # invalid input
                    print("\nError: Incorrect input for command. Consult README for more info.")
                    
    else:
        
        # if no moves have been made
        if len(move_history) < 1:
            print("\nNo moves have been made yet")
            
        else:
            count = 1
            # display previous moves
            for move in move_history:
                print(str(count)+".", move[0].upper(), move[1])
                count += 1

def startgame_cmd(boardsize, ruleset):
    # reset game information
    player, opponent = u.reset_players()
    black_capture_count, white_capture_count = u.reset_cap_counts()
    black_win, white_win, draw = u.reset_win_status()
    # build new board
    board, move_history = u.build_board(boardsize)
    u.show_board(board, boardsize)
    # user chooses colour to play
    arg = input("\nChoose your colour (b for black, w for white, c to cancel): ")
    argcheck = False
    
    # while input not validated
    while not argcheck:
        arg = arg.lower()
        
        # if invalid input
        if arg != "b" and arg != "w" and arg != "c":
            print("\nError: Incorrect input for command. Consult README for more info")
            arg = input("\nChoose your colour (b for black, w for white, c to cancel): ")
            
        else:
            # input validated
            argcheck = True
            
    # if user cancels game
    if arg == "c":
        print("\nGame has been cancelled")
        u.show_board(board, boardsize)
        
    # if user wants to play black
    elif arg == "b":
        player = 1
        
    # if user wants to play white
    elif arg == "w":
        opponent = 1
        
    # user choice of player for cpu to use
    arg2 = input("\nChoose the player for your opponent. 1 for Random, 2 for Heuristic: ")
    argcheck2 = False
    
    # while input not validated
    while not argcheck2:
        
        # if invalid input
        if arg2 != "1" and arg2 != "2":
            print("\nError: Incorrect input for command. Consult README for more info")
            arg2 = input("\nChose the player for your opponent. 1 for Random, 2 for Heuristic: ")
            
        else:
            # input validated
            argcheck2 = True
            
    # if user playing white
    if opponent == 1:
        
        # while game is ongoing
        while not black_win and not white_win and not draw:
            
            # if black using random player
            if arg2 == "1":
                # generate and play random move
                board, player, opponent, black_capture_count, white_capture_count,\
                    black_win, white_win, draw \
                    = genmove_cmd(board, boardsize, 1, 2, black_capture_count, 
                                  white_capture_count, black_win, white_win, draw, move_history, ruleset)
                
            # if black using heuristic player
            elif arg2 == "2":
                # obtain black's heuristic-determined move
                black_move = current_position_evaluation(player, opponent, board, boardsize, move_history, ruleset, 1)
                # play specified move
                board, player, opponent, black_capture_count, white_capture_count,\
                    black_win, white_win, draw \
                    = play_cmd(board, boardsize, player, opponent, black_capture_count, 
                               white_capture_count, black_win, white_win, draw, black_move, move_history)
                
            # if black's move ended the game
            if black_win or white_win or draw:
                # exit game
                break
            
            else:
                # user enters move they want to play
                move_arg = input("\nPlease enter your move, or enter 'quit' to exit: ")
                move_arg = move_arg.lower()
                
                # if user wants to exit
                if move_arg == "quit":
                    print("\nGame cancelled")
                    # exit game
                    break
                # else
                # play specified move
                board, player, opponent, black_capture_count, white_capture_count,\
                    black_win, white_win, draw \
                    = play_cmd(board, boardsize, 2, 1, black_capture_count, 
                               white_capture_count, black_win, white_win, draw, move_arg, move_history)
                
    # if user playing black
    elif player == 1:
        
        # while game is ongoing
        while not black_win and not white_win and not draw:
            # user enters move they want to play
            move_arg = input("\nPlease enter your move, or enter 'quit' to exit: ")
            move_arg = move_arg.lower()
            
            # if user wants to exit
            if move_arg == "quit":
                print("\nGame cancelled")
                # exit game
                break
            
            movecheck = False
            
            # while input not validated
            while not movecheck:
                
                # if no moves have been made
                if len(move_history) == 0:
                    # get center point
                    pos = (len(board) - 1) // 2
                    center = u.point_to_boardloc(pos, boardsize)
                    
                    # if move specified is not center point
                    if move_arg != center:
                        print("\nError: Black's first move must be the center point")
                        # display current board
                        u.show_board(board, boardsize)
                        # user enters move they want to make
                        move_arg = input("\nPlease enter your move, or enter 'quit' to exit: ")
                        move_arg = move_arg.lower()
                        
                        # if user wants to exit
                        if move_arg == "quit":
                            print("\nGame cancelled")
                            # exit game
                            break
                        
                    else:
                        # input validated
                        movecheck = True
                        # play specified move
                        board, player, opponent, black_capture_count, white_capture_count,\
                            black_win, white_win, draw \
                            = play_cmd(board, boardsize, 1, 2, black_capture_count, 
                                       white_capture_count, black_win, white_win, draw, move_arg, move_history)
                        
                # if previous check passes and tournament rules are in use
                elif ruleset == 1:
                    # check if move entered is legal according to tournament rules
                    check = u.tournament_rule_check(board, boardsize, player, move_history, move_arg)
                    
                    # if move is legal
                    if check:
                        # input validated
                        movecheck = True
                        # play specified move
                        board, player, opponent, black_capture_count, white_capture_count,\
                            black_win, white_win, draw \
                            = play_cmd(board, boardsize, 1, 2, black_capture_count, 
                                       white_capture_count, black_win, white_win, draw, move_arg, move_history)
                        
                    else:
                        # display current board
                        u.show_board(board, boardsize)
                        # user enters move they want to make
                        move_arg = input("\nPlease enter your move, or enter 'quit' to exit: ")
                        move_arg = move_arg.lower()
                        
                        # if user wants to exit
                        if move_arg == "quit":
                            print("\nGame cancelled")
                            # exit game
                            break
                        
                else:
                    # input validated
                    movecheck = True
                    # play specified move
                    board, player, opponent, black_capture_count, white_capture_count,\
                        black_win, white_win, draw \
                        = play_cmd(board, boardsize, 1, 2, black_capture_count, 
                                   white_capture_count, black_win, white_win, draw, move_arg, move_history)
            
            # if black's move ended the game
            if black_win or white_win or draw:
                # exit game
                break
            
            else:
                
                # if white is using random player
                if arg2 == "1":
                    # generate and play random move
                    board, player, opponent, black_capture_count, white_capture_count,\
                        black_win, white_win, draw \
                        = genmove_cmd(board, boardsize, 2, 1, black_capture_count, 
                                      white_capture_count, black_win, white_win, draw, move_history, ruleset)
                    
                # if white is using heuristic player
                elif arg2 == "2":
                    # obtain white's heurisitc-determined move
                    white_move = current_position_evaluation(player, opponent, board, boardsize, move_history, ruleset, 1)
                    # play specified move
                    board, player, opponent, black_capture_count, white_capture_count,\
                        black_win, white_win, draw \
                        = play_cmd(board, boardsize, player, opponent, black_capture_count, 
                                   white_capture_count, black_win, white_win, draw, white_move, move_history)
                    
def current_position_evaluation(player, opponent, board, boardsize, move_history, ruleset, mode=0):
    
    # if current player is black
    if player == 1:
        playercolour = 'black'
        
    # if current player is white
    elif player == 2:
        playercolour = 'white'
        
    # if no moves have been made
    if len(move_history) == 0:
        # get center point
        pos = (len(board) - 1) // 2
        move = u.point_to_boardloc(pos, boardsize)
        
        # if display mode
        if mode == 0:
            print("\nblack must play", move, "to start the game")
            
        # if return mode
        else:
            return move
        
    # if tournament rules are in use and it is black's second move
    elif player == 1 and ruleset == 1 and len(move_history) == 2:
        # get list of empty spaces on current board
        available_moves = u.get_empty_spaces(board, boardsize)
        # get center point
        center = (len(board) - 1) // 2
        center = u.point_to_boardloc(center, boardsize)
        center_ord = ord(center[0])
        
        legal_moves = []
        # for every empty space
        for move in available_moves:
            move_ord = ord(move[0])
            ord_diff = abs(center_ord - move_ord)
            
            # if current column is less than 3 spaces away from center
            if ord_diff < 3:
                center_coord = int(center[1])
                move_coord = int(move[1])
                coord_diff = abs(center_coord - move_coord)
                
                # if current row is 3+ spaces away from center
                if coord_diff >= 3:
                    # add to legal move list
                    legal_moves.append(move)
            else:
                # add to legal move list
                legal_moves.append(move)
                
        # if display lower
        if mode == 0:
            count = 1
            print('\nblack must play in one of the following spaces as per tournament rules:')
            # display legal moves
            for i in legal_moves:
                print(i, end =' ')
                # max row of 10 for readability
                if count == 10:
                    print('')
                    count = 1
                else:
                    count += 1
            print('')
        
        # if return mode
        else:
            # return random legal move
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
