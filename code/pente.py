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
    board = [0] * ((boardsize + 1) ** 2)
    
    # build board
    board, move_history = u.build_board(boardsize)
    
    # show board
    print("Pente random player, by Adam Pumphrey")
    print("\nBlack = 1")
    print("White = 2")
    print("Empty space = 0")
    u.show_board(board, boardsize)
    
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
        check_result = u.check_inp_command(command, commandlist)
        if not check_result:
            print("\nError: Command does not exist. Use 'commands' to list existing commands")
        elif check_result:
            # execute command
            if command[0] == "boardsize":
                board, boardsize, move_history, success = com.boardsize_cmd(command, board, boardsize, move_history)
                if success:
                    player, opponent = u.reset_players()
                    black_capture_count, white_capture_count = u.reset_cap_counts()
                    black_win, white_win, draw = u.reset_win_status()                        
            elif command[0] == "reset":
                if len(command) > 1:
                    print("\nError: Command does not require additional input. Consult README for more info")
                else:
                    player, opponent = u.reset_players()
                    black_capture_count, white_capture_count = u.reset_cap_counts()
                    black_win, white_win, draw = u.reset_win_status()
                    board, move_history = u.build_board(boardsize)
                    u.show_board(board, boardsize)
            elif command[0] == "quit":
                if len(command) > 1:
                    print("\nError: Command does not require additional input. Consult README for more info")
                else:                
                    u.quit()
            elif command[0] == "genmove":
                if len(command) > 1:
                    print("\nError: Command does not require additional input. Consult README for more info")
                elif u.check_game_status(black_win, white_win, draw):
                    print("\nGame is over. To start a new game, please use the 'reset' command")
                else:
                    board, player, opponent, black_capture_count, white_capture_count,\
                    black_win, white_win, draw \
                    = com.genmove_cmd(board, boardsize, player, opponent, black_capture_count, 
                                  white_capture_count, black_win, white_win, draw, move_history, ruleset)                  
            elif command[0] == "play":
                if len(command) < 2:
                    print("\nError: Command requires additional input. Consult README for more info")
                elif len(command) > 2:
                    print("\nError: Incorrect amount of input for command. Consult README for more info")
                elif u.check_game_status(black_win, white_win, draw):
                    print("\nGame is over. To start a new game, please use the 'reset' command")
                else:
                    if player == 1 and len(move_history) == 0:
                        pos = (len(board) - 1) // 2
                        center = u.point_to_boardloc(pos, boardsize)
                        if command[1] != center:
                            print("\nError: Black's first move must be the center point")
                            u.show_board(board, boardsize)
                        else:
                            board, player, opponent, black_capture_count, white_capture_count,\
                                black_win, white_win, draw \
                                = com.play_cmd(board, boardsize, player, opponent, black_capture_count, 
                                           white_capture_count, black_win, white_win, draw, command[1], move_history)                             
                    elif ruleset == 1:
                        check = u.tournament_rule_check(board, boardsize, player, move_history, command[1])
                        if check:
                            board, player, opponent, black_capture_count, white_capture_count,\
                                black_win, white_win, draw \
                                = com.play_cmd(board, boardsize, player, opponent, black_capture_count, 
                                           white_capture_count, black_win, white_win, draw, command[1], move_history)
                        else:
                            u.show_board(board, boardsize)
                    else:
                        board, player, opponent, black_capture_count, white_capture_count,\
                            black_win, white_win, draw \
                            = com.play_cmd(board, boardsize, player, opponent, black_capture_count, 
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
                    com.emptyspaces_cmd(board, boardsize)
            elif command[0] == "ptm":
                if len(command) > 1:
                    print("\nError: Command does not require additional input. Consult README for more info")
                else:
                    if u.check_game_status(black_win, white_win, draw):
                        print("\nThe game has ended. To start a new game, please use the 'reset' command")
                    else: 
                        com.ptm_cmd(player)
            elif command[0] == "changeptm":
                if len(command) < 2:
                    print("\nError: Command requires additional input. Consult README for more info")
                elif len(command) > 2:
                    print("\nError: Incorrect amount of input for command. Consult README for more info")                
                elif u.check_game_status(black_win, white_win, draw):
                    print("\nThe game has ended. To start a new game, please use the 'reset' command")
                else:
                    inp = command[1]
                    if not inp.isalpha():
                        print("\nError: Incorrect input for command. Consult README for more info")
                    else:
                        player, opponent = com.changeptm_cmd(inp, player, opponent)
            elif command[0] == "winner":
                if len(command) > 1:
                    print("\nError: Command does not require additional input. Consult README for more info")
                else:
                    com.winner_cmd(black_win, white_win, draw)
            elif command[0] == "showboard":
                if len(command) > 1:
                    print("\nError: Command does not require additional input. Consult README for more info")
                else:
                    u.show_board(board, boardsize)
            elif command[0] == "capturecounts":
                if len(command) > 1:
                    print("\nError: Command does not require additional input. Consult README for more info")
                else:
                    com.capturecounts_cmd(black_capture_count, white_capture_count)
            elif command[0] == "playcpugame":
                if len(command) > 1:
                    print("\nError: Command does not require additional input. Consult README for more info")
                else:
                    player, opponent = u.reset_players()
                    black_capture_count, white_capture_count = u.reset_cap_counts()
                    black_win, white_win, draw = u.reset_win_status()
                    board, move_history = u.build_board(boardsize)
                    u.show_board(board, boardsize)
                    inp1 = input("Choose the player for black. 1 for Random, 2 for Heuristic: ")
                    inp1check = False
                    while not inp1check:
                        if inp1 != "1" and inp1 != "2":
                            print("\nError: Incorrect input for command. Consult README for more info")
                            inp1 = input("Choose the player for black. 1 for Random, 2 for Heuristic: ")
                        else:
                            inp1check = True
                    inp2 = input("Choose the player for white. 1 for Random, 2 for Heuristic: ")
                    inp2check = False
                    while not inp2check:
                        if inp2 != "1" and inp2 != "2":
                            print("\nError: Incorrect input for command. Consult README for more info")
                            inp2 = input("Choose the player for white. 1 for Random, 2 for Heuristic: ")
                        else:
                            inp2check = True
                    if inp1 == "1" and inp2 == "1":
                        while not black_win and not white_win and not draw:
                            board, player, opponent, black_capture_count, white_capture_count,\
                                black_win, white_win, draw \
                                = com.genmove_cmd(board, boardsize, player, opponent, black_capture_count, 
                                      white_capture_count, black_win, white_win, draw, move_history, ruleset)
                    elif inp1 == "2" and inp2 == "1":
                        while not black_win and not white_win and not draw:
                            black_move = com.current_position_evaluation(player, opponent, board, boardsize, move_history, ruleset, 1)
                            board, player, opponent, black_capture_count, white_capture_count,\
                                black_win, white_win, draw \
                                = com.play_cmd(board, boardsize, player, opponent, black_capture_count, 
                                           white_capture_count, black_win, white_win, draw, black_move, move_history)
                            if not black_win and not white_win and not draw:
                                board, player, opponent, black_capture_count, white_capture_count,\
                                    black_win, white_win, draw \
                                    = com.genmove_cmd(board, boardsize, player, opponent, black_capture_count, 
                                          white_capture_count, black_win, white_win, draw, move_history, ruleset)
                    elif inp1 == "1" and inp2 == "2":
                        while not black_win and not white_win and not draw:
                            board, player, opponent, black_capture_count, white_capture_count,\
                                black_win, white_win, draw \
                                = com.genmove_cmd(board, boardsize, player, opponent, black_capture_count, 
                                      white_capture_count, black_win, white_win, draw, move_history, ruleset)
                            if not black_win and not white_win and not draw:
                                white_move = com.current_position_evaluation(player, opponent, board, boardsize, move_history, ruleset, 1)
                                board, player, opponent, black_capture_count, white_capture_count,\
                                    black_win, white_win, draw \
                                    = com.play_cmd(board, boardsize, player, opponent, black_capture_count, 
                                               white_capture_count, black_win, white_win, draw, white_move, move_history)
                    elif inp1 == "2" and inp2 == "2":
                        while not black_win and not white_win and not draw:
                            black_move = com.current_position_evaluation(player, opponent, board, boardsize, move_history, ruleset, 1)
                            board, player, opponent, black_capture_count, white_capture_count,\
                                black_win, white_win, draw \
                                = com.play_cmd(board, boardsize, player, opponent, black_capture_count, 
                                           white_capture_count, black_win, white_win, draw, black_move, move_history)   
                            if not black_win and not white_win and not draw:
                                white_move = com.current_position_evaluation(player, opponent, board, boardsize, move_history, ruleset, 1)
                                board, player, opponent, black_capture_count, white_capture_count,\
                                    black_win, white_win, draw \
                                    = com.play_cmd(board, boardsize, player, opponent, black_capture_count, 
                                               white_capture_count, black_win, white_win, draw, white_move, move_history)                                
            elif command[0] == "movehistory":
                com.movehistory_cmd(command, move_history)
            elif command[0] == "changerules":
                arg = input("\nEnter 1 for Tournament Rules, enter 2 for Casual Rules, enter c to cancel: ")
                argcheck = False
                while not argcheck:
                    if arg != "1" and arg != "2" and arg != "c":
                        print("\nError: Incorrect input for command. Consult README for more info")
                        u.check_ruleset(ruleset)
                        arg = input("\nEnter 1 for Tournament Rules, enter 2 for Casual Rules, enter c to cancel: ")
                    else:
                        argcheck = True
                if arg == "c":
                    u.check_ruleset(ruleset)
                    u.show_board(board, boardsize)
                else:
                    ruleset = int(arg)
                    u.check_ruleset(ruleset)
                    player, opponent = u.reset_players()
                    black_capture_count, white_capture_count = u.reset_cap_counts()
                    black_win, white_win, draw = u.reset_win_status()
                    board, move_history = u.build_board(boardsize)
                    u.show_board(board, boardsize)
            elif command[0] == "rules":
                u.check_ruleset(ruleset)
            elif command[0] == "startgame":
                com.startgame_cmd(boardsize, ruleset)
            elif command[0] == "poseval":
                if len(command) > 1:
                    print("\nError: Command does not require additional input. Consult README for more info")
                else:
                    if u.check_game_status(black_win, white_win, draw):
                        print("\nThe game has ended. To start a new game, please use the 'reset' command")
                    else:
                        com.current_position_evaluation(player, opponent, board, boardsize, move_history, ruleset)
        user_inp = input("\nPlease enter a command: ")
    
main()