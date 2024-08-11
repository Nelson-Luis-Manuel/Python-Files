#Data Structure in Python

#Lists
mList = [[1,3,'heloo'],'world',1,3,False,1]
print(mList)
print(len(mList))
print(len(mList[0]))

print([1,2]==[1,2])

#Sets
mSet = {1,2,3,4,5,5,1}
print(mSet)
print(type(mSet))
print(len(mSet))

#Tuples
mTuple = (1,2,3)
print(mTuple)
print(type(mTuple))
print(len(mTuple))

mList.append(111111)
mList2 = mList
print(mList2)

#Tuples VS Lists:
# Tuples are basically a type of Lists. Tuples save memory if the-
# elements are known to not change during the running time.

#Dictionaries
mDict = {
    'firstName': 'Nelson Luis',
    'surName': 'Manuel',
    'age': 28,
    'profession': 'Electrical Enginner'
}
print(mDict)
print(type(mDict))
print(len(mDict))
print(mDict['firstName'])
print(mDict['age'])


#Sets VS Dictionary:

# Both Sets and Dictionaries are defined using curly brackets {}.
# The elements of Sets and the keys of Dictionaries must be unique.
# The order doesn't matter.