#               Mahmoud Khaled Jamal Qasem              AI Project Using DFS Agorithm                 201910708                 #

from tkinter import *
import random
import math
import time

root = Tk()

btn = []  # Array storing all the buttons
numOfBombs = 40  # Number of bombs
numOfRows = 20  # Number of rows
numOfCols = 20  # Number of columns
# countIterations=0

initialPause = 2000
waitTime = 1000


restartCount = 0

StartRow = 10
StartCol = 10
StartIndex = ((StartRow-1)*numOfCols) + StartCol - 1

btnNumber = 0  # Variable to track which button has been clicked

numOfClickedTiles = 0


my_str = StringVar()
l1 = Label(root, textvariable=my_str)
l1.grid(row=0, column=0, columnspan=10)


def FlagClick(x, y, index):
    btnBox = btn[index]
    if isClickedList[index] == 0:
        if isFlaggedList[index] == 0:
            btnBox.config(text="f")
            btnBox.config(fg="red")
            isFlaggedList[index] = 1
        else:
            if isFlaggedList[index] == 1:
                btnBox.config(text="")
                isFlaggedList[index] = 0


def spiral(X, Y):
    updateCount = 0
    x = y = 0
    dx = 0
    dy = -1
    #print(str(X) + " + " + str(Y))
    # The function enters a for loop that will run max(X, Y)**2 times.
    # This is because the maximum number of iterations needed to cover the entire grid is equal to the maximum of X and Y squared.
    for i in range(max(X, Y)**2):
        if (-X/2 < x <= X/2) and (-Y/2 < y <= Y/2):
            #print(math.ceil(x+X/2), math.ceil(y+Y/2))
            xtemp = math.ceil(x+X/2)-1
            ytemp = math.ceil(y+Y/2)-1
            indextemp = ((ytemp)*numOfCols) + xtemp
            btnBox = btn[indextemp]

            nearbyClickedCount = 0

            numOfNearbyTiles = 0

            if isClickedList[indextemp] == 1:

                tileClick(xtemp, ytemp, indextemp)

                # Check how many surrounding cells have been clicked
                # Check cell to the left
                if xtemp != 0 and isClickedList[indextemp-1] == 1:
                    nearbyClickedCount = nearbyClickedCount + 1
                # Check cell to the right
                if xtemp != numOfCols-1 and isClickedList[indextemp+1] == 1:
                    nearbyClickedCount = nearbyClickedCount + 1
                # Check cell above
                if ytemp != 0 and isClickedList[indextemp-numOfCols] == 1:
                    nearbyClickedCount = nearbyClickedCount + 1
                # Check cell below
                if ytemp != numOfRows-1 and isClickedList[indextemp+numOfCols] == 1:
                    nearbyClickedCount = nearbyClickedCount + 1
                # Check cell up & left
                if xtemp != 0 and ytemp != 0 and isClickedList[indextemp-1-numOfCols] == 1:
                    nearbyClickedCount = nearbyClickedCount + 1
                # Check cell up & right
                if xtemp != numOfCols-1 and ytemp != 0 and isClickedList[indextemp+1-numOfCols] == 1:
                    nearbyClickedCount = nearbyClickedCount + 1
                # Check cell down & left
                if xtemp != 0 and ytemp != numOfRows-1 and isClickedList[indextemp-1+numOfCols] == 1:
                    nearbyClickedCount = nearbyClickedCount + 1
                # Check cell down & right
                if xtemp != numOfCols-1 and ytemp != numOfRows-1 and isClickedList[indextemp+1+numOfCols] == 1:
                    nearbyClickedCount = nearbyClickedCount + 1

                if xtemp != 0 and xtemp != numOfCols-1 and ytemp != 0 and ytemp != numOfRows-1:
                    numOfNearbyTiles = 8
                if xtemp == 0 and ytemp != 0 and ytemp != numOfRows-1:
                    numOfNearbyTiles = 5
                if xtemp == 0 and ytemp == 0:
                    numOfNearbyTiles = 3
                if xtemp == 0 and ytemp == numOfRows-1:
                    numOfNearbyTiles = 3
                if xtemp != 0 and xtemp != numOfCols-1 and ytemp == 0:
                    numOfNearbyTiles = 5
                if xtemp != 0 and xtemp != numOfCols-1 and ytemp == numOfRows-1:
                    numOfNearbyTiles = 5
                if xtemp == numOfCols-1 and ytemp != 0 and ytemp != numOfRows-1:
                    numOfNearbyTiles = 5
                if xtemp == numOfCols-1 and ytemp == 0:
                    numOfNearbyTiles = 3
                if xtemp == numOfCols-1 and ytemp == numOfRows-1:
                    numOfNearbyTiles = 3
                if numOfNearbyTiles == 0:
                    print("Nearby tile count has failed")

                if nearbyClickedCount == numOfNearbyTiles-int(btnBox.cget('text')):

                    # flag all non-clicked cells
                    if xtemp != 0 and isClickedList[indextemp-1] == 0 and isFlaggedList[indextemp-1] == 0:
                        updateCount = updateCount + 1
                        FlagClick(xtemp-1, ytemp, indextemp-1)
                    if xtemp != numOfCols-1 and isClickedList[indextemp+1] == 0 and isFlaggedList[indextemp+1] == 0:
                        updateCount = updateCount + 1
                        FlagClick(xtemp+1, ytemp, indextemp+1)
                    if ytemp != 0 and isClickedList[indextemp-numOfCols] == 0 and isFlaggedList[indextemp-numOfCols] == 0:
                        updateCount = updateCount + 1
                        FlagClick(xtemp, ytemp-1, indextemp-numOfCols)
                    if ytemp != numOfRows-1 and isClickedList[indextemp+numOfCols] == 0 and isFlaggedList[indextemp+numOfCols] == 0:
                        updateCount = updateCount + 1
                        FlagClick(xtemp, ytemp+1, indextemp+numOfCols)
                    if xtemp != 0 and ytemp != 0 and isClickedList[indextemp-1-numOfCols] == 0 and isFlaggedList[indextemp-1-numOfCols] == 0:
                        updateCount = updateCount + 1
                        FlagClick(xtemp-1, ytemp-1, indextemp-1-numOfCols)
                    if xtemp != numOfCols-1 and ytemp != 0 and isClickedList[indextemp+1-numOfCols] == 0 and isFlaggedList[indextemp+1-numOfCols] == 0:
                        updateCount = updateCount + 1
                        FlagClick(xtemp+1, ytemp-1, indextemp+1-numOfCols)
                    if xtemp != 0 and ytemp != numOfRows-1 and isClickedList[indextemp-1+numOfCols] == 0 and isFlaggedList[indextemp-1+numOfCols] == 0:
                        updateCount = updateCount + 1
                        FlagClick(xtemp-1, ytemp+1, indextemp-1+numOfCols)
                    if xtemp != numOfCols-1 and ytemp != numOfRows-1 and isClickedList[indextemp+1+numOfCols] == 0 and isFlaggedList[indextemp+1+numOfCols] == 0:
                        updateCount = updateCount + 1
                        FlagClick(xtemp+1, ytemp+1, indextemp+1+numOfCols)
        # The aim of this algorithm is to generate a spiral pattern that starts from the center tile
        # and goes outward to cover all the other tiles.
        # This is useful in the context of Minesweeper because when the player clicks on a tile,
        # it may reveal nearby tiles that also need to be clicked.
        # By using a spiral pattern to reveal tiles,
        # the game ensures that all nearby tiles are revealed in a logical and efficient order.
        if x == y or (x < 0 and x == -y) or (x > 0 and x == 1-y):
            dx, dy = -dy, dx
        x, y = x+dx, y+dy

    global restartCount
    global waitTime

    if updateCount == 0:
        restartCount = restartCount + 1

    if restartCount < 5:
        root.after(waitTime, spiral, numOfCols, numOfRows)
    else:
        root.after(waitTime, spiralGuess, numOfCols, numOfRows)
        # root.mainloop()


def spiralGuess(X, Y):
    print("guess")

    global restartCount
    global waitTime

    onlyClickOneCount = 0

    x = y = 0
    dx = 0
    dy = -1
    for i in range(max(X, Y)**2):
        if (-X/2 < x <= X/2) and (-Y/2 < y <= Y/2):
            # print (math.ceil(x+X/2),math.ceil(y+Y/2))
            xtemp = math.ceil(x+X/2)-1
            ytemp = math.ceil(y+Y/2)-1
            # plt.scatter(math.ceil(x+X/2),math.ceil(y+Y/2))
            indextemp = ((ytemp)*numOfCols) + xtemp
            btnBox = btn[indextemp]

            if isClickedList[indextemp] == 0 and isFlaggedList[indextemp] == 0 and onlyClickOneCount == 0:
                onlyClickOneCount = 1
                # print("guess",xtemp,ytemp,indextemp)
                myDfsFun(xtemp, ytemp, indextemp)
                if bombCheck(indextemp) == 1:
                    root.after(2*waitTime, showAllBombs)
                else:
                    restartCount = 0
                    root.after(waitTime, spiral, numOfCols, numOfRows)

        if x == y or (x < 0 and x == -y) or (x > 0 and x == 1-y):
            dx, dy = -dy, dx
        x, y = x+dx, y+dy


def showAllBombs():

    global waitTime
    for i in range(len(btn)):
        btnBox = btn[i]
        if bombCheck(i) == 1 and isFlaggedList[i] == 0:
            btnBox.config(text="b")
            btnBox.config(fg="black")

    root.after(waitTime, restartSweep)


def tileClick(x, y, index):

    btnBox = btn[index]
    nearbyFlagCount = 0
    if isClickedList[index] == 1 and btnBox.cget('text') != "b":

        # Check number of nearby flagged cells
        # Check cell to the left
        if x != 0 and isFlaggedList[index-1] == 1:
            nearbyFlagCount = nearbyFlagCount + 1
        # Check cell to the right
        if x != numOfCols-1 and isFlaggedList[index+1] == 1:
            nearbyFlagCount = nearbyFlagCount + 1
        # Check cell above
        if y != 0 and isFlaggedList[index-numOfCols] == 1:
            nearbyFlagCount = nearbyFlagCount + 1
        # Check cell below
        if y != numOfRows-1 and isFlaggedList[index+numOfCols] == 1:
            nearbyFlagCount = nearbyFlagCount + 1
        # Check cell up & left
        if x != 0 and y != 0 and isFlaggedList[index-1-numOfCols] == 1:
            nearbyFlagCount = nearbyFlagCount + 1
        # Check cell up & right
        if x != numOfCols-1 and y != 0 and isFlaggedList[index+1-numOfCols] == 1:
            nearbyFlagCount = nearbyFlagCount + 1
        # Check cell down & left
        if x != 0 and y != numOfRows-1 and isFlaggedList[index-1+numOfCols] == 1:
            nearbyFlagCount = nearbyFlagCount + 1
        # Check cell down & right
        if x != numOfCols-1 and y != numOfRows-1 and isFlaggedList[index+1+numOfCols] == 1:
            nearbyFlagCount = nearbyFlagCount + 1

        # print("Nearby flag count is " + str(nearbyFlagCount) + " and nearby bomb count is " + btnBox.cget('text'))

        # Check if all nearby bombs have been flagged
        if nearbyFlagCount == int(btnBox.cget('text')):
            # print("match")
            # reveal all non-flagged nearby tiles
            # left
            if x != 0 and isFlaggedList[index-1] == 0:
                myDfsFun(x-1, y, index-1)
            # top left
            if x != 0 and y != 0 and isFlaggedList[index-1-numOfCols] == 0:
                myDfsFun(x-1, y-1, index-1-numOfCols)
            # top
            if y != 0 and isFlaggedList[index-numOfCols] == 0:
                myDfsFun(x, y-1, index-numOfCols)
            # top right
            if x != numOfCols-1 and y != 0 and isFlaggedList[index+1-numOfCols] == 0:
                myDfsFun(x+1, y-1, index+1-numOfCols)
            # right
            if x != numOfCols-1 and isFlaggedList[index+1] == 0:
                myDfsFun(x+1, y, index+1)
            # bottom right
            if x != numOfCols-1 and y != numOfRows-1 and isFlaggedList[index+1+numOfCols] == 0:
                myDfsFun(x+1, y+1, index+1+numOfCols)
            # bottom
            if y != numOfRows-1 and isFlaggedList[index+numOfCols] == 0:
                myDfsFun(x, y+1, index+numOfCols)
            # bottom left
            if x != 0 and y != numOfRows-1 and isFlaggedList[index-1+numOfCols] == 0:
                myDfsFun(x-1, y+1, index-1+numOfCols)


def bombCheck(index):
    bombFlag = 0
    exist_count = isBombList.count(index)
    if exist_count > 0:
        bombFlag = 1

    return bombFlag


def restartSweep():

    # Create a list of all the tiles. Take a random sample from that list to assign bombs to
    list_of_numbers = list(range(0, len(btn)))
    # First remove the start tile and it's surrounding tiles
    del list_of_numbers[StartIndex+numOfCols+1]
    del list_of_numbers[StartIndex+numOfCols]
    del list_of_numbers[StartIndex+numOfCols-1]
    del list_of_numbers[StartIndex+1]
    del list_of_numbers[StartIndex]
    del list_of_numbers[StartIndex-1]
    del list_of_numbers[StartIndex-numOfCols+1]
    del list_of_numbers[StartIndex-numOfCols]
    del list_of_numbers[StartIndex-numOfCols-1]

    global isFlaggedList
    global isClickedList
    global recursiveCheckList
    global numOfClickedTiles

    isFlaggedList = [0] * len(btn)
    isClickedList = [0] * len(btn)
    recursiveCheckList = [0] * len(btn)
    numOfClickedTiles = 0

    global isBombList

    isBombList = random.sample(list_of_numbers, numOfBombs)

    # Reset all tile appearances
    for k in range(len(btn)):
        btnBox = btn[k]
        btnBox.config(bg='SystemButtonFace')
        btnBox.config(relief="raised")
        btnBox.config(text="")
        btnBox.config(image="")

    global restartCount

    restartCount = 0

    root.after(10, myDfsFun, StartCol-1, StartRow-1, StartIndex)
    root.after(waitTime+10, spiral, numOfCols, numOfRows)


def myDfsFun(x, y, index):
    # global countIterations
    global waitTime
    btnBox = btn[index]

    nearbyBombCount = 0

    if isClickedList[index] == 0:
        # Check for bombs in surrounding cells
        dx = [-1, 0, 1, 0, -1, -1, 1, 1]
        dy = [0, -1, 0, 1, -1, 1, -1, 1]
        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx >= 0 and nx < numOfCols and ny >= 0 and ny < numOfRows:
                i = nx + ny * numOfCols
                nearbyBombCount += bombCheck(i)

        if nearbyBombCount == 0 and bombCheck(index) != 1 and recursiveCheckList[index] == 0:
            recursiveCheckList[index] = 1

            # DFS recursion for all unclicked neighboring cells
            dx = [-1, 0, 1, 0, -1, -1, 1, 1]
            dy = [0, -1, 0, 1, -1, 1, -1, 1]
            for k in range(8):
                nx = x + dx[k]
                ny = y + dy[k]
                if nx >= 0 and nx < numOfCols and ny >= 0 and ny < numOfRows:
                    i = nx + ny * numOfCols
                    if recursiveCheckList[i] == 0 and isClickedList[i] == 0:
                        myDfsFun(nx, ny, i)

        # Set the font colour based on number of bombs nearby
        if nearbyBombCount == 0:
            btnBox.config(fg="#d9d9d9")
        elif nearbyBombCount == 1:
            btnBox.config(fg="blue")
        elif nearbyBombCount == 2:
            btnBox.config(fg="green")
        elif nearbyBombCount == 3:
            btnBox.config(fg="red")
        elif nearbyBombCount == 4:
            btnBox.config(fg="#9900ff")
        elif nearbyBombCount == 5:
            btnBox.config(fg="#660000")
        elif nearbyBombCount == 6:
            btnBox.config(fg="#4a86e8")
        elif nearbyBombCount == 7:
            btnBox.config(fg="black")
        elif nearbyBombCount == 8:
            btnBox.config(fg="#d9d9d9")
        else:
            pass

        global numOfClickedTiles

        numOfClickedTiles = numOfClickedTiles + 1

        # Update cell number
        # Check for bomb in current cell
        if bombCheck(index) == 1:
            btnBox.config(text="💣")
            btnBox.config(fg="black")
            print("You Lose")
        else:
            btnBox.config(text=str(nearbyBombCount))
            btnBox.config(relief="flat")
            btnBox.config(bg="#e9e9e9")
            # Check to see if you've won
            if numOfClickedTiles == (numOfRows*numOfCols)-numOfBombs:
                print("You Win ")

                root.after(3*waitTime, restartSweep)

        # countIterations=countIterations+1
    isClickedList[index] = 1


# Loop which creates all the tiles
for i in range(numOfRows):
    for j in range(numOfCols):
        btn.append(Button(root, width=2, height=1, font='Terminal'))
        btn[btnNumber].grid(row=i, column=j)
        btnNumber = btnNumber + 1

# Create a list of all the tiles. Take a random sample from that list to assign bombs to
list_of_numbers = list(range(0, len(btn)))
# First remove the start tile and it's surrounding tiles
btn[StartIndex].config(text="S")
# Indices of the surrounding tiles
surrounding_indices = [StartIndex+numOfCols+1, StartIndex+numOfCols,
                       StartIndex+numOfCols-1, StartIndex+1, StartIndex,
                       StartIndex-1, StartIndex-numOfCols+1, StartIndex-numOfCols,
                       StartIndex-numOfCols-1]
for index in surrounding_indices:
    if index in list_of_numbers:
        del list_of_numbers[index]

isBombList = random.sample(list_of_numbers, numOfBombs)


# Create lists to store whether a button has been flagged or clicked
isFlaggedList = [0] * len(btn)
isClickedList = [0] * len(btn)
recursiveCheckList = [0] * len(btn)


root.after(initialPause, myDfsFun, StartCol-1, StartRow-1, StartIndex)
root.after(initialPause+waitTime, spiral, numOfCols, numOfRows)
root.mainloop()
