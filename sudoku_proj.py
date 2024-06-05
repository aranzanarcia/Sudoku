#!/usr/bin/env python
# coding: utf-8

# In[194]:


def display_board(board):
    """Display the Sudoku board in a user-friendly format.
    Parameters:
        board (list of lists): The Sudoku board represented as a list of lists.
    Returns:
        None
    """
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("-" * 21)  # Print horizontal separator after every 3 rows
        for j in range(len(board[i])):
            if j % 3 == 0 and j != 0:
                print("|", end=" ")  # Print vertical separator after every 3 columns
            if board[i][j] == "":
                print(" ", end=" ")
            else:
                print(board[i][j], end=" ")
        print()  # Move to the next line after printing each row


# In[177]:


def rules_sdk ():
    return ("\nWELCOME TO SUDOKU\nIn this game you need to use logic to fill in a 9x9 grid so that each column, horizontal row,\nand 3x3 subgrid has digits 1-9 without repeating\n\n")


# In[178]:


def bold(type):
    import sys
    sys.stdout.write("\033[1m" + type + "\033[0m")


# In[179]:


def is_valid_move(board, row, col, num):
    """ Check if placing a number at a specific position on the Sudoku board violates any Sudoku rules.
    Parameters:
        board (list of lists): The Sudoku board represented as a list of lists.
        row (int): The row index where the number will be placed.
        col (int): The column index where the number will be placed.
        num (int): The number to be placed on the Sudoku board.
    Returns:
        bool: True if the move is valid, False otherwise.
    """
    # Check if the number already exists in the same row
    if num in board[row]:
        return False
    # Check if the number already exists in the same column
    for i in range(9):
        if board[i][col] == num:
            return False
    # Check if the number already exists in the same 3x3 box
    box_row = row // 3 * 3
    box_col = col // 3 * 3
    for i in range(3):
        for j in range(3):
            if board[box_row + i][box_col + j] == num:
                return False
    
    return True


# In[180]:


def get_user_move():
    """Prompt the user to enter the row, column, and number they want to place on the Sudoku board.
    Returns:
        tuple: A tuple containing the row, column, and number entered by the user.
    """
    while True:
        try:
            # Prompt the user for row, column, and number
            row = int(input("Enter the row number (1-9): ")) - 1  # Subtract 1 to convert to 0-based index
            col = int(input("Enter the column number (1-9): ")) - 1  # Subtract 1 to convert to 0-based index
            num = int(input("Enter the number (1-9): "))
            
            # Check if row, column, and number are within valid range
            if 0 <= row <= 8 and 0 <= col <= 8 and 1 <= num <= 9:
                return row, col, num
            else:
                print("Invalid input! Please enter numbers within the specified range.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")


# In[181]:


def check_solution(board):
    """
    Check if the Sudoku board represents a valid solution to the puzzle.
    Parameters:
        board (list of lists): The Sudoku board represented as a list of lists.
    Returns:
        bool: True if the board is a valid solution, False otherwise.
    """
    # Check rows
    for row in board:
        if not is_valid_set(row):
            return False
    # Check columns
    for col in range(9):
        column = [board[row][col] for row in range(9)]
        if not is_valid_set(column):
            return False
    # Check 3x3 boxes
    for row_start in range(0, 9, 3):
        for col_start in range(0, 9, 3):
            box = [board[i][j] for i in range(row_start, row_start + 3) for j in range(col_start, col_start + 3)]
            if not is_valid_set(box):
                return False
    return True

def is_valid_set(nums):
    """
    Check if a set of numbers (a row, column, or 3x3 box) contains valid Sudoku numbers.
    Parameters:
        nums (list): The set of numbers to be checked.
    Returns:
        bool: True if the set is valid, False otherwise.
    """
    num_set = set(nums)
    return len(num_set) == 9 and all(num in num_set for num in range(1, 10))


# In[182]:


def check_board_complete(board):
    """
    Check if the Sudoku board is completely filled with numbers.
    Parameters:
        board (list of lists): The Sudoku board represented as a list of lists.
    Returns:
        bool: True if the board is complete, False otherwise.
    """
    for row in board:
        for cell in row:
            if cell == " ":
                return False  # If any cell is empty, the board is not complete
    return True


# In[183]:


def undo_last_move(board, history):
    """
    Undo the last move made by the player on the Sudoku board.
    Parameters:
        board (list of lists): The Sudoku board represented as a list of lists.
        history (list): A list containing the history of moves made by the player.
    Returns:
        None
    """
    
    row, col, prev_num = history.pop()  # Retrieve the last move from the history
    board[row][col] = " "
    return board


# In[184]:


undo_last_move(board, [(0, 1, 3)])


# In[185]:


history


# In[186]:


(row, col, num)


# In[187]:


board


# In[188]:


# Assuming row, col, and num represent the row index, column index, and number placed by the player
prev_num = board[row][col]  # Get the number previously present in the cell
history.append((row, col, prev_num))  # Add the move to the history list


# In[189]:


def reset_board(board):
    """
    Reset the Sudoku board to its initial state.

    Parameters:
        board (list of lists): The Sudoku board represented as a list of lists.

    Returns:
        None
    """
    board = generate_partially_filled_sudoku()
    ###for row in range(len(board)):
        ###for col in range(len(board[row])):
            ###board[row][col] = " "
            


# In[193]:


import random

def generate_sudoku_board4():
    board = [[0] * 9 for _ in range(9)]

    def is_valid_move(row, col, num):
        # Check if the number is already in the row
        if num in board[row]:
            return False
        
        # Check if the number is already in the column
        if num in [board[i][col] for i in range(9)]:
            return False
        
        # Check if the number is already in the 3x3 subgrid
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == num:
                    return False
        
        return True

    def solve_sudoku():
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    for num in random.sample(range(1, 10), 9):
                        if is_valid_move(row, col, num):
                            board[row][col] = num
                            if solve_sudoku():
                                return True
                            board[row][col] = 0
                    return False
        return True

    solve_sudoku()
    return board

def generate_partially_filled_sudoku():
    sudoku_board = generate_sudoku_board4()
    for _ in range(13):
        row = random.randint(0, 8)
        col = random.randint(0, 8)
        sudoku_board[row][col] = " "
    return sudoku_board
        
bold (rules_sdk())

partially_filled_board = generate_partially_filled_sudoku()
board = partially_filled_board

while True:
    
    history = []
    
        # Display the Sudoku board
    display_board(board)
    print ("\n")

        # Get user move
    row, col, num = get_user_move()
    print ("\n")

        # Check if the move is valid
    if is_valid_move(board, row, col, num):
        board[row][col] = num
        history.append((row, col, num))  # Store the move in history
        print ("\n")
        display_board(board)
        
    else:
        print("\nInvalid move! Please try again.\n")
        continue  # Ask for input again
        
    # Check if the board is complete
    if check_board_complete(board):
        bold("\n🎉Congratulations! You solved the sudoku.🎉")
        break  # Exit the game loop if the puzzle is solved
        
    undo_move = input("Do you wanna undo your last move? Y/N: ")
    if undo_move.lower().startswith("y"):
        board = undo_last_move(board, history)
    else:
        print ("\n")
        pass
    
    reset_b = input("Do you wanna reset the board to start a new game? Y/N: ")
    
    if reset_b.lower().startswith("y"):
        reset_board(board)
    else:
        print ("\n")
    

        


# In[ ]:





# 
