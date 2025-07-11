# version 1 that prints empty grid and has commented but unimplemented 
game logic

from typing import List

def main():
    gameGrid = [None] * 9 # TODO: change 1-9
    current_player = 1 #X
    turn_counter = 0

    print("Welcome to a new round of Tic tac toe!")

    while turn_counter < 9:
        printGrid(gameGrid)
        # prompts input for player in while loop till isValidInput - takes 
valid input, 
        # updates gameGrid [X or O depending on curr_player; X if 
curr_player = 1 and O if player2], > gameGrid[input-1]
        # if winCheck() is True: print(f"Player {current_player} won!")
        turn_counter += 1
        # alternates player turns by incremented turn_counter logic (NOTE: 
current_player = 1 if turn_counter % 2 == 0 else 2)
        
    print("Draw!")
    # NOTE: remapping 0-8 indices to 1-9 board inputs / or easier way? > 
gameGrid[input-1]

def printGrid(gameGrid: List) -> None:
    # TODO: Display 1-9 numbers if empty somehow??
    print(f" {gameGrid[0]} | {gameGrid[1]} | {gameGrid[2]} \n 
{gameGrid[3]} | {gameGrid[4]} | {gameGrid[5]} \n {gameGrid[6]} | 
{gameGrid[7]} | {gameGrid[8]} \n")

def isValidInput(input, gameGrid: List) -> bool:
    if input > 0 and input < 10 and gameGrid[input-1] is None:
        return True
    return False

def winCheck(gameGrid: List) -> bool:
    # TODO: see if more optimal way than for loop thru all 8 winning 
combos
    # NOTE: Rather than regex, store as a list of tuples/lists? How would 
this work?
    # NOTE: For checking: instead of duplicating for X and O, check if all 
three positions in a winning combo contain the same symbol (and aren't 
null) -- have to do for loop thru gamGrid to see of satisfies 8 times? Or 
more optimal?

    #     return True - if win (no player)
    # return False - if no win
    pass

main()
