# DAY 3

#Complex_data_type

# In python, complex data type is used to represent complex data. It contains real part and imaginary part.

Complex_data_type = 3 + 4j
print(type(Complex_data_type))

#List  [ ]
# A list can be any element such as below and is mutable and ordered squence.
List = [1,2,3,4,5,"Shravan",5.5,"shravan_321",{1,2},(1,2)]
print(List)
print(id(List))
List.append("Kumar")
print(List)
print(id(List))

#Tuples ( )
''' A tuple can be of any element and is basically similar to list.
 But it is immutable datatype'''

Tuple = (1,2,3,4,5,"Shravan",5.5,"shravan_321",{1,2},(1,2))
print(Tuple)
print(type(Tuple))

#sets

# A sets is unordered datatype and with no duplicates { }

''' Here in the below set it removes the duplicates and 
projects only unique values, every time it shuffles the output which makes it an unordered'''

Sets = {'Shravan',5.6,8,'shravan@124','Shravan'}
print(Sets)
print(type(Sets))

# Dictionary {} & :

# A dictionary is a datatype which is unordered and is a combination of keys and values

Dictionary = {'Name' :'Shravan_kumar_vampu','Height' : '5.6', 'Employee' : 'True'}
print(Dictionary)
print(type(Dictionary))

# Boolean
# represents either 'True or 'False
Employee = True
print(type(Employee))


# List to set Conversion

List = [1,2,3,4,5]
set_converion = set(List)
print(list(set_converion)) 

# set to list conversion


