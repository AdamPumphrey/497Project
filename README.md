# 497Project
UAlberta CMPUT 497 Project - Pente Random Player

Built with Python 3

Runs out of command line (for now)

Commands:

    boardsize - resets game and creates new board with specified boardsize
  
        usage: boardsize <int>  
        
            <int> must be between 5 and 19 (5 <= <int> <= 19)  eg) boardsize 7
            
            reasoning for 5-19: 5x5 is smallest board possible, 19x19 is the traditional size board
        
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
            
Error Messages:

    command does not exist - the command entered is not in the existing command list
    
    command requires additional input - the command entered requires an argument
    
    incorrect amount of input for command - the command entered does not require an argument
    
    illegal move - move specified violates the rules of the game
    
    boardsize must be an integer between 5 and 19 - boardsize specified is not within the correct range
    
    board location syntax incorrect - move specified is not formatted correctly
    
    board location out of bounds - move specified is off of the board

Rules of Pente:

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
    
        this program uses tournament rules
        
        only difference is that the first player's second move must be at least 3 spaces away from center
        
    For more information about Pente, please consult https://www.pente.net/instructions.html or https://en.wikipedia.org/wiki/Pente
