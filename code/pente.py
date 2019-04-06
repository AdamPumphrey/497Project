''' 
Adam Pumphrey, CMPUT 497, ID: 1469319 

Random Pente Player
'''
import sys, random
import utility as u
import commands as com
import heuristic as heur

#def build_board(boardsize):
    #board = [0] * ((boardsize + 1) ** 2)
    #top_border = [3] * (boardsize + 1)
    #board[0:(boardsize + 1)] = top_border
    #count = 1
    #while count <= boardsize:
        #board[((boardsize + 1) * count):(((boardsize + 1) * count) + 1)] = [3]
        #count += 1
    ##board.append(0)
    #board.extend(top_border)
    #board.append(3)
    #move_history = []
    #return board, move_history

#def show_board(board, boardsize):
    #column_list = []
    #for x in range(0, (boardsize)):
        #column_list.append(chr(97 + x))
    #column_str = '   '
    #for i in column_list:
        #column_str += i
        #column_str += '  '
    #print("\nCurrent Board:")
    #print(column_str)
    #count = 1
    #while count < (boardsize + 1):
        #row_list = []
        #for i in board[(((boardsize + 1) * count) + 1):((boardsize + 1) * (count + 1))]:
            #row_list.append(str(i))
        #row_str = ''
        #row_str += str(count)
        #tempcount = 1
        #for i in row_list:
            #if tempcount == 1 and count < 10:
                #row_str += '  '
            #else:
                #row_str += ' '
            #row_str += i
            #row_str += ' '
            #tempcount += 1
        #count += 1
        #print(row_str)
        
#def quit():
    #print("\nShutting down...")
    #sys.exit()
        
#def point_to_boardloc(point, boardsize):
    ## eg) 9 --> c1
    #if point > ((boardsize * 2) + 1):
        #temp_point = point - (boardsize + 1)
        #while temp_point > ((boardsize * 2) + 1):
            #temp_point -= (boardsize + 1)
        #boardloc_0 = chr((temp_point - (boardsize + 2)) + 97)
    #else:
        #boardloc_0 = chr((point - (boardsize + 2)) + 97)
    #boardloc_1 = point//(boardsize + 1)
    #boardloc = boardloc_0 + str(boardloc_1)
    #return boardloc

#def boardloc_to_point(boardloc, boardsize):
    #col = boardloc[0:1]
    #if not col.isalpha():
        #print("\nError: board location syntax incorrect")
        #return "error"
    #col = col.lower()
    #row = boardloc[1:]
    #if not row.isdigit():
        #print("\nError: board location syntax incorrect")
        #return "error"
    #row = int(row)
    #if row > boardsize:
        #print("\nError: board location out of bounds")
        #return "error"
    #cols = "abcdefghijklmnopqrs"
    #if col not in cols:
        #print("\nError: board location out of bounds")
        #return "error"
    #if cols.index(col) > (boardsize - 1):
        #print("\nError: board location out of bounds")
        #return "error"
    #coord_col = (cols.index(col)) + 1
    #point = (((boardsize + 1) * row) + coord_col)
    #return point
    ##coord = (coord_col, row)
    ##return coord

#def check_inp_command(command, commandlist):
    #if not command[0].isalpha():
        #return 1
    #else:
        #command[0] = command[0].lower()
    #if command[0] not in commandlist:
        #return 1
    #else:
        #return 0

#def boardsize_change(new_size):
    #if not new_size.isdigit():
        #print("\nError: Boardsize must be an odd integer between 7 and 19")
        #return 1
    #else:
        #new_boardsize = int(new_size)
        #if new_boardsize < 7 or new_boardsize > 19:
            #print("\nError: Boardsize must be an odd integer between 7 and 19")
            #return 1
        #elif new_boardsize % 2 == 0:
            #print("\nError: Boardsize must be an odd integer between 7 and 19")
            #return 1
        #else:
            #return new_boardsize
        
#def get_empty_spaces(board, boardsize):
    #empty_space_list = []
    #count = (boardsize + 2)
    #for i in board[(boardsize + 2):((boardsize + 1) ** 2)]:
        #if i == 0:
            #space = point_to_boardloc(count, boardsize)
            #empty_space_list.append(space)
        #count += 1
    #return empty_space_list

#def play_move(move, board, boardsize, player, opponent, mode=0):
    #point = boardloc_to_point(move, boardsize)
    #if point == "error":
        #if mode == 0:
            #return False, None, None, None, None
        #else:
            #return False
    ## no need to deep check if move legal
    ## every empty space is a legal move
    ## only need to check for capture
    #if board[point] != 0:
        #print("\nError: Illegal move - position already occupied")
        #if mode == 0:
            #return False, None, None, None, None
        #else:
            #return False
    #board[point] = player
    ## check for capture
    ## capture can only be in form of O-X-X-O as per rules
    #capture_status, capture_list, capture_count = capture_check(board, boardsize, player, opponent, point)
    #if capture_status:
        #for i in capture_list:
            #board[i] = 0
    ## check for win
    ## need to implement calling 4 in a row (tessera) and 3 in a row (tria)
    #if mode == 0:
        #win_status, blocks = check_win(board, boardsize, player, point)
        #return True, capture_status, capture_count, win_status, blocks
    #else:
        #return True

#def check_win(board, boardsize, player, point):
    #win = False
    #blocks = []
    ## vertical check
    #win, block1 = check_win_directions(board, point, win, (boardsize + 1), player)
    #blocks.append(block1)
    #if not win:
        ## horizontal check
        #win, block2 = check_win_directions(board, point, win, 1, player)
        #blocks.append(block2)
        #if not win:
            ## diagonal up/left, down/right check
            #win, block3 = check_win_directions(board, point, win, (boardsize + 2), player)
            #blocks.append(block3)
            #if not win:
                ## diagonal up/right, down/left check
                #win, block4 = check_win_directions(board, point, win, (boardsize), player)
                #blocks.append(block4)
    #return win, blocks

#def check_win_directions(board, point, found, increment, player):
    #count = 1
    #posi_check = True
    #negi_check = True
    #index1 = point
    #index2 = point
    #while not found:
        #if posi_check:
            #index1 += increment
            #if board[index1] == player:
                #count += 1
            #else:
                #posi_check = False
        #if negi_check:
            #index2 -= increment
            #if board[index2] == player:
                #count += 1
            #else:
                #negi_check = False
        #if count >= 5:
            #found = True
            #return found, count
        #if not posi_check and not negi_check:
            #return found, count
        
#def capture_check_direction(board, index, pos_list, status, increment, player, opponent, mode):
    #if board[index] == opponent:
        #pos1 = index
        #if mode == 1:
            ## positive increment
            #index += increment
            #if board[index] == opponent:
                #pos2 = index
                #index += increment
                #if board[index] == player:
                    #status = True
                    #pos_list.extend([pos1, pos2])
        #else:
            #index -= increment
            #if board[index] == opponent:
                #pos2 = index
                #index -= increment
                #if board[index] == player:
                    #status = True
                    #pos_list.extend([pos1, pos2])
    #return status, pos_list

#def capture_check(board, boardsize, player, opponent, point):
    #capture = False
    #capture_list = []
    #count = 0
    ## vertical - check
    #index = point - (boardsize + 1)
    #capture, capture_list = capture_check_direction(board, index, capture_list, capture, (boardsize + 1), player, opponent, 2)
    #if capture:
        #count += 1
    ## vertical + check
    #capture = False
    #index = point + (boardsize + 1)
    #capture, capture_list = capture_check_direction(board, index, capture_list, capture, (boardsize + 1), player, opponent, 1)
    #if capture:
        #count += 1
    #capture = False    
    ## horizontal - check
    #index = point - 1
    #capture, capture_list = capture_check_direction(board, index, capture_list, capture, 1, player, opponent, 2)
    #if capture:
        #count += 1
    #capture = False    
    ## horizontal + check
    #index = point + 1
    #capture, capture_list = capture_check_direction(board, index, capture_list, capture, 1, player, opponent, 1)
    #if capture:
        #count += 1
    #capture = False    
    ## diagonal up/left check
    #index = point + (boardsize + 2)
    #capture, capture_list = capture_check_direction(board, index, capture_list, capture, (boardsize + 2), player, opponent, 1)
    #if capture:
        #count += 1
    #capture = False    
    ## diagonal down/right check
    #index = point - (boardsize + 2)
    #capture, capture_list = capture_check_direction(board, index, capture_list, capture, (boardsize + 2), player, opponent, 2)
    #if capture:
        #count += 1
    #capture = False    
    ## diagonal up/right check
    #index = point + boardsize
    #capture, capture_list = capture_check_direction(board, index, capture_list, capture, boardsize, player, opponent, 1)
    #if capture:
        #count += 1
    #capture = False    
    ## diagonal down/left check
    #index = point - boardsize
    #capture, capture_list = capture_check_direction(board, index, capture_list, capture, boardsize, player, opponent, 2)
    #if capture:
        #count += 1
    #if count > 0:
        #capture = True
    #return capture, capture_list, count

#def check_draw(board, boardsize, status):
    #empty_spaces = get_empty_spaces(board, boardsize)
    #if len(empty_spaces) == 0:
        #status = True
    #return status

#def check_game_status(black_status, white_status, draw_status):
    #if black_status or white_status or draw_status:
        #return True
    #else:
        #return False
    
#def generate_random_move(board, boardsize, player, opponent, move_history, ruleset):
    #if player == 1 and len(move_history) == 0:
        #pos = (len(board) - 1) // 2
        #move = point_to_boardloc(pos, boardsize)
    #elif ruleset == 1 and player == 1 and len(move_history) == 2:
        #available_moves = get_empty_spaces(board, boardsize)
        #center = (len(board) - 1) // 2
        #center = point_to_boardloc(center, boardsize)
        #center_ord = ord(center[0])
        #legal_moves = []
        #for move in available_moves:
            #move_ord = ord(move[0])
            #ord_diff = abs(center_ord - move_ord)
            #if ord_diff < 3:
                #center_coord = int(center[1])
                #move_coord = int(move[1])
                #coord_diff = abs(center_coord - move_coord)
                #if coord_diff >= 3:
                    #legal_moves.append(move)
            #else:
                #legal_moves.append(move)
        #random.shuffle(legal_moves)
        #move = legal_moves[0]
    #else:
        #available_moves = get_empty_spaces(board, boardsize)
        #random.shuffle(available_moves)
        #move = available_moves[0]
    #move_status, capture, capture_count, win, blocks = play_move(move, board, boardsize, player, opponent)
    #return move_status, capture, capture_count, win, move, blocks

#def tournament_rule_check(board, boardsize, player, move_history, move):
    #if player == 1 and len(move_history) == 2:
        #available_moves = get_empty_spaces(board, boardsize)
        #center = (len(board) - 1) // 2
        #center = point_to_boardloc(center, boardsize)
        #center_ord = ord(center[0])
        #legal_moves = []
        #for i in available_moves:
            #move_ord = ord(i[0])
            #ord_diff = abs(center_ord - move_ord)
            #if ord_diff < 3:
                #center_coord = int(center[1])
                #move_coord = int(i[1])
                #coord_diff = abs(center_coord - move_coord)
                #if coord_diff >= 3:
                    #legal_moves.append(i)
            #else:
                #legal_moves.append(i)
        #if move not in legal_moves:
            #print("\nError: Black's second move must be at least 3 spaces away from the center point")
            #return False
        #else:
            #return True
    #else:
        #return True

#def display_move(move_status, player, move, board, boardsize):
    #if move_status:
        #if player == 1:
            #p1 = "black"
            #p2 = "white"
        #else:
            #p1 = "white"
            #p2 = "black"
        #print("")
        #print(p1, "played", move)
        ##show_board(board, boardsize)
    #else:
        #print("Move was not played")

#def display_capture(capture, player, black_capture_count, white_capture_count, capture_count, black_win, white_win, p1, p2):
    #capture_win = False
    #if capture:
        #if player == 1:
            #black_capture_count += capture_count
            #if black_capture_count >= 5:
                #capture_win = True
                #black_win = True
        #else:
            #white_capture_count += capture_count
            #if white_capture_count >= 5:
                #capture_win = True
                #white_win = True
        #if capture_count == 1:
            #print("")
            #print(p1, "made 1 capture")
        #elif capture_count > 1:
            #print("")
            #print(p1, "made", capture_count, "captures")
        #if capture_win:
            #if black_win:
                #print("\nBlack made 5 or more captures - black wins!")
            #elif white_win:
                #print("\nWhite made 5 or more captures - white wins!")
    #return black_capture_count, white_capture_count, black_win, white_win

#def display_win(win, player, black_win, white_win, draw, board, boardsize, move_status, opponent):
    #if win:
        #if player == 1:
            #black_win = True
        #else:
            #white_win = True
        #if black_win:
            #print("\nBlack wins via 5 in a row!")
        #elif white_win:
            #print("\nWhite wins via 5 in a row!")
    #else:
        #draw = check_draw(board, boardsize, draw)
        #if draw:
            #print("\nGame has ended in a draw")
        #else:
            ## game continues, switch internal current-player values
            #if move_status:
                #if player == 1:
                    #player = 2
                    #opponent = 1
                #else:
                    #player = 1
                    #opponent = 2
    #return black_win, white_win, draw, player, opponent

#def boardsize_cmd(command, board, boardsize, move_history):
    #if len(command) != 2:
        #print("\nError: Command requires additional input. Consult README for more info")
        #show_board(board, boardsize)
        #return board, boardsize, move_history, False
    #else:
        #new_boardsize = boardsize_change(command[1])
        #if new_boardsize == 1:
            #return board, boardsize, move_history, False
        #else:
            #boardsize = new_boardsize                
            #board, move_history = build_board(boardsize)
            #show_board(board, boardsize)
            #return board, boardsize, move_history, True

#def reset_win_status():
    #b_win = False
    #w_win = False
    #draw_win = False
    #return b_win, w_win, draw_win

#def reset_players():
    #p1 = 1
    #p2 = 2
    #return p1, p2
        
#def reset_cap_counts():
    #bcc = 0
    #wcc = 0
    #return bcc, wcc

#def genmove_cmd(board, boardsize, player, opponent, b_cap_count, w_cap_count, b_win, w_win, draw, move_history, ruleset):
    #move_status, capture, capture_count, win, move, blocks = generate_random_move(board, boardsize, player, opponent, move_history, ruleset)
    #if player == 1:
        #p1 = "black"
        #p2 = "white"
    #else:
        #p1 = "white"
        #p2 = "black"
    #return format_move(board, boardsize, player, opponent, b_cap_count, w_cap_count, b_win, w_win, draw, move_status, 
                       #capture, capture_count, move, p1, p2, win, move_history, blocks)

#def format_move(board, boardsize, player, opponent, b_cap_count, w_cap_count, b_win, 
                #w_win, draw, move_status, capture, capture_count, move, p1, p2, win, move_history, blocks):
    #display_move(move_status, player, move, board, boardsize)
    #display_blocks(blocks, player)
    #b_cap_count, w_cap_count, b_win, w_win \
        #= display_capture(capture, player, b_cap_count, w_cap_count, capture_count, b_win, w_win, p1, p2)
    #b_win, w_win, draw, player, opponent \
        #= display_win(win, player, b_win, w_win, draw, board, boardsize, move_status, opponent)
    #move_history.append((p1[0], move))
    #show_board(board, boardsize)
    #divider = '-'*25
    #print('\n'+divider)
    #return board, player, opponent, b_cap_count, w_cap_count, b_win, w_win, draw

#def display_blocks(blocks, player):
    #if blocks:
        #if player == 1:
            #p1 = "black"
        #elif player == 2:
            #p1 = "white"
        #for i in blocks:
            #if i == 3:
                #print("\nTria!", p1, "has made 3 in a row!")
            #elif i == 4:
                #print("\nTessera!", p1, "has made 4 in a row!")
    #else:
        #return

#def play_cmd(board, boardsize, player, opponent, b_cap_count, w_cap_count, b_win, w_win, draw, move, move_history):
    #move_status, capture, capture_count, win, blocks = play_move(move, board, boardsize, player, opponent)
    #if player == 1:
        #p1 = "black"
        #p2 = "white"
    #else:
        #p1 = "white"
        #p2 = "black"
    #return format_move(board, boardsize, player, opponent, b_cap_count, w_cap_count, b_win, 
                       #w_win, draw, move_status, capture, capture_count, move, p1, p2, win, move_history, blocks)

#def emptyspaces_cmd(board, boardsize):
    #empty_spaces = get_empty_spaces(board, boardsize)
    #empty_spaces.sort()
    #count = 1
    #print("")
    #for i in empty_spaces:
        #print(i, end =' ')
        #if count == 10:
            #print("")
            #count = 1
        #else:
            #count += 1
    #print("")

#def capturecounts_cmd(b_cap_count, w_cap_count):
    #print("\n5 or more captures are needed for a capture win")
    #print("Black has made", b_cap_count, "capture(s)")
    #print("White has made", w_cap_count, "capture(s)")
    
#def winner_cmd(b_win, w_win, draw):
    #if b_win:
        #print("\nBlack is the winner!")
    #elif w_win:
        #print("\nWhite is the winner!")
    #elif draw:
        #print("\nThe game is a draw")
    #else:
        #print("\nGame is still ongoing") 

#def ptm_cmd(player):
    #if player == 1:
        #print("\nIt is black's turn")
    #else:
        #print("\nIt is white's turn")    
    
#def changeptm_cmd(inp, player, opponent):
    #inp = inp.lower()
    #if inp == "b":
        #player = 1
        #opponent = 2
        #print("\nPlayer to move is now Black")
    #elif inp == "w":
        #player = 2
        #opponent = 1
        #print("\nPlayer to move is now White")
    #else:
        #print("\nError: Incorrect input for command. Consult README for more info") 
    #return player, opponent

#def movehistory_cmd(inp, move_history):
    #if len(inp) > 1:
        #if len(inp) > 2:
            #print("\nError: Incorrect amount of input for command. Consult README for more info.")
        #else:
            #if not inp[1].isalpha():
                #print("\nError: Incorrect input for command. Consult README for more info.")
            #else:
                #if inp[1].lower() == "b":
                    #if len(move_history) < 1:
                        #print("\nBlack has not made a move yet")
                    #else:
                        #count = 1
                        #for move in move_history:
                            #if move[0] == "b":
                                #print(str(count)+".", move[0].upper(), move[1])
                                #count += 1
                #elif inp[1].lower() == "w":
                    #if len(move_history) < 1:
                        #print("\nWhite has not made a move yet")
                    #else:
                        #count = 1
                        #for move in move_history:
                            #if move[0] == "w":
                                #print(str(count)+".", move[0].upper(), move[1])
                                #count += 1
                #else:
                    #print("\nError: Incorrect input for command. Consult README for more info.")
    #else:
        #if len(move_history) < 1:
            #print("\nNo moves have been made yet")
        #else:
            #count = 1
            #for move in move_history:
                #print(str(count)+".", move[0].upper(), move[1])
                #count += 1    
                
#def check_ruleset(ruleset):
    #if ruleset == 1:
        #print("\nThe current ruleset is: Tournament")
    #elif ruleset == 2:
        #print("\nThe current ruleset is: Casual")

#def startgame_cmd(boardsize, ruleset):
    #player, opponent = reset_players()
    #black_capture_count, white_capture_count = reset_cap_counts()
    #black_win, white_win, draw = reset_win_status()
    #board, move_history = build_board(boardsize)
    #show_board(board, boardsize)                
    #arg = input("\nChoose your colour (b for black, w for white, c to cancel): ")
    #argcheck = False
    #while not argcheck:
        #arg = arg.lower()
        #if arg != "b" and arg != "w" and arg != "c":
            #print("\nError: Incorrect input for command. Consult README for more info")
            #arg = input("\nChoose your colour (b for black, w for white, c to cancel): ")
        #else:
            #argcheck = True
    #if arg == "c":
        #print("\nGame has been cancelled")
        #show_board(board, boardsize)
    #elif arg == "b":
        #player = 1
    #elif arg == "w":
        #opponent = 1
    #arg2 = input("\nChoose the player for your opponent. 1 for Random, 2 for Heuristic: ")
    #argcheck2 = False
    #while not argcheck2:
        #if arg2 != "1" and arg2 != "2":
            #print("\nError: Incorrect input for command. Consult README for more info")
            #arg2 = input("\nChose the player for your opponent. 1 for Random, 2 for Heuristic: ")
        #else:
            #argcheck2 = True
    #if opponent == 1:
        #while not black_win and not white_win and not draw:
            #if arg2 == "1":
                #board, player, opponent, black_capture_count, white_capture_count,\
                    #black_win, white_win, draw \
                    #= genmove_cmd(board, boardsize, 1, 2, black_capture_count, 
                                  #white_capture_count, black_win, white_win, draw, move_history, ruleset)
            #elif arg2 == "2":
                #black_move = current_position_evaluation(player, opponent, board, boardsize, move_history, ruleset, 1)
                #board, player, opponent, black_capture_count, white_capture_count,\
                    #black_win, white_win, draw \
                    #= play_cmd(board, boardsize, player, opponent, black_capture_count, 
                               #white_capture_count, black_win, white_win, draw, black_move, move_history)                
            #if black_win or white_win or draw:
                #break
            #else:
                #move_arg = input("\nPlease enter your move, or enter 'quit' to exit: ")
                #move_arg = move_arg.lower()
                #if move_arg == "quit":
                    #print("\nGame cancelled")
                    #break
                #board, player, opponent, black_capture_count, white_capture_count,\
                    #black_win, white_win, draw \
                    #= play_cmd(board, boardsize, 2, 1, black_capture_count, 
                               #white_capture_count, black_win, white_win, draw, move_arg, move_history)
    #elif player == 1:
        #while not black_win and not white_win and not draw:
            #move_arg = input("\nPlease enter your move, or enter 'quit' to exit: ")
            #move_arg = move_arg.lower()
            #if move_arg == "quit":
                #print("\nGame cancelled")
                #break
            #movecheck = False
            #while not movecheck:
                #if len(move_history) == 0:
                    #pos = (len(board) - 1) // 2
                    #center = point_to_boardloc(pos, boardsize)
                    #if move_arg != center:
                        #print("\nError: Black's first move must be the center point")
                        #show_board(board, boardsize)
                        #move_arg = input("\nPlease enter your move, or enter 'quit' to exit: ")
                        #move_arg = move_arg.lower()
                        #if move_arg == "quit":
                            #print("\nGame cancelled")
                            #break
                    #else:
                        #movecheck = True
                        #board, player, opponent, black_capture_count, white_capture_count,\
                            #black_win, white_win, draw \
                            #= play_cmd(board, boardsize, 1, 2, black_capture_count, 
                                       #white_capture_count, black_win, white_win, draw, move_arg, move_history)                             
                #elif ruleset == 1:
                    #check = tournament_rule_check(board, boardsize, player, move_history, move_arg)
                    #if check:
                        #movecheck = True
                        #board, player, opponent, black_capture_count, white_capture_count,\
                            #black_win, white_win, draw \
                            #= play_cmd(board, boardsize, 1, 2, black_capture_count, 
                                       #white_capture_count, black_win, white_win, draw, move_arg, move_history)
                    #else:
                        #show_board(board, boardsize)
                        #move_arg = input("\nPlease enter your move, or enter 'quit' to exit: ")
                        #move_arg = move_arg.lower()
                        #if move_arg == "quit":
                            #print("\nGame cancelled")
                            #break
                #else:
                    #movecheck = True
                    #board, player, opponent, black_capture_count, white_capture_count,\
                        #black_win, white_win, draw \
                        #= play_cmd(board, boardsize, 1, 2, black_capture_count, 
                                   #white_capture_count, black_win, white_win, draw, move_arg, move_history)
            #if black_win or white_win or draw:
                #break
            #else:
                #if arg2 == "1":
                    #board, player, opponent, black_capture_count, white_capture_count,\
                        #black_win, white_win, draw \
                        #= genmove_cmd(board, boardsize, 2, 1, black_capture_count, 
                                      #white_capture_count, black_win, white_win, draw, move_history, ruleset)
                #elif arg2 == "2":
                    #white_move = current_position_evaluation(player, opponent, board, boardsize, move_history, ruleset, 1)
                    #board, player, opponent, black_capture_count, white_capture_count,\
                        #black_win, white_win, draw \
                        #= play_cmd(board, boardsize, player, opponent, black_capture_count, 
                                   #white_capture_count, black_win, white_win, draw, white_move, move_history)                    

#def get_line(board, opponent, player, last_move_index, offset, diag_search=False, mode=0):
    #""" parse row/column/diagonal of board starting from last move played """
    #stone_count1 = 0
    #stone_count2 = 0
    #block_count = 1
    #space_count1 = 0
    #space_count2 = 0
    #p_stone1 = False
    #p_stone2 = False
    #p_stone1_sp = False
    #p_stone2_sp = False
    #play_locations = []
    #end_block1 = 0
    #end_block2 = 0
    #i = 1

    #while space_count1 != 2 or space_count2 != 2:
        #if space_count1 < 2:
            #if not diag_search:
                #pos1 = board[last_move_index + (offset * i)]
            #else:
                #pos1 = board[last_move_index + (offset * i) + i]
            #if pos1 == opponent:
                #if space_count1 < 1:
                    #block_count += 1
                #else:
                    #stone_count1 += 1
            #elif pos1 == player or pos1 == 3:
                #if space_count1 == 1:
                    #p_stone1_sp = True
                    #space_count1 = 2
                #else:
                    #p_stone1 = True
                    #space_count1 = 2
            #else:
                #if end_block1 == 0:
                    #if diag_search:
                        #end_block1 = (last_move_index + (offset * i) + i)
                    #else:
                        #end_block1 = (last_move_index + (offset * i))
                #space_count1 += 1
        #if space_count2 < 2:
            #if not diag_search:
                #pos2 = board[last_move_index + (offset * -i)]
            #else:
                #pos2 = board[last_move_index + (offset * -i) - i]
            #if pos2 == opponent:
                #if space_count2 < 1:
                    #block_count += 1
                #else:
                    #stone_count2 += 1
            #elif pos2 == player or pos2 == 3:
                #if space_count2 == 1:
                    #p_stone2_sp = True
                    #space_count2 = 2
                #else:
                    #p_stone2 = True
                    #space_count2 = 2
            #else:
                #if end_block2 == 0:
                    #if diag_search:
                        #end_block2 = (last_move_index + (offset * -i) - i)
                    #else:
                        #end_block2 = (last_move_index + (offset * -i))
                #space_count2 += 1
        #i += 1
        
    #if ((block_count == 1 and stone_count1 == 2) or (block_count == 2 and stone_count1 == 1)) and stone_count2 == 0:
        #if (board[last_move_index - offset] == 0) and (board[last_move_index + offset] == 0):
            #if not (p_stone1_sp or p_stone2_sp):
                #if diag_search:
                    #if not p_stone2:
                        #play_locations.append(end_block2)
                    #if not p_stone1:
                        #newblock2 = last_move_index + (4 * offset) + 4
                        #play_locations.append(newblock2)
                #else:
                    #if not p_stone2:
                        #play_locations.append(end_block2)
                    #if not p_stone1:
                        #newblock2 = last_move_index + (4 * offset)
                        #play_locations.append(newblock2)
                #if (block_count + stone_count1) > 2:
                    #play_locations.append(end_block1)
                #if (block_count + stone_count2) > 2:
                    #play_locations.append(end_block2)
        #elif (board[last_move_index - offset] == 0) and (board[last_move_index + offset] == opponent):
            #if not (p_stone1_sp or p_stone2_sp):
                #if diag_search:
                    #if not p_stone2:
                        #play_locations.append(end_block2)
                    #if not p_stone1:
                        #newblock2 = last_move_index + (4 * offset) + 4
                        #play_locations.append(newblock2)
                #else:
                    #if not p_stone2:
                        #play_locations.append(end_block2)
                    #if not p_stone1:
                        #newblock2 = last_move_index + (4 * offset)
                        #play_locations.append(newblock2)
                #if (block_count + stone_count1) > 2:
                    #play_locations.append(end_block1)
                #if (block_count + stone_count2) > 2:
                    #play_locations.append(end_block2)                
        #elif (board[last_move_index - offset] == opponent) and (board[last_move_index + offset] == 0):
            #if not (p_stone1_sp or p_stone2_sp):
                #if diag_search:
                    #if not p_stone2:
                        #play_locations.append(end_block2)
                    #if not p_stone1:
                        #newblock2 = last_move_index + (3 * offset) + 3
                        #play_locations.append(newblock2)
                #else:
                    #if not p_stone2:
                        #play_locations.append(end_block2)
                    #if not p_stone1:
                        #newblock2 = last_move_index + (3 * offset)
                        #play_locations.append(newblock2)
                #if (block_count + stone_count1) > 2:
                    #play_locations.append(end_block1)
                #if (block_count + stone_count2) > 2:
                    #play_locations.append(end_block2)                
    #elif ((block_count == 1 and stone_count2 == 2) or (block_count == 2 and stone_count2 == 1)) and stone_count1 == 0:
        #if (board[last_move_index - offset] == 0) and (board[last_move_index + offset] == 0):
            #if not (p_stone1_sp or p_stone2_sp):
                #if diag_search:
                    #if not p_stone1:
                        #play_locations.append(end_block1)
                    #if not p_stone2:
                        #newblock2 = last_move_index - (4 * offset) - 4
                        #play_locations.append(newblock2)            
                #else:
                    #if not p_stone1:
                        #play_locations.append(end_block1)
                    #if not p_stone2:
                        #newblock2 = last_move_index - (4 * offset)
                        #play_locations.append(newblock2)
                #if (block_count + stone_count1) > 2:
                    #play_locations.append(end_block1)
                #if (block_count + stone_count2) > 2:
                    #play_locations.append(end_block2)                
        #elif (board[last_move_index - offset] == 0) and (board[last_move_index + offset] == opponent):
            #if not (p_stone1_sp or p_stone2_sp):
                #if diag_search:
                    #if not p_stone1:
                        #play_locations.append(end_block1)
                    #if not p_stone2:
                        #newblock1 = last_move_index - (3 * offset) - 3
                        #play_locations.append(newblock1)
                #else:
                    #if not p_stone1:
                        #play_locations.append(end_block1)
                    #if not p_stone2:
                        #newblock2 = last_move_index - (3 * offset)
                        #play_locations.append(newblock2)              
                #if (block_count + stone_count1) > 2:
                    #play_locations.append(end_block1)
                #if (block_count + stone_count2) > 2:
                    #play_locations.append(end_block2)                
        #elif (board[last_move_index - offset] == opponent) and (board[last_move_index + offset] == 0):
            #if not (p_stone1_sp or p_stone2_sp):
                #if diag_search:
                    #if not p_stone1:
                        #newblock1 = last_move_index + (4 * offset) + 4
                        #play_locations.append(newblock1)
                    #if not p_stone2:
                        #play_locations.append(end_block2)
                #else:
                    #if not p_stone1:
                        #play_locations.append(end_block1)
                    #if not p_stone2:
                        #newblock1 = last_move_index - (4 * offset)
                        #play_locations.append(newblock1)
                #if (block_count + stone_count1) > 2:
                    #play_locations.append(end_block1)
                #if (block_count + stone_count2) > 2:
                    #play_locations.append(end_block2)                
    
    #if block_count == 3 and (p_stone1_sp or p_stone2_sp) and not (p_stone1_sp and p_stone2_sp):
        #if diag_search:
            #if p_stone1_sp:
                #newblock = end_block2 - offset - 1
                #play_locations.append(newblock)
            #elif p_stone2_sp:
                #newblock = end_block1 + offset + 1
                #play_locations.append(newblock)
        #else:
            #if p_stone1_sp:
                #newblock = end_block2 - offset
                #play_locations.append(newblock)
            #elif p_stone2_sp:
                #newblock = end_block1 + offset
                #play_locations.append(newblock)

    #if (block_count + stone_count1) > 2 and (block_count + stone_count2) > 2:
        #if stone_count1 != 0 and stone_count2 != 0:
            #play_locations.append(end_block1)
            #play_locations.append(end_block2)
        #elif stone_count1 == 0 and stone_count2 == 0:
            #if not p_stone1:
                #play_locations.append(end_block1)
            #if not p_stone2:
                #play_locations.append(end_block2)
        #elif stone_count1 == 0:
            #play_locations.append(end_block2)
        #elif stone_count2 == 0:
            #play_locations.append(end_block1)
    #elif (block_count + stone_count1) > 2:
        #if (block_count + stone_count1) == 4:
            #play_locations.append(end_block1)
    #elif (block_count + stone_count2) > 2:
        #if (block_count + stone_count2) == 4:
            #play_locations.append(end_block2)
            
    #if mode == 0:
        #return blockwin_threat_eval(block_count, stone_count1, p_stone1, stone_count2, p_stone2, p_stone1_sp, p_stone2_sp, play_locations)
    #elif mode == 4:
        #return openfour_threat_eval(block_count, stone_count1, p_stone1, stone_count2, p_stone2, p_stone1_sp, p_stone2_sp, play_locations)
    #elif mode == -4:
        #return blockfour_threat_eval(block_count, stone_count1, p_stone1, stone_count2, p_stone2, p_stone1_sp, p_stone2_sp, play_locations)    
            
#def check_blockwin(board, player, opponent, last_move_index, boardsize, mode=0):
    #if mode == 0:
        #def_moves = []
        #def_moves1 = get_line(board, opponent, player, last_move_index, (boardsize + 1))
        #if def_moves1:
            #for x in def_moves1:
                #if x not in def_moves:
                    #def_moves.append(x)
        #def_moves1 = get_line(board, opponent, player, last_move_index, 1)
        #if def_moves1:
            #for x in def_moves1:
                #if x not in def_moves:
                    #def_moves.append(x)
        #def_moves1 = get_line(board, opponent, player, last_move_index, (boardsize + 1), True)
        #if def_moves1:
            #for x in def_moves1:
                #if x not in def_moves:
                    #def_moves.append(x)
        #def_moves1 = get_line(board, opponent, player, last_move_index, -(boardsize + 1), True)
        #if def_moves1:
            #for x in def_moves1:
                #if x not in def_moves:
                    #def_moves.append(x)
    #elif mode == 4:
        #def_moves = []
        #def_moves1 = get_line(board, opponent, player, last_move_index, (boardsize + 1), False, -4)
        #if def_moves1:
            #for x in def_moves1:
                #if x not in def_moves:
                    #def_moves.append(x)
        #def_moves1 = get_line(board, opponent, player, last_move_index, 1, False, -4)
        #if def_moves1:
            #for x in def_moves1:
                #if x not in def_moves:
                    #def_moves.append(x)
        #def_moves1 = get_line(board, opponent, player, last_move_index, (boardsize + 1), True, -4)
        #if def_moves1:
            #for x in def_moves1:
                #if x not in def_moves:
                    #def_moves.append(x)
        #def_moves1 = get_line(board, opponent, player, last_move_index, -(boardsize + 1), True, -4)
        #if def_moves1:
            #for x in def_moves1:
                #if x not in def_moves:
                    #def_moves.append(x)
    #return def_moves

#def blockfour_threat_eval(block, left_count, playerstone_L, right_count, playerstone_R, playerstone_L_sp, playerstone_R_sp, move_locations):
    #""" evaluate loss-threats from current position """
    #pos_threat_count = 0
    #if block == 2:
        #if left_count == 1 and right_count == 1:
            #if not playerstone_L and not playerstone_R:
                ## ( - o - o o - o -) can create open 4 with either middle move
                ## only need to play one of the middle moves
                #pos_threat_count = 1
        #elif left_count == 1 or right_count == 1:
            #if not playerstone_L and not playerstone_R:
                ## ( - o - o o -) can create open 4 with middle move
                ## must play middle move
                #pos_threat_count = 1
    #elif block == 3:
        #if left_count == 0 and right_count == 0:
            #if not playerstone_L and not playerstone_R and (not playerstone_L_sp or not playerstone_R_sp):
                ## ( - o o o -)
                #pos_threat_count = 1
    #elif block == 1:
        #if left_count == 2 and right_count == 2:
            #if not playerstone_L or not playerstone_R:
                ##( - o o - o - o o x)
                #pos_threat_count = 1
        #elif left_count == 2 or right_count == 2:
            #if not playerstone_L and not playerstone_R:
                ##( x - o o - o - x)
                #pos_threat_count = 1
    #if pos_threat_count >= 1:
        #return move_locations
    #else:
        #return []

#def blockwin_threat_eval(block, left_count, playerstone_L, right_count, playerstone_R, playerstone_L_sp, playerstone_R_sp, move_locations):
    #""" evaluate loss-threats from current position """
    #pos_threat_count = 0
    #if block >= 5:
        #pos_threat_count = 10000
        #return [10000]
    #elif block == 2:
        #if left_count == 4:
            #if playerstone_L:
                ## ( x o o o o - o o -)
                ## must play middle move
                #pos_threat_count = 1
            #else:
                ## ( - o o o o - o o -)
                #pos_threat_count = 2
        #elif right_count == 4:
            #if playerstone_R:
                #pos_threat_count = 1
            #else:
                #pos_threat_count = 2
        #elif left_count in list(range(2, 4)) and right_count in list(range(2, 4)):
            ## ( - o o - o o - o o o -) cannot prevent loss
            #pos_threat_count = 2
        #elif left_count in list(range(2, 4)) or right_count in list(range(2, 4)):
            ## ( - o o - o o -) or ( - o o o - o o -) can win with middle move
            ## must play middle move
            #pos_threat_count = 1

    #elif block == 3:
        #if left_count == 4:
            #if playerstone_L:
                ## ( x o o o o - o o o -)
                ## must play middle move
                #pos_threat_count = 1
            #else:
                ## ( - o o o o - o o o -) or ( - o o o o - o o o x)
                #pos_threat_count = 2
        #elif right_count == 4:
            #if playerstone_R:
                #pos_threat_count = 1
            #else:
                #pos_threat_count = 2
        #elif left_count in list(range(1,4)) and right_count in list(range(1,4)):
            ## ( - o - o o o - o o o -)
            #pos_threat_count = 2
        #elif left_count in list(range(1,4)) or right_count in list(range(1,4)):
            ## ( - o - o o o -) or ( - o o - o o o -) or ( - o o o - o o o -)
            #pos_threat_count = 1

    #elif block == 4:
        #if left_count == 4 or right_count == 4:
            #if playerstone_L and playerstone_R:
                ## ( x o o o o - o o o o x)
                #pos_threat_count = 1
            #else:
                ## ( - o o o o - o o o o x)
                #pos_threat_count = 2
        #elif left_count == 0 and right_count == 0:
            #if not playerstone_L and not playerstone_R:
                ## ( - o o o o -)
                #pos_threat_count = 2
            #elif playerstone_L and not playerstone_R:
                ## ( x o o o o -)
                #pos_threat_count = 1
            #elif playerstone_R and not playerstone_L:
                #pos_threat_count = 1
        #elif left_count in list(range(1,5)) and right_count in list(range(1,5)):
            ## ( - o o o - o o o o - o -)
            #pos_threat_count = 2
        #elif left_count in list(range(1,4)):
            #if playerstone_R:
                ## ( - o o - o o o o x)
                #pos_threat_count = 1
            #else:
                ## ( - o o - o o o o -)
                #pos_threat_count = 2
        #elif right_count in list(range(1,4)):
            #if playerstone_L:
                #pos_threat_count = 1
            #else:
                #pos_threat_count = 2

    #elif block == 1:
        #if left_count in list(range(3,5)) and right_count in list(range(3,5)):
            ##( x o o o o - o - o o o x)
            #pos_threat_count = 2
        #elif left_count == 4:
            #if not playerstone_L:
                ##(- o o o o - o)
                #pos_threat_count = 2
        #elif right_count == 4:
            #if not playerstone_R:
                #pos_threat_count = 2
        #elif left_count == 3 or right_count == 3:
            ##( - o - o o o x)
            #pos_threat_count = 1

    #if pos_threat_count >= 1:
        #return move_locations
    #else:
        #return []
    
#def openfour_threat_eval(block, left_count, playerstone_L, right_count, playerstone_R, playerstone_L_sp, playerstone_R_sp, move_locations):
    #""" evaluate loss-threats from current position """
    #if block == 4:
        #if left_count == 0 and right_count == 0:
            #if not playerstone_L and not playerstone_R:
                ## ( - o o o o -)
                #return [4]
    #else:
        #return []

#def parse_move_history(player, move_history):
    #player_previous_moves = []
    #i = 0
    #found = False
    #if player == 1:
        #match = 'b'
    #elif player == 2:
        #match = 'w'
    #while i < len(move_history):
        #player_last_move = move_history[i]
        #if player_last_move[0] == match:
            #player_previous_moves.append(player_last_move[1])
            #i += 1
        #else:
            #i += 1
    #return player_previous_moves

#def get_win_moves(previous_moves, board, player, opponent, boardsize, mode=0):
    #moves_analyzed = []
    #moves = []
    #for m in reversed(previous_moves):
        #tempmove_index = boardloc_to_point(m, boardsize)
        #templist = []
        #emptycount = 8
        #if board[tempmove_index + (boardsize + 1)] == 0 and tempmove_index + (boardsize + 1) not in moves_analyzed:
            #templist.append(tempmove_index + (boardsize + 1))
        #elif board[tempmove_index + (boardsize + 1)] != 0:
            #emptycount -= 1
        #if board[tempmove_index - (boardsize + 1)] == 0 and tempmove_index - (boardsize + 1) not in moves_analyzed:
            #templist.append(tempmove_index - (boardsize + 1))
        #elif board[tempmove_index - (boardsize + 1)] != 0:
            #emptycount -= 1
        #if board[tempmove_index + 1] == 0 and tempmove_index + 1 not in moves_analyzed:
            #templist.append(tempmove_index + 1)
        #elif board[tempmove_index + 1] != 0:
            #emptycount -= 1
        #if board[tempmove_index - 1] == 0 and tempmove_index - 1 not in moves_analyzed:
            #templist.append(tempmove_index - 1)
        #elif board[tempmove_index - 1] != 0:
            #emptycount -= 1
        #if board[tempmove_index + (boardsize + 1) + 1] == 0 and tempmove_index + (boardsize + 1) + 1 not in moves_analyzed:
            #templist.append(tempmove_index + (boardsize + 1) + 1)
        #elif board[tempmove_index + (boardsize + 1) + 1] != 0:
            #emptycount -= 1
        #if board[tempmove_index - (boardsize + 1) - 1] == 0 and tempmove_index - (boardsize + 1) - 1 not in moves_analyzed:
            #templist.append(tempmove_index - (boardsize + 1) - 1)
        #elif board[tempmove_index - (boardsize + 1) - 1] != 0:
            #emptycount -= 1
        #if board[tempmove_index + (boardsize + 1) - 1] == 0 and tempmove_index + (boardsize + 1) - 1 not in moves_analyzed:
            #templist.append(tempmove_index + (boardsize + 1) - 1)
        #elif board[tempmove_index + (boardsize + 1) - 1] != 0:
            #emptycount -= 1
        #if board[tempmove_index - (boardsize + 1) + 1] == 0 and tempmove_index - (boardsize + 1) + 1 not in moves_analyzed:
            #templist.append(tempmove_index - (boardsize + 1) + 1)
        #elif board[tempmove_index - (boardsize + 1) + 1] != 0:
            #emptycount -= 1
        #if emptycount == 0:
            ##templist = get_empty_spaces(board, boardsize)
            #pass
        #else:
            #for pos in templist:
                #tempboard = board.copy()
                #move = point_to_boardloc(pos, boardsize)
                #move_status = play_move(move, tempboard, boardsize, player, opponent, 1)
                #if mode == 0:
                    #moves1 = get_line(tempboard, player, opponent, pos, (boardsize + 1))
                    #if moves1:
                        #if moves1[0] == 10000:
                            ## move caused a win
                            #if pos not in moves:
                                #moves.append(pos)
                    #moves1 = get_line(tempboard, player, opponent, pos, 1)
                    #if moves1:
                        #if moves1[0] == 10000:
                            #if pos not in moves:
                                #moves.append(pos)
                    #moves1 = get_line(tempboard, player, opponent, pos, (boardsize + 1), True)
                    #if moves1:
                        #if moves1[0] == 10000:
                            #if pos not in moves:
                                #moves.append(pos)
                    #moves1 = get_line(tempboard, player, opponent, pos, -(boardsize + 1), True)
                    #if moves1:
                        #if moves1[0] == 10000:
                            #if pos not in moves:
                                #moves.append(pos)
                #elif mode == 4:
                    #moves1 = get_line(tempboard, player, opponent, pos, (boardsize + 1), False, 4)
                    #if moves1:
                        #if moves1[0] == 4:
                            ## move caused an open four
                            #if pos not in moves:
                                #moves.append(pos)
                    #moves1 = get_line(tempboard, player, opponent, pos, 1, False, 4)
                    #if moves1:
                        #if moves1[0] == 4:
                            #if pos not in moves:
                                #moves.append(pos)
                    #moves1 = get_line(tempboard, player, opponent, pos, (boardsize + 1), True, 4)
                    #if moves1:
                        #if moves1[0] == 4:
                            #if pos not in moves:
                                #moves.append(pos)
                    #moves1 = get_line(tempboard, player, opponent, pos, -(boardsize + 1), True, 4)
                    #if moves1:
                        #if moves1[0] == 4:
                            #if pos not in moves:
                                #moves.append(pos)
                #moves_analyzed.append(pos)
    #return moves

#def win_heuristic(player_move_history, board, player, opponent, boardsize, mode=0):
    #if mode == 4:
        #win_moves = get_win_moves(player_move_history, board, player, opponent, boardsize, 4)
    #else:
        #win_moves = get_win_moves(player_move_history, board, player, opponent, boardsize)
    #if win_moves:
        #count = 0
        #while count < len(win_moves):
            #move = int(win_moves[count])
            #move = point_to_boardloc(move, boardsize)
            #win_moves[count] = move
            #count += 1
        #return win_moves
    #else:
        #return []

#def def_heuristic(board, player, opponent, last_move_index, boardsize, mode=0):
    #if mode == 4:
        #def_moves = check_blockwin(board, player, opponent, last_move_index, boardsize, 4)
    #else:
        #def_moves = check_blockwin(board, player, opponent, last_move_index, boardsize)
    #if def_moves:
        #count = 0
        #while count < len(def_moves):
            #move = int(def_moves[count])
            #move = point_to_boardloc(move, boardsize)
            #def_moves[count] = move
            #count += 1    
        #return def_moves
    #else:
        #return []
    
#def current_position_evaluation(player, opponent, board, boardsize, move_history, ruleset, mode=0):
    #if player == 1:
        #playercolour = 'black'
    #elif player == 2:
        #playercolour = 'white'
    #if len(move_history) == 0:
        #pos = (len(board) - 1) // 2
        #move = point_to_boardloc(pos, boardsize)
        #if mode == 0:
            #print("\nblack must play", move, "to start the game")
        #else:
            #return move
    #elif player == 1 and ruleset == 1 and len(move_history) == 2:
        #available_moves = get_empty_spaces(board, boardsize)
        #center = (len(board) - 1) // 2
        #center = point_to_boardloc(center, boardsize)
        #center_ord = ord(center[0])
        #legal_moves = []
        #for move in available_moves:
            #move_ord = ord(move[0])
            #ord_diff = abs(center_ord - move_ord)
            #if ord_diff < 3:
                #center_coord = int(center[1])
                #move_coord = int(move[1])
                #coord_diff = abs(center_coord - move_coord)
                #if coord_diff >= 3:
                    #legal_moves.append(move)
            #else:
                #legal_moves.append(move)
        #if mode == 0:
            #count = 1
            #print('\nblack must play in one of the following spaces as per tournament rules:')
            #for i in legal_moves:
                #print(i, end =' ')
                #if count == 10:
                    #print('')
                    #count = 1
                #else:
                    #count += 1
            #print('')            
        #else:
            #random.shuffle(legal_moves)
            #move = legal_moves[0]
            #return move
    #else:
        #last_move = move_history[-1]
        #last_move_index = boardloc_to_point(last_move[1], boardsize)
        #player_move_history = parse_move_history(player, move_history)
        #win_moves = win_heuristic(player_move_history, board, player, opponent, boardsize)
        #if win_moves:
            #if mode == 0:
                #print("\nwinning moves for", playercolour, "are: ", end='')
                #for move in win_moves:
                    #move = move + ' '
                    #print(move, end='')
                #print('')
            #else:
                #random.shuffle(win_moves)
                #move = win_moves[0]
                #return move
        #else:
            #def_moves = def_heuristic(board, player, opponent, last_move_index, boardsize)
            #if def_moves:
                #if mode == 0:
                    #if len(def_moves) > 1:
                        #print("\na", playercolour, "loss is inevitable. blocking moves would be: ", end='')
                    #else:
                        #print("\nmove that will prevent a", playercolour, "loss is: ", end='')
                    #for move in def_moves:
                        #move = move + ' '
                        #print(move, end='')
                    #print('')
                #else:
                    #random.shuffle(def_moves)
                    #move = def_moves[0]
                    #return move
            #else:
                #four_moves = win_heuristic(player_move_history, board, player, opponent, boardsize, 4)
                #if four_moves:
                    #if mode == 0:
                        #print('')
                        #print(playercolour, "can make an open four with: ", end='')
                        #for move in four_moves:
                            #move = move + ' '
                            #print(move, end='')
                        #print('')
                    #else:
                        #random.shuffle(four_moves)
                        #move = four_moves[0]
                        #return move
                #else:
                    #def_moves = def_heuristic(board, player, opponent, last_move_index, boardsize, 4)
                    #if def_moves:
                        #if mode == 0:
                            #print('')
                            #print(playercolour, "can block an open four with: ", end='')
                            #for move in def_moves:
                                #move = move + ' '
                                #print(move, end='')
                            #print('')
                        #else:
                            #random.shuffle(def_moves)
                            #move = def_moves[0]
                            #return move
                    #else:
                        #if mode == 0:
                            #print("\nthere are no specific moves to play at this time")
                        #else:
                            #legal_moves = get_empty_spaces(board, boardsize)
                            #random.shuffle(legal_moves)
                            #move = legal_moves[0]
                            #return move

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
        if check_result == 1:
            error = True
            print("\nError: Command does not exist. Use 'commands' to list existing commands")
        elif check_result == 0:
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
                    if u.check_game_status(black_win, white_win, draw):
                        print("\nThe game has ended. To start a new game, please use the 'reset' command") 
                    else:
                        player, opponent = u.reset_players
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
