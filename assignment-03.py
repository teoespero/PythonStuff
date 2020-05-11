# name: assignment-03.py
# description:
# This Python program was created to fulfill the following goals;
#       - Use a Python Dictionary
#       - Write a simple algorithm that solves a difficult problem
#       - Test your program thoroughly
#       - Paste the console output to the bottom of your source code file to submit in Canvas
# date written: 20200510
# author: Teo Espero


# BOF


####################################################
# define our dictionaries

# below are our original dictionaries

# original dictionaries
roommate1Shopping = {'fruit': 'apples', 'meat': 'chicken', 'vegetables': 'potatoes', 'drinks': ['beer','wine'], 'dessert': 'ice cream'}
roommate3Shopping = {'fruit': 'lemons', 'meat': 'hamburger', 'drinks': ['apple juice', 'orange juice', 'vodka']}
roommate2Shopping = {'fruit': ['oranges', 'bananas'], 'vegetables': ['lettuce', 'carrots'],'drinks': 'milk'}

# step 1
# initialize our merged dictionary

resultingMergedDictionary = roommate1Shopping.copy()

# step # 2
for key in roommate2Shopping:
    if key in resultingMergedDictionary:
        if isinstance(resultingMergedDictionary[key], list):
            if isinstance(roommate2Shopping[key], list):
                resultingMergedDictionary[key] = resultingMergedDictionary[key] + roommate2Shopping[key]
            else:
                myList = []
                myList.append(roommate2Shopping[key])
                resultingMergedDictionary[key] = resultingMergedDictionary[key] + myList
        else:
            if isinstance(roommate2Shopping[key], list):
                tempList = []
                tempList.append(resultingMergedDictionary[key])
                roommate2Shopping[key] = roommate2Shopping[key] + tempList
                resultingMergedDictionary[key] = roommate2Shopping[key]
            else:
                # print(roommate2Shopping[key])
                # print(resultingMergedDictionary[key])
                tempList2 = [roommate2Shopping[key], resultingMergedDictionary[key]]
                resultingMergedDictionary[key] = tempList2


# step # 3
for key in roommate3Shopping:
    if key in resultingMergedDictionary:
        if isinstance(resultingMergedDictionary[key], list):
            if isinstance(roommate3Shopping[key], list):
                resultingMergedDictionary[key] = resultingMergedDictionary[key] + roommate3Shopping[key]
            else:
                myList = []
                myList.append(roommate3Shopping[key])
                resultingMergedDictionary[key] = resultingMergedDictionary[key] + myList
        else:
            if isinstance(roommate3Shopping[key], list):
                tempList = []
                tempList.append(resultingMergedDictionary[key])
                roommate3Shopping[key] = roommate3Shopping[key] + tempList
                resultingMergedDictionary[key] = roommate3Shopping[key]
            else:
                # print(roommate3Shopping[key])
                # print(resultingMergedDictionary[key])

                tempList3 = [roommate3Shopping[key], resultingMergedDictionary[key]]
                resultingMergedDictionary[key] = tempList3


# step 4
print(resultingMergedDictionary)

## OUTPUT
'''
{'fruit': ['oranges', 'bananas', 'apples', 'lemons'], 'meat': ['hamburger', 'chicken'], 'vegetables': ['lettuce', 'carrots', 'potatoes'], 'drinks': ['beer', 'wine', 'milk', 'apple juice', 'orange juice', 'vodka'], 'dessert': 'ice cream'}
'''