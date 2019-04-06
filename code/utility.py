import random, sys

def build_board(boardsize):
    board = [0] * ((boardsize + 1) ** 2)
    top_border = [3] * (boardsize + 1)
    board[0:(boardsize + 1)] = top_border
    count = 1
    while count <= boardsize:
        board[((boardsize + 1) * count):(((boardsize + 1) * count) + 1)] = [3]
        count += 1
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
        count += 1
        print(row_str)

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

def check_inp_command(command, commandlist):
    if not command[0].isalpha():
        return False
    else:
        command[0] = command[0].lower()
    if command[0] not in commandlist:
        return False
    else:
        return True

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
    return win, blocks

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
    return win, blocks

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
    if player == 1 and len(move_history) == 0:
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
    move_status, capture, capture_count, win, blocks = play_move(move, board, boardsize, player, opponent)
    return move_status, capture, capture_count, win, move, blocks

def tournament_rule_check(board, boardsize, player, move_history, move):
    if player == 1 and len(move_history) == 2:
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
        #show_board(board, boardsize)
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

def format_move(board, boardsize, player, opponent, b_cap_count, w_cap_count, b_win, 
                w_win, draw, move_status, capture, capture_count, move, p1, p2, win, move_history, blocks):
    display_move(move_status, player, move, board, boardsize)
    display_blocks(blocks, player)
    b_cap_count, w_cap_count, b_win, w_win \
        = display_capture(capture, player, b_cap_count, w_cap_count, capture_count, b_win, w_win, p1, p2)
    b_win, w_win, draw, player, opponent \
        = display_win(win, player, b_win, w_win, draw, board, boardsize, move_status, opponent)
    move_history.append((p1[0], move))
    show_board(board, boardsize)
    divider = '-'*25
    print('\n'+divider)
    return board, player, opponent, b_cap_count, w_cap_count, b_win, w_win, draw

def display_blocks(blocks, player):
    if blocks:
        if player == 1:
            p1 = "black"
        elif player == 2:
            p1 = "white"
        for i in blocks:
            if i == 3:
                print("\nTria!", p1, "has made 3 in a row!")
            elif i == 4:
                print("\nTessera!", p1, "has made 4 in a row!")
    else:
        return

def check_ruleset(ruleset):
    if ruleset == 1:
        print("\nThe current ruleset is: Tournament")
    elif ruleset == 2:
        print("\nThe current ruleset is: Casual")

def play_move(move, board, boardsize, player, opponent, mode=0):
    point = boardloc_to_point(move, boardsize)
    if point == "error":
        if mode == 0:
            return False, None, None, None, None
        else:
            return False
    # no need to deep check if move legal
    # every empty space is a legal move
    # only need to check for capture
    if board[point] != 0:
        print("\nError: Illegal move - position already occupied")
        if mode == 0:
            return False, None, None, None, None
        else:
            return False
    board[point] = player
    # check for capture
    # capture can only be in form of O-X-X-O as per rules
    capture_status, capture_list, capture_count = capture_check(board, boardsize, player, opponent, point)
    if capture_status:
        for i in capture_list:
            board[i] = 0
    # check for win
    # need to implement calling 4 in a row (tessera) and 3 in a row (tria)
    if mode == 0:
        win_status, blocks = check_win(board, boardsize, player, point)
        return True, capture_status, capture_count, win_status, blocks
    else:
        return True

def quit():
    print("\nShutting down...")
    sys.exit()
