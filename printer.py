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

from tabulate import tabulate


# Helper method to print a dictionary in tabular format.
def printDictionary(dictionary):
    for key, value in dictionary.items():
        print("{0}\t|\t{1}".format(key, value))


#A helper method to print a 2D matrix
def print2DMatrix(matrix):
    print(tabulate(matrix))
