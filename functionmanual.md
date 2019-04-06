# Pente.py

Only function is main( ), but split up by command.

For descriptions of commands, see README.

Variables will only be listed under commands if they are local to that command section of main
eg) player variable is not local to 'reset' command (initialized in main), not listed under 'reset'
eg) success variable is local to 'boardsize' command (initialized in boardsize), listed under 'boardsize'

Variables:

    commandlist (str array): list of commands in use
    boardsize (int): size of board, if size is n, board is n x n
    board (int array): the board, where 0 = empty space, 1 = black stone, 2 = white stone, 3 = border
    move_history (tuple array): list of moves played + which player played the move eg) 1. B d4
    player (int): the current player. default is 1 (black)
    opponent (int): the opponent. default is 2 (white)
    ruleset (int): the rules being used by the game. default is 1 (tournament rules). can be changed to 2 (casual rules)
    black_capture_count (int): the number of captures black has made in the current game
    white_capture_count (int): the number of captures white has made in the current game
    black_win (bool): False if black has not won, True if black has won
    white_win (bool): False is white has not won, True is white has won
    draw (bool): False if game is not a draw, True if game is a draw
    user_inp (str): input retrieved from user after prompt for a command
    command (list): the command the user entered. first value is the command, second value would be additional arguments
    check_result (bool): True if command entered is valid, False if not

Commands:

    boardsize:
    
        calls commands.boardsize_cmd to get new boardsize as per user input
        
        if boardsize change is successful, board and info is reset, new board created
        
        Variables:
            success (bool): True if boardsize change is valid, False if not
        
    reset:
        
        resets board and game information
        
    quit:
    
        kills program
        
    genmove:
    
        if game is ongoing, generates and plays random move for current player using commands.genmove_cmd
        
    play:
    
        if game is ongoing, multiple cases:
            1. black is to play and it is the first move of the game
                black is forced to play center of the board as per rules.
                error message if center of board is not entered by player
            2. case 1 is false and tournament rules are in use
                uses utility.tournament_rule_check to see if move entered is legal.
                if move entered is legal, move is played using commands.play_cmd.
                if move entered is illegal, error message
            3. case 1 is false and casual rules are in use
                uses commands.play_cmd to play move entered by player
                
        Variables:
            pos (int): board index of center point
            center (str): point form of center point eg) 'd4'
            check (bool): True if move entered is legal within tournament rules, False if not
    
    commands:
        
        displays all commands within str array commandlist
        
    emptyspaces:
    
        uses commands.emptyspaces_cmd to display all remaining empty spaces on the board
        
    ptm:
    
        if game is ongoing, uses commands.ptm_cmd to display current player-to-move
        
    changeptm:
    
        if game is ongoing, uses commands.changeptm_cmd to change the current player-to-move
        
        Variables:
            inp (str): argument entered along with initial command
            
    winner:
    
        uses commands.winner_cmd to display current status of game
        
    showboard:
    
        uses utility.show_board to display the current board
        
    capturecounts:
    
        uses commands.capturecounts_cmd to display current capture counts for each player
        
    playcpugame:
    
        if 
