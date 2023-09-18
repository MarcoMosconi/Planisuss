from cells.setup import setupCells
from vegetobs.setup import setupVegetobs
from parameters import parameters
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
import time
from interact import *
import sys

# seed(1)

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
pause = 0.04

def main():
    # fig, ((ax, bx),(cx,dx)) = plt.subplots(2,2)
    fig, dx = plt.subplots(figsize=(6,6))
    fig.suptitle("Map")
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
        # print(pause)
        plt.pause(pause)
    plt.show()
    root1.destroy()

    fig, (ax,bx,cx) = plt.subplots(3,1, figsize=(8,6))
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
    info.forget()
    startButton.forget()
    settingButton.forget()
    root1.title('Options')
    root1.geometry("270x80")
    speedupButton.pack(side='right')
    slowdownButton.pack(side='left')
    pauseButton.pack()
    run()

def pauseSimulation():
    pauseButton.forget()
    resumeButton.pack()
    global isRunning
    isRunning = False

def resumeSimulation():
    resumeButton.forget()
    pauseButton.pack()
    global isRunning
    isRunning = True
    
def speedupSimulation():
    global pause
    if pause > 0.01:
        pause = pause/2

def slowdownSimulation():
    global pause 
    pause = pause*2

startButton['command'] = startSimulation
pauseButton['command'] = pauseSimulation
resumeButton['command'] = resumeSimulation
speedupButton['command'] = speedupSimulation
slowdownButton['command'] = slowdownSimulation


root1.mainloop()

# with open('C:\\Users\\marco\\OneDrive\\Desktop\\Planisuss\\ex.txt', 'w') as file:
#     original_stdout = sys.stdout
#     sys.stdout = file
#     run()
#     sys.stdout = original_stdout

# run()
