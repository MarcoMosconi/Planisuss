import tkinter as tk
from parameters import parameters
from tkinter import simpledialog
from tkhtmlview import HTMLLabel

#buttons to interactively change the parameters

root1 = tk.Tk()
root1.geometry("700x600")
root1.title('Menu')

def settingsChange():
    info.forget()
    root1.geometry("200x450")
    startButton.forget()
    settingButton.forget()
    root1.title('Parameters')
    listBox.pack()
    submitButton.pack(side='left')
    closeButton.pack(side='right')

def submit():
    parameter = listBox.get(listBox.curselection())
    value = getattr(parameters, parameter)
    if type(value) == int:
        newvalue = simpledialog.askinteger("Parameters", f"Enter new {parameter}",initialvalue=value)
    else:
        newvalue = simpledialog.askfloat("Parameters", f"Enter new {parameter}",initialvalue=value)
    if newvalue is not None:
        setattr(parameters,parameter,newvalue)

def close():
    root1.geometry("700x600")
    root1.title('Menu')
    closeButton.forget()
    listBox.forget()
    submitButton.forget()
    info.set_html(information())
    info.pack(fill="both", expand=True, pady=5, padx=5)
    startButton.pack(side='left', padx=100, pady=5)
    settingButton.pack(side='right', padx=100, pady=5)

def information():
    html = f"""
        <div style="background-color: #cdcdcd;">
            <h1>Welcome to Planisuss</h1>
            <h2>Parameters</h2>
            <div>The following simulation parameters currently have these values which can be changed:</div>
            <ul>
                <li> Aging: {parameters.getAging()} </li>
                <li> Carviz Probability: {parameters.getCarvizProb()}</li>
                <li> Cell Probability: {parameters.getCellProb()}</li>
                <li> Erbast Probability: {parameters.getErbastProb()}</li>
                <li> Growing: {parameters.getGrowing()}</li>
                <li> Max Density: {parameters.getMaxDensity()}</li>
                <li> Max Energy: {parameters.getMaxEnergy()}</li>
                <li> Max Herd: {parameters.getMaxHerd()}</li>
                <li> Max Life: {parameters.getMaxLife()}</li>
                <li> Max Pride: {parameters.getMaxPride()}</li>
                <li> Minimum Social Attitude: {parameters.getMinSocAtt()}</li>
                <li> Move Probability: {parameters.getMoveProb()}</li>
                <li> Neighborhood: {parameters.getNeighborhood()}</li>
                <li> Numcells: {parameters.getNumcells()}</li>
                <li> Numdays: {parameters.getNumdays()}</li>
            </ul>
            <h2>Controls</h2>
            <div> During the simulation you have the possibility to pause, resume, increase or decrease speed</div>
            <h2>Plots</h2>
            <div>During the simulation Planisuss map is constantly updated</div>
            <div> At the end three plots are shown:</div>
            <ul>
                <li> Vegetob Density over time</li>
                <li> Erbast population over time</li>
                <li> Carviz population over time</li>
            </ul>
        </div>
        """
    return html
   
startButton = tk.Button(root1, text="Start", font=('comic sans', 16), border="5px")
settingButton = tk.Button(root1,text="Change Settings", command=settingsChange, font=('comic sans', 16), border="5px")
pauseButton = tk.Button(root1,text="⏯️", font=('comic sans', 30), border="3px")
resumeButton = tk.Button(root1,text="⏯", font=('comic sans', 30), border="3px")
speedupButton = tk.Button(root1, text="⏩", font=('comic sans', 30), border="3px")
slowdownButton = tk.Button(root1, text="⏪", font=('comic sans', 30), border="3px")
submitButton = tk.Button(root1, text="Submit",command=submit, font=('comic sans', 16), border="3px") 
closeButton = tk.Button(root1, text="Close",command=close, font=('comic sans', 16), border="3px") 
info = HTMLLabel(root1, html=information())

listBox = tk.Listbox(root1, bg="#cdcdcd", font=('comic sans', 16), width=20)
listBox.insert(1,"Aging")
listBox.insert(2,"Carviz_Probability")
listBox.insert(3,"Cell_Probability")
listBox.insert(4,"Erbast_Probability")
listBox.insert(5,"Growing")
listBox.insert(6,"Max_Density")
listBox.insert(7,"Max_Energy")
listBox.insert(8,"Max_Herd")
listBox.insert(9,"Max_Life")
listBox.insert(10,"Max_Pride")
listBox.insert(11,"Min_Social_Attitude")
listBox.insert(12,"Move_Probability")
listBox.insert(13,"Neighborhood")
listBox.insert(14,"Numcells")
listBox.insert(15,"Numdays")
listBox.config(height=listBox.size())

info.pack(fill="both", expand=True, pady=5, padx=5)
startButton.pack(side="left", padx=100, pady=5)
settingButton.pack(side="right", padx=100, pady=5)

