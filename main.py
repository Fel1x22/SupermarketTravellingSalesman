from itertools import permutations
from random import choice

#TODO:
#Change program to work with stores of any size: multiple functions
#Error checking!!
#Find a way to check best path from upcoming functions: maybe brute force?


#Aim is to store each location as a square on a grid
#Translate from base store notation into the grid form?

#How to store each square? As list of distances? That doesnt make sense

#m rows and n columns
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

#Gonna start by just specifying using regular coordinates.

basestart = [0, 6]

baseitems = [[3, 2], [4, 2], [3, 11], [7, 10]]

bigstart = [0, 19]

#We can make assumptions about the layout of the store to make traversing much easier
#So that we dont have to search to find an optimal route between items.

#With an item at [a, b] and another at [c, d]
#The theoretical shortest route would be |a-b| down and |c-d| across
#However we have walls. If we make an assumption that the 2nd and (n-1) row of the store will always be
#empty to allow walking between aisles, then no matter if there are walls preventing our initial strategy,
#The maximum amount of vertical steps will be m - 3

#How to decide which way round the aisles to move when getting another item?

def generatePositions(amt):
    aisles = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
    sides = ["L", "R", "T", "B"]
    bays = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16"]

    positions = []

    for i in range(amt):
        aisle = choice(aisles)
        side = choice(sides)
        if side != "T" and side != "B":
            bay = choice(bays)
        else:
            bay = ""
        final = aisle + side + bay

        if final != "12B" and final != "12T" and final not in positions:
            positions.append(final)
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
def printWithItems(store, itemList):
    storePic = printStore(store)
    for item in itemList:
        row = storePic[item[0]]
        newRow = row[:item[1]] + "*" + row[item[1] + 1:]
        storePic[item[0]] = newRow

    numberrow = "•"
    for i in range(len(storePic[0])):
        numberrow += "•"

    print(numberrow)
    for line in range(len(storePic)):
        print("•" + storePic[line])

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

    if (abs(itemA[1]-itemB[1]) == 0 and (itemA[1] % 3 == 0)):
        #Take one step right, go down aisle then go one back left.
        currentPos = itemA.copy()
        steps += 2 + abs(itemA[0] - itemB[0])

        currentPos[1] = currentPos[1] + 1
        path.append([currentPos[0], currentPos[1]])

        verticalSteps = abs(itemA[0] - itemB[0])
        for i in range(1, verticalSteps + 1):
            if itemA[0] > itemB[0]:
                currentPos[0] = currentPos[0] - 1
                path.append([currentPos[0], currentPos[1]])
            else:
                currentPos[0] = currentPos[0] + 1
                path.append([currentPos[0], currentPos[1]])


        currentPos[1] = currentPos[1] - 1
        path.append([currentPos[0], currentPos[1]])

        return steps, path
        #Currently just checking whether in top/bot rows. Should add check for adjacent cols as well.
    elif (itemA[0] == 1) or (itemA[0] == 2) or (itemA[0] == len(store)-2) or (itemA[0] == len(store)-3):

        steps += abs(itemA[1] - itemB[1]) + abs(itemA[0] - itemB[0])
        currentPos = itemA.copy()

        horizontalSteps = abs(itemA[1] - itemB[1])
        for i in range(1, horizontalSteps + 1):
            if itemA[1] > itemB[1]:
                currentPos[1] = currentPos[1] - 1
                path.append([currentPos[0], currentPos[1]])
            else:
                currentPos[1] = currentPos[1] + 1
                path.append([currentPos[0], currentPos[1]])

        verticalSteps = abs(itemA[0] - itemB[0])
        for i in range(1, verticalSteps+1):
            if itemA[0] > itemB[0]:
                currentPos[0] = currentPos[0] - 1
                path.append([currentPos[0], currentPos[1]])
            else:
                currentPos[0] = currentPos[0] + 1
                path.append([currentPos[0], currentPos[1]])

        return steps, path

    elif (itemB[0] == 1) or (itemB[0] == 2) or (itemB[0] == len(store)-2) or (itemB[0] == len(store)-3)\
            or (abs(itemA[1]-itemB[1]) == 1) or (abs(itemA[1]-itemB[1]) == 0):

        steps += abs(itemA[1] - itemB[1]) + abs(itemA[0] - itemB[0])
        currentPos = itemA.copy()

        verticalSteps = abs(itemA[0] - itemB[0])
        for i in range(1, verticalSteps+1):
            if itemA[0] > itemB[0]:
                currentPos[0] = currentPos[0] - 1
                path.append([currentPos[0], currentPos[1]])
            else:
                currentPos[0] = currentPos[0] + 1
                path.append([currentPos[0], currentPos[1]])

        horizontalSteps = abs(itemA[1] - itemB[1])
        for i in range(1, horizontalSteps+1):
            if itemA[1] > itemB[1]:
                currentPos[1] = currentPos[1] - 1
                path.append([currentPos[0], currentPos[1]])
            else:
                currentPos[1] = currentPos[1] + 1
                path.append([currentPos[0], currentPos[1]])

        return steps, path
    else:
        #Current plan is to model going over and under, and take the fastest route.

        upperRoute = abs(2-itemA[0]) + abs(itemA[1] - itemB[1]) + abs(2-itemB[0])
        lowerRoute = abs((len(store)-3)-itemA[0]) + abs(itemA[1] - itemB[1]) + abs((len(store)-3)-itemB[0])

        if upperRoute <= lowerRoute:
            steps = upperRoute

            currentPos = itemA.copy()
            verticalStepsOne = abs(2 - itemA[0])
            for i in range(1, verticalStepsOne + 1):
                currentPos[0] = currentPos[0] - 1
                path.append([currentPos[0], currentPos[1]])

            horizontalSteps = abs(itemA[1] - itemB[1])
            for i in range(1, horizontalSteps + 1):
                if itemA[1] > itemB[1]:
                    currentPos[1] = currentPos[1] - 1
                    path.append([currentPos[0], currentPos[1]])
                else:
                    currentPos[1] = currentPos[1] + 1
                    path.append([currentPos[0], currentPos[1]])

            verticalStepsTwo = abs(2 - itemB[0])
            for i in range(1, verticalStepsTwo + 1):
                currentPos[0] = currentPos[0] + 1
                path.append([currentPos[0], currentPos[1]])

        else:
            steps = lowerRoute

            currentPos = itemA.copy()
            verticalStepsOne = abs((len(store)-3) - itemA[0])
            for i in range(1, verticalStepsOne + 1):
                currentPos[0] = currentPos[0] + 1
                path.append([currentPos[0], currentPos[1]])

            horizontalSteps = abs(itemA[1] - itemB[1])
            for i in range(1, horizontalSteps + 1):
                if itemA[1] > itemB[1]:
                    currentPos[1] = currentPos[1] - 1
                    path.append([currentPos[0], currentPos[1]])
                else:
                    currentPos[1] = currentPos[1] + 1
                    path.append([currentPos[0], currentPos[1]])

            verticalStepsTwo = abs((len(store)-3) - itemB[0])
            for i in range(1, verticalStepsTwo + 1):
                currentPos[0] = currentPos[0] - 1
                path.append([currentPos[0], currentPos[1]])


        return steps, path

#Naive solution that places items in the order they're listed. No thought about distances.
#Looks like its working!
def firstSolution(store, start, items):
    steps = 1


    #Program runs into difficulty when dealing with the start zone, since its a row above. TO solve this, im gonna
    #basically make the square in front the start/stop, then manually make the first/final steps.

    fakeStart = [start[0]+1, start[1]]
    finalpath = [fakeStart]
    #print("Path at start", finalpath)

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
        tempSteps, tempPath, tempOrder = firstSolution(store, bigstart, order)
        if tempSteps < bestSteps:
            bestSteps = tempSteps
            bestPath = tempPath
            bestOrder = tempOrder

    return bestSteps, bestPath, bestOrder

def greedyAlgo(store, items, start):

    steps = 0
    path = []
    order = []

    fakeStart = [start[0] + 1, start[1]]

    toVisit = [fakeStart]
    toVisit.extend(items)

    currentPos = start

    #print("Variables at start: ", start, fakeStart, toVisit, currentPos)


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

        """ print("TempSteps: ", closestDist)
        print("TempPath: ", closestPath)
        print("Closest Item: ", closestItem)"""

        steps += closestDist
        #print("Path Before : ", path)
        path.extend(closestPath)
        #print("Path After : ", path)

        currentPos = closestItem.copy()
        order.append(currentPos)

        toVisit.remove(closestItem)


        """print("Path at this point: ", path)
        print("")
        print("Visited: ", order)
        print("To Visit: ", toVisit)
        print("")
        print("")"""

    tempSteps, tempPath = findPath(currentPos, fakeStart, store)

    steps += tempSteps
    path.extend(tempPath)
    order.append(fakeStart)

    steps += 1
    path.append(start)

    return steps, path, order



positions = generatePositions(6)

#positions = ["7L16"]


print(positions)
printWithItems(bigbase, textListToCoordList(positions, bigbase))
brute = list(bruteForce(bigbase, textListToCoordList(positions, bigbase)))
print("Brute Force:")
print(brute[0])
print(brute[1])
print(brute[2])

greedy = list(greedyAlgo(bigbase, textListToCoordList(positions, bigbase), bigstart))
print("Greedy:")
print(greedy[0])
print(greedy[1])
print(greedy[2])

print("")
print("First: ")
print(firstSolution(bigbase, bigstart, textListToCoordList(positions, bigbase)))


print("")
print(brute[1])
print(greedy[1])
print(len(brute[1]))
print(len(greedy[1]))