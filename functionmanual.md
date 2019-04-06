# Pente.py

Only function is main( ), but split up by command.

For descriptions of commands, see README.

Variables:

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
    command (str): the command the user entered
    check_result (int):

    boardsize:
    
        calls commands.boardsize_cmd to get new boardsize as per user input
        
        if boardsize change is successful, board and info is reset, new board created
        
    reset:
        
        
