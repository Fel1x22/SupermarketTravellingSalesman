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

#We can make assumptions about the layout of the store to make traversing much easier
#So that we dont have to search to find an optimal route between items.

#With an item at [a, b] and another at [c, d]
#The theoretical shortest route would be |a-b| down and |c-d| across
#However we have walls. If we make an assumption that the 2nd and (n-1) row of the store will always be
#empty to allow walking between aisles, then no matter if there are walls preventing our initial strategy,
#The maximum amount of vertical steps will be m - 3

#How to decide which way round the aisles to move when getting another item?

#Converts initial grid to ascii version
def printStore(store):
    rows = len(store)
    cols = len(store[0])

    out = []

    line = ""
    line += "╔"
    for i in range(cols-2):
        line += "═"
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

    for line in storePic:
        print(line)

def textToCoord(input, store):
    Col = 1 + 3*(int(input[0])-1)

    if input[1] == "R":
        Col += 1
    elif input[1] == "T":
        Col += 2
        Row =  2
        return Row, Col
    elif input[1] == "B":
        Col += 2
        Row = len(store)-3
        return Row, Col

    Row = (len(store)-4) - int(input[2:])
    return Row, Col



#Find shortest path between two specified items in a given store
def findPath(itemA, itemB, store):
    steps = 0
    #Right now im unsure how to represent the paths, should they include start and dest?
    path = []

    #Currently just checking whether in top/bot rows. Should add check for adjacent cols as well.
    if (itemA[0] == 1) or (itemA[0] == 2) or (itemB[0] == 1) or (itemB[0] == 2) or (itemA[0] == len(store)-2) or (itemA[0] == len(store)-3) or (itemB[0] == len(store)-2) or (itemB[0] == len(store)-3)\
            or (abs(itemA[1]-itemB[1]) < 1):

        steps += abs(itemA[1] - itemB[1]) + abs(itemA[0] - itemB[0])
        currentPos = itemA

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
        print(len(store))
        print(upperRoute, lowerRoute)

        if upperRoute <= lowerRoute:
            steps = upperRoute

            currentPos = itemA
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
                print("hello")
                currentPos[0] = currentPos[0] + 1
                path.append([currentPos[0], currentPos[1]])

        else:
            steps = lowerRoute

            currentPos = itemA
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


def firstSolution(store, start, items):
    stepsTaken = 0
    finished = False
    stepsTaken += abs(start[0] - items[0][0])
    stepsTaken += abs(start[1] - items[0][1])
    print(stepsTaken)


#def bruteForce(store, items):


#firstSolution(basestore, basestart, baseitems)

steps, path = findPath([4, 2], [3, 11], basestore)
print(steps)
print(path)

Row, Col = textToCoord("4L12", bigbase)
print(Row, Col)

printWithItems(bigbase, [[Row, Col]])