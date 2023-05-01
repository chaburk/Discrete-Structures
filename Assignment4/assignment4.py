"""
Author: Chase Burkdoll
KUID: 3082972
Date: 9/19/2022
Assignment: Assignment 4
Last modified: 10/5/2022
Purpose: Check if a relation is reflexive, symmetric, transitive, an equivalence relation, or a poset.
"""

from weakref import ref
def find_reflex(sets): #Function that finds the reflexive set
        reflexive_set = set() #declares a variable to an empty set
        for a in sets: #for loop that loops through the sets
            reflexive_set.add((a,a)) #adds the item to the set to make it reflexive
        return reflexive_set #returns the reflexive set

def reflexive_check(relation, reflex_relation, check): #function that checks if a relation is reflexive
    is_reflexive = True #initalizes variable to True
    for (a,b) in reflex_relation: #for loop that goes through the items in the reflexive relation
        if (a,b) not in relation: #if statement that checks if the ordered pair is not in the relation
            is_reflexive = False #if ordered pair is not in the relation set variable to False
    if check == 'Y': #if statement that checks if we only need to return whether or not it is true
        return is_reflexive #return statement that returns the value of is_reflexive
    else: #else statement that runs if the check is anything else
        if is_reflexive: #if statement that runs if it is reflexive
            print('1b. R is reflexive') #print statement that says answer part b 
            print('1c. N/A') #print statement that answers part c
        else: #else statement that runs if it is not reflexive
            print('1b. R is not reflexive') #print statement that answers part b
            r_star = relation.union(reflex_relation) #Set union to find the reflexive relation
            print('1c.', r_star) #print statement that answers part c, and displays the reflexive relation

def symmetric_check(relation, check): #function that checks if a relation symmetric
    rstar = set() #declares an empty set
    is_symmetric = True #initalizes variable to True
    for (a,b) in relation: #for loop that checks the symmetric nature of the relation
        if (b,a) in relation: #if statement that checks if the ordered pair is in the relation
            pass #pass if it is in the relation
        else: #else statement that runs if the ordered pair is not in the relation
            is_symmetric = False #sets variable to False
            rstar.add((b,a)) #adds the ordered pair to the set if not the in the relation
    if check == 'Y':  #if statement that checks if we only need to return whether or not it is true
        return is_symmetric #return statement that returns the value of is_symmetric
    else: #else statement that runs if the check is anything else
        if is_symmetric:  #if statement that runs if it is symmetric
            print('2b. R is symmetric')  #print statement that answers part b
            print('2c. N/A')  #print statement that answers part c
        else: #else statement that runs if it is not symmetric
            print('2b. R is not symmetric')  #print statement that answers part b
            rstar = rstar.union(relation) #Set union to find the symmetric closure
            print('2c.', rstar)  #print statement that answers part c

def transitive_check(relation, check): #function that checks if a relation is transitive
    rstar = set() #declares an empty set
    is_trans = True #declaring variable to True
    for (a,b) in relation: #for loop that goes through the ordered pairs in relation
        for (c,d) in relation: #for loop that goes through the ordered pairs in relation
            if b == c and ((a,d) not in relation): #if statement that checks the transitive nature of the relation
                is_trans = False #sets the variable to False if it is not transitive
                rstar.add((a,d))
    if check == 'Y': #if statement that checks if we only need to return whether or not it is true
        return is_trans #return statement that returns the value of is_trans
    else: #else statement that runs if the check is anything else
        if is_trans: #if statement that runs if it is transitive
            print('3b. R is transitive') #print statement that answers part b
            print('3c. N/A') #print statement that answers part c
        else: #else statement that runs if it is not transitive
            print('3b. R is not transitive') #print statement that answers part b
            rstar = rstar.union(relation) #Set union to find the transitive closure
            print('3c.', rstar) #print statement that answers part c

def antisymmetric_check(relation): #function that checks if a relation is antisymmetric
    is_antisymmetric = True #declares variable to True
    for (a,b) in relation: #for loop that checks if the ordered pair is in the relation
        if (b,a) in relation and a != b: #if statement that runs if the ordered pair is not in the relation
            is_antisymmetric = False #sets the variable to True if it is antisymmetric
    return is_antisymmetric #returns statement that returns the value of is_antisymmetric

def equivalence_check(relation, set): #function that checks if a relation is a equivalence relation
    reflex_s = find_reflex(set) #declares variable to function call
    is_reflexive = reflexive_check(relation, reflex_s, 'Y') #declares variable to function call
    is_symmetric = symmetric_check(relation, 'Y') #declares variable to function call
    is_trans = transitive_check(relation, 'Y') #declares variable to function call
    is_equiv = True #declares variables to True
    if (is_reflexive and is_symmetric and is_trans) == True: #checks if all the variables are True to make it an equivalance relation
        print('4b. R is an equivalence relation')  #print statement that answers part b
        print('4c. N/A')  #print statement that answers part c
    else:
        is_equiv = False
        print('4b. R is not an equivalence relation')  #print statement that answers part b
        if not is_reflexive: #if statement to find why it is not an equivalance relation
            print('4c. R is not reflexive')  #print statement that answers part c
        if not is_symmetric: #if statement to find why it is not an equivalance relation
            print('4c. R is not symmetric')  #print statement that answers part c
        if not is_trans: #if statement to find why it is not an equivalance relation
            print('4c. R is not transitive')  #print statement that answers part c
    return is_equiv #return statement that returns the value of is_equiv

def poset_check(relation, set): #function that checks if a relation is a poset
    reflex_s = find_reflex(set) #declares variable to function call
    is_reflexive = reflexive_check(relation, reflex_s, 'Y') #declares variable to function call
    is_antisymmetric = antisymmetric_check(relation) #declares variable to function call
    is_trans = transitive_check(relation, 'Y') #declares variable to function call
    is_poset = True #declares variable to True
    if (is_reflexive and is_antisymmetric and is_trans) == True: #checks if all the variables are True to make it a poset
        print('5b. (S,R) is a poset') #print statement that answers part b
        print('5c. N/A') #print statement that answers part c
    else:
        is_poset = False
        print('5b. (S,R) is not a poset') #print statement that answers part b
        if not is_reflexive: #if statement to find why it is not a poset
            print('5c. (S,R) is not reflexive') #print statement that answers part c
        if not is_antisymmetric: #if statement to find why it is not a poset
            print('5c. (S,R) is not antisymmetric') #print statement that answers part c
        if not is_trans: #if statement to find why it is not a poset
            print('5c. (S,R) is not transitive') #print statement that answers part c
    return is_poset #return statement that returns the value of is_poset

def prob_one(): #function that displays the output to question one
    #Sets
    S = {1,2,3,4} # declare set for problem one
    S_letters = {'a', 'b', 'c', 'd'} #declare set for problem one

    #Reflexive sets
    reflex_S = find_reflex(S) #reflexive sets for problem one
    reflex_letters = find_reflex(S_letters) #reflexive sets for problem one

    R = {(1,1), (4,4), (2,2), (3,3)} #relation for problem one
    R_letters = {('a', 'a'), ('c', 'c')} #relation for problem one

    print('REFLEXIVE') #print statement that says which problem
    print('Show the code works for the relation {(1,1), (4,4), (2,2), (3,3)} on the set {1,2,3,4}.') #print statement that says which problem
    print(f'1a. R = {R}') #print statement that answers part a
    reflexive_check(R, reflex_S, 'N') #function call to display the answers to the problems
    
    print('Show the code works for the relation {(a,a), (c,c)} on the set {a,b,c,d}.') #print statement that says which problem
    print(f'1a. R = {R_letters}') #print statement that answers part a
    reflexive_check(R_letters, reflex_letters, 'N') #function call to display the answers to the problems

def prob_two(): #function that displays the output to question two
    S = {1,2,3,4} #declare set for problem one
    R1 = {(1,2), (4,4), (2,1), (3,3)} #relation for problem two
    R2 =  {(1,2), (3,3)} #relation for problem two
    print() #print statement adds space
    print('SYMMETRIC')#print statement that says which problem
    print('Show the code works for the relation {(1,2), (4,4), (2,1), (3,3)} on the set {1,2,3,4}.') #print statement that says which problem
    print(f'2a. R = {R1}') #print statement that answers part a
    symmetric_check(R1, 'N') #function call to display the answers to the problems
    print('Show the code works for the relation {(1,2), (3,3)} on the set {1,2,3,4}') #print statement that says which problem
    print(f'2a. R = {R2}')  #print statement that answers part a
    symmetric_check(R2, 'N') #function call to display the answers to the problems

def prob_three(): #function that displays the output to question three
    S = {1,2,3} #declare set for problem three
    S_letters = {'a', 'b', 'c', 'd'} #declare set for problem three
    R = {(1,1),(1,3),(2,2),(3,1),(3,2)} #relation for problem three
    R_letters =  {('a','b'), ('d','d'), ('b','c'), ('a','c')} #relation for problem three
    print() #print statement adds space
    print('TRANSITIVE') #print statement that says which problem
    print('Show the code works for the relation {(a,b), (d,d), (b,c), (a,c)} on the set {a,b,c,d}.') #print statement that says which problem
    print(f'3a. R = {R_letters}')  #print statement that answers part a
    transitive_check(R_letters, 'N') #function call to display the answers to the problems
    print('Show the code works for the relation {(1,1),(1,3),(2,2),(3,1),(3,2)} on the set {1,2,3}.') #print statement that says which problem
    print(f'3a. R = {R}')  #print statement that answers part a
    transitive_check(R, 'N') #function call to display the answers to the problems
    
def prob_four():#function that displays the output to question four
    S = {1,2,3} #declare set for problem four
    S_letters = {'a', 'b', 'c'} #declare set for problem four

    R = {(1,1),(2,2),(2,3)} #relation for problem four
    R_letters =  {('a','a'),('b','b'),('c','c'),('b','c'),('c','b')} #relation for problem four

    print() #print statement adds space
    print('EQUIVALENCE') #print statement that says which problem
    print('Show the code works for the relation {(1,1),(2,2),(2,3)} on the set {1,2,3}.') #print statement that says which problem
    print(f'4a. R = {R}')  #print statement that answers part a
    equivalence_check(R, S) #function call to display the answers to the problems

    print('Show the code works for the relation {(a,a),(b,b),(c,c),(b,c),(c,b)} on the set {a,b,c}.') #print statement that says which problem
    print(f'4a. R = {R_letters}')  #print statement that answers part a
    equivalence_check(R_letters, S_letters) #function call to display the answers to the problems

def prob_five(): #function that displays the output to question five
    S = {1, 2, 3, 4} #declare set for problem five
    S2 = {0, 1, 2, 3} #declare set for problem five

    R1 = {(1,1), (1,2), (2,2), (3,3), (4,1), (4,2), (4,4)} #relation for problem five
    R2 = {(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 2), (3, 3)} #relation for problem five

    print() #print statement adds space
    print('POSET') #print statement that says which problem
    print('Show the code works for the relation {(1,1), (1,2), (2,2), (3,3), (4,1), (4,2), (4,4)} on the set {1, 2, 3, 4}.') #print statement that says which problem
    print(f'5a. S = {S}')  #print statement that answers part a
    print(f'5b. R = {R1}') #print statement that answers part b
    poset_check(R1, S) #function call to display the answers to the problems
    print('Show the code works for the relation {(0, 0), (0, 1), (0, 2), (0, 3), (1, 0), (1, 1), (1, 2), (1, 3), (2, 0), (2, 2), (3, 3)} on the set {0, 1, 2, 3}.') #print statement that says which problem
    print(f'5a. S = {S2}')  #print statement that answers part a
    print(f'5b. R = {R2}')  #print statement that answers part b
    poset_check(R2, S2) #function call to display the answers to the problems


prob_one() #function call for problem one
prob_two() #function call for problem two
prob_three()#function call for problem three
prob_four()#function call for problem four
prob_five()#function call for problem five