"""
Author: Chase Burkdoll
KUID: 3082972
Date: 8/30/2022
Assignment: Assignment 1
Last modified: 8/31/2022
Purpose: Prints truth tables showing the logical equivalence of propositions.
"""

print("1. De Morgan's First Law") #print statment which tells which proposition
print('p', 'q', '!p', '!q', 'p*q', '!p*q', '!p + !q', sep = "\t") #print statment which shows the truth table steps / headers
for p in [True, False]: #Outer for loop to assign values to p and build the foundation for the logic.
    for q in [True, False]: #Inner for loop to assign values to q and build the foundation for the logic.
        print(p, q, not p, not q, p and q, not(p and q), not p or not q, sep="\t") #print statement that displays the values for p and q, and uses logical operators to build the truth table for De Morgan's First Law 

print()#print statment to add space between propositions
print("2. De Morgan's Second Law") #print statment which tells which proposition
print('p', 'q', '!p', '!q', 'p+q', '!p+q', '!p * !q', sep = "\t") #print statment which shows the truth table steps / headers
for p in [True, False]: #Outer for loop to assign values to p and build the foundation for the logic.
    for q in [True, False]: #Inner for loop to assign values to q and build the foundation for the logic.
        print(p, q, not p, not q, p or q, not(p or q), not p and not q, sep="\t") #print statement that displays the values for p and q, and uses logical operators to build the truth table for De Morgan's Second Law 

print()#print statment to add space between propositions
print("3. First Associative Law") #print statment which tells which proposition
print('p', 'q', 'r', 'p * q', 'q * r', '(p * q) * r', 'p * (q * r)', sep = '\t') #print statment which shows the truth table steps / headers
for p in [True, False]: #Outer for loop to assign values to p and build the foundation for the logic.
    for q in [True, False]: #Inner for loop to assign values to q and build the foundation for the logic.
        for r in [True, False]: #Inner for loop to assign values to r and build the foundation for the logic.
            print(p, q, r, p and q, q and r, (p and q) and r,'   ', p and (q and r), sep ="\t") #print statement that displays the values for p, q, and r, and uses logical operators to build the truth table for First Associative Law

print()#print statment to add space between propositions
print("4. Second Associative Law") #print statment which tells which proposition
print('p', 'q', 'r', 'p + q', 'q + r', '(p + q) + r', 'p + (q + r)', sep = '\t') #print statment which shows the truth table steps / headers
for p in [True, False]: #Outer for loop to assign values to p and build the foundation for the logic.
    for q in [True, False]: #Inner for loop to assign values to q and build the foundation for the logic.
        for r in [True, False]: #Inner for loop to assign values to r and build the foundation for the logic.
            print(p, q, r, p or q, q or r, (p or q) or r,'   ', p or (q or r), sep ="\t") #print statement that displays the values for p, q, and r, and uses logical operators to build the truth table for Second Associative Law

print()#print statment to add space between propositions
print("5. [(p ∨ q) ∧ (p → r) ∧ (q → r)] → r ≡ T")  #print statment which tells which proposition
print('p', 'q', 'r', 'p + q', 'p -> r', 'q -> r', '(p + q) * (p -> r) * (q -> r)', '[(p + q) * (p -> r) * (q -> r)] -> r', sep = '\t') #print statment which shows the truth table steps / headers
for p in [True, False]: #Outer for loop to assign values to p and build the foundation for the logic.
    for q in [True, False]: #Inner for loop to assign values to q and build the foundation for the logic.
        for r in [True, False]: #Inner for loop to assign values to r and build the foundation for the logic.
            print(p, q, r, p or q, sep ="\t", end='\t') #Print statment to display the three variables and the first logic operation.
            if (p and r) or not p: #if statement that contains the logic for an Implication
                p_then_r = True #assigns variable based on Implication results
                print(True, sep='\t', end='\t') #print statement to display results of Implication
            else: #else statment that determines what to do if implication is false
                p_then_r = False #assigns variable based on Implication results
                print(False, sep='\t', end='\t') #print statement to display results of Implication
            if (q and r) or not q: #if statement that contains the logic for an Implication
                q_then_r = True #assigns variable based on Implication results
                print(True, sep='\t', end='\t') #print statement to display results of Implication
            else: #else statment that determines what to do if implication is false
                q_then_r = False #assigns variable based on Implication results
                print(False, sep='\t', end='\t') #print statement to display results of Implication
            final_implication = (p or q) and p_then_r and q_then_r #assigns variable using logical operators
            print((p or q) and p_then_r and q_then_r, sep='\t', end='\t') #print statment to display the results of the logic operation
            if (final_implication and r) or not final_implication: #if statement that contains the logic for an Implication
                print('                    ',True, sep='\t') #print statement to display results of Implication
            else: #else statment that determines what to do if implication is false
                print('                    ',False, sep='\t') #print statement to display results of Implication

print()#print statment to add space between propositions
print("6. p ↔ q ≡ (p → q) ∧ (q → p)")  #print statment which tells which proposition
print('p', 'q', 'p -> q', 'q -> p', '(p -> q) * (q -> p)', 'p <-> q', sep='\t') #print statment which shows the truth table steps / headers
for p in [True, False]: #Outer for loop to assign values to p and build the foundation for the logic.
    for q in [True, False]: #Inner for loop to assign values to q and build the foundation for the logic.
        print(p, q, sep='\t', end='\t')
        if p and q or not p: #if statement that contains the logic for an Implication
            p_then_q = True #assigns variable based on Implication results
            print(p_then_q, sep='\t', end='\t')
        else: #else statment that determines what to do if implication is false
            p_then_q = False #assigns variable based on Implication results
            print(p_then_q, sep='\t', end='\t')
        if p and q or not q: #if statement that contains the logic for an Implication
            q_then_p = True #assigns variable based on Implication results
            print(q_then_p, sep='\t', end='\t')
        else: #else statment that determines what to do if implication is false
            q_then_p = False #assigns variable based on Implication results
            print(q_then_p, sep='\t', end='\t')
        print(p_then_q and q_then_p, end='\t')
        if p == q: #if statment that checks for equivalence 
            print('               ',True) #print statment that prints True if they are equivalent
        else: # else statment that prints if the variables are not equivalent
            print('               ',False) #print statment that prints False if they are not equivalent



