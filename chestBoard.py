from tkinter import * 

colors = [
   ["#663b27", "#d9b7a7"],
   ["#000000", "#ffffff"],
   ["#2f3834", "#bae3d1"],
   ["#692645", "#e3bacd"]
]

# cells showed in screen
cells = []


root = Tk()
root.title("Chest board")
colorIndex = IntVar(value=0)

def calculateCellColor(r, c, colorIndex):
   cellColor = None
   if(r % 2 == 0):
      cellColor = colors[colorIndex][0] if (c % 2 == 0) else colors[colorIndex][1]
   else:
      cellColor = colors[colorIndex][0] if (c % 2 != 0) else colors[colorIndex][1]

   return cellColor


def initTable():
   for r in range(0, 8):
      for c in range(0, 8):
         index = colorIndex.get()
         cellColor = calculateCellColor(r, c, index)

         colorLabel = Label(root, textvariable=colorIndex, background=cellColor)
         colorLabel.grid(row=12, column=3)

         cell = Label(root, width=10, height=5, background=cellColor, borderwidth=2, relief="groove")
         cell.grid(row=r, column=c)
         cells.append(cell)

def updateTable():
   for r in range(0, 8):
      for c in range(0, 8):
         cellIndex = (r * 8) + c
         cell = cells[cellIndex]
         cell.config(background=calculateCellColor(r, c, colorIndex.get()))

def setPrevColor():
   currentValue = colorIndex.get()
   newValue = (currentValue - 1) % len(colors)
   colorIndex.set(newValue)
   updateTable()

def setNextColor():
   currentValue = colorIndex.get()
   newValue = (currentValue + 1) % len(colors)
   colorIndex.set(newValue)
   updateTable()


prevColorBtn = Button(root, text="<", command=setPrevColor)
prevColorBtn.grid(row=13, column=3)

nextColorBtn = Button(root, text=">", command=setNextColor)
nextColorBtn.grid(row=13, column=4)

initTable()
root.mainloop()



