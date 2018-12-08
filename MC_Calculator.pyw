from tkinter import *
from tkinter import ttk

from GUIImages import *

import sys, os 
def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

VillagerGif = VillagerImageString
DoorGif = DoorImageString
TitleGif = TitleImageString


def submitFunc():
    
    golemCalc()
    villagerCalc()
    
    
def golemCalc():
# the following code calculates for iron golems. 
    inCensus = census.get()
    doorCount = doors.get()
    
    
    def golemReqCensus():
        '''
        Calculates how many villgers you need to get one more IRON GOLEM
        '''
        
        Gcensus = census.get()
        censusstring = (str(Gcensus)[-1])
        censuslast = int(censusstring) #these last two lines of code are involved in truncating the number to whole digits.
        golemreqcensus = 10 - censuslast
        return golemreqcensus

        
    if doorCount >= 21 and inCensus >= 10: # Your village must be over 21 doors big. 1 golem can then spawn per 10 villagers.
        
        golemcount = int(inCensus / 10)
        golemreqcount = golemReqCensus()
        golemText.set('''
                        
        \nYour village should be able to spawn an IRON GOLEM\       
        \nThere are enough villagers to spawn %d IRON GOLEM(S).
        \nYou need %d villagers to spawn one more GOLEM.
        
        ''' % (golemcount, golemreqcount))
        
    else:
        golemreqcount = golemReqCensus()
        golemText.set('''
                        
               \nYou need at least 10 villagers and 21 doors to spawn 1 IRON GOLEM\n
               
                       ''')
        
        
        
def villagerCalc():
    
    inCensus = census.get()
    doorCount = doors.get()
    
    villagerpotential = int(round(doorCount * 0.35)) #The magic no. for villagers is you can have a number of villagers equal to 35% the number of doors. Weird!
    

    
    nextvillagerdoors = (inCensus + 1) / 0.35
    nextvillagerdoors = int(round(nextvillagerdoors, 2))
     #This is based on the current census, which due to natural spawning census, might mean you need lots more doors.
    if (nextvillagerdoors - doorCount) < 0:
        
        villagerText.set('''
        \nYou have enough doors to have %d villager(s) in your village.                
        \nYour village should be spawning new villagers soon.
        \nVillager breeding is also affected by how much food is available so be sure to provide farms.
        
        ''' % villagerpotential)
 
    elif inCensus >= villagerpotential:
        moreDoors = nextvillagerdoors - doorCount
        villagerText.set('''
          \nYour data indicates you have more villagers than your village would typically support:              
          \nYou have enough doors to have %d villager(s) in your village.           
          \nYou will need to build at least %d more doors in order to get one more villager.          
       ''' % (villagerpotential, moreDoors))
    
    else:
       moreDoors = nextvillagerdoors - doorCount
       villagerText.set('''
          \nYou have enough doors to have %d villager(s) in your village.           
          \nYou will need to have at least %d more doors in order to get one more villager.\n
          \nVillager breeding is also affected by how much food is available so be sure to provide farms.
       ''' % (villagerpotential, moreDoors))


# --- GUI SECTION

base = Tk()
base.resizable(0,0)
base.title('Minecraft Village Calculator')


mainframe = ttk.Frame(base).grid()


# - Inputs and output text
census = IntVar()
doors = IntVar()
golemText = StringVar()
villagerText = StringVar()

leftImage = PhotoImage(data=VillagerGif)
rightImage = PhotoImage(data=DoorGif)
titleImage = PhotoImage(data=TitleGif)


# --- Initialise Widgets

titleBar = ttk.Label(mainframe, image=titleImage)

golemTitle = Label(mainframe)
golemMessage = Label(mainframe)

villagerTitle = Label(mainframe)
villagerMessage = Label(mainframe)

leftImageLabel = ttk.Label(mainframe, image=leftImage)
rightImageLabel = ttk.Label(mainframe, image=rightImage)


censusEntryLabel = ttk.Label(mainframe)
censusInputBox = ttk.Entry(mainframe)


doorEntryLabel = ttk.Label(mainframe)
doorInputBox = ttk.Entry(mainframe)

submitButton = ttk.Button(mainframe)



# --- Widget Configuration Section --------------------

# --- Display Box Configuration

golemTitle.configure(text='IRON GOLEM results:')
golemMessage.configure(textvariable=golemText, background='white', relief='sunken', borderwidth='2', height='7', width='80', justify = LEFT, wraplength = '550')
villagerTitle.configure(text='Villager results:')
villagerMessage.configure(textvariable=villagerText, background='white', relief='sunken', borderwidth='2', height='7', width='80', justify = LEFT, wraplength = '550')

villagerText.set('''
    \nTo use this calculator:
    \nCount the villagers and doors in your village.
    \nEnter only digits into the census and door boxes.            
''')

golemText.set('''
    \nUse this calculator to work out how many IRON GOLEMs you should be able to have in your village.
    \nIt also estimates how many villagers your village can support based on the number of doors.
    \nFinally, it will advise you how many doors you need to build to spawn more villagers and GOLEMs.            
''')
    
    
# --- Census Side Configuration


censusEntryLabel.configure(text='Enter Villager Census')
censusInputBox.configure(textvariable=census)


# --- Golem Side Configuration


doorEntryLabel.configure(text='Enter Door Count')
doorInputBox.configure(textvariable=doors)

# --- Button Configuration
submitButton.configure(text='Calculate', command=submitFunc)

# --- Grid Arrangement Section ---------------------

# --- Title Grid Arrangement

titleBar.grid(column ='0', row='0', columnspan='6', pady='5')


# --- Image Grid Arrangement

leftImageLabel.grid(column='0', row='2', rowspan='4', padx='8', pady='3')
rightImageLabel.grid(column='5', row='2', rowspan='4', padx='8', pady='25')

golemTitle.grid(column='1', row='1', pady='5', sticky=W+S, ipadx='10')
golemMessage.grid(column='1', row='2', columnspan='4', sticky=W+E+S, padx='3', pady='5')

villagerTitle.grid(column='1', row='3', sticky=W, ipadx='10')
villagerMessage.grid(column='1', row='4', columnspan='4', sticky=W+E+S, padx='3', pady='5')



# --- Census Side Grid Arrangement
censusEntryLabel.grid(column='1', row='5', sticky=S)
censusInputBox.grid(column='1', row='6', sticky=S, pady='10')


# --- Button Grid Arrangement
submitButton.grid(column='2', row='6', columnspan='2', sticky=W+E+S, pady='10')


#---Door Side Grid Arrangement
doorEntryLabel.grid(column='4', row='5', sticky=S)
doorInputBox.grid(column='4', row='6', sticky=S, pady='10')



base.mainloop()

