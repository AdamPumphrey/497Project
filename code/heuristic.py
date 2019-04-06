import utility as u

def get_line(board, opponent, player, last_move_index, offset, diag_search=False, mode=0):
    """ parse row/column/diagonal of board starting from last move played """
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

    while space_count1 != 2 or space_count2 != 2:
        if space_count1 < 2:
            if not diag_search:
                pos1 = board[last_move_index + (offset * i)]
            else:
                pos1 = board[last_move_index + (offset * i) + i]
            if pos1 == opponent:
                if space_count1 < 1:
                    block_count += 1
                else:
                    stone_count1 += 1
            elif pos1 == player or pos1 == 3:
                if space_count1 == 1:
                    p_stone1_sp = True
                    space_count1 = 2
                else:
                    p_stone1 = True
                    space_count1 = 2
            else:
                if end_block1 == 0:
                    if diag_search:
                        end_block1 = (last_move_index + (offset * i) + i)
                    else:
                        end_block1 = (last_move_index + (offset * i))
                space_count1 += 1
        if space_count2 < 2:
            if not diag_search:
                pos2 = board[last_move_index + (offset * -i)]
            else:
                pos2 = board[last_move_index + (offset * -i) - i]
            if pos2 == opponent:
                if space_count2 < 1:
                    block_count += 1
                else:
                    stone_count2 += 1
            elif pos2 == player or pos2 == 3:
                if space_count2 == 1:
                    p_stone2_sp = True
                    space_count2 = 2
                else:
                    p_stone2 = True
                    space_count2 = 2
            else:
                if end_block2 == 0:
                    if diag_search:
                        end_block2 = (last_move_index + (offset * -i) - i)
                    else:
                        end_block2 = (last_move_index + (offset * -i))
                space_count2 += 1
        i += 1
        
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
            
    if mode == 0:
        return blockwin_threat_eval(block_count, stone_count1, p_stone1, stone_count2, p_stone2, p_stone1_sp, p_stone2_sp, play_locations)
    elif mode == 4:
        return openfour_threat_eval(block_count, stone_count1, p_stone1, stone_count2, p_stone2, p_stone1_sp, p_stone2_sp, play_locations)
    elif mode == -4:
        return blockfour_threat_eval(block_count, stone_count1, p_stone1, stone_count2, p_stone2, p_stone1_sp, p_stone2_sp, play_locations)    
            
def check_blockwin(board, player, opponent, last_move_index, boardsize, mode=0):
    if mode == 0:
        def_moves = []
        def_moves1 = get_line(board, opponent, player, last_move_index, (boardsize + 1))
        if def_moves1:
            for x in def_moves1:
                if x not in def_moves:
                    def_moves.append(x)
        def_moves1 = get_line(board, opponent, player, last_move_index, 1)
        if def_moves1:
            for x in def_moves1:
                if x not in def_moves:
                    def_moves.append(x)
        def_moves1 = get_line(board, opponent, player, last_move_index, (boardsize + 1), True)
        if def_moves1:
            for x in def_moves1:
                if x not in def_moves:
                    def_moves.append(x)
        def_moves1 = get_line(board, opponent, player, last_move_index, -(boardsize + 1), True)
        if def_moves1:
            for x in def_moves1:
                if x not in def_moves:
                    def_moves.append(x)
    elif mode == 4:
        def_moves = []
        def_moves1 = get_line(board, opponent, player, last_move_index, (boardsize + 1), False, -4)
        if def_moves1:
            for x in def_moves1:
                if x not in def_moves:
                    def_moves.append(x)
        def_moves1 = get_line(board, opponent, player, last_move_index, 1, False, -4)
        if def_moves1:
            for x in def_moves1:
                if x not in def_moves:
                    def_moves.append(x)
        def_moves1 = get_line(board, opponent, player, last_move_index, (boardsize + 1), True, -4)
        if def_moves1:
            for x in def_moves1:
                if x not in def_moves:
                    def_moves.append(x)
        def_moves1 = get_line(board, opponent, player, last_move_index, -(boardsize + 1), True, -4)
        if def_moves1:
            for x in def_moves1:
                if x not in def_moves:
                    def_moves.append(x)
    return def_moves

def blockfour_threat_eval(block, left_count, playerstone_L, right_count, playerstone_R, playerstone_L_sp, playerstone_R_sp, move_locations):
    """ evaluate loss-threats from current position """
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
    """ evaluate loss-threats from current position """
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
    """ evaluate loss-threats from current position """
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
    if player == 1:
        match = 'b'
    elif player == 2:
        match = 'w'
    while i < len(move_history):
        player_last_move = move_history[i]
        if player_last_move[0] == match:
            player_previous_moves.append(player_last_move[1])
            i += 1
        else:
            i += 1
    return player_previous_moves

def get_win_moves(previous_moves, board, player, opponent, boardsize, mode=0):
    moves_analyzed = []
    moves = []
    for m in reversed(previous_moves):
        tempmove_index = u.boardloc_to_point(m, boardsize)
        templist = []
        emptycount = 8
        if board[tempmove_index + (boardsize + 1)] == 0 and tempmove_index + (boardsize + 1) not in moves_analyzed:
            templist.append(tempmove_index + (boardsize + 1))
        elif board[tempmove_index + (boardsize + 1)] != 0:
            emptycount -= 1
        if board[tempmove_index - (boardsize + 1)] == 0 and tempmove_index - (boardsize + 1) not in moves_analyzed:
            templist.append(tempmove_index - (boardsize + 1))
        elif board[tempmove_index - (boardsize + 1)] != 0:
            emptycount -= 1
        if board[tempmove_index + 1] == 0 and tempmove_index + 1 not in moves_analyzed:
            templist.append(tempmove_index + 1)
        elif board[tempmove_index + 1] != 0:
            emptycount -= 1
        if board[tempmove_index - 1] == 0 and tempmove_index - 1 not in moves_analyzed:
            templist.append(tempmove_index - 1)
        elif board[tempmove_index - 1] != 0:
            emptycount -= 1
        if board[tempmove_index + (boardsize + 1) + 1] == 0 and tempmove_index + (boardsize + 1) + 1 not in moves_analyzed:
            templist.append(tempmove_index + (boardsize + 1) + 1)
        elif board[tempmove_index + (boardsize + 1) + 1] != 0:
            emptycount -= 1
        if board[tempmove_index - (boardsize + 1) - 1] == 0 and tempmove_index - (boardsize + 1) - 1 not in moves_analyzed:
            templist.append(tempmove_index - (boardsize + 1) - 1)
        elif board[tempmove_index - (boardsize + 1) - 1] != 0:
            emptycount -= 1
        if board[tempmove_index + (boardsize + 1) - 1] == 0 and tempmove_index + (boardsize + 1) - 1 not in moves_analyzed:
            templist.append(tempmove_index + (boardsize + 1) - 1)
        elif board[tempmove_index + (boardsize + 1) - 1] != 0:
            emptycount -= 1
        if board[tempmove_index - (boardsize + 1) + 1] == 0 and tempmove_index - (boardsize + 1) + 1 not in moves_analyzed:
            templist.append(tempmove_index - (boardsize + 1) + 1)
        elif board[tempmove_index - (boardsize + 1) + 1] != 0:
            emptycount -= 1
        if emptycount == 0:
            #templist = get_empty_spaces(board, boardsize)
            pass
        else:
            for pos in templist:
                tempboard = board.copy()
                move = u.point_to_boardloc(pos, boardsize)
                move_status = u.play_move(move, tempboard, boardsize, player, opponent, 1)
                if mode == 0:
                    moves1 = get_line(tempboard, player, opponent, pos, (boardsize + 1))
                    if moves1:
                        if moves1[0] == 10000:
                            # move caused a win
                            if pos not in moves:
                                moves.append(pos)
                    moves1 = get_line(tempboard, player, opponent, pos, 1)
                    if moves1:
                        if moves1[0] == 10000:
                            if pos not in moves:
                                moves.append(pos)
                    moves1 = get_line(tempboard, player, opponent, pos, (boardsize + 1), True)
                    if moves1:
                        if moves1[0] == 10000:
                            if pos not in moves:
                                moves.append(pos)
                    moves1 = get_line(tempboard, player, opponent, pos, -(boardsize + 1), True)
                    if moves1:
                        if moves1[0] == 10000:
                            if pos not in moves:
                                moves.append(pos)
                elif mode == 4:
                    moves1 = get_line(tempboard, player, opponent, pos, (boardsize + 1), False, 4)
                    if moves1:
                        if moves1[0] == 4:
                            # move caused an open four
                            if pos not in moves:
                                moves.append(pos)
                    moves1 = get_line(tempboard, player, opponent, pos, 1, False, 4)
                    if moves1:
                        if moves1[0] == 4:
                            if pos not in moves:
                                moves.append(pos)
                    moves1 = get_line(tempboard, player, opponent, pos, (boardsize + 1), True, 4)
                    if moves1:
                        if moves1[0] == 4:
                            if pos not in moves:
                                moves.append(pos)
                    moves1 = get_line(tempboard, player, opponent, pos, -(boardsize + 1), True, 4)
                    if moves1:
                        if moves1[0] == 4:
                            if pos not in moves:
                                moves.append(pos)
                moves_analyzed.append(pos)
    return moves

def win_heuristic(player_move_history, board, player, opponent, boardsize, mode=0):
    if mode == 4:
        win_moves = get_win_moves(player_move_history, board, player, opponent, boardsize, 4)
    else:
        win_moves = get_win_moves(player_move_history, board, player, opponent, boardsize)
    if win_moves:
        count = 0
        while count < len(win_moves):
            move = int(win_moves[count])
            move = u.point_to_boardloc(move, boardsize)
            win_moves[count] = move
            count += 1
        return win_moves
    else:
        return []

def def_heuristic(board, player, opponent, last_move_index, boardsize, mode=0):
    if mode == 4:
        def_moves = check_blockwin(board, player, opponent, last_move_index, boardsize, 4)
    else:
        def_moves = check_blockwin(board, player, opponent, last_move_index, boardsize)
    if def_moves:
        count = 0
        while count < len(def_moves):
            move = int(def_moves[count])
            move = u.point_to_boardloc(move, boardsize)
            def_moves[count] = move
            count += 1    
        return def_moves
    else:
        return []
