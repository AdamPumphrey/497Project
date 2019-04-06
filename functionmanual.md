# pente.py

Only function is main( ), but split up by command.

For descriptions of commands, see README.

Variables in this section will only be listed under commands if they are local to that command section of main
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
    
        resets board and info, asks user to choose player for black - Random player or Heuristic player.
        if input is valid, asks user to choose player for white - Random player or Heuristic player.
        if input is valid, four cases:
            1. black and white are using random player
                while game is ongoing, both black and white use commands.genmove_cmd to generate and play random moves
            2. black uses heuristic, white plays random
                while game is ongoing, black obtains its move using commands.current_position_evaluation, and plays the move
                using commands.play_cmd.
                white generates and plays its move using commands.genmove_cmd
            3. black plays random, white uses heuristic
                while game is ongoing, black generates and plays its move using commands.genmove_cmd.
                white obtains its move using commands.current_position_evaluation, and plays the move using
                commands.play_cmd
            4. black and white are using heuristic
                while game is ongoing, black and white obtain their moves using commands.current_position_evaluation,
                and plays their moves using commands.play_cmd
                
        Variables:
            inp1 (str): user-entered choice of player for black
            inp1check (bool): True if input entered for inp1 is valid, False if not
            inp2 (str): user-entered choice of player for white
            inp2check (bool): True if input entered for inp1 is valid, False if not
    
    movehistory:
        
        uses commands.movehistory_cmd to display move history of current game
        
    changerules:
    
        changes value of ruleset depending on user input, then resets board and info
        depending on user input, three cases:
            1. user enters 1
                ruleset is changed to Tournament Rules
            2. user enters 2
                ruleset is changed to Casual Rules
            3. user enters c
                ruleset change is cancelled, nothing is reset
        
        Variables:
            arg (str): user-entered choice of ruleset to use
            argcheck (bool): True if input entered for arg is valid, False if not
            
    rules:
    
        uses utility.check_ruleset to display current ruleset in use
        
    startgame:
    
        uses commands.startgame_cmd to initiate a player vs. cpu game
        
    poseval:
    
        if game is ongoing, uses commands.current_position_evaluation to evaluate current board position for
        player-to-move
        
# commands.py

boardsize_cmd:

    input:
        command (tuple): command entered by user, in form of ('boardsize', <int>)
        board (int array): current board in use
        boardsize (int): current boardsize
        move_history (tuple array): history of moves for current game
        
    variables:
        new_boardsize (int): two cases:
            1. boardsize entered by user is valid
                new_boardsize contains that value
            2. boardsize entered by user is invalid
                new_boardsize contains 1
                
    1. checks to see if input entered by user is valid (contains two values - ['boardsize', <int>]
        a. if input is invalid, uses utility.show_board to display current board, does not change anything,
           returns old board, boardsize, move_history, False (boardsize change did not occur)
        b. if input is valid, moves to step 2
    2. uses utility.boardsize_change to change boardsize
        a. if return value from utility.boardsize_change is 1, change did not occur,
           returns old board, boardsize, move_history, False
        b.
