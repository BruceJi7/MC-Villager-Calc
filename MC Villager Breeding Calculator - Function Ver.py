# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 22:38:01 2018

@author: User
"""



def GetDoorcount():
    try:
        userin = int(input('How many doors are in the village?\n'))
        return userin
    except ValueError:
        print('Please enter a number in digits')

def GetCensus():
    try:
        userin = int(input('How many villagers are in the village?\n'))
        return userin
    except ValueError:
        print('Please enter a number in digits')
            

def golemCalc(doorcount, census):
# the following code calculates for iron golems. 
    
    def golemReqCensus(census):
        '''
        Calculates how many villgers you need to get one more IRON GOLEM
        '''
        censusstring = (str(census)[-1])
        censuslast = int(censusstring) #these last two lines of code are involved in truncating the number to whole digits.
        golemreqcensus = 10 - censuslast
        return ('You need to get at least ' + str(golemreqcensus) + ' more villagers to spawn an additional IRON GOLEM.')
        
        
    if doorcount >= 21 and census >= 10: # Your village must be over 21 doors big. 1 golem can then spawn per 10 villagers.
        print('---------------------------------------------------')
        print('Your village should be able to spawn an IRON GOLEM.')
        golemcount = int(census / 10)
        print('There are enough villagers to spawn ' + str(golemcount) + ' IRON GOLEM(S).')
        print(golemReqCensus(census))
        print('----------------------------------------------------')
    else:
        print('----------------------------------------------------')
        print('You need at least 10 villagers to spawn 1 IRON GOLEM')
        print(golemReqCensus(census))
        print('----------------------------------------------------')

def villagerCalc(doorcount, census):
    villagerpotential = int(round(doorcount * 0.35)) #The magic no. for villagers is you can have a number of villagers equal to 35% the number of doors. Weird!
    
    print('You have enough doors to have ' + str(villagerpotential) + ' villager(s) in your village.')
    
    nextvillagerdoors = (census + 1) / 0.35
    nextvillagerdoors = int(round(nextvillagerdoors, 2))
     #This is based on the current census, which due to natural spawning census, might mean you need lots more doors.
    if (nextvillagerdoors - doorcount) < 0:
        print('You have way more doors than villagers, and can expect more villagers soon.')
        
    else:
        print('You will need to have at least ' + str(nextvillagerdoors - doorcount) + ' more doors to get one more villager.')
        print('Do remember that villager breeding is also affected by the fullness of the villager.')
    print('----------------------------------------------------')

doorcount = GetDoorcount()
census = GetCensus()

golemCalc(doorcount, census)
villagerCalc(doorcount, census)

