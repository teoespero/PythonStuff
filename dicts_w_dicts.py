#########################################################################
# Teo Espero
# BS Cloud and Systems Admin (WGU)
# CEA GIS Technology II (Foothill)
# 10-20-2020
# This program is mainly created to mimic/simulate a DBMS system. Giving
# the user basic functionalities for adding/removing/displaying records


#########################################################################
# addData allows the user to add data to the DB
from time import sleep


def addData():
    print()
    print('ADD DATA')
    print()
    recName = 'rec' + str(len(data) + 1)
    newName = input('Name: ')

    data[recName] = dict(name=newName)

    newDegree = 'D'
    degreeList = []

    # note that degrees are always treated as list
    # if you leave it blank it will exit this function
    while newDegree != '':
        newDegree = input('Degree: ')
        if len(newDegree) > 1:
            degreeList.append(newDegree)
            data[recName]['degree'] = degreeList
        else:
            break
    print()
    print('Record {} has been added.'.format(recName).title())
#########################################################################


#########################################################################
# printData creates a sequential display of the data that we have in
# the "DB"
def printData():
    print()
    print('PRINT DATA')
    print()

    # note that this function will only print if there
    # is data to print
    if len(data) > 0:
        for key, value in data.items():
            print('Record ID: {}'.format(str(key)).title())
            for rec in value:
                if rec == 'name':
                    print(str(rec).title() + ':', str(value[rec]).title())
                else:
                    print(str(rec).title() + ':', value[rec])
            print()
    else:
        print('No data to display.')
#########################################################################


#########################################################################
# delData allows the user to remove a specific record in the "DB"
def delData():
    print()
    print('REMOVE DATA')
    printData()
    print()
    whichOne = input('Which one do I delete? ')
    try:
        del data[whichOne.lower()]
        print()
        print('{} has been deleted.'.format(whichOne))
        printData()
    except:
        print('Key does not exist.')
#########################################################################


#########################################################################
# locate the record base on whats part of the name field
def findData():
    print()
    print('LOCATE DATA')
    print()
    found = False
    foundCtr = 0
    whichOne = input('Find who? ')
    for key, value in data.items():
        for rec in value:
            if rec == 'name':
                if whichOne in str(value[rec].lower()):
                    foundCtr += 1
                    print()
                    print(str(rec).title() + ':', str(value[rec]).title())
                    print('degree: '.title(), value['degree'])
                    found = True
                    break
            if found:
                break
    print()
    print('{} record(s) were found'.format(foundCtr))
#########################################################################


#########################################################################
# pretty much self explanatory
def menu():
    print()
    print('MENU CHOICES')
    print('\t1-Add new record')
    print('\t2-Delete record')
    print('\t3-Search record')
    print('\t4-Print record(s)')
    print('\t5-Purge')
    print('\t6-Exit')
    print()
    myChoice = input('Selection: ')
    return myChoice
#########################################################################


#########################################################################
# defineAction is the task master, passing the action to the
# correct function
def defineAction(myChoice):
    if myChoice == 1:
        addData()
    if myChoice == 2:
        delData()
    if myChoice == 3:
        findData()
    if myChoice == 4:
        printData()
    if myChoice == 5:
        print()
        print('PURGING DATA')
        sleep(1)
        print()
        data.clear()
        print('All data have been removed.')


#########################################################################
# main

# base data
data = {
    'rec1':
        {
            'name': 'teo espero',
            'degree': ['BS Cloud/Sys Adm', 'CEA GIST']
        },
    'rec2':
        {
            'name': 'Josie Espero',
            'degree': ['AA Psychology']
        }
}

menuChoice = 0
while str(menuChoice) not in '123456':
    menuChoice = menu()
    if menuChoice not in '123456':
        print('Not valid.')
    else:
        menuChoice = int(menuChoice)
        if menuChoice == 6:
            break
        else:
            menuChoice = int(menuChoice)
            defineAction(menuChoice)
            menuChoice = 0

print('Goodbye.')
#########################################################################