# Initial scratchpad brainstorming tic-tac-toe game engine requirements & possible code org/helper functions

print("Welcome to Tic tac toe v1!")

'''
tic-tac-toe 
- need a 3 by 3 grid
- 2 players - each player alternates turns
- once a grid spot isMarked, can't overwrite

2 players playing in a terminal
print 
  1 | 2 | 3
  4 | 5 | 6
  7 | 8 | 9

don't need 2D array structure, single-array in our blackbox 9*[null]

for statement that runs 9 times OR till game won:

    get player input alternatingly:
    print- Player 1, choose a number to make a move:
    TODO: player alternation logic (hacky back-and-forth? like if p0, then p1?) 
    TODO: player state (apart from storing moves)

    - if p1 & valid input > update non-null index to X
    - if p2 & valid input > update non-null index to O

    valid input check:
    - make sure not overwritten: if # non-null, ask player to select another box
    - + more input validation > if not 1-9, ask for valid input again
    
    
    - if win condition met: return Player1Win / Player2Win
    TODO: how to determine win condition
    winning_index_combinations - if either X OR O in this configs
    0, 1, 2, 3, 4, 5, 6, 7, 8
      0 | 1 | 2
      3 | 4 | 5
      6 | 7 | 8

      rows -
      0, 1, 2
      3, 4, 5
      6, 7, 8

      cols -
      0, 3, 6
      1, 4, 7
      2, 5, 8

      diags - 
      0, 4, 8
      2, 4, 6

      but how to ignore  state of other indices that may not be relevant? some regex format?
      reduplicate for X and O or simpler way?
      and more optimal way to do winCheck than switch statements?


    - return winning player if won (how stored? just return curr_player?)

reaches end - return Draw

decompose functions: 
main func -
    variables- gameGrid, curr_player, turn_counter
    # curr_player = whichPlayer(turn_counter)
    gameGrid = 9*null
    current_player = 1
    turn_counter = 0

    within main - whichPlayer logic, 
    prints grid (function call)
    prompts input for player in while loop till isValidInput - takes valid input, 
    updates gameGrid [X or O depending on curr_player; X if curr_player = 1 and O if player2],
    alternates player turns by incremented turn_counter logic (NOTE: current_player = 1 if turn_counter % 2 == 0 else 2)
    
    > calls

    NOTE: remapping 0-8 indices to 1-9 board inputs / or easier way? > gameGrid[input-1]

# INLINE - whichPlayer(turn_counter) - needed or within main? (turns 0, 2, 4, 6, 8 are p1 / turns 1, 3, 5, 7, 9 are p2)
#     NOTE: if turn_counter % 2 == 0: 
#         return 1
#     return 2

isValidInput(input, gameGrid[List[int]], curr_player[int])
    NOTE: don't need curr_player parameter here - checking: input is 1-9, and NOTE: gameGrid[input-1] is None
    TODO: if not validInput, reprompt logic - here or in main?

printGrid(gameGrid) - needed or within main?
    print(gameGrid)

winCheck(gameGrid[List[int]], curr_player) function - to check if curr grid has winning combo
    TODO: see if more optimal way than for loop thru all 8 winning combos
    NOTE: Rather than regex, store as a list of tuples/lists? How would this work?
    NOTE: For checking: instead of duplicating for X and O, check if all three positions in a winning combo contain the same symbol (and aren't null) -- have to do for loop thru gamGrid to see of satisfies 8 times? Or more optimal?
'''

