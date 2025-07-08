from itertools import permutations
from random import choice
import time
import os

#TODO:
#Change program to work with stores of any size: multiple functions
#Error checking!!
#Find a way to check best path from upcoming functions: maybe brute force?


#Aim is to store each location as a square on a grid
#Translate from base store notation into the grid form?

basestore = [
    [1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

bigbase = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, -1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

basestart = [0, 6]

baseitems = [[3, 2], [4, 2], [3, 11], [7, 10]]

bigstart = [0, 19]

def findDoor(store):
    # Finding start
    i = 0
    while i < len(store[0]):
        if store[0][i] == -1:
            break
        i += 1
    start = [0, i]
    return start

def buildStore(aisles, aisleLength):
    matrixWidth = 3 * aisles + 1
    matrixHeight = aisleLength + 6

    final = []

    for i in range(matrixHeight):
        if i == 0:
            newRow = [1]*matrixWidth
            newRow[int(matrixWidth/2)] = -1
            final.append(newRow)
        elif i == matrixHeight-1:
            newRow = [1]*matrixWidth
            final.append(newRow)
        elif i == 1 or i == 2 or i == matrixHeight-2 or i == matrixHeight-3:
            newRow = [0]*matrixWidth
            newRow[0] = 0
            newRow[matrixWidth-1] = 1
            final.append(newRow)
        else:
            newRow = [1, 0, 0]*aisles
            newRow.append(1)
            final.append(newRow)

    return final

def itemPlace(store):
    opt = input("Would you like a random set of items (R) or place them manually (M)?")
    items = []
    if opt == "R":
        amt = int(input("How many items would you like to place?"))
        items = generatePositions(amt, store)
        print("Item List Generated")
        print(items)
        return textListToCoordList(items, store)
    elif opt == "M":
        item = input("Enter the item you wish to place (Q to quit):\n")
        while item != "Q":
            items.append(item)
            item = input("Enter the item you wish to place (Q to quit):\n")
        return textListToCoordList(items, store)

def animateRoute(store, path, items):

    start = findDoor(store)

    items = printWithItems(store, items, start)

    for i in path:
        os.system('clear')
        items = printWithItems(store, items, i)
        time.sleep(0.25)


def start():
    storeChoice = ""
    while storeChoice != "1" and storeChoice != "2" and storeChoice != "3":
        storeChoice = input("""
    Which store would you like to use?
    1. Small
    2. Large
    3. Custom
    : """)
        if storeChoice == "1":
            store = basestore
        elif storeChoice == "2":
            store = bigbase
        elif storeChoice == "3":
            aisles = int(input("Enter the number of Aisles: \n"))
            length = int(input("Enter the length of the Aisles: \n"))
            store = buildStore(aisles, length)
        else:
            print("Invalid option chosen.")

    items = []
    printWithItems(store, items)

    while True:
        print("")
        print("What would you like to do?")
        optionChoice = input("""
    1. Chose item locations
    2. Run an algorithm on your store
    3. Return to store select
    4. Quit
    : """)

        if optionChoice == "1":
            items = itemPlace(store)
            printWithItems(store, items)
        elif optionChoice == "2":
            #Need check to see if items have been added.
            if items == []:
                print("Error. No items have been added.")
            else:
                algo = ""
                while algo != "1" and algo != "2" and algo != "3" and algo != "4" and algo != "5":
                    algo = input("""Which algorithm would you like to use?
1. First solution found
2. Brute Force
3. Brute Force with Pruning
4. Greedy Algorithm
5. Branch and Bound (WIP)
: """)

                if algo == "1":
                    print("Running First Solution Found Algorithm on your store:")
                    print("")
                    t = time.time()
                    result = list(firstSolution(store, items))
                    timeTaken = time.time() - t
                    print("Steps taken: " + str(result[0]))
                    print("Full Route: " + str(result[1]))
                    print("Item Order: " + str(result[2]))
                    print("Time taken: " + str(round(timeTaken*1000, 4)) + "ms")
                if algo == "2":
                    print("Running Brute Force Algorithm on your store:")
                    print("")
                    t = time.time()
                    result = list(bruteForce(store, items))
                    timeTaken = time.time() - t
                    print("Steps taken: " + str(result[0]))
                    print("Full Route: " + str(result[1]))
                    print("Item Order: " + str(result[2]))
                    print("Time taken: " + str(round(timeTaken * 1000, 4)) + "ms")
                if algo == "3":
                    print("Running Brute Force with Pruning Algorithm on your store:")
                    print("")
                    t = time.time()
                    result = list(improvedBruteForce(store, items))
                    timeTaken = time.time() - t
                    print("Steps taken: " + str(result[0]))
                    print("Full Route: " + str(result[1]))
                    print("Item Order: " + str(result[2]))
                    print("Time taken: " + str(round(timeTaken * 1000, 4)) + "ms")
                if algo == "4":
                    print("Running Greedy Algorithm on your store:")
                    print("")
                    t = time.time()
                    result = list(greedyAlgo(store, items))
                    timeTaken = time.time() - t
                    print("Steps taken: " + str(result[0]))
                    print("Full Route: " + str(result[1]))
                    print("Item Order: " + str(result[2]))
                    print("Time taken: " + str(round(timeTaken * 1000, 4)) + "ms")
                if algo == "5":
                    print("Running Branch and Bound Algorithm on your store:")
                    print("")
                    t = time.time()
                    result = list(branchAndBound(store, items))
                    timeTaken = time.time() - t
                    print("Steps taken: " + str(result[0]))
                    print("Full Route: " + str(result[1]))
                    print("Item Order: " + str(result[2]))
                    print("Time taken: " + str(round(timeTaken * 1000, 4)) + "ms")

                print("Animate the route taken? Y/N (Note: only works in terminal.)")
                anim = input(":")
                if anim == "Y":
                    animateRoute(store, result[1], items.copy())

                    #Testing stuff
                    print("Full Route: " + str(result[1]))
                    print("Item Order: " + str(result[2]))
                    print("Actual Items: " + str(items))
                    printWithItems(store, items)





        elif optionChoice == "3":
            start()
        elif optionChoice == "4":
            quit()
        else:
            print("Invalid option chosen.")






#We can make assumptions about the layout of the store to make traversing much easier
#So that we dont have to search to find an optimal route between items.

#With an item at [a, b] and another at [c, d]
#The theoretical shortest route would be |a-b| down and |c-d| across
#However we have walls. If we make an assumption that the 2nd and (n-1) row of the store will always be
#empty to allow walking between aisles, then no matter if there are walls preventing our initial strategy,
#The maximum amount of vertical steps will be m - 3

def generatePositions(amt, store):

    #matrixWidth = 3 * aisles + 1
    #matrixHeight = aisleLength + 6

    numAisles = int((len(store[0]) - 1) / 3)
    aisleHeight = int(len(store) - 6)

    aisles = []
    for i in range(1, numAisles + 1):
        aisles.append(str(i))

    bays = []
    for i in range(1, aisleHeight + 1):
        bays.append(str(i))

    sides = ["L", "R", "T", "B"]

    positions = []

    i = 0

    while i < amt:
        aisle = choice(aisles)
        side = choice(sides)
        if side != "T" and side != "B":
            bay = choice(bays)
        else:
            bay = ""
        final = aisle + side + bay

        if final != (aisles[-1] + "T") and final != (aisles[-1] + "B") and final not in positions:
            positions.append(final)
            i += 1
    return positions


#Converts initial grid to ascii version
def printStore(store):
    rows = len(store)
    cols = len(store[0])

    out = []

    line = ""
    line += "╔"
    for i in range(1, cols-1):
        if store[0][i] == 1:
            line += "═"
        elif store[0][i] == -1:
            line += "O"
    line += "╗"
    out.append(line)

    for row in store[1:-1]:
        row = row[1:-1]
        line = "║"
        for char in row:
            if char == 0:
                line += " "
            if char == 1:
                line += "│"
        line += "║"
        out.append(line)

    line = ""
    line += "╚"
    for i in range(cols - 2):
        line += "═"
    line += "╝"
    out.append(line)

    return out

#Adds items and prints ascii grid
def printWithItems(store, itemList, person=[]):
    storePic = printStore(store)




    for item in itemList:
        row = storePic[item[0]]
        newRow = row[:item[1]] + "*" + row[item[1] + 1:]
        storePic[item[0]] = newRow

    if person != []:
        row = storePic[person[0]]
        newRow = row[:person[1]] + "X" + row[person[1] + 1:]
        storePic[person[0]] = newRow

        if person in itemList:
            itemList.remove(person)


    numberrow = "•"
    for i in range(len(storePic[0])):
        numberrow += "•"

    print(numberrow)
    for line in range(len(storePic)):
        print("•" + storePic[line])

    return itemList

def textToCoord(input, store):
    #Currently no way to address top and bottom rows of the store, maybe add soon?
    aisle = input[0]
    if input[1] in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        aisle += input[1]
        pos = input[2]
        bay = input[3:]
    else:
        pos = input[1]
        bay = input[2:]

    Col = 1 + 3*(int(aisle)-1)

    if pos == "R":
        Col += 1
    elif pos == "T":
        Col += 2
        Row =  2
        return Row, Col
    elif pos == "B":
        Col += 2
        Row = len(store)-3
        return Row, Col

    Row = (len(store)-3) - int(bay)
    return Row, Col

def textListToCoordList(inputList, store):
    out = []
    for input in inputList:
        Row, Col = textToCoord(input, store)
        out.append([Row, Col])

    return out



#Find shortest path between two specified items in a given store
def findPath(itemA, itemB, store):
    steps = 0
    #Right now im unsure how to represent the paths, should they include start and dest?
    path = []

    #Note!! Currently my logic assumes that the start/end point is not on the same column as a wall.
    #As otherwise it would sidestep into the wall next to the entrance before going down. Which is not good.


    #bugfix! Currently if two items are both in the top two/bottom two rows, it does an extra sidestep.
    #only really relevant rn when moving off from start/back to end.

    #This bugfix created a new bug!

    #Rewriting this function
    #Current cases: ###
    #1. Items inside the same aisle
    #2. Items inside different aisles
    #3. One item on outside of aisle, one inside.
    #4. Both items outside of aisles.


    Arow, Acol, Brow, Bcol = itemA[0], itemA[1], itemB[0], itemB[1]

    matrixRows = len(store)


    #1: Both inside the same aisle.
    if abs(Acol - Bcol) <= 1 and (2 < Arow < (matrixRows-3)) and (2 < Brow < (matrixRows-3)):
        steps += abs(Acol - Bcol) + abs(Arow - Brow)

        currentPos = itemA.copy()

        #Note for future optimisation, could create a helper function for this, to avoid repeated code.
        horizontalSteps = abs(Acol - Bcol)
        for i in range(1, horizontalSteps + 1):
            if Acol > Bcol:
                currentPos[1] -= 1
                #Better way to append this?
                path.append([currentPos[0], currentPos[1]])
            else:
                currentPos[1] += 1
                path.append([currentPos[0], currentPos[1]])

        verticalSteps = abs(Arow - Brow)
        for i in range(1, verticalSteps + 1):
            if Arow > Brow:
                currentPos[0] -= 1
                path.append([currentPos[0], currentPos[1]])
            else:
                currentPos[0] += 1
                path.append([currentPos[0], currentPos[1]])

        return steps, path

    #2: Items inside different columns
    elif abs(Acol - Bcol) > 1 and (2 < Arow < (matrixRows-3)) and (2 < Brow < (matrixRows-3)):
        #This is shite, can it be made better?

        # Current plan is to model going over and under, and take the fastest route.
        upperRoute = abs(2 - Arow) + abs(Acol - Bcol) + abs(2 - Brow)
        lowerRoute = abs((matrixRows - 3) - Arow) + abs(Acol - Bcol) + abs((matrixRows - 3) - Brow)

        if upperRoute <= lowerRoute:
            steps = upperRoute

            currentPos = itemA.copy()
            verticalStepsOne = abs(2 - Arow)
            for i in range(1, verticalStepsOne + 1):
                currentPos[0] -= 1
                path.append([currentPos[0], currentPos[1]])

            horizontalSteps = abs(Acol - Bcol)
            for i in range(1, horizontalSteps + 1):
                if Acol > Bcol:
                    currentPos[1] -= 1
                    path.append([currentPos[0], currentPos[1]])
                else:
                    currentPos[1] += 1
                    path.append([currentPos[0], currentPos[1]])

            verticalStepsTwo = abs(2 - Brow)
            for i in range(1, verticalStepsTwo + 1):
                currentPos[0] += 1
                path.append([currentPos[0], currentPos[1]])

        else:
            steps = lowerRoute

            currentPos = itemA.copy()
            verticalStepsOne = abs((len(store) - 3) - Arow)
            for i in range(1, verticalStepsOne + 1):
                currentPos[0] += 1
                path.append([currentPos[0], currentPos[1]])

            horizontalSteps = abs(Acol - Bcol)
            for i in range(1, horizontalSteps + 1):
                if Acol > Bcol:
                    currentPos[1] -= 1
                    path.append([currentPos[0], currentPos[1]])
                else:
                    currentPos[1] += 1
                    path.append([currentPos[0], currentPos[1]])

            verticalStepsTwo = abs((len(store) - 3) - Brow)
            for i in range(1, verticalStepsTwo + 1):
                currentPos[0] -= 1
                path.append([currentPos[0], currentPos[1]])

        return steps, path

    #3: One item outside of aisle, one inside.
    #Gonna split this one into two separate statements, as the order of horizontal/vertical moves depends
    #On whether A is on the Outside or B

    #NOTE: Might need to add logic here or somewhere else for the impossible spots above aisles.
    elif ((2 < Arow < (matrixRows-3)) and (Brow <= 2 or (matrixRows-3) <= Brow)):
        steps += abs(Acol - Bcol) + abs(Arow - Brow)

        currentPos = itemA.copy()

        verticalSteps = abs(Arow - Brow)
        for i in range(1, verticalSteps + 1):
            if Arow > Brow:
                currentPos[0] -= 1
                path.append([currentPos[0], currentPos[1]])
            else:
                currentPos[0] += 1
                path.append([currentPos[0], currentPos[1]])

        horizontalSteps = abs(Acol - Bcol)
        for i in range(1, horizontalSteps + 1):
            if Acol > Bcol:
                currentPos[1] -= 1
                path.append([currentPos[0], currentPos[1]])
            else:
                currentPos[1] += 1
                path.append([currentPos[0], currentPos[1]])

        return steps, path

    #Aitem outside, Bitem inside aisle.
    elif ((Arow <= 2 or (matrixRows-3) <= Arow) and (2 < Brow < (matrixRows-3))):
        steps += abs(Acol - Bcol) + abs(Arow - Brow)

        currentPos = itemA.copy()

        horizontalSteps = abs(Acol - Bcol)
        for i in range(1, horizontalSteps + 1):
            if Acol > Bcol:
                currentPos[1] -= 1
                path.append([currentPos[0], currentPos[1]])
            else:
                currentPos[1] += 1
                path.append([currentPos[0], currentPos[1]])

        verticalSteps = abs(Arow - Brow)
        for i in range(1, verticalSteps + 1):
            if Arow > Brow:
                currentPos[0] -= 1
                path.append([currentPos[0], currentPos[1]])
            else:
                currentPos[0] += 1
                path.append([currentPos[0], currentPos[1]])



        return steps, path

    #4: Both items outside of aisles. Think it would be smart to split again, into cases where both are
    #same end of store, vs different ends.

    #This one maybe can be combined with a previous one, very similar body.
    elif (Arow <= 2 and Brow <= 2) or ((matrixRows-3) <= Arow and (matrixRows-3) <= Brow):
        steps += abs(Acol - Bcol) + abs(Arow - Brow)

        currentPos = itemA.copy()

        horizontalSteps = abs(Acol - Bcol)
        for i in range(1, horizontalSteps + 1):
            if Acol > Bcol:
                currentPos[1] -= 1
                path.append([currentPos[0], currentPos[1]])
            else:
                currentPos[1] += 1
                path.append([currentPos[0], currentPos[1]])

        verticalSteps = abs(Arow - Brow)
        for i in range(1, verticalSteps + 1):
            if Arow > Brow:
                currentPos[0] -= 1
                path.append([currentPos[0], currentPos[1]])
            else:
                currentPos[0] += 1
                path.append([currentPos[0], currentPos[1]])

        return steps, path

    elif ((Arow <= 2 and (matrixRows - 3) <= Brow) or ((matrixRows - 3) <= Arow and Brow <= 2)) and (Acol == Bcol):
        steps += 2 + abs(Arow - Brow)

        currentPos = itemA.copy()

        #One right step
        currentPos[1] += 1
        path.append([currentPos[0], currentPos[1]])

        verticalSteps = abs(Arow - Brow)
        for i in range(1, verticalSteps + 1):
            if Arow > Brow:
                currentPos[0] -= 1
                path.append([currentPos[0], currentPos[1]])
            else:
                currentPos[0] += 1
                path.append([currentPos[0], currentPos[1]])

        # One left step
        currentPos[1] -= 1
        path.append([currentPos[0], currentPos[1]])

        return steps, path

    #Does this need a special case when theyre on the end of the same aisle?? Yes.
    #Gonna take one horizontal step, go down/up then do rest of horizontal.
    elif (Arow <= 2 and (matrixRows-3) <= Brow) or ((matrixRows-3) <= Arow and Brow <= 2):
        steps += abs(Acol - Bcol) + abs(Arow - Brow)

        currentPos = itemA.copy()

        #One horizontal step.
        if Acol > Bcol:
            currentPos[1] -= 1
            path.append([currentPos[0], currentPos[1]])
        else:
            currentPos[1] += 1
            path.append([currentPos[0], currentPos[1]])

        verticalSteps = abs(Arow - Brow)
        for i in range(1, verticalSteps + 1):
            if Arow > Brow:
                currentPos[0] -= 1
                path.append([currentPos[0], currentPos[1]])
            else:
                currentPos[0] += 1
                path.append([currentPos[0], currentPos[1]])

        horizontalSteps = abs(currentPos[1] - Bcol)
        for i in range(1, horizontalSteps + 1):
            if currentPos[1] > Bcol:
                currentPos[1] -= 1
                path.append([currentPos[0], currentPos[1]])
            else:
                currentPos[1] += 1
                path.append([currentPos[0], currentPos[1]])

        return steps, path

    else:
        print("Error. Something went wrong calculating a path between two items")
        print(f"ItemA: {itemA}, ItemB {itemB}")

#Naive solution that places items in the order they're listed. No thought about distances.
#Looks like its working!
def firstSolution(store, items):
    steps = 1

    #Change to mean we don't need to pass start in, it will find it itself.
    start = findDoor(store)

    #Program runs into difficulty when dealing with the start zone, since its a row above. TO solve this, im gonna
    #basically make the square in front the start/stop, then manually make the first/final steps.

    fakeStart = [start[0]+1, start[1]]
    finalpath = [fakeStart]

    stops = [fakeStart]
    stops.extend(items)
    stops.append(fakeStart)



    i = 0
    while i < len(stops)-1:
        tempSteps, tempPath = findPath(stops[i].copy(), stops[i+1].copy(), store)
        steps += tempSteps
        finalpath.extend(tempPath)
        i = i + 1
    finalpath.append(start)
    steps += 1

    return steps, finalpath, stops



def bruteForce(store, items):
    perms = []
    for perm in permutations(items):
        perms.append(list(perm))

    bestSteps = 1000000
    bestPath = []
    bestOrder = []

    for order in perms:
        tempSteps, tempPath, tempOrder = firstSolution(store, order)
        if tempSteps < bestSteps:
            bestSteps = tempSteps
            bestPath = tempPath
            bestOrder = tempOrder

    return bestSteps, bestPath, bestOrder

def greedyAlgo(store, items):

    start = findDoor(store)

    steps = 0
    path = []
    order = []

    fakeStart = [start[0] + 1, start[1]]

    toVisit = [fakeStart]
    toVisit.extend(items)

    currentPos = start

    while len(toVisit) > 0:
        tempSteps, tempPath = 0, []

        closestDist = 10000000
        closestItem = None
        closestPath = []

        for item in toVisit:
            tempDist, tempPath = findPath(currentPos.copy(), item.copy(), store)
            if tempDist < closestDist:
                closestDist = tempDist
                closestItem = item.copy()
                closestPath = tempPath

        steps += closestDist
        path.extend(closestPath)

        currentPos = closestItem.copy()
        order.append(currentPos)

        toVisit.remove(closestItem)

    tempSteps, tempPath = findPath(currentPos, fakeStart, store)

    steps += tempSteps
    path.extend(tempPath)
    order.append(fakeStart)

    steps += 1
    path.append(start)

    return steps, path, order

#Improved brute force helper function, returns 0 0 0 if the current solution is worse than the best seen.
def improvedBFHelper(store, start, items, best):
    steps = 1

    # Program runs into difficulty when dealing with the start zone, since its a row above. TO solve this, im gonna
    # basically make the square in front the start/stop, then manually make the first/final steps.

    fakeStart = [start[0] + 1, start[1]]
    finalpath = [fakeStart]

    stops = [fakeStart]
    stops.extend(items)
    stops.append(fakeStart)

    i = 0
    while i < len(stops) - 1:
        tempSteps, tempPath = findPath(stops[i].copy(), stops[i + 1].copy(), store)
        steps += tempSteps
        finalpath.extend(tempPath)
        i = i + 1

        if steps > best:
            return 0, 0, 0
    finalpath.append(start)
    steps += 1

    if steps > best:
        return 0, 0, 0

    return steps, finalpath, stops




#Improved brute force: will be the same, but if a solution exceeds the current best seen, then it will not be considered further.
def improvedBruteForce(store, items):
    perms = []
    for perm in permutations(items):
        perms.append(list(perm))

    bestSteps = 1000000
    bestPath = []
    bestOrder = []

    start = findDoor(store)

    for order in perms:
        tempSteps, tempPath, tempOrder = improvedBFHelper(store, start, order, bestSteps)
        if tempSteps != 0 and tempSteps < bestSteps:
            bestSteps = tempSteps
            bestPath = tempPath
            bestOrder = tempOrder

    return bestSteps, bestPath, bestOrder

def createAdjacencyMatrix(store, items):

    start = findDoor(store)
    fakeStart = [1, start[1]]

    nodes = [fakeStart]
    nodes.extend(items)

    adj = []
    for a in range(len(nodes)):
        row = [0] * len(nodes)
        adj.append(row)

    i = 0

    while i < len(nodes):
        for j in range(i, len(nodes)):
            if i == j:
                continue
            else:
                steps, path = findPath(nodes[i], nodes[j], store)
                adj[i][j], adj[j][i] = steps, steps
        i += 1


    return adj

def firstMin(adj, i):
    min = 100000
    for k in range(len(adj[0])):
        if adj[i][k] < min and i != k:
            min = adj[i][k]

    return min

def secondMin(adj, i):
    first, second = 100000, 100000
    for j in range(len(adj[0])):
        if i == j:
            continue
        if adj[i][j] <= first:
            second = first
            first = adj[i][j]

        elif(adj[i][j] <= second and
             adj[i][j] != first):
            second = adj[i][j]

    return second

def BnBHelper(adj, currentBound, currentWeight, currentPath, level, visited):
    global finalSteps
    global finalPath
    layers = len(adj[0])

    #print("level: ", level)
    #print("currentWeight: ", currentWeight)
    #print("currentPath: ", currentPath)
    #print("currentBound: ", currentBound)

    if level == layers:

        if adj[currentPath[level-1]][currentPath[level]] != 0:
            currentResult = currentWeight + adj[currentPath[level-1]][currentPath[level]]

            if currentResult < finalSteps:
                finalPath[:layers + 1] = currentPath[:]
                finalPath[layers] = currentPath[0]
                finalSteps = currentResult
        return

    for i in range(layers):
        #print("hello")
        if (adj[currentPath[level-1]][i] != 0 and visited[i] == False):
            #print("taken!")
            temp = currentBound
            currentWeight += adj[currentPath[level-1]][i]

            if level == 1:
                currentBound -= ((firstMin(adj, currentPath[level - 1]) +
                                firstMin(adj, i)) / 2)
            else:
                currentBound -= ((secondMin(adj, currentPath[level - 1]) +
                                firstMin(adj, i)) / 2)

            #print(currentBound)
            #print(currentWeight)

            if currentBound + currentWeight < finalSteps:
                currentPath[level] = i
                visited[i] = True

                BnBHelper(adj, currentBound, currentWeight, currentPath, level + 1, visited)

            currentWeight -= adj[currentPath[level-1]][i]
            currentBound  = temp

            visited = [False] * len(visited)
            for j in range(level):
                if currentPath[j] != -1:
                    visited[currentPath[j]] = True

def branchAndBound(store, items):
    global finalSteps
    global finalPath
    #1. Create adjacency matrix.
        #New func for this?
        #NOTE: For this to work, we need to consider fakestart as a location in the adjacency matrix (node 0)

    #Idea taken closely from geeksforgeekscode lmao
    adj = createAdjacencyMatrix(store, items)

    layers = len(adj[0])
    finalPath = [None] * (layers+1)
    visited = [False] * layers
    finalSteps = 100000

    currentBound = 0
    currentPath = [-1] * (layers+1)

    for i in range(layers):
        currentBound += (firstMin(adj, i) + secondMin(adj, i))

    currentBound = int(currentBound / 2)

    visited[0] = True
    currentPath[0] = 0

    BnBHelper(adj, currentBound, 0, currentPath, 1, visited)


    #print("Final Steps: ", finalSteps)
    #print("Final Path in BNB: ", finalPath)

    #print("items", items)

    #Need to convert to regular format, plus add two for final/first steps.
    finalSteps += 2

    fullPath = []
    itemPath = []

    start = findDoor(store)
    fakeStart = [1, start[1]]
    nodes = [fakeStart]
    nodes.extend(items)

    i = 0
    itemPath.append(nodes[0])
    while i < len(finalPath)-1:
        steps, path = findPath(nodes[finalPath[i]], nodes[finalPath[i+1]], store)
        fullPath.extend(path)
        itemPath.append(nodes[finalPath[i+1]])
        i += 1

    return finalSteps, fullPath, itemPath

finalPath = []
finalSteps = 100000

start()
#test = [[2, 8], [3, 7]]

#Known bug with one item! to do with 2ndmin function.
#test = [[2, 8]]

"""printWithItems(basestore, [[3, 10], [1, 6]])
steps, path = findPath([3, 10], [1, 6], basestore)
print(path)"""

#animateRoute(basestore, path, [[2, 3], [6, 3]])

#branchAndBound(basestore, test)

#steps, path, order = bruteForce(basestore, [[2, 9], [3, 7]])


#animateRoute(basestore, path, [[2, 9], [3, 7]])

