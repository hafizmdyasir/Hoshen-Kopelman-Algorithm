from random import uniform


#A helper method to print a 2D matrix
def print2DMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end = " ")
        print("")


# Generate a random grid with a given occupation probability. Note that the probability effects kick in best when size is very large.
def oneDimensionRandom():
    # A random number being smaller than occupation probability is considered to be the criterion for the site to be occupied.
    
    occupationProbability = float(input("\nEnter the occupation probability desired... "))
    size = int(input("Enter the length of the matrix... "))
    grid = [uniform(0, 1) <= occupationProbability for i in range(size)]
    return grid


# This time, let the user enter a one dimensional lattice.
def oneDimensionInput(tab = False):
    message ="{0}Enter the grid information in terms of 0 and 1, separated by comma (,)... ".format("\t" if tab else "")
    raw = list(map(int, str(input(message)).split(",")))
    return raw


# Same as oneDimensionRandom(), but in two dimensions
# The parameter size is a tuple,
def twoDimensionRandom():

    occupationProbability = float(input("\nEnter the occupation probability desired... "))
    size = list(map(int, str(input("Enter the number of rows and columns, separated by comma only... ")).split(",")))

    rows = size[0]
    columns = size[1]

    grid = [[0 for i in range(rows)] for j in range(columns)]
    for i in range(rows):
        for j in range(columns):
            # Once again, we generate a random number and say the site is occupied if the random number is less than occupation probability.
            grid[i][j] = uniform(0, 1) <= occupationProbability
    
    return grid


# Same as oneDimensionInput(), but in two dimensions.
def twoDimensionInput():
    rows = int(input("Enter the number of rows you want... "))
    grid = [[]]*rows
    # We can simply reuse the oneDimensionInput() function for each row of the lattice.
    for i in range(rows):
        print("Row number {0}:".format(i))
        grid[i] = oneDimensionInput(True)
    
    return grid