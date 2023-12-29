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
		- cell 				-
		- table 				-
			- subgroups		-
		- puzz generator	/
		- nav					-
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

`~~~~~~~~~~`

## Hierarchy
```txt

<Main>----(Table)-------,-------
			  /   \			|       \
		[sudoku]	[cell] [nav]	 [UI]

```
- Main() runs the entire app
- Table() contains the subgroups, access the sudoku() (generator) and each cell(), handles the nav and so as the UI

`~~~~~~~~~~`

Move Execution
```txt
# pseudo

if clicked a cell:
	cell_coor = (cell.row, cell.col)
	cell_answer = get_cell_from_pos(table, cell_coor)
	if cell.value == 0 or cell.value != cell_answer.value:
		keys = pygame.key.get_pressed()

		if self.guess_mode == True and keys.unicode not in cell.guesses:
			cell.guesses.append(keys.unicode)

		elif self.guess_mode == False and cell.value == 0:
			cell.value = keys.unicode

```

`~~~~~~~~~~`

To Plan

### Table()
- click_nums_below
- modes() method (guess_mode on/off)
	~ toggle button - if on and clicked; off, if off and clicked; on
	~ if on; cell.guesses[num - 1] = num
	~ if off and clicked_cell.value != 0; cell.value = num, cell.guesses.clear()
- erase() method
	~ if cell.value != 0 and not cell.is_correct_guess; cell.value = 0

### Cell()
- display guesses
	~ if cell.value == 0; blit cell.guesses
	~ elif cell.value != 0; blit cell.value
- font color for different guessing mode
	~ if cell.value != 0 and not cell.is_correct_guess; font_color = pygame.Color("red")
	~ if len(cell.guesses) > 0;
		font_color = pygame.Color("gray") 
		font_size = cell_size // 3
		text_direction (different for each guess)
			for  num in cell.guesses:
				text_dir = abs_x + (font_size * num), 

`~~~~~~~~~~`

### Adding Guesses on guess value list (specific for each tile)
```python

gv = [0,0,3,4,0,0,7,8,0]

for x in range(len(gv)):
	if gv[x] == 0:
		gv[x] = x +1

print(gv)

```