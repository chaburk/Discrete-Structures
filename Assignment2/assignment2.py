"""
Author: Chase Burkdoll
KUID: 3082972
Date: 9/07/2022
Assignment: Assignment 1
Last modified: 9/14/2022
Purpose: Prints truth values for predicate statements.
"""


# ∃x P(x), where P(x) is the statement “x<2”
print('1. a)') #print statement that outputs which problem
px = False #initalizing the variable to False for an existential quantifier
for x in range(11): #for loop that loops through the domain 0-10
    if x < 2: #if statement that implements the predicate
        px = True #changes the value of px if the predicate is True
        break #breaks out of the loop if the condition is met
print(px, x, 'proves the assertion', end='\n\n') #print statement that shows the truth value, and the value that proves it

#∀x P(x), where P(x) is the statement “x<2” 
print('b)') #print statement that outputs which problem
px = True #initalizing the variable to True for an Universal quantifier
for x in range(11): #for loop that loops through the domain 0-10
    if not (x < 2): #if statement that implements the predicate
        px = False #changes the value of px if the predicate is False
        break #breaks out of the loop if the condition is met 
print(px, x, 'disproves the assertion', end='\n\n') #print statement that shows the truth value, and the value that disproves it

#∃x (P(x) ∨ Q(x)) where P(x) is the statement “x<2” and where Q(x) is the statement “x>7” 
print('c)') #print statement that outputs which problem
px = False #initalizing the variable to False for an existential quantifier
for x in range(11): #for loop that loops through the domain 0-10
    if (x < 2) or (x > 7): #if statement that implements the predicates
        px = True #changes the value of px if the predicate is True
        break #breaks out of the loop if the condition is met
print(px, x, 'proves the assertion', end='\n\n') #print statement that shows the truth value, and the value that proves it

#∀x (P(x) ∨ Q(x)) where P(x) is the statement “x<2” and where Q(x) is the statement “x>7” 
print('d)') #print statement that outputs which problem
px = True #initalizing the variable to True for an Universal quantifier
for x in range(11): #for loop that loops through the domain 0-10
    if (x > 2) and (x < 7): #if statement that implements the predicates
        px = False #changes the value of px if the predicates are False
        break #breaks out of the loop if the condition is met
print(px, x, 'disproves the assertion', end='\n\n') #print statement that shows the truth value, and the value that disproves it

#Prove De Morgan’s Law for the Existential Quantifier where P(x) is the statement “x<5” 
print('e)') #print statement that outputs which problem
print('¬∃xP(x)') #print statement that outputs which side of De Morgan's Law is being proved
px = True #initalizing the variable for a quantifier
for x in range(11): #for loop that loops through the domain 0-10
    if x < 5: #if statement that implements the predicate
        px = False #changes the value of px if the predicate is False
        break #breaks out of the loop if the condition is met
print(px, x, 'proves the assertion') #print statement that shows the truth value, and the value that disproves it

print('∀x¬P(x)') #print statement that outputs which side of De Morgan's Law is being proved
px = True #initalizing the variable to True for an Universal quantifier
for x in range(11): #for loop that loops through the domain 0-10
    if not (x < 5): #if statement that implements the predicate
        px = False #changes the value of px if the predicate is False
        break #breaks out of the loop if the condition is met
print(px, x, 'disproves the assertion', end='\n\n') #print statement that shows the truth value, and the value that disproves it

#Prove De Morgan’s Law for the Universal Quantifier where P(x) is the statement “x<5”
print('f)') #print statement that outputs which problem
print('¬∀xP(x)') #print statement that outputs which side of De Morgan's Law is being proved
px = False #initalizing the variable for a quantifier
for x in range(11): #for loop that loops through the domain 0-10
    if x < 5: #if statement that implements the predicate
        px = True #changes the value of px if the predicate is False
        break #breaks out of the loop if the condition is met
print(px, x, 'disproves the assertion') #print statement that shows the truth value, and the value that proves it

print('∃x¬P(x)') #print statement that outputs which side of De Morgan's Law is being proved
px = False #initalizing the variable to False for an existential quantifier
for x in range(11): #for loop that loops through the domain 0-10
    if x >= 5: #if statement that implements the predicate
        px = True #changes the value of px if the predicate is True
        break #breaks out of the loop if the condition is met
print(px, x, 'proves the assertion', end='\n\n') #print statement that shows the truth value, and the value that proves it

print('2. a) ∀x∀yP(x,y)') #print statement that outputs which problem
pxy = True #initalizing the variable to True for the two Universal quantifiers
for x in range(11): #for loop that loops through the domain 0-10
    for y in range(11): #for loop that loops through the domain 0-10
        if x * y != 0: #if statement that implements the predicate
            pxy = False #changes the value of px if the predicate is False
            break #breaks out of the loop if the condition is met
print(pxy, x, y, end='\n\n') #print statement that outputs the truth value 

print('b) ∀x∃yP(x,y)') #print statement that outputs which problem
for x in range(11): #for loop that loops through the domain 0-10
    pxy = False #initalizing the variable to False for the two quantifiers
    for y in range(11): #for loop that loops through the domain 0-10
        if x * y == 0: #if statement that implements the predicate
            pxy = True #changes the value of px if the predicates are True
            if y == 0: #if statement to print values that make predicate True
                break #breaks out of the loop if the condition is met
print(pxy, x, y, end='\n\n')#print statement that outputs the truth value 

print('c) ∃x∀yP(x,y)') #print statement that outputs which problem
for y in range(11): #for loop that loops through the domain 0-10
    pxy = False #initalizing the variable to False for the two quantifiers
    for x in range(11): #for loop that loops through the domain 0-10
        if x * y == 0: #if statement that implements the predicate
            pxy = True #changes the value of px if the predicates are True
            if x == 0: #if statement to print values that make predicate True
                break #breaks out of the loop if the condition is met
print(pxy, x, y, end='\n\n') #print statement that outputs the truth value 

print('d) ∃x∃yP(x,y)') #print statement that outputs which problem
pxy = False #initalizing the variable to False for the two existential quantifiers
for x in range(11): #for loop that loops through the domain 0-10
    for y in range(11): #for loop that loops through the domain 0-10
        if x * y == 0: #if statement that implements the predicate
            pxy = True #changes the value of px if the predicates are True
            break #breaks out of the loop if the condition is met
print(pxy, x, y, end='\n\n') #print statement that outputs the truth value 
