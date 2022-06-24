# Google Code Jam 2022
# Twisty Little Passages
# Naman Modani

# Press F to pay respects

import random

def main():
    numberOfCases = int(input())

    for case in range(numberOfCases):
        numberOfRooms, numberOfTries = map(int, input().split())
        roomNumber, numberOfPassages = map(int, input().split())

        allPassages = 0

        if numberOfTries > numberOfRooms:
            numberOfTries = numberOfRooms
        randomTries = list(range(1, numberOfRooms + 1))
        random.shuffle(randomTries)
        randomTries = randomTries[:numberOfTries-1]

        for i in randomTries:
            print('T ' + str(i), flush = True)
            roomNumber, numberOfPassages = map(int, input().split())
            allPassages += numberOfPassages

        if numberOfRooms <= numberOfTries:
            m = int(allPassages / 2)
        else:
            n = numberOfRooms - numberOfTries
            m = int(allPassages / 2) + ((n * allPassages / numberOfTries) / 2)

        print('E ' + str(int(m)), flush = True)

main()

