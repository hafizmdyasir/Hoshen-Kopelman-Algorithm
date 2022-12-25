import gridgenerator


def countClusters(grid):
    
    clusterCount = 0
    sizeOfCluster = {}
    modifiedGrid = [int(x==1) for x in grid]

    for i in range(len(grid)):
        # If the site isn't occupied, we can simply continue to the next one.
        if not grid[i]:
            continue
        # From this point on, the site at index 'i' is necessarily occupied.

        # The first scenario is when the first site is occupied and thus, starts a cluster, the first cluster.
        if i == 0:
            clusterCount += 1
            sizeOfCluster[clusterCount] = 1
            continue

        # This is the second scenario wherein, the previous site is occupied and thus, this is not a new cluster.
        if grid[i-1] == 1:
            sizeOfCluster[clusterCount] += 1
            modifiedGrid[i] = modifiedGrid[i-1]
            continue

        # In the final senario, the site [i] starts an entirely new cluster.
        # No condition check is required since the control flow is sure to have reached there only as a last resort.
        clusterCount += 1
        sizeOfCluster[clusterCount] = 1
        modifiedGrid[i] = clusterCount

    print(grid)
    print(clusterCount)
    print(sizeOfCluster)
    print(modifiedGrid)

countClusters(gridgenerator.oneDimensionRandom(0.6, 12))