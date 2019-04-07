# 497Project
UAlberta CMPUT 497 Project - Pente Random/Heuristic Player

Built with Python 3

Runs out of command line (for now)

Easiest way to setup is to download ZIP of repository.
File to run is pente.py inside of code folder.
Other files (utility.py, commands.py, heuristic.py) contain code/functions relevant to their filename.

# Rules of Pente:

    Win conditions:
    
        creating a 5-in-a-row with your stones
        
        capturing 5 or more pairs of opponent's stones (5 or more captures)
        
        game ends immediately when one of the conditions is met
        
    Play:
    
        black plays first, must play center point for first move
        
        alternating turns
        
        stones cannot be moved once placed except for capture
        
        if captured, the pair of stones must be removed from the board
        
        if a player creates a 3-in-a-row, player must announce "three" or "tria"
        
        if a player creates a 4-in-a-row, player must announce "four" or "tessera"
        
    Capturing:
    
        captures only occur when two (and only two) adjacent stones are flanked by two opposing stones
        
            eg) X O O X
        
        captures can be made in any direction, and singular move can create multiple captures
        
        suicide (putting your own stones in a capture position) does not exist
        
            eg) X - O X, O places their stone in the middle, their stones cannot captured by the existing X's --> X O O X
            
    Tournament Rules:
    
        this program uses tournament rules by default
        
        only difference is that the first player's second move must be at least 3 spaces away from center
        
        the option to change rules is available with the 'changerules' command:
        
            changing the rules to 'Casual' allows first player to make their second move without tournament restriction
            
            the game will reset every time the ruleset is changed using the 'changerules' command, unless cancelled
        
For more information about Pente, please consult https://www.pente.net/instructions.html or https://en.wikipedia.org/wiki/Pente

# Commands:

    boardsize - resets game and creates new board with specified boardsize
  
        usage: boardsize <int>  
        
            <int> must be odd integer between 7 and 19 (7 <= <int> <= 19)  eg) boardsize 9
            
            reasoning for 7-19: 7x7 is smallest board possible for tournament rules.
                                19x19 is the traditional size board.
                                odd integer to ensure that a center point exists
        
        output: Current board: <board>
        
    reset - creates a new game
    
        usage: reset
        
        output: Current board: <board>
   
    quit - exits the program
    
        usage: quit
        
        output: Shutting down... 
        
    genmove - generates a random move for the player-to-move
    
        usage: genmove
        
        output: <player> played <move> (usage error, captures, end of game possible outputs as well)
        
    play - plays the specified move for the player-to-move
    
        usage: play <str>  eg) play c3
        
            the move specified must be in the format of <letter><number> as shown in example
        
        output: <player> played <move> (usage error, captures, end of game possible outputs as well)
        
    commands - lists existing commands 
    
        usage: commands
        
        output: <command> <command> etc...
        
    emptyspaces - lists remaining empty spaces on board
    
       usage: emptyspaces
       
       output: <space> <space> etc...
      
    ptm - displays the current player-to-move
    
        usage: ptm
        
        output: It is <player>'s turn (end of game notification also possible)
        
    winner - displays current status of game
    
        usage: winner
        
        output:
        
            if a player has won: <player> is the winner!
            if the game is a draw: The game is a draw
            if the game is still in progress: Game is still ongoing
    
    showboard - displays the current board
    
        usage: showboard
        
        output: Current board: <board>
        
    capturecounts - displays current amount of captures for each player
    
        usage: capturecounts
        
        output: 
        
            5 or more captures are needed for a capture win
            Black has made <int> capture(s)
            White has made <int> capture(s)
    
    playcpugame - initiates a cpu vs. cpu game of Pente
    
        usage: playcpugame
        
        output:
        
            Choose the player for black. 1 for Random, 2 for Heuristic: <userinput>
            Choose the player for white. 1 for Random, 2 for Heuristic: <userinput>
            <player> played <move>
            Current board: <board>
            
    changeptm - changes the current player-to-move
    
        usage: changeptm <str>  eg) changeptm b
        
        output:
        
            Player to move is now <player>
            
    movehistory - displays move history for entire game or specified player
    
        usage: movehistory <str>  eg) movehistory b
            
            can be used without additional input to display full move history of game
            
            eg) movehistory
        
        output:
        
            1. <player> <move>
            2. <player> <move>
            etc...
    
    rules - displays ruleset for current game
    
        rulesets only effect first player's second move - see "Rules of Pente: for more info
        
        usage: rules
        
        output:
        
            The current ruleset is: <ruleset>
        
    changerules - creates a new game with the specified ruleset, unless command is cancelled
    
        usage: ruleset
        
        output:
        
            Enter 1 for Tournament Rules, enter 2 for Casual Rules, enter c to cancel: <userinput>
            The current ruleset is: <userinput>
            Current board: <board>
    
    startgame - starts a player vs. cpu game with current ruleset and boardsize
    
        usage: startgame
        
        output:
        
            Choose your colour (b for black, w for white, c to cancel): <userinput>
            Choose the player for your opponent. 1 for Random, 2 for Heuristic: <userinput>
            if colour chosen is b:
                Please enter your move, or enter 'quit' to exit: <userinput>
            if colour chosen is w:
                black played d4
                Current board: <board>
                Please enter your move, or enter 'quit' to exit: <userinput>
            if c:
                Game has been cancelled
                Current board: <board>
    
    poseval - evaluates the current board position for the player-to-move
    
        usage: poseval
        
        output:
        
            if initial move:
                black must play d4 to start the game
            if black's second move w/ tournament rules enabled:
                black must play one of the following spaces as per tournament rules: <moves>
            if winning moves exist for player:
                winning moves for <player> are: <moves>
            if opponent has 2 or more winning moves:
                a <player> loss is inevitable. blocking moves would be: <moves>
            if opponent has 1 winning move:
                move that will prevent a <player> loss is <move>
            if player can create an open four:
                <player> can make an open four with <moves>
            if opponent can create an open four:
                <player> can block an open four with: <moves>
            if no heuristic-detected moves exist:
                there are no specific moves to play at this time
            
        for more information on the heuristic used in the evaluation, see the Heuristic section of the README
            
# Error Messages:

    command does not exist - the command entered is not in the existing command list
    
    command requires additional input - the command entered requires an argument, but no argument was provided
    
    command does not require additional input - the command entered does not require an argument, but one was provided
    
    incorrect amount of input for command - too many arguments were provided for the command entered
    
    incorrect input for command - the argument provided is not permitted for the command entered
    
    illegal move - move specified violates the rules of the game
    
    boardsize must be an odd integer between 7 and 19 - boardsize specified is not within the correct range
    
    board location syntax incorrect - move specified is not formatted correctly
    
    board location out of bounds - move specified is off of the board

# Heuristic

    This program uses a simple heuristic to evaluate positions on the board. 
    
    The heuristic works by checking for different moves based on varying priorities.
    
    The heuristic does not consider capturing as part of the evaluation.
    
    Jargon:
    
        "open four" - a winning position for the player eg) - O O O O - 
            
            the opponent cannot block a win here, as O has two moves that result in 5-in-a-row. 
            if a player creates an "open four", that player is guaranteed to win.
    
    Priorities:
    
        1. winning moves
            
            if the current player has a winning move available, the player should play that move
        
        2. blocking opponent winning moves
        
            if the current player cannot immediately win, and can block an opponent win, the player should block the 
            opponent win
        
        3. creating an "open four"
            
            if neither player has any winning moves available, and the current player can create an "open four", 
            the current player should create an "open four"
            
        4. block an "open four"
        
            if neither player has any winning moves available, the current player cannot create an "open four", 
            and the current player can prevent the opponent from creating an "open four", the current player should
            prevent the creation of an opponent "open four"
            
        5. random move
        
            if no specific moves are detected by the heuristic, it will default to a random move
            
    The heuristic can be improved by adding further priorities.
    
    The following priorities (in the following order) could be inserted in between priority 4 and priority 5 above:
        
        1. creating an "open three" (similar to "open fours", just one move away from being an "open four")
            eg) - O O O - 
                O can create an "open four" if the "open three" is left unchecked
        
        2. blocking an "open three"
        
        3. creating an "open two" (again, similar to "open threes", just one move away from being an "open three")
            eg) - O O -
                as the game progresses, the likelihood of this priority being reached decreases.
                more stones on the board, higher chances for wins, blocking wins, "open three/four", 
                lower chance for "open two".
            I consider this priority to be the worst overall, but still better than simply playing a random move, 
            as it is at least working towards a winning position
            
        The three priorities listed above are not implemented in the program (yet).
