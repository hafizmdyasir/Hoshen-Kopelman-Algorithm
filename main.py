from os import system, name
import gridgenerator
import oneDimension
import twodimensions


clearConsole = lambda: system('cls' if name in ('nt', 'dos') else 'clear')


def showMainScreen():
    print("\nHOSHEN - KOPELMAN ALGORITHM IMPLEMENTATION\nby Mohammad Yasir, M. Sc. Physics\n")
    print("""To continue, make a choice per the following:
        1. One dimension implementation:
            1.1. For a randomly generated matrix.
            1.2. For a user-input matrix.
        2. Two dimensions implementation:
            2.1 For a randomly generated matrix.
            2.2. For a user-input matrix.
        3. Exit the program.""")
    choice = float(input("Enter your choice... "))
    if choice not in (1.1, 1.2, 2.1, 2.2, 3):
        print("You have entered an incorrect choice. Press enter to retry...")
        delay = input()
        return False
    else:
        return choice


gridDictionary = {
    1.1: gridgenerator.oneDimensionRandom, 1.2: gridgenerator.oneDimensionInput,
    2.1: gridgenerator.twoDimensionRandom, 2.2: gridgenerator.twoDimensionInput
}

while True:
    clearConsole()
    choice = showMainScreen()
    if not choice:
        continue

    if choice == 3:
        break

    matrix = gridDictionary.get(key = choice)()
    if choice in (1.1, 1.2):
        oneDimension.countClusters(matrix)
    else:
        twodimensions.countClusters(matrix)

    restart = str(input("Program has finished execution. Would you like to restart? (Y/N)... "))
    if restart not in ('Y', 'y'):
        break