# Dictionary is a Key value pair and is declared by enclosing {}. comma sepreared 

# sample = {}
# print(type(sample))

Dictionary = {
    'Name' : 'Shravan',
    'Age' : 35, 
    'Profession' : 'Data_Engineer' , 
    'Resident' : 'Hyderabad'}
# print(Dictionary)

# copy 

# Dictionary_1 = Dictionary.copy()
# print(Dictionary_1)

# Clear 

# Dictionary_1.clear()
# print(Dictionary_1)

# get

# print(Dictionary.get('Age'),('Name'))

# we can also use square brackets [] inorder get the values of the keys, as shown below.
# print(Dictionary['Name'],Dictionary['Age'])

'''pop it removes the key value pair from the dictionary. 
As we can see after using pop() key value "Name" has been removed from Dictionary'''

# print(Dictionary)
# Dictionary.pop('Name')
# print(Dictionary)

# obj = Dictionary
# print(Dictionary)
# print(obj)

# keys() & Values() it will only project the list of keys available in the Dictinary
# print(Dictionary.keys())
# print(Dictionary.values())
# Items() this will projoect the key and values in a list with pair of tuples.
#print(Dictionary.items())

# Update which performs an update to the existing dictionary with another dictionary

# Dictionary_1 = {
#     'Qualification' : 'B.com,MBA'}
# print(Dictionary_1)

# Dictionary.update(Dictionary_1)
# print(Dictionary)

''' "Adding" with the help if square bracket notation[] , 
we can add the key value pair in the Dictionary and also can change the existing key values pair'''
# print(Dictionary)
Dictionary['Qualification'] ='B.Com,MBA,LLB' # adding Quialification
Dictionary['Resident'] = 'Telangana' # here we are changing the details by using assigment with list
# print(Dictionary)

# print(Dictionary)

# In Dic object has ni attribute 'add()','insert()' and 'append()'.

# Dictionary.add({'Height' : '165cm', 'Weight' : '72kgs'})
# Dictionary.insert({'Height' : '165cm', 'Weight' : '72kgs'})
# Dictionary.append({'Height' : '165cm', 'Weight' : '72kgs'})

Dictionary['Height'] = '165cms'
Dictionary['Weight'] = '72kgs'
print(Dictionary)
