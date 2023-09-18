from cells.setup import setupCells
from vegetobs.setup import setupVegetobs
from parameters import parameters
from phases.growing import growing
import matplotlib.pyplot as plt
from erbasts.setup import setupHerds
from carvizes.setup import setupPrides
from phases.spawning import spawning
from phases.grazing import grazing
from phases.visualizing import visualizing
from phases.movement import movement
from phases.struggle import struggle
from map import setupMap
import time
from interact import *

totalDays = []
totalDensities = []
totalNumberErbasts = []
totalNumberCarvizes = []

#initial setup

def setup():
    totalDays.append(0)
    setupCells()
    totalDensity = setupVegetobs()
    totalDensities.append(totalDensity)
    totalNumberErbast = setupHerds()
    totalNumberErbasts.append(totalNumberErbast)
    totalNumberCarviz = setupPrides()
    totalNumberCarvizes.append(totalNumberCarviz)

#for loop with plotting of the simulation and at the end of the plots

isRunning = True
pause = 0.04

def main():
    fig, dx = plt.subplots(figsize=(6,6))
    fig.suptitle("Map")
    for day in range(1, parameters.getNumdays() + 1):
        while not isRunning:
            root1.update()
            time.sleep(0.5)  
        totalDays.append(day)
        growing()
        movement()
        grazing()
        struggle()
        spawning()
        totalDensity, totalNumberErbast, totalNumberCarviz = visualizing()
        totalDensities.append(totalDensity)
        totalNumberErbasts.append(totalNumberErbast)
        totalNumberCarvizes.append(totalNumberCarviz)
        setupMap(dx,day)
        root1.update()
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

#buttons which actively influence the progress of the simulation 

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
    else:
        speedupButton['state'] = "disabled"

def slowdownSimulation():
    global pause 
    pause = pause*2
    speedupButton['state'] = "active"

startButton['command'] = startSimulation
pauseButton['command'] = pauseSimulation
resumeButton['command'] = resumeSimulation
speedupButton['command'] = speedupSimulation
slowdownButton['command'] = slowdownSimulation

root1.mainloop()
