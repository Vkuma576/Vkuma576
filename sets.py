#sets

# set = {1,2,3,(1,2),4.5}
# print(type(set))

# set_2 = set()
# print(type(set_2))  

#set contians string, integer, float and tuple

# sample = {"shravan",1,2,1.2,(1,2),1,1,1,} #----> unordered sequense and immutable data types
# print(sample) #---> does not support duplicates and outputs only unique values.

# set_1 = {1,2,3,4} # set doesn't support indexing as it is unordered

'''set methods
add()   adds element to set
clear()      removes all elements from set
copy()  returns a copy of set
pop()   removes an element from set
remove()    removes the specified element
update()    update the set with another set'''

set_1 = {"mahesh", "radha","ram",1,2,3}
set_1.add("Kumar")
print(set_1)