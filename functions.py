# def greet(): # function defenition
#     print("Hi, Shravan_kumar_vampu") #  function body
# # syntax for calling function
# #functionname()
# greet()

# def add():
#     shravan = 10
#     veena = 20
#     result = shravan + veena 
#     print(result)
# # add()

# def details(user,id): # passing parameters
#     print(user)
#     print(id)
# details("shravan",2184754)
# details({"kumar :9010219912"},1234) # ant datatype can be passed in the arguments

# def multiply(x,y):
#     print(x*y)
# multiply(2,2)

# return is usesd to exit a function, returns a value to caller

# def add(shravan,veena):
#     return shravan+veena
# obj = add(10,10)
# print(obj*3)

# Default parameters

# def details(user,dept,id=1234):
#     print(user,dept,id)
# details("shravan","Analyst",345)
# details("kumar","support") # here id is missing but default value takeovers as we have provided defalutvalue

                            ###### Arbitary arguments ########

# def my_fun(*x): # arbitary argument has been given *
#     print(x)
# my_fun(1,123,5.7,(1,2,3),{2,3,4},"shravan")

#-----> * results in tuple format

                           ###### keyword argument #####

# def myf_fun(**x): # ** is used to key value pairs in result.
#     print(x)
# myf_fun(x=1,y=2,z=3)
# #----> ** resuts in dictinary format        

                            #### Calculator #######        

# import Calculator 

# # syntax
# # modualanme.functionname()
# # print(Calculator.add(10,10 ))
# # print(Calculator.add(20,12))

# from Calculator import *
# print(add(10,10))
# print(sub(10,2))
# print(mul(10,2))
# print(expo(10,4))
# print(div(10,2))

# import math

# print(math.sqrt(4))

# import random

# print(random.randint(1,10))
# print(random.choice(['Shravan','veena','Ayra']))

# from datetime import *
# now = datetime.now()
# print(now)