''' 
Adam Pumphrey, CMPUT 497, ID: 1469319 

Random Pente Player
'''
import sys, random
import utility as u
import commands as com
import heuristic as heur

def main():
    
    commandlist = ["boardsize", "reset", "quit", "genmove", "play", "commands", "emptyspaces", 
                   "ptm", "winner", "showboard", "capturecounts", "playcpugame", "changeptm", "movehistory",
                   "rules", "changerules", "startgame", "poseval"]

    boardsize = 7
    
    # build board
    board, move_history = u.build_board(boardsize)
    
    # show board
    print("Pente random player, by Adam Pumphrey")
    print("\nBlack = 1")
    print("White = 2")
    print("Empty space = 0")
    u.show_board(board, boardsize)
    
    # initialize game information
    player = 1
    opponent = 2
    ruleset = 1
    black_capture_count = 0
    white_capture_count = 0
    black_win = False
    white_win = False
    draw = False
    
    # prompt for command
    user_inp = input("\nPlease enter a command: ")
    
    while user_inp:
        command = user_inp.split(" ")
        # checks validity of command entered
        check_result = u.check_inp_command(command, commandlist)
        
        # if command entered is invalid
        if not check_result:
            print("\nError: Command does not exist. Use 'commands' to list existing commands")
        
        # if command entered is valid
        elif check_result:
            
            '''execute command'''
            
            # boardsize command
            if command[0] == "boardsize":
                # try changing boardsize
                board, boardsize, move_history, success = com.boardsize_cmd(command, board, boardsize, move_history)
                
                # if boardsize change successful
                if success:
                    # reset game information
                    player, opponent = u.reset_players()
                    black_capture_count, white_capture_count = u.reset_cap_counts()
                    black_win, white_win, draw = u.reset_win_status()
                    
            # reset command
            elif command[0] == "reset":
                # if too many arguments
                if len(command) > 1:
                    print("\nError: Command does not require additional input. Consult README for more info")
                    
                else:
                    # reset game information
                    player, opponent = u.reset_players()
                    black_capture_count, white_capture_count = u.reset_cap_counts()
                    black_win, white_win, draw = u.reset_win_status()
                    # build new board
                    board, move_history = u.build_board(boardsize)
                    # display board
                    u.show_board(board, boardsize)
                    
            # quit command
            elif command[0] == "quit":
                
                # if too many arguments
                if len(command) > 1:
                    print("\nError: Command does not require additional input. Consult README for more info")
                    
                else:
                    # kill program
                    u.quit()
                    
            # genmove command
            elif command[0] == "genmove":
                
                # if too many arguments
                if len(command) > 1:
                    print("\nError: Command does not require additional input. Consult README for more info")
                
                # if game has ended and board + info not reset
                elif u.check_game_status(black_win, white_win, draw):
                    print("\nGame is over. To start a new game, please use the 'reset' command")
                
                else:
                    # generate and play random move
                    board, player, opponent, black_capture_count, white_capture_count,\
                    black_win, white_win, draw \
                    = com.genmove_cmd(board, boardsize, player, opponent, black_capture_count, 
                                  white_capture_count, black_win, white_win, draw, move_history, ruleset)
            
            # play command
            elif command[0] == "play":
                
                # if not enough arguments
                if len(command) < 2:
                    print("\nError: Command requires additional input. Consult README for more info")
                
                # if too many arguments
                elif len(command) > 2:
                    print("\nError: Incorrect amount of input for command. Consult README for more info")
                
                # if game has ended and board + info not reset
                elif u.check_game_status(black_win, white_win, draw):
                    print("\nGame is over. To start a new game, please use the 'reset' command")
                    
                else:
                    
                    # if black to move and it is the first move of the game
                    if player == 1 and len(move_history) == 0:
                        # get center point
                        pos = (len(board) - 1) // 2
                        center = u.point_to_boardloc(pos, boardsize)
                        
                        # if move entered is not the center point
                        if command[1] != center:
                            print("\nError: Black's first move must be the center point")
                            u.show_board(board, boardsize)
                            
                        else:
                            # play specified move
                            board, player, opponent, black_capture_count, white_capture_count,\
                                black_win, white_win, draw \
                                = com.play_cmd(board, boardsize, player, opponent, black_capture_count, 
                                           white_capture_count, black_win, white_win, draw, command[1], move_history)        
                    
                    # if previous check passes and tournament rules are in use 
                    elif ruleset == 1:
                        # check if move entered is legal according to tournament rules
                        check = u.tournament_rule_check(board, boardsize, player, move_history, command[1])
                        
                        # if move is legal
                        if check:
                            # play specified move
                            board, player, opponent, black_capture_count, white_capture_count,\
                                black_win, white_win, draw \
                                = com.play_cmd(board, boardsize, player, opponent, black_capture_count, 
                                           white_capture_count, black_win, white_win, draw, command[1], move_history)
                            
                        # if move is illegal
                        else:
                            # show current board
                            u.show_board(board, boardsize)
                            
                    else:
                        # play specified move
                        board, player, opponent, black_capture_count, white_capture_count,\
                            black_win, white_win, draw \
                            = com.play_cmd(board, boardsize, player, opponent, black_capture_count, 
                                       white_capture_count, black_win, white_win, draw, command[1], move_history)
            
            # commands command (lol)
            elif command[0] == "commands":
                
                # if too many arguments
                if len(command) > 1:
                    print("\nError: Command does not require additional input. Consult README for more info")
                    
                else:
                    print("\nCommands:")
                    # display commands
                    for i in commandlist:
                        print(" ", i)
                        
            # emptyspaces command
            elif command[0] == "emptyspaces":
                
                # if too many arguments
                if len(command) > 1:
                    print("\nError: Command does not require additional input. Consult README for more info")
                    
                else:
                    # display remaining empty board spaces
                    com.emptyspaces_cmd(board, boardsize)
                    
            # ptm command
            elif command[0] == "ptm":
                
                # if too many arguments
                if len(command) > 1:
                    print("\nError: Command does not require additional input. Consult README for more info")
                    
                else:
                    # if game has ended and board + info not reset
                    if u.check_game_status(black_win, white_win, draw):
                        print("\nThe game has ended. To start a new game, please use the 'reset' command")
                        
                    else:
                        # display player-to-move
                        com.ptm_cmd(player)
                        
            # changeptm command
            elif command[0] == "changeptm":
                
                # if not enough arguments
                if len(command) < 2:
                    print("\nError: Command requires additional input. Consult README for more info")
                
                # if too many arguments
                elif len(command) > 2:
                    print("\nError: Incorrect amount of input for command. Consult README for more info") 
                    
                # if game has ended and board + info not reset
                elif u.check_game_status(black_win, white_win, draw):
                    print("\nThe game has ended. To start a new game, please use the 'reset' command")
                    
                else:
                    inp = command[1]
                    
                    # if invalid input
                    if not inp.isalpha():
                        print("\nError: Incorrect input for command. Consult README for more info")
                        
                    else:
                        # change player-to-move
                        player, opponent = com.changeptm_cmd(inp, player, opponent)
                        
            # winner command
            elif command[0] == "winner":
                
                # if too many arguments
                if len(command) > 1:
                    print("\nError: Command does not require additional input. Consult README for more info")
                    
                else:
                    # display current game status
                    com.winner_cmd(black_win, white_win, draw)
                    
            # showboard command
            elif command[0] == "showboard":
                
                # if too many arguments
                if len(command) > 1:
                    print("\nError: Command does not require additional input. Consult README for more info")
                    
                else:
                    # display current board
                    u.show_board(board, boardsize)
            
            # capturecounts command
            elif command[0] == "capturecounts":
                
                # if too many arguments
                if len(command) > 1:
                    print("\nError: Command does not require additional input. Consult README for more info")
                    
                else:
                    # display capture counts for each player
                    com.capturecounts_cmd(black_capture_count, white_capture_count)
                    
            # playcpugame command
            elif command[0] == "playcpugame":
                
                # if too many arguments
                if len(command) > 1:
                    print("\nError: Command does not require additional input. Consult README for more info")
                    
                else:
                    # reset game information
                    player, opponent = u.reset_players()
                    black_capture_count, white_capture_count = u.reset_cap_counts()
                    black_win, white_win, draw = u.reset_win_status()
                    # build new board
                    board, move_history = u.build_board(boardsize)
                    u.show_board(board, boardsize)
                    # user choice of player for black
                    inp1 = input("Choose the player for black. 1 for Random, 2 for Heuristic: ")
                    inp1check = False
                    
                    # while input not validated
                    while not inp1check:
                        
                        # if input invalid
                        if inp1 != "1" and inp1 != "2":
                            print("\nError: Incorrect input for command. Consult README for more info")
                            inp1 = input("Choose the player for black. 1 for Random, 2 for Heuristic: ")
                            
                        else:
                            # input validated
                            inp1check = True
                    
                    # user choice of player for white
                    inp2 = input("Choose the player for white. 1 for Random, 2 for Heuristic: ")
                    inp2check = False
                    
                    # while input not validated
                    while not inp2check:
                        
                        # if input invalid
                        if inp2 != "1" and inp2 != "2":
                            print("\nError: Incorrect input for command. Consult README for more info")
                            inp2 = input("Choose the player for white. 1 for Random, 2 for Heuristic: ")
                            
                        else:
                            # input validated
                            inp2check = True
                            
                    # if both black and white are using random player
                    if inp1 == "1" and inp2 == "1":
                        
                        # while game is ongoing
                        while not black_win and not white_win and not draw:
                            
                            # generate and play random moves
                            board, player, opponent, black_capture_count, white_capture_count,\
                                black_win, white_win, draw \
                                = com.genmove_cmd(board, boardsize, player, opponent, black_capture_count, 
                                      white_capture_count, black_win, white_win, draw, move_history, ruleset)
                            
                    # if black using heuristic, white using random
                    elif inp1 == "2" and inp2 == "1":
                        
                        # while game is ongoing
                        while not black_win and not white_win and not draw:
                            
                            # obtain black's heuristic-determined move
                            black_move = com.current_position_evaluation(player, opponent, board, boardsize, move_history, ruleset, 1)
                            # play specified move
                            board, player, opponent, black_capture_count, white_capture_count,\
                                black_win, white_win, draw \
                                = com.play_cmd(board, boardsize, player, opponent, black_capture_count, 
                                           white_capture_count, black_win, white_win, draw, black_move, move_history)
                            
                            # if black's move did not end the game
                            if not black_win and not white_win and not draw:
                                # generate and play random move for white
                                board, player, opponent, black_capture_count, white_capture_count,\
                                    black_win, white_win, draw \
                                    = com.genmove_cmd(board, boardsize, player, opponent, black_capture_count, 
                                          white_capture_count, black_win, white_win, draw, move_history, ruleset)
                                
                    # if black using random, white using heuristic
                    elif inp1 == "1" and inp2 == "2":
                        
                        # while game is ongoing
                        while not black_win and not white_win and not draw:
                            
                            # generate and play random move for black
                            board, player, opponent, black_capture_count, white_capture_count,\
                                black_win, white_win, draw \
                                = com.genmove_cmd(board, boardsize, player, opponent, black_capture_count, 
                                      white_capture_count, black_win, white_win, draw, move_history, ruleset)
                            
                            # if black's move did not end the game
                            if not black_win and not white_win and not draw:
                                # obtain white's heuristic-determined move
                                white_move = com.current_position_evaluation(player, opponent, board, boardsize, move_history, ruleset, 1)
                                # play specified move
                                board, player, opponent, black_capture_count, white_capture_count,\
                                    black_win, white_win, draw \
                                    = com.play_cmd(board, boardsize, player, opponent, black_capture_count, 
                                               white_capture_count, black_win, white_win, draw, white_move, move_history)
                                
                    # if both black and white using heuristic player
                    elif inp1 == "2" and inp2 == "2":
                        
                        # while game is ongoing
                        while not black_win and not white_win and not draw:
                            # obtain black's heuristic-determined move
                            black_move = com.current_position_evaluation(player, opponent, board, boardsize, move_history, ruleset, 1)
                            # play specified moved
                            board, player, opponent, black_capture_count, white_capture_count,\
                                black_win, white_win, draw \
                                = com.play_cmd(board, boardsize, player, opponent, black_capture_count, 
                                           white_capture_count, black_win, white_win, draw, black_move, move_history)
                            
                            # if black's move did not end the game
                            if not black_win and not white_win and not draw:
                                # obtain white's heuristic-determined move
                                white_move = com.current_position_evaluation(player, opponent, board, boardsize, move_history, ruleset, 1)
                                # play specified move
                                board, player, opponent, black_capture_count, white_capture_count,\
                                    black_win, white_win, draw \
                                    = com.play_cmd(board, boardsize, player, opponent, black_capture_count, 
                                               white_capture_count, black_win, white_win, draw, white_move, move_history)
            
            # movehistory command
            elif command[0] == "movehistory":
                # display move history for current game
                com.movehistory_cmd(command, move_history)
                
            # changerules command
            elif command[0] == "changerules":
                # user choice for ruleset change or cancel
                arg = input("\nEnter 1 for Tournament Rules, enter 2 for Casual Rules, enter c to cancel: ")
                argcheck = False
                
                # while input not validated
                while not argcheck:
                    
                    # if input invalid
                    if arg != "1" and arg != "2" and arg != "c":
                        print("\nError: Incorrect input for command. Consult README for more info")
                        # display current ruleset
                        u.check_ruleset(ruleset)
                        arg = input("\nEnter 1 for Tournament Rules, enter 2 for Casual Rules, enter c to cancel: ")
                        
                    else:
                        # input validated
                        argcheck = True
                        
                # if user wants to cancel rule change
                if arg == "c":
                    # display current ruleset
                    u.check_ruleset(ruleset)
                    # display current board
                    u.show_board(board, boardsize)
                    
                else:
                    # change ruleset
                    ruleset = int(arg)
                    # display current ruleset
                    u.check_ruleset(ruleset)
                    # reset game information
                    player, opponent = u.reset_players()
                    black_capture_count, white_capture_count = u.reset_cap_counts()
                    black_win, white_win, draw = u.reset_win_status()
                    # build new board
                    board, move_history = u.build_board(boardsize)
                    u.show_board(board, boardsize)
                    
            # rules command
            elif command[0] == "rules":
                # display current ruleset
                u.check_ruleset(ruleset)
                
            # startgame command
            elif command[0] == "startgame":
                # initialize a player vs. cpu game
                com.startgame_cmd(boardsize, ruleset)
                
            # poseval command
            elif command[0] == "poseval":
                
                # if too many argument
                if len(command) > 1:
                    print("\nError: Command does not require additional input. Consult README for more info")
                    
                else:
                    
                    # if game has ended and board + info not reset
                    if u.check_game_status(black_win, white_win, draw):
                        print("\nThe game has ended. To start a new game, please use the 'reset' command")
                        
                    else:
                        # display evaluation for player-to-move's current position
                        com.current_position_evaluation(player, opponent, board, boardsize, move_history, ruleset)
                        
        user_inp = input("\nPlease enter a command: ")
    
main()