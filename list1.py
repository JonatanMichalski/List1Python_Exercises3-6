# -*- coding: utf-8 -*-
"""
Created on Tue Oct 6 10:39:30 2026

@author: Student
"""
import random
import math
import matplotlib.pyplot as plt    

def divisible(numbers, divisor):
    """Return integers from numbers that are divisible by divisor.

    Args:
        numbers (list[int]): List of integers to check.
        divisor (int): Integer used to test divisibility.

    Returns:
        list[int]: Numbers from numbers that are divisible by divisor.

    Raises:
        TypeError: If numbers is not a list of integers or divisor is not
        an integer.
        ValueError: If divisor is zero.

    Preconditions:
        - numbers is a list containing only integers.
        - divisor is a non-zero integer.

    Postconditions:
        - The returned list contains only numbers from numbers that are
        divisible by divisor.
        - The order of numbers is preserved.
    """
    
    if not isinstance(numbers, list):
        raise TypeError("Numbers must be a list.")
        #checks if numbers is an instance of a list class
        
    if not all(type(number)is int for number in numbers):
        raise TypeError("Numbers must contain only integers.")
        #checks if the list numbers contains integers only
        
    if type(divisor) is not int:
        raise TypeError("A divisor must be an integer.")
        #cheks if the divisor is an integer
        
    if divisor==0:
        raise ValueError("Divisor cannot be 0.")
        #checks if a divisor is equal to 0

    result = []

    for number in numbers:
        if number % divisor == 0:
            result.append(number)

    return result

def common(x, y):
    """Return the intersection of two multisets
    
    Args:
        x( list): The first multiset.
        y (list): The second multiset.
        
    Returns:
        list: Elements common to both multisets, with each element
        appearing as many times as the minimum of its counts in x and y.
        
    Raises:
        TypeError: if x or y is not a list.
        
    Preconditions:
        - x and y are lists.
        
    Postconditions:
        - Each element occurs in the result as many times as the
        minimum of its conts in x and y
        - The order of elements follows their first occurences in x.    
    """
    
    if not isinstance(x, list) or not isinstance(y, list):
        raise TypeError("Both x and y must be lists.")
    #checks if x and y are lists
    
    result = []
    remaining = y.copy()
    
    for element in x:
        if element in remaining:
            result.append(element)
            remaining.remove(element)
            
    return result

def subsets(x: set) -> list[set]:
    """Return a list containing all subsets of a given set.
    
    Args:
        x: A set of hashable elements.
        
    Returns:
        A list of sets containing every subset of x.
        
    Raises:
        TypeError: If x is not an instance of set.
        
    Preconditions:
        x must be an instance of set.
        
    Postconditions:
        The result contains exactly 2**len(x) distinct subsets,
        including the empty set and the x itself.
    """
    if not isinstance(x, set):
        raise TypeError("The argument must be a set.")
        
    result = [set()]
    
    for element in x:
        new_subsets = []
        for subset in result:
            new_subset = subset.copy()
            new_subset.add(element)
            new_subsets.append(new_subset)
        result.extend(new_subsets)
        
    return result


def random_walk(n):
    """Simulate a random walk from the origin until its distance exceeds n.

    At each step, the walker moves one unit up, down, left, or right.
    The coordinates of every visited position are stored in a list.
    Walking in an oblique way is not permitted. 

    Args:
        n (int or float): Non-negative distance threshold from the origin.

    Returns:
        list[tuple[int, int]]: Coordinates of all visited positions,
            starting with (0, 0) and ending at a position whose distance
            from the origin is greater than n.

    Raises:
        TypeError: If n is not an integer or float, or if n is a boolean.
        ValueError: If n is negative.

    Preconditions:
        - n is a non-negative integer or float.

   Postconditions:
       - The returned list starts with (0, 0).
       - Each consecutive pair of coordinates differs by exactly
         one unit in one direction.
       - The final position is at a distance greater than n
         from the origin.
   """
    
    if n < 0:
        raise ValueError("n must be non-negative")
        
    #start at the origin
    x=0
    y=0
    
    #store all visited coordinates
    coordinates = [(x,y)]
    
    #movements
    directions = [(1,0), (0,1), (-1,0), (0,-1)]
    
    #continue until the distance from (0,0) exceeds n
    while math.sqrt(x**2+y**2) <=n:
        #choose random direction 
        dx, dy = random.choice(directions)
        
        #update new position
        x+=dx
        y+=dy
        
        #record the new position
        coordinates.append((x,y))
        
    return coordinates

def dna_complement(orig_strand):
    """Return the complementary DNA strand in the 5' to 3' direction.

    Uses Watson-Crick base pairing rules: A-T and C-G.
    The resulting strand is reversed to represent the complementary
    strand in the 5' to 3' direction.

    Args:
        orig_strand (str): Original DNA sequence containing bases A, T, C, G.

    Returns:
        str: The complementary DNA sequence in the 5' to 3' direction.

    Raises:
        TypeError: If orig_strand is not a string.
        ValueError: If the sequence contains invalid DNA bases.

    Preconditions:
        - orig_strand is a string.
        - The sequence contains only A, T, C, and G.

    Postconditions:
        - The returned sequence has the same length as the input.
        - Each base is paired according to Watson-Crick rules.
        - The returned strand is in the 5' to 3' direction.
    """
    if not isinstance(orig_strand, str):
        raise TypeError("The DNA strand must be a string.")
        
    orig_strand = orig_strand.upper()
    valid_bases = {'A', 'T', 'C', 'G'}
    
    if any(base not in valid_bases for base in orig_strand):
        raise ValueError("DNA strand can contain only A, T, C, and G characters.")
    
    #define complementary base pairs
    pairs = {
        'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C'
    }
    
    #build the complementary strand
    complement = ""
    
    for base in orig_strand:
        complement = pairs[base] + complement
        
    return complement
        
    