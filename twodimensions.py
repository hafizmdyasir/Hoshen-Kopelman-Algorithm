from itertools import product
from gridgenerator import print2DMatrix


# The variable which holds the entire matrix.
grid = []

# In clusterAliases, the value corresponding to a key is the negative of the cluster label to which, it belongs. 
# A positive value implies root label.
clusterAliases = {}

# To create a cluster, we increase the runningVariable by 1, and set the value corresponding to it in clusterSizes equal to 1. Return the label of the newly created cluster, which is basically runningVariable.
def createCluster(runningVariable):
    global clusterAliases

    runningVariable += 1
    clusterAliases[runningVariable] = 1
    return runningVariable


# To add to a particular cluster, we must increment its size by 1. 
# The return value is simply label. 
def addToCluster(label): 
    clusterAliases[findOriginal(label)] += 1
    return label


# The findOriginal method must return the original number to which cluster labelled 'label' belongs.
# This can be checked for by ensuring that the value corresponding to label in clusterAliases is positive.
def findOriginal(label):
    while clusterAliases[label] < 0: 
        label = -clusterAliases[label]
    
    return label


# unifyClusters marks two clusters to be the same.
def unifyClusters(above, left):
    global clusterAliases

    # If the clusters are already linked, just add to the cluster above/left. 
    if above == left:
        return addToCluster(above)

    # If the two clusters are already linked "behind the scenes", then no need to re-link and add masses of both. Just add one to the mass.
    # If we add the masses of both clusters in this scenario, it would cause double addition.
    if findOriginal(left) == findOriginal(above):
        clusterAliases[findOriginal(above)] += 1
        return above

    # The final scenario is when the clusters aren't linked.
    clusterAliases[findOriginal(above)] += clusterAliases[findOriginal(left)] + 1
    clusterAliases[left] = -findOriginal(above)
    return above


# The heart of the Hoshen-Kopelman algorithm
def hoshenKopelman(grid):

    # The running variable denotes the largest cluster number encountered.
    runningVariable = 2

    for i, j in product(range(len(grid)), range(len(grid[0]))):
        # If the site is empty, do nothing
        if grid[i][j] == 0:
            continue

        # Simple boolean variables to check whether no neighbour, one neighbour, or two neighbours. 
        occupiedAbove = False if i == 0 else (grid[i-1][j] != 0)
        occupiedLeft = False if j == 0 else (grid[i][j-1] != 0)

        if (not occupiedAbove) and (not occupiedLeft):
            runningVariable = createCluster(runningVariable)
            grid[i][j] = runningVariable

        # XOR is true when only one is true
        elif occupiedAbove ^ occupiedLeft:
            grid[i][j] = addToCluster(grid[i-1][j] if occupiedAbove else grid[i][j-1])
        
        elif occupiedAbove and occupiedLeft:
            above = grid[i-1][j]
            left = grid[i][j-1]
            grid[i][j] = unifyClusters(above, left)


# The job of reduceMatrix() is to replace the values in grid with the root labels
def renameClusters(grid):
    for i, j in product(range(len(grid)), range(len(grid[0]))):
        if grid[i][j] != 0:  
            grid[i][j] = findOriginal(grid[i][j])


# For counting the clusters, just count the number of keys that have positive values.
def countDistinctClusters():
    clusterCount = 0
    for key in clusterAliases.keys():
        if clusterAliases[key] > 0:
            clusterCount += 1

    return clusterCount


def countClusters(matrix):
    global runningVariable
    global clusterAliases

    grid = [[1 if item else 0 for item in x] for x in matrix]
    clusterAliases.clear()
    runningVariable = 2

    print("The matrix you have entered is:")
    print2DMatrix(grid)
    print("\nStarting labelling... ")
    rename = str(input("Would you like to perform renaming of clusters after labelling is complete? (Y/N)... ")) in ('y', 'Y')
    hoshenKopelman(grid)
    if rename:
        renameClusters(grid)
    clusterCount = countDistinctClusters()

    print("Labelling complete. The matrix is now:\n")
    print2DMatrix(grid)
    print("\nEncountered {0} clusters of which, {1} were distinct. Their sizes and aliases are as follows:\n\t{2}".format(max(map(max, grid)), clusterCount, clusterAliases))
    print("\n")
    delay = input("Press enter to continue...")