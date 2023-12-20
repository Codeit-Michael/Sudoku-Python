# Sudoku

- What
	Detes
	- puzzle with tables and numbers

- Why
	Mechanics
	- has to complete filling the table in able to win
	- write on the cell what number you think is destined for the said cell
	- you were given lives that allows you to continue playing
	- you can wrote directly the number to  a chosen cell by switching "guess" to "off"
	- If you are not sure with the number input, you can switch "guess" to "on"
	- You can put more than 1 guess numbers in a cell as long as it don't exist on the plain/subgroup
	- by switching again to "Guess: off" mode, you can write directly both in cells with guesses, those numbers will be erased/ replaced once you type a number.
	- scores will be defined as the time, on how fast did you finish solving it

	Rules
	- the number to be filled in each cell should not repeated on the same plain (vertical/horizontal alignment) or subgroup
	- each error guess will deduct you life
	- fault placed numbers will be highlight colored so you can easily identify where did you go wrong
	- no more life left = game over

- How
	Requirements
	- Pygame
		Parts
		- cell
		- table
			- subgroups
		- puzz generator
	Approach
	ERV
	Pseudo
	Actual coding



`~~~~~~~`
## Sudoku Generator Algorithm
1. Fill all the diagonal 3x3 matrices.
2. Fill recursively rest of the non-diagonal matrices. For every cell to be filled, we try all numbers until we find a safe number to be placed.  
3. Once matrix is fully filled, remove K elements
   randomly to complete game.
