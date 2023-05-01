"""
Author: Chase Burkdoll
KUID: 3082972
Date: 11/29/2022
Assignment: Assignment 8
Last modified: 12/7/2022
Purpose: Write programs to determine whether a graph has a euler cirucit or is a hamilton circuit
"""

def dfs(u, graph, visited_edge, path=[]): #function declaration for depth first search to find path
    path = path + [u] #add u to the path
    for v in graph[u]: #for each value in the graph at key u
        if visited_edge[u][v] == False: #if the edge hasn't been visted yet
            visited_edge[u][v], visited_edge[v][u] = True, True #changes the edge to visited 
            path = dfs(v, graph, visited_edge, path) #recursively calls the dfs fucnction again to add path
    return path #returns the path

def check_circuit_or_path(graph, max_node): #function declaration to check if the graph has a circuit
    odd_nodes = [] #declares empty list to hold nodes with odd degrees
    odd_degree_nodes = 0 #declares a variable to zero to count number of odd degree nodes
    odd_node = -1 #declares variable to -1
    for i in range(max_node): #for loop that goes through 0 to 10
        if i not in graph.keys(): #if the number is not in the keys then continue
            continue
        if len(graph[i]) % 2 == 1: #if the number is in the keys then key if the len of the values is odd
            odd_nodes.append(i) #append he key to the odd nodes list
            odd_degree_nodes += 1 #increase the number of odd nodes by one
            odd_node = i #set the odd node to the value of i
    if odd_degree_nodes == 0: #if there is no odd nodes 
        return 1, odd_node, odd_nodes #return these values
    if odd_degree_nodes == 2: #if there is 2 odd degree nodes
        return 2, odd_node, odd_nodes #return these values
    return 3, odd_node, odd_nodes #if there are other numbers of odd nodes return these values

def check_euler(graph, max_node): #function declaration to say if it has a circuit and return the path
    visited_edge = [[False for _ in range(max_node + 1)] for _ in range(max_node + 1)] #changes all the visited edges to false
    check, odd_node, odd_nodes = check_circuit_or_path(graph, max_node) #function call that puts values in variables
    if check == 3: #the function call returns 3
        print("graph is not Eulerian") #print statement 
        print("Odd nodes are") #print statement 
        return switch_to_letters(odd_nodes) #returns the odd_nodes
    start_node = 1 #declares start_node variable to 1
    if check == 2: #the function call returns 3
        start_node = odd_node #changes start_node to odd_node
        print("graph has a Euler path") #print statement
        print("Odd nodes are") #print statement
        return odd_nodes #returns the odd_nodes list
    if check == 1: #the function call returns 1
        print("graph has a Euler circuit") #print statement
    path = dfs(start_node, graph, visited_edge) #put the path of the circuit into the path variable
    return path #returns the circuit path

def switch_to_numbers(g): #function declaration to switch letters to numbers
    new_g = {} #declares a new dictionary
    b = g.items() #gets the items from the passed in graph
    for i in list(b): #for loop to extract data from graph
        new_g[ord(i[0]) - 96] = None #declare a new key in the graph
        new_list = [] #declare empty list
        for j in i[1]: #for each value in the key 
            new_list.append(ord(j)-96) #append the new value to the new list
        new_g[ord(i[0])-96] = new_list #assign the values a new keys
        
    return(new_g) #return the new graph

def switch_to_letters(l): #fucntion declartion to switch to letters
    new_list = [] #declares new list
    for i in l: #for loop for each element in passed in list
        new_list.append(chr(i+96)) #append the letter
    return new_list #return new list
        
def dirac_thm(graph): #function declaration for dirac
    max_amount = len(graph)/ 2 #declares new variable
    for i in range(len(graph)): #for loop that goes from 0 to the length of the graph
        if i not in graph.keys(): #if statement to check if the value is in the keys
            continue #if not inkeys then continue
        if len(graph[i]) < max_amount : #if the value is in the keys then check if the degree is less than than max amount
            print('No Hamilton') #print statement
            return False #returns outcome
    print('Hamilton') #print statement
    return True #returns outcome

def ores_thm(graph): #function declaration for ores thm
    n = len(graph) #declares n as the length of the graph
    keys = list(graph.keys()) #declares new variable to hold the keys of the graph
    for i in keys: #for loop to go through each key
        new_keys = list(graph.keys()) #declares new variable to hold the keys of the graph
        new_keys.remove(i) #removes the current key form new_keys
        values = graph[i] #gets the values from the current key
        for j in values: #for each value in the values
            if j in new_keys: #if the value is in new_keys 
                new_keys.remove(j) #remove the value
        if len(new_keys) != 0 and len(new_keys) == 1: #if new_keys is empty and equal to one
            value = len(graph[new_keys[0]]) + len(graph[i]) #get the value of their degrees
            if value < n: #if statement to check if the value is less than n
                print('No Hamilton') #print statement
                return False #returns outcome
        elif len(new_keys) > 1: #if muliplte values still in new_keys
            for k in range(1, len(new_keys)): #go through each of the values
                value = len(graph[new_keys[k]]) + len(graph[i]) #get the value of the degrees of the two nonadajcent vertexs
                if value < n: #if the values is less than n
                    print('No Hamilton') #print statement
                    return False #returns outcome
    print('Hamilton') #print statement
    return True #returns outcome



def main():

    one_a = { #dictionary object to hold graph for problem one
        "a": ["e","b"],
        "b": ["e","a"],
        "c": ["e","d"],
        "d": ["c","e"],
        "e": ["c","d","b","a"]
    }
    one_b = { #dictionary object to hold graph for problem one
        "a": ["e","b","d"],
        "b": ["e","a","c"],
        "c": ["e","d","b"],
        "d": ["c","e","a"],
        "e": ["c","d","b","a"]
    }
    one_c = { #dictionary object to hold graph for problem one
        "a": ["b","c","d"],
        "b": ["a","d","e"],
        "c": ["a","d"],
        "d": ["a","b","c","e"],
        "e": ["b","d"]
    }
    one_d = { #dictionary object to hold graph for problem one
        "a": ["c","b","d"],
        "b": ["d","a"],
        "c": ["a","d"],
        "d": ["c","a","b"],
    }
    one_e = { #dictionary object to hold graph for problem one
        "a" : ["b","d"],
        "b" : ["a", "c", "d", "e"],
        "d" : ["e", "b", "a", "g"],
        "c" : ["b", "f"],
        "e" : ["b", "d", "f", "h"],
        "f" : ["c", "e", "h", "i"],
        "g" : ["d", "h"],
        "h" : ["e", "f", "g", "i"],
        "i" : ["f", "h"]
    }

    two_a = { #dictionary object to hold graph for problem two and three
        "a": ["b","c","e"],
        "b": ["a","c","e"],
        "c": ["a","b","e","d"],
        "d": ["e","c"],
        "e": ["a","c","b","d"]
    }

    two_b = { #dictionary object to hold graph for problem two and three
        "a": ["b"],
        "b": ["a","d","c"],
        "c": ["d","b"],
        "d": ["b","c"],
    }

    two_c = { #dictionary object to hold graph for problem two and three
        "a" : ["b"],
        "b" : ["a", "c", "g"],
        "d" : ["c"],
        "c" : ["b", "d", "e"],
        "e" : ["c", "f", "g"],
        "f" : ["e"],
        "g" : ["b", "e"]
    }

    two_d = { #dictionary object to hold graph for problem two and three
        "a" : ["b", "c"],
        "b" : ["a", "c"],
        "c" : ["a", "b","f"],
        "d" : ["f", "e"],
        "e" : ["d", "f"],
        "f" : ["e", "d", "c"],
    }

    max_node = 10
    print("Problem 1. Euler Circuit") #print statement to display which problem
    print("Problem G1 in lecture") #print statement to display which problem
    print(switch_to_letters(check_euler(switch_to_numbers(one_a), max_node))) #print statement to display results of function call
    print() #print statement to add space
    print("Problem G2 in lecture") #print statement to display which problem
    print(check_euler(switch_to_numbers(one_b), max_node)) #print statement to display results of function call
    print() #print statement to add space
    print("Problem G3 in lecture") #print statement to display which problem
    print(switch_to_letters(check_euler(switch_to_numbers(one_c), max_node))) #print statement to display results of function call
    print() #print statement to add space
    print("Bridges of Konigsberg") #print statement to display which problem
    print(switch_to_letters(check_euler(switch_to_numbers(one_d), max_node))) #print statement to display results of function call
    print() #print statement to add space
    print("Test graph on assignment page") #print statement to display which problem
    print(switch_to_letters(check_euler(switch_to_numbers(one_e), max_node))) #print statement to display results of function call
    print() #print statement to add space
    print("Problem 2. Dirac's Theorem") #print statement to display which problem
    print('Problem G1 in lecture') #print statement to display which problem
    print(dirac_thm(switch_to_numbers(two_a))) #print statement to display results of function call
    print() #print statement to add space
    print('Problem G2 in lecture') #print statement to display which problem
    print(dirac_thm(switch_to_numbers(two_b))) #print statement to display results of function call
    print() #print statement to add space
    print('Problem G3 in lecture') #print statement to display which problem
    print(dirac_thm(switch_to_numbers(two_c))) #print statement to display results of function call
    print() #print statement to add space
    print('Test graph on assignment page') #print statement to display which problem
    print(dirac_thm(switch_to_numbers(two_d))) #print statement to display results of function call
    print() #print statement to add space
    print("Problem 3. Ore's Theorem") #print statement to display which problem
    print('Problem G1 in lecture') #print statement to display which problem
    print(ores_thm(switch_to_numbers(two_a))) #print statement to display results of function call
    print() #print statement to add space
    print('Problem G2 in lecture') #print statement to display which problem
    print(ores_thm(switch_to_numbers(two_b))) #print statement to display results of function call
    print() #print statement to add space
    print('Problem G3 in lecture') #print statement to display which problem
    print(ores_thm(switch_to_numbers(two_c))) #print statement to display results of function call
    print() #print statement to add space
    print('Test graph on assignment page') #print statement to display which problem
    print(ores_thm(switch_to_numbers(two_d))) #print statement to display results of function call
    print() #print statement to add space



if __name__ == "__main__":
    main()