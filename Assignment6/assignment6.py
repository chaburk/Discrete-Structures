"""
Author: Chase Burkdoll
KUID: 3082972
Date: 10/27/2022
Assignment: Assignment 6
Last modified: 10/30/2022
Purpose: Sudoku solver using backtracking
"""

def open_file(file_name): #function declaration to open a file and return a formatted board
    file = open(file_name) #declare variable to hold file
    board = [line.split() for line in file] #list comprehension to put file input into a list
    for i in range(len(board)): #outer for loop to go through the list
        for j in range(len(board)): #inner for loop to go through the list
            if board[i][j] != '_': #if statement to check if list location is not an empty space
                board[i][j] = int(board[i][j]) #turn the string into an integer
    return board #return the board from an input file

def print_board(board): #function declaration to print the sudoku board
    for i in range(0, 9): #outer for loop that goes from 0 to 8
        for j in range(0, 9): #inner for loop that goes from 0 to 8
            print(board[i][j], end=" ") #print statement to print each index and at the end of a row start new line
        print()#print statement for formatting

def valid(row, col, board, value): #function declaration to check if a spot on the board is valid to put a certain number
    #Check Row
    for i in range(9): #for loop that goes from 0 to 8
        if board[row][i] == value: #checks if the current number we're checking is in the row
            return False #if the number is already in the row return False

    #Check Column
    for j in range(9): #for loop that goes from 0 to 8
        if board[j][col] == value: #checks if the current number we're checking is in the column
            return False #if the number is already in the column return False
    
    #Check Box
    startRow = row - row % 3 #equation to get the starting row for the box we are in
    startCol = col - col % 3 #equation to get the starting row for the box we are in
    for i in range(3): #outer for loop to check every location in our box
        for j in range(3): #inner for loop to check every location in our box
            if board[startRow+i][startCol+j] == value: #checks if the current number we're checking is in the box
                return False #if the number is already in the box return False

    return True #return True if the number is not in the box, column, or row

def solve(row, col, board): #function declaration to solve sudoku recursively 
    if (row == 8 and col == 9): #if statement to check if we've reached the end of the puzzle
        return True # return true if we reached the end of the puzzle without any error
    
    if col == 9: #if statement that checks if we've reached the end of a row
        row += 1 #move to the next row
        col = 0 #move to the first element of the new row

    if board[row][col] != '_': #If statement that checks if the square is empty or not
        return solve(row, col + 1, board) #move to the next square if the square is not empty

    for value in range(1, 10): # for loop that inputs which value we're trying to input in the square
        if valid(row, col, board, value): #checks if that square is valid with the input number
            board[row][col] = value #if it is valid then make the value of the square the input number
            if solve(row, col +1, board): #if statement that recursively calls the function to the next square
                return True #return True if the number works

        board[row][col] = "_" #if the input number is not valid then reset the square back to empty
    return False #if the value does not work return False and try a different value

def print_solution(puzzle): #function declaration to print the solutions
    board = open_file(f'{puzzle}.txt') #function call to get the board for the puzzle
    if solve(0,0, board): #function call to check if the puzzle is solvable
        print_board(board) #function call to print the board
        print() #print statement to add spacing
    else: #if the puzzle is not solvable
        print("no solution") #print statement telling the user the puzzle is not solvable
        print() #print statement to add spacing


print('   PUZZLE ONE') #print statement to say which puzzle
print('|---------------|') #print declaration to add formatting
print_solution("puzzle1") #function call to print the solution
print('   PUZZLE TWO') #print statement to say which puzzle
print('|---------------|') #print declaration to add formatting
print_solution("puzzle2") #function call to print the solution
print('   PUZZLE THREE') #print statement to say which puzzle
print('|---------------|') #print declaration to add formatting
print_solution("puzzle3") #function call to print the solution
print('   PUZZLE FOUR') #print statement to say which puzzle
print('|---------------|') #print declaration to add formatting
print_solution("puzzle4") #function call to print the solution
print('   PUZZLE FIVE') #print statement to say which puzzle
print('|---------------|') #print declaration to add formatting
print_solution("puzzle5") #function call to print the solution