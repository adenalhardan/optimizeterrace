from Tkinter import *
from random import *

LENGTH = 20;
WIDTH = 20;
CANVAS_SIZE = 20;

window = Tk()
window.title("Optimize Terrace")
window.geometry('520x550')
window.resizable(False, False)

inputFrame = Frame(window)
inputFrame.pack(side = TOP)

mapFrame = Frame(window)
mapFrame.pack(side = TOP)

dataMap = [[randint(0, 167) for x in range(LENGTH)] for y in range(WIDTH)]
blockMap = [[0 for x in range(LENGTH)] for y in range(WIDTH)]

lengthLabel = Label(inputFrame, text = 'Length:')
lengthLabel.pack(side = LEFT)

lengthEntry = Entry(inputFrame, width = 5)
lengthEntry.pack(side = LEFT)

widthLabel = Label(inputFrame, text = 'Width:')
widthLabel.pack(side = LEFT)

widthEntry = Entry(inputFrame, width = 5)
widthEntry.pack(side = LEFT)

def buttonPressed():
    costLabel['text'] = 'Cost: ' + str(buildTerrace(int(lengthEntry.get()), int(widthEntry.get())))
    drawMap()

goButton = Button(inputFrame, text = 'Go!', command = buttonPressed)
goButton.pack(side = LEFT)

costLabel = Label(inputFrame, text = 'Cost: ')
costLabel.pack(side = LEFT)

def main():
    drawMap()
    window.mainloop()

def drawMap():
    for i in range(LENGTH):
        for j in range(WIDTH):
            blockMap[i][j] = Canvas(mapFrame, width = CANVAS_SIZE, height = CANVAS_SIZE)
            blockMap[i][j].create_rectangle(0, 0, CANVAS_SIZE, CANVAS_SIZE, fill = "#%06x" % (dataMap[i][j] * 100000))
            blockMap[i][j].grid(column = i, row = j + 1)

def isValidPlacement(x, y, terraceLength, terraceWidth):
    if (x + terraceLength) < LENGTH and (y + terraceWidth) < WIDTH:
        return True

    return False

def findAverageLevel(x, y, terraceLength, terraceWidth):
    sum = 0

    for i in range(x, x + terraceLength):
        for j in range(y, y + terraceWidth):
            sum += dataMap[i][j]

    return int(sum / (terraceLength * terraceWidth))

def projectCost(x, y, terraceLength, terraceWidth):
    cost = 0
    level = findAverageLevel(x, y, terraceLength, terraceWidth)

    for i in range(x, x + terraceLength):
        for j in range(y, y + terraceWidth):
            cost += abs(dataMap[i][j] - level)

    return cost

def drawTerrace(x, y, terraceLength, terraceWidth):
    level = findAverageLevel(x, y, terraceLength, terraceWidth)

    for i in range(x, x + terraceLength):
        for j in range(y, y + terraceWidth):
            dataMap[i][j] = level

def buildTerrace(terraceLength, terraceWidth):
    minCost = sys.maxint

    minX = 0
    minY = 0

    if terraceLength <= LENGTH and terraceWidth <= WIDTH and terraceLength > 1 and terraceWidth > 1:
        for i in range(LENGTH):
            for j in range(WIDTH):
                if isValidPlacement(i, j, terraceLength, terraceWidth):
                    if projectCost(i, j, terraceLength, terraceWidth) < minCost:
                        minCost = projectCost(i, j, terraceLength, terraceWidth)
                        minX = i
                        minY = j

        drawTerrace(minX, minY, terraceLength, terraceWidth)
    else:
        print("bad input into buildTerrace!")

    return minCost

if __name__ == '__main__':
    main()
