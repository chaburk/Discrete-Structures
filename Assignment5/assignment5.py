"""
Author: Chase Burkdoll
KUID: 3082972
Date: 10/13/2022
Assignment: Assignment 5
Last modified: 10/6/2022
Purpose: Determine whether a relation is a function, 
and if it is then whether it is injective, surjective, or bijective,
"""
def is_func(function): #function declaration to check if the relation is a function
    seen = set() #declares an empty set
    for (a,b) in function: #for loop that runs through all the preimages
        if a in seen: #if statement that checks if the preimage is in the seen set
            return False #returns whether it is a function
        seen.add(a) #adds preimage if not already in set
    return True #returns whether it is a function

def is_injective(function): #function declaration to check if the function is injective
    seen = set() #declares an empty set
    for (a, b) in function: #for loop that runs through all the images
        if b in seen: #if statement that checks if the image is in the seen set
            return False #returns whether it is a injective function
        seen.add(b) #adds image if not already in set
    return True #returns whether it is a injective function

def is_surjection(function, set_b): #function declaration to check if the function is surjective
    seen = set() #declares an empty set
    for (a, b) in function: #for loop that runs through all the images
        seen.add(b) #adds the image to the set
    for c in set_b: #foor loop that goes through the B set
        if c not in seen: #if statement that checks if not in the B set
            return False #returns False if it is a random character
    if len(seen) == len(set_b): #if the lengths are equal then it is surjective
        return True #returns whether it is a  surjectivefunction
    return False #returns whether it is a surjective function

def inverse_func(function):   #function declaration that returns the inverse function
    inverse = set() #declares an empty set
    for (a,b) in function: #for loop that runs through all ordered pairs
        inverse.add((b,a)) #adds the inverse function to the inverse set
    return inverse #returns the inverse function set

def automate_project(function, set_a, set_b): #function definition to simplify problem
    print(f'A = {set_a}') #print statement that displays set A
    print(f'B = {set_b}') #print statement that displays set B
    print(f'f = {function}') #print statement that displays function f
    if is_func(function): #if statement that makes a function call to determine if it's a function
        injective = is_injective(function) #assigning variable to results of function call
        surjective = is_surjection(function, set_b) #assigning variable to results of function call
        if injective and surjective == True: #checks the results of function calls to determine if function is bijective
            print('The function is a bijective function') #print statement that outputs which type of function it is
            print('The inverse function is', inverse_func(function))
        elif injective: #elif statement if is an injective function
            print('The function is an injective function') #print statement that outputs which type of function it is
        elif surjective: #elif statement if is an surjective function
            print('The function is a surjective function') #print statement that outputs which type of function it is
        else: #else statement if none of the above.
            print('Just a function') #print statement that outputs if it's none of the above
    else: #else statement that runs if it is not a function
        print('Sorry, not a function') #print statement that outputs it is not a function
    print() #print statement to add space


def prob_one(): #function definition for problem one
    A = {'a','b','c','d'}  #declares set A for the problem
    B = {'v','w','x','y','z'} #declares set B for the problem
    f = {('a','z'),('b','y'),('c','x'),('d','w')} #declares function for the problem
    print('1.') #print statement which prints which problem
    automate_project(f, A, B) #function call that determines what type of function

def prob_two(): #function definition for problem two
    A = {'a','b','c','d'} #declares set A for the problem
    B = {'x','y','z'} #declares set B for the problem
    f = {('a','z'),('b','y'),('c','x'),('d','z')} #declares function for the problem
    print('2.') #print statement which prints which problem
    automate_project(f, A, B) #function call that determines what type of function


def prob_three(): #function definition for problem three
    A = {'a','b','c','d'} #declares set A for the problem
    B = {'w','x','y','z'} #declares set B for the problem
    f = {('a','z'),('b','y'),('c','x'),('d','w')} #declares function for the problem
    print('3.') #print statement which prints which problem
    automate_project(f, A, B) #function call that determines what type of function

def prob_four(): #function definition for problem four
    A = {'a','b','c','d'} #declares set A for the problem
    B = {1,2,3,4,5} #declares set B for the problem 
    f = {('a',4),('b',5),('c',1),('d',3)} #declares function for the problem
    print('4.') #print statement which prints which problem
    automate_project(f, A, B) #function call that determines what type of function

def prob_five(): #function definition for problem five 
    A = {'a','b','c'} #declares set A for the problem
    B = {1,2,3,4} #declares set B for the problem 
    f = {('a',3),('b',4),('c',1)} #declares function for the problem
    print('5.') #print statement which prints which problem
    automate_project(f, A, B) #function call that determines what type of function

def prob_six(): #function definition for problem six
    A = {'a','b','c','d'} #declares set A for the problem
    B = {1,2,3} #declares set B for the problem 
    f = {('a',2),('b',1),('c',3),('d',2)} #declares function for the problem
    print('6.') #print statement which prints which problem
    automate_project(f, A, B) #function call that determines what type of function

def prob_seven(): #function definition for problem seven
    A = {'a','b','c','d'} #declares set A for the problem
    B = {1,2,3,4} #declares set B for the problem 
    f = {('a',4),('b',1),('c',3),('d',2)} #declares function for the problem
    print('7.') #print statement which prints which problem
    automate_project(f, A, B) #function call that determines what type of function

def prob_eight(): #function definition for problem eight
    A = {'a','b','c','d'} #declares set A for the problem
    B = {1,2,3,4} #declares set B for the problem 
    f = {('a',2),('b',1),('c',2),('d',3)} #declares function for the problem
    print('8.') #print statement which prints which problem
    automate_project(f, A, B) #function call that determines what type of function

def prob_nine(): #function definition for problem nine
    A = {'a','b','c'} #declares set A for the problem
    B = {1,2,3,4} #declares set B for the problem 
    f = {('a',2),('b',1),('a',4),('c',3)} #declares function for the problem
    print('9.') #print statement which prints which problem
    automate_project(f, A, B) #function call that determines what type of function


prob_one() #function call for problem one
prob_two() #function call for problem one
prob_three() #function call for problem one
prob_four() #function call for problem four
prob_five() #function call for problem five
prob_six() #function call for problem six
prob_seven() #function call for problem seven
prob_eight() #function call for problem eight
prob_nine() #function call for problem nine