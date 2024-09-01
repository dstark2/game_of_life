# The Game of Life
The Game of Life, devised by John Conway in 1970, is a cellular automaton where a grid of cells evolves through discrete time steps based on simple rules. Each cell can either be alive or dead, and its next state depends on the number of live neighbors. It is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves.

## Overview
The Game of Life is played on a two-dimensional grid of cells. Each cell is in one of two possible states: alive or dead. The state of each cell in the grid changes from one generation to the next based on a set of rules that examine the states of neighboring cells. The grid can simulate various patterns over time, some of which remain stable, some oscillate, and others grow infinitely.

## Rules of the Game
The Game of Life is governed by four simple rules that determine the fate of each cell in the grid:

### Underpopulation: 
A live cell with fewer than two live neighbors dies (as if by underpopulation).

### Survival: 
A live cell with two or three live neighbors lives on to the next generation.

### Overpopulation: 
A live cell with more than three live neighbors dies (as if by overpopulation).

### Reproduction: 
A dead cell with exactly three live neighbors becomes a live cell (as if by reproduction).


## Implementation Details

This Python implementation uses the numpy and matplotlib libraries to create and display the Game of Life grid.

### Key Components
#### Grid Initialization: 
The grid is initialized randomly based on a specified probability for each cell to be alive.
#### Grid Update Function: 
The grid is updated according to the rules of the Game of Life, marking cells that are about to die or be born.
#### Animation: 
The simulation is animated using Matplotlib's FuncAnimation to visualize the evolution of the grid over generations.
#### Stopping Condition:
The simulation runs until a stable state is reached, where no cells change state from one generation to the next. Once stability is detected, the generation count stops incrementing, and the generation number at which stability was reached is printed.