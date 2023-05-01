"""
Author: Chase Burkdoll
KUID: 3082972
Date: 11/10/2022
Assignment: Assignment 7
Last modified: 11/29/2022
Purpose: Write programs for various problems dealing with objects and boxes
"""

import math
import itertools

def dodb(num_objects, num_boxes, num_objects_in_boxes): #function declaration for distinct boxes and objects
    value = math.factorial(num_objects) #declares variable to hold the factorial of the number of total objects
    for i in range(num_boxes): #for loop to go through the amount of boxes
        value /= math.factorial(num_objects_in_boxes) #divides value by the facotorial of the number of objects in the boxes
        num_objects -= num_objects_in_boxes #take away from the total number of objects
    if num_objects != 0: #if there are additonal objects left over 
        value /= math.factorial(num_objects) #calculate the value with leftover objects
    return value #else return the value if no additional objects

def iodb(n, r):  #function declaration for distinct boxes and indisntict objects
    combination = math.factorial(n + r -1) / (math.factorial(r) * math.factorial(n-1)) #formula using factorials to calculate combinations
    return combination #return total number of combinations

def norm_comb(n,r): #function declaration for helper function
    return math.factorial(n) / (math.factorial(n-r)*math.factorial(r)) #return combination for no repeition

def doib(n, k): #function declaration for indistinct boxes and disntict objects
    total_value = 0 #declares variable that contains the total value
    for j in range(1,k+1): #outer for loop from 1 to k + 1
        value = 0 #declares a temp variable for each iteration
        for i in range(j): #inner for loop that goes from 0 to j
            value += ((-1)**i)*norm_comb(j,i)*((j-i)**n) #adds part of sterling equations
        total_value += value * (1/math.factorial(j)) #adds the value times 1 over a factorial of j to the total value 
    return total_value #returns the total number of ways

    
def ioid(n, k): #function declaration for indistinct boxes and indisntict objects
    if (n == 0): #if statement that checks if n has reached 0
        return 1 #return statement that returns 1
    elif (k == 0 or n < 0): #elif statement that checks if these conditions are met
        return 0 #return statement that returns 0
    return ioid(n,k-1) + ioid(n-k,k) #recursively calls the function with different n and k values

print("""1. A professor packs her collection of 40 issues of a mathematics journal in four boxes with 10 
issues per box. How many ways can she distribute the journals if each box is numbered, so that they are distinguishable?""") #print problem
print(dodb(40,4,10)) #print to show problem one
print() #print statement for spacing
print("""2. How many ways are there to distribute 12 indistinguishable balls into six distinguishable bins""") #print problem
print(iodb(3, 11)) #print to show problem two
print() #print statement for spacing
print("3. How many ways are there to put five temporary employees into four identical offices?") #print problem
print(doib(5,4)) #print to show problem three
print() #print statement for spacing
print("4. How many ways are there to distribute five indistinguishable objects into three indistinguishable boxes?") #print problem
print(ioid(5,3)) #print to show problem four
print() #print statement for spacing
