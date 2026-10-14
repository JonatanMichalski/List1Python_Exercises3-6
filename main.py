from list1 import divisible
from list1 import common
from list1 import subsets
from list1 import random_walk
import matplotlib.pyplot as plt    
from list1 import dna_complement
from find_genes import find_genes

numbers = [1,2,3,4,5]
divisor = 3
my_set = {1, 2, 3}
steps = 100

try:
    result = divisible(numbers, divisor)
    print("Original list:", numbers)
    print("Divisor: ", divisor)
    print("Result: ", result)
except (TypeError, ValueError) as error:
    print("Error: ", error)
    
x = [7,5,2,1,8,5,6,8]
y = [8,6,8,3,4,5,2]

try:
    result = common(x, y)
    print("List x:", x)
    print("List y:", y)
    print("Common:", result)
except (TypeError) as error:
    print("Error: ", error)
    
try:
    result = subsets(my_set)
    print("Original set: ", my_set)
    print("Subsets of x: ", result)
except TypeError as error:
    print("Error: ", error)
    
try:
    coordinates = random_walk(steps)
    x, y = zip(*coordinates)
    plt.plot(x, y, marker='o', linestyle='-', markersize=2)
    plt.xlabel('X Coordinate')
    plt.ylabel('Y Coordinate')
    plt.title("Walker's Trajectory")
    plt.grid(True)
    plt.axis('equal')
    plt.show()
except (ValueError, TypeError) as error:
    print(f"Input error: {error}")
    
try:
    orig_strand = "ATCG"
    result = dna_complement(orig_strand)

    print("Original strand:", orig_strand)
    print("Complementary strand:", result)
except (TypeError, ValueError) as error:
    print("Error:", error)
    