# version 2 - working cli input vs cli input

from typing import List

def main():
    gameGrid = [None] * 9
    current_player = 1 # player 1 - X, player 2 - O
    turn_counter = 0

    print("Welcome to a new round of tic-tac-toe!")

    # max 9-turn game initiated
    while turn_counter < 9:

        # prints grid
        printGrid(gameGrid)

        # gets player input for turn
        turn_input = input(f"Player {current_player}, enter a position 1-9: ")
        while not isValidInput(turn_input, gameGrid):
            turn_input = input(f"Invalid input! Try again: ")
        
        # updates gameGrid [X or O] depending on curr_player
        if current_player == 1:
            gameGrid[int(turn_input-1)] = "X"
        else: 
            gameGrid[int(turn_input-1)] = "O"

        # checks if winning combo hit
        if winCheck(gameGrid) is True:
            print(f"Player {current_player} won!")
            break

        # update ctrs
        turn_counter += 1
        current_player = 1 if turn_counter % 2 == 0 else 2
        
    print("Draw!")

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
    # NOTE: For checking - instead of duplicating for X and O, check if all three positions in a winning combo contain the same non-null symbol -- have to do for loop thru gameGrid to see if satisfies 8 times (# of rows + # of cols + 2 for diag) - more optimal way?
    # NOTE: see if more optimal way than for loop thru all 8 winning combos > bit masking??

    #     return True - if win (no player)
    # return False - if no win
    pass

main()
