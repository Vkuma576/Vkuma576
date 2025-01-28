# #Operators
# # addition operation
# Num_1 = 10
# Num_2 = 20
# Addition = Num_1 + Num_2
# print(f"Number_1 is {Num_1} and Number_2 is {Num_2} perform additon as result {Addition} ")

# #Subtraction

# Num_1 = 10
# Num_2 = 20
# Subtraction = Num_2 - Num_1
# print(f"Number_1 is {Num_2} and Number_2 is {Num_1} perform subtract as result {Subtraction} ")

# #Multiplication

# Num_1 = 10
# Num_2 = 20
# Multiplication = Num_1 * Num_2
# print(f"Number_1 is {Num_1} and Number_2 is {Num_2} perform Multiplicaton  as result {Multiplication} ")

#Division (projects Quotiant) it projects floating or precise values like 3.75 and not int like 3

# Num_1 = 10
# Num_2 = 3
# Division = Num_1 / Num_2
# print(f"Number_1 is {Num_1} and Number_2 is {Num_2} perform Division  as result {Division} ")

#Floor division (output's the Quotient) it only give int values not floating values

# Num_1 = 10
# Num_2 = 3
# Floor_division = Num_1 // Num_2
# print(f"Number_1 is {Num_1} and Number_2 is {Num_2} perform Floor division  as result {Floor_division} ")

#Exponentiation 3^2 (3*3)

# Num_1 = 2
# Num_2 = 3
# Exponent = Num_2 ** Num_1
# print(f"Number_1 is {Num_2} and Number_2 is {Num_1} perform Expinent as result {Exponent} ")


#Modules ( projects only reminder in division)

# Num_1 = 4
# Num_2 = 3
# Modules = Num_1 % Num_2
# print(f"Number_1 is {Num_1} and Number_2 is {Num_2} perform Multiplicaton  as result {Modules} ")

##### Assignment Operators #####

# +=

# Num_1 = 5
# Num_1 += 5 # equilant Num_1 = Num_1 + 5
# print(Num_1)

#Input operations
# Shravan_1 = int(input("enter the price: "))
# Shravan_1 += 5
# print(Shravan_1)

# -=
# Shravan_1 = int(input("enter number: "))
# Shravan_1 -= 4
# print(Shravan_1)

# *=
# Shravan_1 = int(input("enter number: "))
# Shravan_1 *= 4
# print(Shravan_1)

# comparison operator

# == equal to operator
# !=
# <
# <=
# >
# >=

# Product_1 = 1000
# Product_2 = 100
# print(Product_1 == Product_2)
# print(Product_1 != Product_2)
# print(Product_1 < Product_2)
# print(Product_1 <= Product_2)
# print(Product_1 > Product_2)
# print(Product_1 >= Product_2)

# Logical Operators

# and ( Logical AND)
# or ( Locical OR)
# not ( Logical NOT)

# User_name = "Shravan"
# Password = 1234
# #Otp = 345
# print(User_name == "Shravan" and Password == 1234) #and Otp == 345)
# print(User_name == "Shravan" or Password == 1234)

# X = True
# print(not X)

# Identity Operators to check if two variables refer to the same object.

# is # is not 

# List_1 = [1,2,3]
# print(id(List_1))
# List_2 = [1,2,3]
# print(id(List_2))
# print(List_1 is List_2)
# print(List_1 is not List_2)

# Membership operators

# in # not in

# List = ["oranges", "apples","bananas","grapes"]
# print("bananas" in List)
# print("bananas" not in List)

# Output formatting ( F-Strings)

# Discount Calculator
# Total_cost = 1000
# Discount = 10
# After_Discount = Total_cost *(Discount/100) #discount calculator formulae
# #print(After_Discount)
# Total_cost -= After_Discount
# print(f"Discount given on product {Discount}%  total discount {After_Discount} and final cost after discount {Total_cost}")

X = 15 
Y = 4
result = X / Y
print(result)