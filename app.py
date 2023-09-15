from cells.setup import setupCells
from vegetobs.setup import setupVegetobs
from constants import parameters
from phases.growing import growing
import matplotlib.pyplot as plt
import numpy as np
from erbasts.setup import setupHerds
from carvizes.setup import setupPrides
from phases.spawning import spawning
from phases.grazing import grazing
from phases.visualizing import visualizing
from phases.movement import movement
from phases.struggle import struggle
from map import setupMap
from random import seed
import tkinter as tk
from tkinter import simpledialog
import time
import sys

root1 = tk.Tk()
root1.title('Menu')

seed(1)

totalDays = []
totalDensities = []
totalNumberErbasts = []
totalNumberCarvizes = []

def setup():
    totalDays.append(0)
    setupCells()
    totalDensity = setupVegetobs()
    totalDensities.append(totalDensity)
    totalNumberErbast = setupHerds()
    totalNumberErbasts.append(totalNumberErbast)
    totalNumberCarviz = setupPrides()
    totalNumberCarvizes.append(totalNumberCarviz)
    
    # A = np.asarray(setupMap())
    # colors = ['dodgerblue', 'saddlebrown']
    # cmap = ListedColormap(colors)
    # plt.imshow(A, cmap=cmap)

isRunning = True
pause = 0.01

def main():
    # fig, ((ax, bx),(cx,dx)) = plt.subplots(2,2)
    fig, dx = plt.subplots()
    # ax.set_title("Total Daily Vegetob Density")
    # bx.set_title("Total Daily Erbast Number")
    # cx.set_title("Total Daily Carviz Number")
    # dx.set_aspect('equal')
    for day in range(1, parameters.getNumdays() + 1):
        while not isRunning:
            root1.update()
            time.sleep(0.5)  
        print('--------------DAY', day)
        totalDays.append(day)
        growing()
        movement()
        # print('---------------')
        grazing()
        struggle()
        spawning()
        totalDensity, totalNumberErbast, totalNumberCarviz = visualizing()
        totalDensities.append(totalDensity)
        totalNumberErbasts.append(totalNumberErbast)
        totalNumberCarvizes.append(totalNumberCarviz)
        # ax.plot(totalDays, totalDensities, 'tab:green')
        # bx.plot(totalDays, totalNumberErbasts, 'tab:orange')
        # cx.plot(totalDays, totalNumberCarvizes, 'tab:red')
        setupMap(dx,day)
        root1.update()
        # figManager = plt.get_current_fig_manager()
        # figManager.full_screen_toggle()
        print(pause)
        plt.pause(pause)
    plt.show()
    root1.destroy()

    fig, (ax,bx,cx) = plt.subplots(3,1)
    ax.set_title("Total Daily Vegetob Density")
    bx.set_title("Total Daily Erbast Number")
    cx.set_title("Total Daily Carviz Number")
    ax.plot(totalDays, totalDensities, 'tab:green')
    bx.plot(totalDays, totalNumberErbasts, 'tab:orange')
    cx.plot(totalDays, totalNumberCarvizes, 'tab:red')
    fig.tight_layout()
    plt.show()

def run():
    setup()
    main()

def startSimulation():
    startButton.forget()
    settingButton.forget()
    root1.title('Options')
    speedupButton.pack(side='right')
    slowdownButton.pack(side='left')
    pauseButton.pack()
    root1.bind("<Left>",slowdownSimulation)
    root1.bind("<Right>",speedupSimulation)
    root1.bind("<space>",pauseSimulation)
    run()

def settingsChange():
    startButton.forget()
    settingButton.forget()
    root1.title('Parameters')
    listBox.pack()
    submitButton.pack(side='left')
    closeButton.pack(side='right')
    root1.bind("<Return>",submit)
    root1.bind("<Escape>",close)
    # newNumcells = simpledialog.askinteger("Contants", "Enter new numcells", initialvalue=parameters.parameters.getNumcells())
    # newCellProb = simpledialog.askfloat("Constants", "Enter new cell propability", initialvalue=parameters.parameters.getCellProb())

def submit(event):
    parameter = listBox.get(listBox.curselection())
    value = getattr(parameters, parameter)
    if type(value) == int:
        newvalue = simpledialog.askinteger("Parameters", f"Enter new {parameter}",initialvalue=value)
    else:
        newvalue = simpledialog.askfloat("Parameters", f"Enter new {parameter}",initialvalue=value)
    if newvalue is not None:
        setattr(parameters,parameter,newvalue)
    

def close(event):
    closeButton.forget()
    listBox.forget()
    submitButton.forget()
    startButton.pack(side='left')
    settingButton.pack(side='right')


def pauseSimulation(event):
    pauseButton.forget()
    resumeButton.pack()
    global isRunning
    isRunning = False
    root1.bind("<space>",resumeSimulation)

def resumeSimulation(event):
    resumeButton.forget()
    pauseButton.pack()
    global isRunning
    isRunning = True
    root1.bind("<space>",pauseSimulation)
    
def speedupSimulation(event):
    global pause
    if pause > 0.01:
        pause = pause/2

def slowdownSimulation(event):
    global pause 
    pause = pause*2

startButton = tk.Button(root1, text="Start", command=startSimulation, font=('comic sans', 30))
settingButton = tk.Button(root1,text="Change Settings", command=settingsChange, font=('comic sans', 30))
pauseButton = tk.Button(root1,text="⏯️", command=pauseSimulation, font=('comic sans', 30))
resumeButton = tk.Button(root1,text="⏯", command=resumeSimulation, font=('comic sans', 30))
speedupButton = tk.Button(root1, text="⏩", command=speedupSimulation, font=('comic sans', 30))
slowdownButton = tk.Button(root1, text="⏪", command=slowdownSimulation, font=('comic sans', 30))
submitButton = tk.Button(root1, text="Submit",command=submit) 
closeButton = tk.Button(root1, text="Close",command=close) 

listBox = tk.Listbox(root1, font=('comic sans', 20), width=22)
listBox.insert(1,"Numcells")
listBox.insert(2,"Cell_Probability")
listBox.insert(3,"Growing")
listBox.insert(4,"Numdays")
listBox.insert(5,"Max_Density")
listBox.insert(6,"Max_Energy")
listBox.insert(7,"Max_Life")
listBox.insert(8,"Max_Herd")
listBox.insert(9,"Max_Pride")
listBox.insert(10,"Erbast_Probability")
listBox.insert(11,"Carviz_Probability")
listBox.insert(12,"Aging")
listBox.insert(13,"Neighborhood")
listBox.insert(14,"Min_Social_Attitude")
listBox.insert(15,"Move_Probability")

listBox.config(height=listBox.size())

startButton.pack(side="left")
settingButton.pack(side="right")

root1.mainloop()

# with open('C:\\Users\\marco\\OneDrive\\Desktop\\Planisuss\\ex.txt', 'w') as file:
#     original_stdout = sys.stdout
#     sys.stdout = file
#     run()
#     sys.stdout = original_stdout

# run()
