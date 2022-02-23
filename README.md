# 8-tile

Implemented **DFS**, **IDS** and **A-star** algorithms on the 8-tile problem.

# About the Problem

The 8-tile puzzle is a 3x3 grid with numbers 1-8 and one blank space. The objective of the puzzle is to move the tiles such that a goal state is reached given a specific starting state.

Below are the rules around which the puzzle should be solved:

- Can only move tiles to adjecent spots.

- Tile can be moved in only if the adjecent tile is blank

Possible Moves are:

- Move UP

- Move DOWN

- Move RIGHT

- Move LEFT

# How to run the code

Run the following command in the command line

**8-tile.py <algorithm_name> <file_name>**

The alogorithm_name can take the following values

- dsf – depth first search
- ids – Iterative deepening search
- astar1 – A star search using heuristic 1 (Manhattan Distance)
- astar2 – A star search using heuristic 2 (Number of Misplaced Tiles)

# Text file containing start state

Enter a single space separated list of values from 1-8 and 0(indicating blank cell) in any order.

Eg: 8 1 3 7 2 4 0 6 5
