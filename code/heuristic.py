import utility as u

'''
I (Adam Pumphrey) wrote and used the following functions for CMPUT 496 Assignment 3.
I modified them to work for this program:

    blockfour_threat_eval
    blockwin_threat_eval
    check_blockwin
    get_line
    get_win_moves
    openfour_threat_eval
    parse_move_history
    
To avoid any possible misconceptions, I (Adam Pumphrey), am the sole author of
the functions listed in this file.

The following functions were written specifically for this program:

    def_heuristic
    win_heuristic
'''

def get_line(board, opponent, player, last_move_index, offset, diag_search=False, mode=0):
    ''' 
    parse row/column/diagonal of board starting from last move played 
    
    was originally made to detect opponent wins/win threats.
    modified to look for open fours/open four threats.
    '''
    stone_count1 = 0
    stone_count2 = 0
    block_count = 1
    space_count1 = 0
    space_count2 = 0
    p_stone1 = False
    p_stone2 = False
    p_stone1_sp = False
    p_stone2_sp = False
    play_locations = []
    end_block1 = 0
    end_block2 = 0
    i = 1
    
    # while 2 empty spaces on each side have not been detected
    while space_count1 != 2 or space_count2 != 2:
        
        # if 2 empty spaces have not been found going forward
        if space_count1 < 2:
            
            # if not diagonal search mode
            if not diag_search:
                # move forward one increment
                pos1 = board[last_move_index + (offset * i)]
                
            # if diagonal search mode
            else:
                # move forward diagonally by one increment
                pos1 = board[last_move_index + (offset * i) + i]
                
            # if current board space contains opponent's stone
            if pos1 == opponent:
                
                # if a space has not yet been found going forward
                if space_count1 < 1:
                    # add to current block
                    block_count += 1
                    
                # if a space has been found going forward
                else:
                    # add to forward adjacent block
                    stone_count1 += 1
                    
            # if current board space contains player's stone or is the border
            elif pos1 == player or pos1 == 3:
                
                # if a space has been found going forward
                if space_count1 == 1:
                    # player stone at forward end after space present
                    p_stone1_sp = True
                    # stop searching forward
                    space_count1 = 2
                    
                # if a space has not yet been found going forward
                else:
                    # player stone at forward end without space present
                    p_stone1 = True
                    # stop searching forward
                    space_count1 = 2
                    
            # if current board space is empty
            else:
                
                # if end of block not yet found
                if end_block1 == 0:
                    # store end of block location
                    if diag_search:
                        end_block1 = (last_move_index + (offset * i) + i)
                    else:
                        end_block1 = (last_move_index + (offset * i))
                        
                space_count1 += 1
                
        # if 2 empty spaces have not been found going backward
        if space_count2 < 2:
            
            # if not diagonal search mode
            if not diag_search:
                # move backward one increment
                pos2 = board[last_move_index + (offset * -i)]
                
            # if diagonal search mode    
            else:
                # move backward diagonally by one increment
                pos2 = board[last_move_index + (offset * -i) - i]
                
            # if current board space contains opponent's stone    
            if pos2 == opponent:
                
                # if a space has not yet been found going backward
                if space_count2 < 1:
                    # add to current block
                    block_count += 1
                 
                # if a space has been found going backward    
                else:
                    # add to backward adjacent block
                    stone_count2 += 1
            
            # if current board space contains player's stone or is the border
            elif pos2 == player or pos2 == 3:
                
                # if a space has been found going backward
                if space_count2 == 1:
                    # player stone at backward end after space present
                    p_stone2_sp = True
                    # stop searching backward
                    space_count2 = 2
                
                # if a space has not yet been found going forward
                else:
                    # player stone at backward end without space present
                    p_stone2 = True
                    # stop searching backward
                    space_count2 = 2
            
            # if current board space is empty
            else:
                
                # if end of block not yet found
                if end_block2 == 0:
                    # store end of block location
                    if diag_search:
                        end_block2 = (last_move_index + (offset * -i) - i)
                    else:
                        end_block2 = (last_move_index + (offset * -i))
                        
                space_count2 += 1
        
        # number of increments
        i += 1
    
    ''' 
    the following section of code goes through a series of checks to determine 
    whether empty spaces between blocks and adjacent stones, as well as at the
    end of blocks and stones, should be considered as valid play locations.
    
    valid play locations are spaces where the player can play and prevent
    a loss, open four, etc
    '''
    
    if ((block_count == 1 and stone_count1 == 2) or (block_count == 2 and stone_count1 == 1)) and stone_count2 == 0:
        if (board[last_move_index - offset] == 0) and (board[last_move_index + offset] == 0):
            if not (p_stone1_sp or p_stone2_sp):
                if diag_search:
                    if not p_stone2:
                        play_locations.append(end_block2)
                    if not p_stone1:
                        newblock2 = last_move_index + (4 * offset) + 4
                        play_locations.append(newblock2)
                else:
                    if not p_stone2:
                        play_locations.append(end_block2)
                    if not p_stone1:
                        newblock2 = last_move_index + (4 * offset)
                        play_locations.append(newblock2)
                if (block_count + stone_count1) > 2:
                    play_locations.append(end_block1)
                if (block_count + stone_count2) > 2:
                    play_locations.append(end_block2)
        elif (board[last_move_index - offset] == 0) and (board[last_move_index + offset] == opponent):
            if not (p_stone1_sp or p_stone2_sp):
                if diag_search:
                    if not p_stone2:
                        play_locations.append(end_block2)
                    if not p_stone1:
                        newblock2 = last_move_index + (4 * offset) + 4
                        play_locations.append(newblock2)
                else:
                    if not p_stone2:
                        play_locations.append(end_block2)
                    if not p_stone1:
                        newblock2 = last_move_index + (4 * offset)
                        play_locations.append(newblock2)
                if (block_count + stone_count1) > 2:
                    play_locations.append(end_block1)
                if (block_count + stone_count2) > 2:
                    play_locations.append(end_block2)                
        elif (board[last_move_index - offset] == opponent) and (board[last_move_index + offset] == 0):
            if not (p_stone1_sp or p_stone2_sp):
                if diag_search:
                    if not p_stone2:
                        play_locations.append(end_block2)
                    if not p_stone1:
                        newblock2 = last_move_index + (3 * offset) + 3
                        play_locations.append(newblock2)
                else:
                    if not p_stone2:
                        play_locations.append(end_block2)
                    if not p_stone1:
                        newblock2 = last_move_index + (3 * offset)
                        play_locations.append(newblock2)
                if (block_count + stone_count1) > 2:
                    play_locations.append(end_block1)
                if (block_count + stone_count2) > 2:
                    play_locations.append(end_block2)                
    elif ((block_count == 1 and stone_count2 == 2) or (block_count == 2 and stone_count2 == 1)) and stone_count1 == 0:
        if (board[last_move_index - offset] == 0) and (board[last_move_index + offset] == 0):
            if not (p_stone1_sp or p_stone2_sp):
                if diag_search:
                    if not p_stone1:
                        play_locations.append(end_block1)
                    if not p_stone2:
                        newblock2 = last_move_index - (4 * offset) - 4
                        play_locations.append(newblock2)            
                else:
                    if not p_stone1:
                        play_locations.append(end_block1)
                    if not p_stone2:
                        newblock2 = last_move_index - (4 * offset)
                        play_locations.append(newblock2)
                if (block_count + stone_count1) > 2:
                    play_locations.append(end_block1)
                if (block_count + stone_count2) > 2:
                    play_locations.append(end_block2)                
        elif (board[last_move_index - offset] == 0) and (board[last_move_index + offset] == opponent):
            if not (p_stone1_sp or p_stone2_sp):
                if diag_search:
                    if not p_stone1:
                        play_locations.append(end_block1)
                    if not p_stone2:
                        newblock1 = last_move_index - (3 * offset) - 3
                        play_locations.append(newblock1)
                else:
                    if not p_stone1:
                        play_locations.append(end_block1)
                    if not p_stone2:
                        newblock2 = last_move_index - (3 * offset)
                        play_locations.append(newblock2)              
                if (block_count + stone_count1) > 2:
                    play_locations.append(end_block1)
                if (block_count + stone_count2) > 2:
                    play_locations.append(end_block2)                
        elif (board[last_move_index - offset] == opponent) and (board[last_move_index + offset] == 0):
            if not (p_stone1_sp or p_stone2_sp):
                if diag_search:
                    if not p_stone1:
                        newblock1 = last_move_index + (4 * offset) + 4
                        play_locations.append(newblock1)
                    if not p_stone2:
                        play_locations.append(end_block2)
                else:
                    if not p_stone1:
                        play_locations.append(end_block1)
                    if not p_stone2:
                        newblock1 = last_move_index - (4 * offset)
                        play_locations.append(newblock1)
                if (block_count + stone_count1) > 2:
                    play_locations.append(end_block1)
                if (block_count + stone_count2) > 2:
                    play_locations.append(end_block2)                
    
    if block_count == 3 and (p_stone1_sp or p_stone2_sp) and not (p_stone1_sp and p_stone2_sp):
        if diag_search:
            if p_stone1_sp:
                newblock = end_block2 - offset - 1
                play_locations.append(newblock)
            elif p_stone2_sp:
                newblock = end_block1 + offset + 1
                play_locations.append(newblock)
        else:
            if p_stone1_sp:
                newblock = end_block2 - offset
                play_locations.append(newblock)
            elif p_stone2_sp:
                newblock = end_block1 + offset
                play_locations.append(newblock)

    if (block_count + stone_count1) > 2 and (block_count + stone_count2) > 2:
        if stone_count1 != 0 and stone_count2 != 0:
            play_locations.append(end_block1)
            play_locations.append(end_block2)
        elif stone_count1 == 0 and stone_count2 == 0:
            if not p_stone1:
                play_locations.append(end_block1)
            if not p_stone2:
                play_locations.append(end_block2)
        elif stone_count1 == 0:
            play_locations.append(end_block2)
        elif stone_count2 == 0:
            play_locations.append(end_block1)
    elif (block_count + stone_count1) > 2:
        if (block_count + stone_count1) == 4:
            play_locations.append(end_block1)
    elif (block_count + stone_count2) > 2:
        if (block_count + stone_count2) == 4:
            play_locations.append(end_block2)
            
    # if checking for a win threat to block        
    if mode == 0:
        return blockwin_threat_eval(block_count, stone_count1, p_stone1, stone_count2, p_stone2, p_stone1_sp, p_stone2_sp, play_locations)
    
    # if looking for open fours possibilities to play
    elif mode == 4:
        return openfour_threat_eval(block_count, stone_count1, p_stone1, stone_count2, p_stone2, p_stone1_sp, p_stone2_sp, play_locations)
    
    # if checking for an open four threat to block
    elif mode == -4:
        return blockfour_threat_eval(block_count, stone_count1, p_stone1, stone_count2, p_stone2, p_stone1_sp, p_stone2_sp, play_locations)    
            
def check_blockwin(board, player, opponent, last_move_index, boardsize, mode=0):
    
    # if checking for win threats to block
    if mode == 0:
        def_moves = []
        # get vertical defending moves
        def_moves1 = get_line(board, opponent, player, last_move_index, (boardsize + 1))
        
        # if defending moves available
        if def_moves1:
            # for each defending move
            for x in def_moves1:
                
                # if defending move not in movelist
                if x not in def_moves:
                    # add move to list
                    def_moves.append(x)
                    
        # get horizontal defending moves
        def_moves1 = get_line(board, opponent, player, last_move_index, 1)
        
        # if defending moves available
        if def_moves1:
            # for each defending move
            for x in def_moves1:
                
                # if defending move not in movelist
                if x not in def_moves:
                    # add move to list
                    def_moves.append(x)
                    
        # get diagonal up/left down/right defending moves
        def_moves1 = get_line(board, opponent, player, last_move_index, (boardsize + 1), True)
        if def_moves1:
            for x in def_moves1:
                if x not in def_moves:
                    def_moves.append(x)
                    
        # get diagonal up/right down/left defending moves
        def_moves1 = get_line(board, opponent, player, last_move_index, -(boardsize + 1), True)
        if def_moves1:
            for x in def_moves1:
                if x not in def_moves:
                    def_moves.append(x)
    
    # if checking for open four threats to block
    elif mode == 4:
        def_moves = []
        
        # get vertical defending moves
        def_moves1 = get_line(board, opponent, player, last_move_index, (boardsize + 1), False, -4)
        if def_moves1:
            for x in def_moves1:
                if x not in def_moves:
                    def_moves.append(x)
                    
        # get horizontal defending moves
        def_moves1 = get_line(board, opponent, player, last_move_index, 1, False, -4)
        if def_moves1:
            for x in def_moves1:
                if x not in def_moves:
                    def_moves.append(x)
                    
        # get diagonal up/left down/right defending moves
        def_moves1 = get_line(board, opponent, player, last_move_index, (boardsize + 1), True, -4)
        if def_moves1:
            for x in def_moves1:
                if x not in def_moves:
                    def_moves.append(x)
                    
        # get diagonal up/right down/left defending moves
        def_moves1 = get_line(board, opponent, player, last_move_index, -(boardsize + 1), True, -4)
        if def_moves1:
            for x in def_moves1:
                if x not in def_moves:
                    def_moves.append(x)
                    
    return def_moves

def blockfour_threat_eval(block, left_count, playerstone_L, right_count, playerstone_R, playerstone_L_sp, playerstone_R_sp, move_locations):
    ''' 
    this function evaluates a block and adjacent stones to see if
    the position is dangerous.
    if position is dangerous, defending move(s) will be returned
    
    this function specifically checks for open four threats
    '''
    pos_threat_count = 0
    if block == 2:
        if left_count == 1 and right_count == 1:
            if not playerstone_L and not playerstone_R:
                # ( - o - o o - o -) can create open 4 with either middle move
                # only need to play one of the middle moves
                pos_threat_count = 1
        elif left_count == 1 or right_count == 1:
            if not playerstone_L and not playerstone_R:
                # ( - o - o o -) can create open 4 with middle move
                # must play middle move
                pos_threat_count = 1
    elif block == 3:
        if left_count == 0 and right_count == 0:
            if not playerstone_L and not playerstone_R and (not playerstone_L_sp or not playerstone_R_sp):
                # ( - o o o -)
                pos_threat_count = 1
    elif block == 1:
        if left_count == 2 and right_count == 2:
            if not playerstone_L or not playerstone_R:
                #( - o o - o - o o x)
                pos_threat_count = 1
        elif left_count == 2 or right_count == 2:
            if not playerstone_L and not playerstone_R:
                #( x - o o - o - x)
                pos_threat_count = 1
    if pos_threat_count >= 1:
        return move_locations
    else:
        return []

def blockwin_threat_eval(block, left_count, playerstone_L, right_count, playerstone_R, playerstone_L_sp, playerstone_R_sp, move_locations):
    ''' 
    this function evaluates a block and adjacent stones to see if
    the position is dangerous.
    if position is dangerous, defending move(s) will be returned
    
    this function specifically checks for win threats
    '''
    pos_threat_count = 0
    if block >= 5:
        pos_threat_count = 10000
        return [10000]
    elif block == 2:
        if left_count == 4:
            if playerstone_L:
                # ( x o o o o - o o -)
                # must play middle move
                pos_threat_count = 1
            else:
                # ( - o o o o - o o -)
                pos_threat_count = 2
        elif right_count == 4:
            if playerstone_R:
                pos_threat_count = 1
            else:
                pos_threat_count = 2
        elif left_count in list(range(2, 4)) and right_count in list(range(2, 4)):
            # ( - o o - o o - o o o -) cannot prevent loss
            pos_threat_count = 2
        elif left_count in list(range(2, 4)) or right_count in list(range(2, 4)):
            # ( - o o - o o -) or ( - o o o - o o -) can win with middle move
            # must play middle move
            pos_threat_count = 1

    elif block == 3:
        if left_count == 4:
            if playerstone_L:
                # ( x o o o o - o o o -)
                # must play middle move
                pos_threat_count = 1
            else:
                # ( - o o o o - o o o -) or ( - o o o o - o o o x)
                pos_threat_count = 2
        elif right_count == 4:
            if playerstone_R:
                pos_threat_count = 1
            else:
                pos_threat_count = 2
        elif left_count in list(range(1,4)) and right_count in list(range(1,4)):
            # ( - o - o o o - o o o -)
            pos_threat_count = 2
        elif left_count in list(range(1,4)) or right_count in list(range(1,4)):
            # ( - o - o o o -) or ( - o o - o o o -) or ( - o o o - o o o -)
            pos_threat_count = 1

    elif block == 4:
        if left_count == 4 or right_count == 4:
            if playerstone_L and playerstone_R:
                # ( x o o o o - o o o o x)
                pos_threat_count = 1
            else:
                # ( - o o o o - o o o o x)
                pos_threat_count = 2
        elif left_count == 0 and right_count == 0:
            if not playerstone_L and not playerstone_R:
                # ( - o o o o -)
                pos_threat_count = 2
            elif playerstone_L and not playerstone_R:
                # ( x o o o o -)
                pos_threat_count = 1
            elif playerstone_R and not playerstone_L:
                pos_threat_count = 1
        elif left_count in list(range(1,5)) and right_count in list(range(1,5)):
            # ( - o o o - o o o o - o -)
            pos_threat_count = 2
        elif left_count in list(range(1,4)):
            if playerstone_R:
                # ( - o o - o o o o x)
                pos_threat_count = 1
            else:
                # ( - o o - o o o o -)
                pos_threat_count = 2
        elif right_count in list(range(1,4)):
            if playerstone_L:
                pos_threat_count = 1
            else:
                pos_threat_count = 2

    elif block == 1:
        if left_count in list(range(3,5)) and right_count in list(range(3,5)):
            #( x o o o o - o - o o o x)
            pos_threat_count = 2
        elif left_count == 4:
            if not playerstone_L:
                #(- o o o o - o)
                pos_threat_count = 2
        elif right_count == 4:
            if not playerstone_R:
                pos_threat_count = 2
        elif left_count == 3 or right_count == 3:
            #( - o - o o o x)
            pos_threat_count = 1

    if pos_threat_count >= 1:
        return move_locations
    else:
        return []
    
def openfour_threat_eval(block, left_count, playerstone_L, right_count, playerstone_R, playerstone_L_sp, playerstone_R_sp, move_locations):
    ''' 
    this function evaluates a block and adjacent stones to see if
    the position is dangerous.
    
    this function specifically checks for an open four
    
    if an open four is present, the game is essentially over,
    as an open four is a winning position
    '''
    if block == 4:
        if left_count == 0 and right_count == 0:
            if not playerstone_L and not playerstone_R:
                # ( - o o o o -)
                return [4]
    else:
        return []

def parse_move_history(player, move_history):
    player_previous_moves = []
    i = 0
    found = False
    
    # if player is black
    if player == 1:
        # id to match 
        match = 'b'
        
    # if player is white
    elif player == 2:
        # id to match
        match = 'w'
    
    # for each move in the move history
    while i < len(move_history):
        player_last_move = move_history[i]
        
        # if id of the move matches id of the player
        if player_last_move[0] == match:
            # add to player move history
            player_previous_moves.append(player_last_move[1])
            i += 1
            
        else:
            i += 1
            
    return player_previous_moves

def get_win_moves(previous_moves, board, player, opponent, boardsize, mode=0):
    moves_analyzed = []
    moves = []
    
    # for each move in the move history, starting at the most recent move
    for m in reversed(previous_moves):
        # get board index of move
        tempmove_index = u.boardloc_to_point(m, boardsize)
        templist = []
        emptycount = 8
        
        # if space in row above point is empty and space not yet analyzed
        if board[tempmove_index + (boardsize + 1)] == 0 and tempmove_index + (boardsize + 1) not in moves_analyzed:
            # add space to list
            templist.append(tempmove_index + (boardsize + 1))
        
        # if space in row above point is not empty
        elif board[tempmove_index + (boardsize + 1)] != 0:
            emptycount -= 1
            
        # if space in row below point is empty and space not yet analyzed
        if board[tempmove_index - (boardsize + 1)] == 0 and tempmove_index - (boardsize + 1) not in moves_analyzed:
            # add space to list
            templist.append(tempmove_index - (boardsize + 1))
            
        # # if space in row below point is not empty
        elif board[tempmove_index - (boardsize + 1)] != 0:
            emptycount -= 1
        
        # if space in column to the right of the point is not empty and space not yet analyzed
        if board[tempmove_index + 1] == 0 and tempmove_index + 1 not in moves_analyzed:
            templist.append(tempmove_index + 1)
        
        # if space in column to the right of the point is empty
        elif board[tempmove_index + 1] != 0:
            emptycount -= 1
        
        # if space in column to the left of the point is not empty and space not yet analyzed
        if board[tempmove_index - 1] == 0 and tempmove_index - 1 not in moves_analyzed:
            templist.append(tempmove_index - 1)
        
        # if space in column to the left of the point is empty
        elif board[tempmove_index - 1] != 0:
            emptycount -= 1
        
        # if space up and left of point is not empty and space not yet analyzed
        if board[tempmove_index + (boardsize + 1) + 1] == 0 and tempmove_index + (boardsize + 1) + 1 not in moves_analyzed:
            templist.append(tempmove_index + (boardsize + 1) + 1)
            
        # if space up and left of point is empty
        elif board[tempmove_index + (boardsize + 1) + 1] != 0:
            emptycount -= 1
            
        # if space down and right of point is not empty and space not yet analyzed
        if board[tempmove_index - (boardsize + 1) - 1] == 0 and tempmove_index - (boardsize + 1) - 1 not in moves_analyzed:
            templist.append(tempmove_index - (boardsize + 1) - 1)
            
        # if space down and right of point is empty
        elif board[tempmove_index - (boardsize + 1) - 1] != 0:
            emptycount -= 1
            
        # if space up and right of point is not empty and space not yet analyzed
        if board[tempmove_index + (boardsize + 1) - 1] == 0 and tempmove_index + (boardsize + 1) - 1 not in moves_analyzed:
            templist.append(tempmove_index + (boardsize + 1) - 1)
            
        # if space up and right of point is empty
        elif board[tempmove_index + (boardsize + 1) - 1] != 0:
            emptycount -= 1
            
        # if space down and left of point is not empty and space not yet analyzed
        if board[tempmove_index - (boardsize + 1) + 1] == 0 and tempmove_index - (boardsize + 1) + 1 not in moves_analyzed:
            templist.append(tempmove_index - (boardsize + 1) + 1)
            
        # if space down and left of point is empty
        elif board[tempmove_index - (boardsize + 1) + 1] != 0:
            emptycount -= 1
        
        # if all spaces around point are filled
        if emptycount == 0:
            # not sure if anything needs to be done here
            # leaving in just in case
            pass
        
        # if at least one empty space around point
        else:
            
            # for each empty space around point
            for pos in templist:
                # make a copy of the board
                tempboard = board.copy()
                # get board location of point
                move = u.point_to_boardloc(pos, boardsize)
                # play move on copy of board
                move_status = u.play_move(move, tempboard, boardsize, player, opponent, 1)
                
                # if checking to see if move caused win
                if mode == 0:
                    # vertical win check
                    moves1 = get_line(tempboard, player, opponent, pos, (boardsize + 1))
                    if moves1:
                        # if move caused a win
                        if moves1[0] == 10000:
                            # if move not in movelist
                            if pos not in moves:
                                # add move to list
                                moves.append(pos)
                    # horiztonal win check
                    moves1 = get_line(tempboard, player, opponent, pos, 1)
                    if moves1:
                        if moves1[0] == 10000:
                            if pos not in moves:
                                moves.append(pos)
                    # diagonal up/left down/right win check
                    moves1 = get_line(tempboard, player, opponent, pos, (boardsize + 1), True)
                    if moves1:
                        if moves1[0] == 10000:
                            if pos not in moves:
                                moves.append(pos)
                    # diagonal up/right down/left win check
                    moves1 = get_line(tempboard, player, opponent, pos, -(boardsize + 1), True)
                    if moves1:
                        if moves1[0] == 10000:
                            if pos not in moves:
                                moves.append(pos)
                
                # if checking to see if move caused open four
                elif mode == 4:
                    # vertical open four check
                    moves1 = get_line(tempboard, player, opponent, pos, (boardsize + 1), False, 4)
                    if moves1:
                        # move caused an open four
                        if moves1[0] == 4:
                            # if move not in movelist
                            if pos not in moves:
                                # add move to list
                                moves.append(pos)
                    # horiztonal open four check
                    moves1 = get_line(tempboard, player, opponent, pos, 1, False, 4)
                    if moves1:
                        if moves1[0] == 4:
                            if pos not in moves:
                                moves.append(pos)
                    # diagonal up/right down/left open four check
                    moves1 = get_line(tempboard, player, opponent, pos, (boardsize + 1), True, 4)
                    if moves1:
                        if moves1[0] == 4:
                            if pos not in moves:
                                moves.append(pos)
                    # diagonal up/left down/right open four check
                    moves1 = get_line(tempboard, player, opponent, pos, -(boardsize + 1), True, 4)
                    if moves1:
                        if moves1[0] == 4:
                            if pos not in moves:
                                moves.append(pos)
                # add move to analyzed list
                # prevents looking at same move twice
                moves_analyzed.append(pos)
                
    return moves

def win_heuristic(player_move_history, board, player, opponent, boardsize, mode=0):
    
    # if looking for open four moves
    if mode == 4:
        # get open four moves
        win_moves = get_win_moves(player_move_history, board, player, opponent, boardsize, 4)
    
    # if looking for winning moves
    else:
        # get winning moves
        win_moves = get_win_moves(player_move_history, board, player, opponent, boardsize)
    
    # if open four/winning moves available
    if win_moves:
        count = 0
        # for each move
        while count < len(win_moves):
            # convert move to board location
            move = int(win_moves[count])
            move = u.point_to_boardloc(move, boardsize)
            win_moves[count] = move
            count += 1
        return win_moves
    
    # if no moves available
    else:
        return []

def def_heuristic(board, player, opponent, last_move_index, boardsize, mode=0):
    
    # if looking for open four threats
    if mode == 4:
        # get open four blocking moves
        def_moves = check_blockwin(board, player, opponent, last_move_index, boardsize, 4)
    
    # if looking for win threats
    else:
        # get win blocking moves
        def_moves = check_blockwin(board, player, opponent, last_move_index, boardsize)
    
    # if any open four/win blocking moves
    if def_moves:
        count = 0
        # for each blocking move
        while count < len(def_moves):
            # convert move to board location
            move = int(def_moves[count])
            move = u.point_to_boardloc(move, boardsize)
            def_moves[count] = move
            count += 1    
        return def_moves
    
    # if no blocking moves available
    else:
        return []
