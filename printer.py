# ###################################################### #
#                                                        #
# COPYRIGHT BLOCK. DO NOT REMOVE                         #
#                                                        #
# Filename    | 'printer.py'                             #
# Created     | 27.12.2022                               # 
# Description | The functions in printer.py can be used  #
#               to display a matrix, dictionary, etc. in #
#               proper format.                           #
#                                                        #
# This file and its contents are intellectual properties #
# of Mohammad Yasir and unauthorized usage, or usage     #
# without proper credit to the author may lead to legal  #
# consequences.                                          #
#                                                        #
# ###################################################### #


# Helper method to print a dictionary in tabular format.
def printDictionary(dictionary):
    keys = list(dictionary.keys())
    length = len(keys)
    if length == 0:
        print("Empty dictionary: {}")
        return

    # Prefer an 8-column, 4 entries per line layout
    i = 0
    for key, value in dictionary.items():
        print("{0}\t|\t{1}".format(key, value))


#A helper method to print a 2D matrix
def print2DMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print(matrix[i][j], end = " ")
        print("")
