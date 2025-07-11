# version 3 - cli input vs computer?! added support for a rand_ai player

'''
Next steps: 
- Reorganizing code for n*n grid
- Look into bitmasking implementation for win_check of n*n grid
'''

from typing import List
import random

def play():
    gameGrid = [None] * 9
    current_player = 1 # player 1 - X, player 2 - O
    turn_counter = 0
    game_won = False

    print("Welcome to a new round of tic-tac-toe!")
    game_mode = input("Would you like to play against a computer (C) or a friend (F)?") #TODO: Input validation

    # max 9-turn game initiated
    while turn_counter < 9:

        # prints grid
        printGrid(gameGrid)

        if current_player == 1 or game_mode == "F":
            # gets player input for turn
            turn_input = input(f"Player {current_player}, enter a position 1-9: ")
            while not isValidInput(turn_input, gameGrid):
                turn_input = input(f"Invalid input! Try again: ")
        else:
            # gets computer input for turn
            turn_input = getRandomMove(gameGrid) # turn_input
        
        # updates gameGrid [X or O] depending on curr_player
        if current_player == 1:
            gameGrid[int(turn_input)-1] = "X"
        else: 
            gameGrid[int(turn_input)-1] = "O"

        # checks if winning combo hit
        if winCheck(gameGrid):
            game_won = True
            printGrid(gameGrid) # NOTE: think about way to cross out winning streak in CLI? 
            print(f"Player {current_player} won!")
            break

        # update ctrs
        turn_counter += 1
        current_player = 1 if current_player == 2 else 2

        # NOTE: introduce press 'q' to quit option when clearly reached a draw before exhausting all boxes?

    if not game_won:    
        print("Draw!")

def getRandomMove(gameGrid) -> int:
    null_indices = []
    # determine indices of null spots in array
    for idx, cell in enumerate(gameGrid):
        if cell is None:
            null_indices.append(idx)
    # randomly choose between them & return that as turn_input
    return random.choice(null_indices) + 1

def printGrid(gameGrid: List) -> None:
    display = []
    for idx, cell in enumerate(gameGrid):
        if cell is None: display.append(idx + 1)
        else: display.append(cell)
        
    print(f" {display[0]} | {display[1]} | {display[2]} \n---|---|--- \n {display[3]} | {display[4]} | {display[5]} \n---|---|--- \n {display[6]} | {display[7]} | {display[8]} \n")

def isValidInput(turn_input, gameGrid: List) -> bool:
    try:
        if int(turn_input) > 0 and int(turn_input) < 10 and gameGrid[int(turn_input)-1] is None:
            return True
        return False
    except:
        return False

def winCheck(gameGrid: List) -> bool:  
    # NOTE: see if more optimal way than for loop thru all winning combos (# of rows + # of cols + 2 for diag), esp for n*n scaled game > bit masking??
    winning_combos = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], 
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]]

    for combo in winning_combos:
        if (gameGrid[combo[0]] is not None and 
            gameGrid[combo[0]] == gameGrid[combo[1]] == gameGrid[combo[2]]):
            return True
    return False

play()
