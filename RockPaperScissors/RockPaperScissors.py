#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random
from enum import Enum
from datetime import datetime

class Symbol(Enum):
    rock = "Rock"
    paper = "Paper"
    scissors = "Scissors"

class Result(Enum):
    draw = "Draw"
    win = "Win"
    lose = "Lose"

def decide(userSymbol, oponentSymbol):
    if oponentSymbol == userSymbol:
        return Result.draw
    else:
        if userSymbol == Symbol.rock:
            if oponentSymbol == Symbol.paper:
                return Result.lose
            elif oponentSymbol == Symbol.scissors:
                return Result.win
        elif userSymbol == Symbol.paper:
            if oponentSymbol == Symbol.scissors:
                return Result.lose
            elif oponentSymbol == Symbol.rock:
                return Result.win
        elif userSymbol == Symbol.scissors:
            if oponentSymbol == Symbol.rock:
                return Result.lose
            elif oponentSymbol == Symbol.paper:
                return Result.win
    raise ValueError

def main():
    random.seed(datetime.now())

    chosenSymbol = input("Choose symbol: rock, paper, scissors: ")
    userSymbol = Symbol[chosenSymbol]

    computerSymbol = random.sample((Symbol.rock,Symbol.paper,Symbol.scissors),1)[0]
    print("Computer choice: {}".format(computerSymbol.value))

    result = decide(userSymbol, computerSymbol)
    print(result.value)
    
if __name__ == "__main__":
    main()