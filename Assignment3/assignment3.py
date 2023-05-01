"""
Author: Chase Burkdoll
KUID: 3082972
Date: 9/19/2022
Assignment: Assignment 3
Last modified: 9/29/2022
Purpose: Determine the natural of certain relations, use operations on relations, and relation composition.
"""

def prob_one(): #function declartion for problem one
    relation_one = {(1,1), (2,2), (3,3)} #declaring relation one
    relation_two = {(1,1), (1,2), (1,3), (1,4)} #declaring relation two
    print('1a. Union of R1 and R2') #print statement which outputs current problem
    result = relation_one.union(relation_two) #assigns the variable the union between the two relations using the built in union function
    print(result) #print statement that outputs the result of the union
    print('1b. Intersection of R1 and R2') #print statement which outputs current problem
    result = relation_one.intersection(relation_two) #assigns the variable the intersection between the two relations using the built in function
    print(result) #print statement that outputs the result of the intersection
    print('1c. Difference R1 - R2') #print statement which outputs current problem
    result = relation_one.difference(relation_two) #assigns the variable the differnce between the two relations using the built in function
    print(result) #print statement that outputs the result of the difference
    print('1d. Difference R2 - R1') #print statement which outputs current problem
    result = relation_two.difference(relation_one) #assigns the variable the differnce between the two relations using the built in function
    print(result) #print statement that outputs the result of the difference

def prob_two(): #function declartion for problem two
    r = {(1, 1), (1, 4), (2, 3), (3, 1), (3, 4)} #declaring the relation R
    s = {(1, 0), (2, 0), (3, 1), (3, 2), (4, 1)} #declaring the relation S
    print('2. S ◦ R') #print statement which outputs current problem
    newSet = {(c,b) for (a,b) in s for (c,d) in r if a == d} #relation composition to create a new set by looping through the orderd pairs and comparing
    print(newSet) #print statement that outputs the relation composition

def prob_three(): #function declartion for problem one
    r = {(1, 1), (1, 4), (2, 3), (3, 1), (3, 4)} #declaring the relation R
    print('3. R^2') #print statement which outputs current problem
    newSet = {(c,b) for (a,b) in r for (c,d) in r if a == d} #relation composition to create a new set by looping through the orderd pairs and comparing
    print(newSet) #print statement that outputs the relation composition

def prob_four(): #function declartion for problem one
    r = set() #declaring an empty set for the relation
    for x in range(-11, 11): #outer for loop that loops from -10 to 10
        for y in range(-11, 11): #inner for loop that loops from -10 to 10
            if x + y == 0: #if statement that checks if x plus y is equal to 0 
                r.add((y,x))#adds the ordered pair if condition is met using the built in add function
    print('4a. Show R as a set of ordered pairs') #print statement which outputs current problem
    print(r) #print statement that outputs the relation
    print('4b. Show whether R is reflexive or not.') #print statement which outputs current problem
    for (a,b) in r: #for loop that goes through the ordered pairs in r
        if a != b: #if statement that compares a and b in the ordered pair
            print(f'not reflexive because {a} does not equal {b}') #print statement that only happens if it is not reflexive
            break #breaks out of the loop
        else: #else statement that only prints if it is reflexive
            print('Is reflexive') #print statement that outputs the results
    print('4c. Show whether R is symmetric or not.') #print statement which outputs current problem
    is_symmetric = True #declaring variable to True 
    for (a,b) in r: #for loop that goes through the ordered pairs in r
        if (b,a) not in r: #if statement that checks if another ordered pair is in r
            is_symmetric = False #If the ordered pair is not in r then sets the variable to False
    print(is_symmetric, " is symmetric") #print statement that outputs the results
    print('4d. Show whether R is antisymmetric or not.') #print statement which outputs current problem
    for (a,b) in r: #for loop that goes through the ordered pairs in r
        is_antisymmetric = False #resets the variable to False for each loop
        if (b,a) not in r:  #if statement that checks if another ordered pair is in r
            is_antisymmetric = True #If the ordered pair is not in r then sets the variable to True
    print(is_antisymmetric, 'is not') #print statement that outputs the results
    print('4e. Show whether R is transitive or not.') #print statement which outputs current problem
    is_trans = True #declaring variable to True
    for (a,b) in r: #for loop that goes through the ordered pairs in r
        for (c,d) in r: #for loop that goes through the ordered pairs in r
            if b == c and ((a,d) not in r): #if statement that checks the transitive nature of the relation
                is_trans = False #sets the variable to False if it is not transitive
    print(is_trans, 'is not') #print statement that outputs the results


prob_one() #function call for problem one
prob_two() #function call for problem two
prob_three() #function call for problem three
prob_four() #function call for problem four