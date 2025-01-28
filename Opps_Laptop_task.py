class Laptop():
    def __init__(self,Brandname,Color):
        self.Brandname = Brandname # attributes
        self.color = Color # attributes
    def Movies(self):
        print("watching movies from", self.Brandname,self.color) # functions
    def Coding(self):
        print("Python pratice from", self.Brandname,self.color) #functions
Apple = Laptop("Apple","silver")
Apple.Movies()
Apple.Coding()
Dell = Laptop("Dell","Black")
Dell.Movies()
Dell.Coding()


