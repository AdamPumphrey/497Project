import random, sys

def build_board(boardsize):
    '''
    eg) for a 3x3 board, internal structure would be:
    
    3 3 3 3 - top border
    3 0 0 0 - first row
    3 0 0 0 - second row
    3 0 0 0 - third row
    3 3 3 3 - bottom border
    
    '''
    # create empty board spaces
    board = [0] * ((boardsize + 1) ** 2)
    # create top border of board
    top_border = [3] * (boardsize + 1)
    # insert top border
    board[0:(boardsize + 1)] = top_border
    
    # for each row
    count = 1
    while count <= boardsize:
        # insert row starter
        board[((boardsize + 1) * count):(((boardsize + 1) * count) + 1)] = [3]
        count += 1
        
    # add bottom border
    board.extend(top_border)
    board.append(3)
    # initialize move history
    move_history = []
    return board, move_history

def show_board(board, boardsize):
    
    column_list = []
    # for each column
    for x in range(0, (boardsize)):
        # get column letters
        column_list.append(chr(97 + x))
    
    # create column letter string
    column_str = '   '
    for i in column_list:
        column_str += i
        column_str += '  '
    
    # display column letters
    print("\nCurrent Board:")
    print(column_str)
    
    count = 1
    # for each row
    while count < (boardsize + 1):
        row_list = []
        
        # for each space in row
        for i in board[(((boardsize + 1) * count) + 1):((boardsize + 1) * (count + 1))]:
            # add space to current row's string
            row_list.append(str(i))
        
        row_str = ''
        row_str += str(count)
        
        # for each space in row
        tempcount = 1
        for i in row_list:
            
            # formatting for readability
            if tempcount == 1 and count < 10:
                row_str += '  '
            else:
                row_str += ' '
            row_str += i
            row_str += ' '
            tempcount += 1
        count += 1
        # display current formatted row
        print(row_str)

def point_to_boardloc(point, boardsize):
    # eg) 9 --> c1
    # if point is not on first row of board
    if point > ((boardsize * 2) + 1):
        # move point up a row until point is in first row of board
        temp_point = point - (boardsize + 1)
        while temp_point > ((boardsize * 2) + 1):
            temp_point -= (boardsize + 1)
            
        # get column letter of point
        boardloc_0 = chr((temp_point - (boardsize + 2)) + 97)
    else:
        # get column letter of point
        boardloc_0 = chr((point - (boardsize + 2)) + 97)
    # get row number of point
    boardloc_1 = point//(boardsize + 1)
    # combine column letter and row number
    boardloc = boardloc_0 + str(boardloc_1)
    return boardloc

def boardloc_to_point(boardloc, boardsize):
    '''
    the error returns below would work better as exceptions.
    
    will not be changing them at this moment
    '''
    col = boardloc[0:1]
    
    # if column letter entered is not a letter
    if not col.isalpha():
        # error
        print("\nError: board location syntax incorrect")
        return "error"
    
    col = col.lower()
    row = boardloc[1:]
    # if row number entered is not a number
    if not row.isdigit():
        # error
        print("\nError: board location syntax incorrect")
        return "error"
    
    row = int(row)    
    # if row number outside of current board
    if row > boardsize or row == 0:
        # error
        print("\nError: board location out of bounds")
        return "error"
    
    cols = "abcdefghijklmnopqrs"
    # if column letter not in range of 1-19
    if col not in cols:
        # error
        print("\nError: board location out of bounds")
        return "error"
    
    # if column letter outside of current board
    if cols.index(col) > (boardsize - 1):
        # error
        print("\nError: board location out of bounds")
        return "error"
    
    # get column number
    coord_col = (cols.index(col)) + 1
    # get board point index
    point = (((boardsize + 1) * row) + coord_col)
    return point

def check_inp_command(command, commandlist):
    
    # if command entered contains anything other than letters
    if not command[0].isalpha():
        return False
    
    else:
        command[0] = command[0].lower()
    
    # if command entered does not exist
    if command[0] not in commandlist:
        return False
    else:
        return True

def boardsize_change(new_size):
    
    # if boardsize entered is not a number
    if not new_size.isdigit():
        print("\nError: Boardsize must be an odd integer between 7 and 19")
        return 1
    
    else:
        new_boardsize = int(new_size)
        
        # if boardsize entered not in correct range
        if new_boardsize < 7 or new_boardsize > 19:
            print("\nError: Boardsize must be an odd integer between 7 and 19")
            return 1
        
        # if boardsize entered is even
        elif new_boardsize % 2 == 0:
            print("\nError: Boardsize must be an odd integer between 7 and 19")
            return 1
        
        else:
            return new_boardsize
        
def get_empty_spaces(board, boardsize):
    empty_space_list = []
    
    # for each space on the board
    count = (boardsize + 2)
    for i in board[(boardsize + 2):((boardsize + 1) ** 2)]:
        
        # if space is empty
        if i == 0:
            # get board location
            space = point_to_boardloc(count, boardsize)
            # add to list
            empty_space_list.append(space)
            
        count += 1
        
    return empty_space_list

def check_win(board, boardsize, player, point):
    win = False
    blocks = []
    # vertical win check
    win, block1 = check_win_directions(board, point, win, (boardsize + 1), player)
    # add vertical block size to block list
    blocks.append(block1)
    
    # if a vertical win is not found
    if not win:
        # horizontal win check
        win, block2 = check_win_directions(board, point, win, 1, player)
        # add horizontal block size to block list
        blocks.append(block2)
        
        # if a horizontal win is not found
        if not win:
            # diagonal up/left, down/right win check
            win, block3 = check_win_directions(board, point, win, (boardsize + 2), player)
            # add first diagonal block size to block list
            blocks.append(block3)
            
            # if a first diagonal win is not found
            if not win:
                # diagonal up/right, down/left win check
                win, block4 = check_win_directions(board, point, win, (boardsize), player)
                # add second diagonal block size to block list
                blocks.append(block4)
                
    return win, blocks

def check_win_directions(board, point, found, increment, player):
    '''
    similar to heuristic.get_line function,
    less comprehensive and specific
    
    function moves forward and backward (by one increment) 
    from initial stone each loop, unless the block of stones in 
    said direction has ended.
    
    eg) for block | - O O O O O O - |
                      1 2 3 4 5 6
        if the search starts at stone 4, it will move forward twice,
        and move backwards three times, obtaining a block size of 6
        
    returns true if a block of size 5 or greater has been found,
    signifying a win
    '''
    count = 1
    posi_check = True
    negi_check = True
    index1 = point
    index2 = point
    
    # run until return
    while not found:
        
        # if forward check still valid
        if posi_check:
            # move forward by one increment 
            index1 += increment
            
            # if current board space contains player's stone
            if board[index1] == player:
                count += 1
                
            # if block has ended
            else:
                # forward check invalid
                posi_check = False
        
        # if backward check still valid
        if negi_check:
            # move backward by one increment
            index2 -= increment
            
            # if current board space contains player's stone
            if board[index2] == player:
                count += 1
            
            # if block has ended
            else:
                # backward check invalid
                negi_check = False
                
        # if block size 5 or greater
        if count >= 5:
            # a win has occurred
            found = True
            return found, count
        
        # if the entire block has been counted and no win present
        if not posi_check and not negi_check:
            return found, count
        
def capture_check_direction(board, index, pos_list, status, increment, player, opponent, mode):
    '''
    initial position is the stone beside the stone
    that the current player has last played.
    
    checks specifically for capture condition
    
    eg) | O X X O |
          1 2 3 4
    say the current player just played stone 1 and the function is called
    in forward mode.
    the function would then start at stone 2, iterate over stones 3 and 4, 
    and detect the capture of stones 2 and 3.
    
    returns True and the list of positions captured if a capture occurred
    '''
    
    # if current board space contains opponent's stone
    if board[index] == opponent:
        # save stone location
        pos1 = index
        
        # forward mode
        if mode == 1:
            # move forward one increment
            index += increment
            
            # if current board space contains opponent's stone
            if board[index] == opponent:
                # save stone location
                pos2 = index
                # move forward one increment
                index += increment
                
                # if current board space contains player's stone
                if board[index] == player:
                    # capture has occurred
                    status = True
                    # add opponent stone locations to list
                    pos_list.extend([pos1, pos2])
        
        # backward mode
        else:
            # move backward one increment
            index -= increment
            
            # if current board space contains opponent's stone
            if board[index] == opponent:
                # save stone location
                pos2 = index
                # move backward one increment
                index -= increment
                
                # if current board space contains player's stone
                if board[index] == player:
                    # capture has occurred
                    status = True
                    # add opponent stone locations to list
                    pos_list.extend([pos1, pos2])
                    
    return status, pos_list

def capture_check(board, boardsize, player, opponent, point):
    capture = False
    capture_list = []
    count = 0
    
    # vertical backwards check
    index = point - (boardsize + 1)
    capture, capture_list = capture_check_direction(board, index, capture_list, capture, (boardsize + 1), player, opponent, 2)
    
    # if capture detected
    if capture:
        # capture count + 1
        count += 1
    
    # reset capture status
    capture = False
    # vertical forward check
    index = point + (boardsize + 1)
    capture, capture_list = capture_check_direction(board, index, capture_list, capture, (boardsize + 1), player, opponent, 1)
    
    # if capture detected
    if capture:
        # capture count + 1
        count += 1
        
    # reset capture status
    capture = False   
    
    # horizontal backwards check
    index = point - 1
    capture, capture_list = capture_check_direction(board, index, capture_list, capture, 1, player, opponent, 2)
    if capture:
        count += 1
    capture = False    
    
    # horizontal forwards check
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
    
    # if a capture has occurred after all direction checks
    if count > 0:
        # overall capture status True
        capture = True
        
    return capture, capture_list, count

def check_draw(board, boardsize, status):
    # get all remaining empty spaces on board
    empty_spaces = get_empty_spaces(board, boardsize)
    
    # if no empty spaces remaining
    if len(empty_spaces) == 0:
        # draw has occurred
        status = True
        
    return status

def check_game_status(black_status, white_status, draw_status):
    
    # if game is over
    if black_status or white_status or draw_status:
        return True
    
    # game is ongoing
    else:
        return False
    
def generate_random_move(board, boardsize, player, opponent, move_history, ruleset):
    
    # if first move of the game
    # black always goes first and must play center point
    if player == 1 and len(move_history) == 0:
        # get center point
        pos = (len(board) - 1) // 2
        move = point_to_boardloc(pos, boardsize)
    
    # if black's second move and tournament rules in use
    elif ruleset == 1 and player == 1 and len(move_history) == 2:
        # get all remaining empty spaces on board
        available_moves = get_empty_spaces(board, boardsize)
        # get center point
        center = (len(board) - 1) // 2
        center = point_to_boardloc(center, boardsize)
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
                
        # randomly pick legal move
        random.shuffle(legal_moves)
        move = legal_moves[0]
        
    else:
        # get all remaining empty spaces on board
        available_moves = get_empty_spaces(board, boardsize)
        # randomly pick legal move
        random.shuffle(available_moves)
        move = available_moves[0]
    # play specified move
    move_status, capture, capture_count, win, blocks = play_move(move, board, boardsize, player, opponent)
    return move_status, capture, capture_count, win, move, blocks

def tournament_rule_check(board, boardsize, player, move_history, move):
    
    # if black's second move
    if player == 1 and len(move_history) == 2:
        # get all remaining empty spaces on board
        available_moves = get_empty_spaces(board, boardsize)
        # get center point
        center = (len(board) - 1) // 2
        center = point_to_boardloc(center, boardsize)
        center_ord = ord(center[0])
        legal_moves = []
        # for every empty space
        for i in available_moves:
            move_ord = ord(i[0])
            ord_diff = abs(center_ord - move_ord)

            # if current column is less than 3 spaces away from center            
            if ord_diff < 3:
                center_coord = int(center[1])
                move_coord = int(i[1])
                coord_diff = abs(center_coord - move_coord)
                
                # if current row is 3+ spaces away from center
                if coord_diff >= 3:
                    # add to legal move list                    
                    legal_moves.append(i)
            else:
                # add to legal move list
                legal_moves.append(i)
        
        # if specified move not legal
        if move not in legal_moves:
            print("\nError: Black's second move must be at least 3 spaces away from the center point")
            return False
        
        # if specified move is legal
        else:
            return True
    # if not black's second move
    else:
        return True

def display_move(move_status, player, move, board, boardsize):
    
    # if specified move was successfully played
    if move_status:
        
        # get player colour
        if player == 1:
            p1 = "black"
            p2 = "white"
        else:
            p1 = "white"
            p2 = "black"
        
        # display success message
        print("")
        print(p1, "played", move)
    
    # specified move was not able to be played
    else:
        print("Move was not played")

def display_capture(capture, player, black_capture_count, white_capture_count, capture_count, black_win, white_win, p1, p2):
    capture_win = False
    
    # if a capture occurred
    if capture:
        
        # if black made a capture
        if player == 1:
            # add to black's capture total
            black_capture_count += capture_count
            
            # if black made 5 or more captures overall
            if black_capture_count >= 5:
                # black wins by capture
                capture_win = True
                black_win = True
                
        # if white made a capture
        else:
            # add to white's capture total
            white_capture_count += capture_count
            
            # if white made 5 or more captures overall
            if white_capture_count >= 5:
                # white wins by capture
                capture_win = True
                white_win = True
                
        # if one capture was made
        if capture_count == 1:
            print("")
            print(p1, "made 1 capture")
            
        # if multiple captures were made
        elif capture_count > 1:
            print("")
            print(p1, "made", capture_count, "captures")
            
        # if player has won by capture
        if capture_win:
            
            # if black won
            if black_win:
                print("\nBlack made 5 or more captures - black wins!")
                
            # if white won
            elif white_win:
                print("\nWhite made 5 or more captures - white wins!")
                
    return black_capture_count, white_capture_count, black_win, white_win

def display_win(win, player, black_win, white_win, draw, board, boardsize, move_status, opponent):
    
    # if player has won
    if win:
        
        # if black has won
        if player == 1:
            black_win = True
            
        # if white has won
        else:
            white_win = True
            
        # if black has won
        if black_win:
            print("\nBlack wins via 5 in a row!")
            
        # if white has won
        elif white_win:
            print("\nWhite wins via 5 in a row!")
            
    # if win not detected
    else:
        # check for draw
        draw = check_draw(board, boardsize, draw)
        
        # if game is a draw
        if draw:
            print("\nGame has ended in a draw")
        
        # game is ongoing
        else:
            
            # if specified move was successfully played
            if move_status:
                # switch internal player values
                if player == 1:
                    player = 2
                    opponent = 1
                # keep internal player values the same
                else:
                    player = 1
                    opponent = 2
                    
    return black_win, white_win, draw, player, opponent

def reset_win_status():
    # reset win statuses to defaults
    b_win = False
    w_win = False
    draw_win = False
    return b_win, w_win, draw_win

def reset_players():
    # reset internal player values to defaults
    p1 = 1
    p2 = 2
    return p1, p2
        
def reset_cap_counts():
    # reset overall capture totals to defaults
    bcc = 0
    wcc = 0
    return bcc, wcc

def format_move(board, boardsize, player, opponent, b_cap_count, w_cap_count, b_win, 
                w_win, draw, move_status, capture, capture_count, move, p1, p2, win, move_history, blocks):
    # display the specified move
    display_move(move_status, player, move, board, boardsize)
    # display tria or tessera if 3 in a row or 4 in a row made
    display_blocks(blocks, player)
    # display capture if capture occurred
    b_cap_count, w_cap_count, b_win, w_win \
        = display_capture(capture, player, b_cap_count, w_cap_count, capture_count, b_win, w_win, p1, p2)
    # display win/draw if game ended
    b_win, w_win, draw, player, opponent \
        = display_win(win, player, b_win, w_win, draw, board, boardsize, move_status, opponent)
    # add specified move to move history
    move_history.append((p1[0], move))
    # display current board
    show_board(board, boardsize)
    # display divider for readability
    divider = '-'*25
    print('\n'+divider)
    
    return board, player, opponent, b_cap_count, w_cap_count, b_win, w_win, draw

def display_blocks(blocks, player):
    # if a block of stones exists for player
    if blocks:
        
        # if player is black
        if player == 1:
            p1 = "black"
            
        # if player is white
        elif player == 2:
            p1 = "white"
            
        # for each block count
        for i in blocks:
            
            # if 3-in-a-row
            if i == 3:
                print("\nTria!", p1, "has made 3 in a row!")
            
            # if 4-in-a-row
            elif i == 4:
                print("\nTessera!", p1, "has made 4 in a row!")
                
    else:
        return

def check_ruleset(ruleset):
    
    # if tournament ruleset in use
    if ruleset == 1:
        print("\nThe current ruleset is: Tournament")
        
    # if casual ruleset in use
    elif ruleset == 2:
        print("\nThe current ruleset is: Casual")

def play_move(move, board, boardsize, player, opponent, mode=0):
    # get board index of specified move
    point = boardloc_to_point(move, boardsize)
    
    # if move is off the board/input incorrectly
    if point == "error":
        
        # if detailed return mode
        if mode == 0:
            return False, None, None, None, None
        
        # if status return mode
        else:
            return False
        
    ''' 
    no need to deep check if move is legal
    every empty space is a legal move
    only need to check for capture
    '''
    
    # if specified move's location is not empty
    if board[point] != 0:
        # error
        print("\nError: Illegal move - position already occupied")
        
        # if detailed return mode
        if mode == 0:
            return False, None, None, None, None
        
        # if status return mode
        else:
            return False
        
    # place stone on board at location
    board[point] = player
    # check for capture
    capture_status, capture_list, capture_count = capture_check(board, boardsize, player, opponent, point)
    
    # if capture occurred
    if capture_status:
        # remove captured stones
        for i in capture_list:
            board[i] = 0
            
    # if detailed return mode
    if mode == 0:
        # check for win
        win_status, blocks = check_win(board, boardsize, player, point)
        return True, capture_status, capture_count, win_status, blocks
    
    # if status return mode
    else:
        return True

def quit():
    print("\nShutting down...")
    # kill program
    sys.exit()