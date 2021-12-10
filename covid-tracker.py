import time
import re
from tkinter import *
from tkinter.ttk import Combobox

# RFS - Rebecca, Farzan, Sara

# Class for storying each country's data
class Region():
    def __init__(self, country):
        self.name = country
        self.totalcases = "NaN"
        self.newcases = "NaN"
        self.deaths = "NaN"
        self.recovered = "NaN"
        self.activecases = "NaN"
        self.mortalityrate = "NaN"
        if (country=="World"):
            self.totalcases = 0
            self.newcases = 0
            self.deaths = 0
            self.recovered = 0
            self.activecases = 0
    
    def calcmortality(self):
        self.mortalityrate = str(round(self.deaths / self.totalcases * 100, 2)) + "%"

# Changing the input string to a list
# Attach data to corresponding country
# Calculate mortality and recovery rates
def analyse(line):
    alldata = re.findall(r"\[(.*?)\]", line)
    alldata[0] = alldata[0].strip('\"')
    alldata[0] = alldata[0].replace(" ", "")
    for i in range(1,len(alldata)):
        if (alldata[i]):
            alldata[i] = alldata[i].replace(",", "")
            alldata[i] = int(alldata[i])
        else:
            alldata[i] = "NaN"
    attach(alldata)
    globals()[alldata[0]].calcmortality()

# Attach data to corresponding country
def attach(alldata): 
    if (alldata[1] != 'NaN'):
        globals()[alldata[0]].totalcases = alldata[1]
        World.totalcases += alldata[1]
    if (alldata[2] != 'NaN'):
        globals()[alldata[0]].newcases = alldata[2]
        World.newcases += alldata[2]
    if (alldata[3] != 'NaN'):
        globals()[alldata[0]].deaths = alldata[3]
        World.deaths += alldata[3]
    if (alldata[4] != 'NaN'):
        globals()[alldata[0]].recovered = alldata[4]
        World.recovered += alldata[4]
    if (alldata[5] != 'NaN'):
        globals()[alldata[0]].activecases = alldata[5]
        World.activecases += alldata[5]

# Itterating over already stored data in the file
def readstored():
    with open("data.txt", "r") as datafile:
        datalines = datafile.readlines()
        for line in datalines:
            analyse(line)

# Used to initiate all country objects
def createcountryobjects():
    with open('countries.txt') as fp:
        for line in fp:
            globals()[line.strip()] = Region(line.strip("\n"))
            
createcountryobjects()
World = Region("World")
readstored()
World.calcmortality()

# GUI -----------------
window=Tk()
window.title('Covid 19 - Region Data')
window.geometry("595x650")
window.resizable(width=False, height=False)
window.configure(bg="#565656")
var = StringVar()
var.set("one")
countries = ("World","Algeria","Argentina","Austria","Australia","Bangladesh","Belgium","Brazil","Canada","Chad","Chile","China","Colombia","CostaRica","Egypt","France","Georgia","Germany","Greece","Hungary","India","Indonesia",'Iran','Iraq','Ireland','Israel','Italy','Japan','Kenya','Mexico','Morocco','Nepal','Netherlands','NewZealand','Pakistan','Peru','Philippines','Poland','Portugal','Romania','Russia','SaudiArabia','Singapore','SouthAfrica','SouthKorea','Spain','Sweden','Switzerland','Taiwan','Thailand','Turkey','UK','USA','Ukraine')
countryselect = Combobox(window, values=countries, width=30, height=20)
countryselect.config(font=("Serif", 15))
countryselect.set("Select Region")
countryselect.place(x=0, y=0)

worldobject = globals()["World"]
worldlabel = Label(window, text="%s\n\nTotal Cases: %s\n\nNew Cases: %s\n\nTotal Deaths: %s\n\nTotal Recovered: %s\n\nActive Cases: %s\n\nMortality Rate: %s" % ("World", worldobject.totalcases, worldobject.newcases, worldobject.deaths, worldobject.recovered, worldobject.activecases, worldobject.mortalityrate), justify=LEFT)
worldlabel.config(font=("Serif", 20))
worldlabel.place(x=25, y=100)

label = Label(window, text="")
countrylabel = Label(window, text="")
warninglabel = Label(window, text="")
i = 0

def CallBack():
    global label, worldlabel, i, countrylabel, warninglabel
    if(i==0):
        worldlabel.destroy()
        i=1
    label.destroy()
    countrylabel.destroy()
    warninglabel.destroy()
    
    if (type(globals()[countryselect.get()].activecases) == int):
        if ( globals()[countryselect.get()].activecases >= globals()["World"].activecases/53):
            if (countryselect.get() != "World"):
                print("Average Active Cases: " + str(globals()["World"].activecases/53))
                warninglabel = Label(window, text="HIGH NUMBER OF ACTIVE CASES - TAKE EXTRA PRECAUTIONS")
                warninglabel.place(x=25, y=62)
                warninglabel.config(font=("Serif", 10, "bold"), bg="red", fg="yellow")


    countryobject = globals()[countryselect.get()]
    countrylabel = Label(window, text=countryselect.get())
    countrylabel.config(font=("Serif", 25, UNDERLINE, "bold"), bg="#565656", fg="white")
    countrylabel.place(x=25, y=110)

    label = Label(window, text="Total Cases: %s\n\nNew Cases: %s\n\nTotal Deaths: %s\n\nTotal Recovered: %s\n\nActive Cases: %s\n\nMortality Rate: %s" % (countryobject.totalcases, countryobject.newcases, countryobject.deaths, countryobject.recovered, countryobject.activecases, countryobject.mortalityrate), justify=LEFT)
    label.config(font=("Serif", 20, "bold"), bg="#565656", fg="white")
    label.place(x=25, y=190)


B = Button(window, text ="Search", command = CallBack, bg="white", width=15)
B.config(font=("Serif", 11))
B.place(x=450, y=0)

window.mainloop()
# GUI -----------------

