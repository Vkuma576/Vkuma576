#syntax
# class object():
class dictionary(): # Base class 
    def __init__(self):
        self.dictionary = {}
    def add_word(self):
        word = input("Enter the word: ").lower().strip()
        if word in self.dictionary:
            print(f"The word {word} is already exists")
        else:
            meaning = input("Enter the meaning: ").strip()
            self.dictionary[word] = meaning
            print(f"word added successfully!!")
    def search_for_meaning(self):
        word = input("Enter the word for searching: ").lower().strip()
        if word in self.dictionary:
            print(f"Meaning:", {self.dictionary[word]})
        else:
            print(f"Word not found")
    def Display_all_words(self):
        if self.dictionary:
            print("Word and their meaning:")
            for word, meaning in self.dictionary.items():
                print(f"{word} : {meaning}")
        else:
            print(f"Dictionary is empty")

class Dictionary_updated(dictionary): #derived class
    def Update_meaning(self):
        word = input("Entre the word to update meaning: ").lower().strip()
        if word in self.dictionary:
                New_meaning = input("Enter the new meaning: ").strip()
                print("Are you sure you want to update?")
                check_point_1 = input("Type Y/N: ").lower().strip()
                if check_point_1 == "y":
                    self.dictionary[word] = New_meaning
                    print("New meaning updates sucessfully!")
                    print("updated_meaning:", self.dictionary[word])
                elif check_point_1 == "n":
                    print("updation aborted!")
                else:
                    print("Invalid choice")
        else:
                print("word not found in the dictionary!")
    def Delete_word(self):
        word = input("Enter a word to delete: ").lower().strip()
        if word in self.dictionary:
                print("Are you sure you want to delete?")
                check_point_2 = input("Type Y/N: ").lower().strip()
                if check_point_2 == "y":
                    del self.dictionary[word]
                    print("word deleted successfully!")
                elif check_point_2 == "n":
                    print("Deletion aborted!")
                else:
                    print("Invalid choice!")
        else:
                print("word not found in disctionary")
    def Exit(): 
        print("Are you sure you want to exit?") 
        check_point_3 = input("Type Y/N: ").lower().strip() 
        if check_point_3 == "y": 
            print("Exiting program..") 
            return True # Signal to break the loop 
        elif check_point_3 == "n": 
            print("Welcome Back!") 
        else: 
            print("Invalid option!") 
        return False # Continue the loop if not exiting

DB = Dictionary_updated()

while True:
    print("\n Dictionary operation system")
    print("1. Add a word")
    print("2. Search for Meaning")
    print("3. Display all Words")
    print("4. Update Meaning")
    print("5. Delete Word")
    print("6. Exit")
    choice = input("Enter your choice: ").strip()
    #syntax
    # Object=classname()
    if choice == "1":
        DB.add_word()
    elif choice == "2":
        DB.search_for_meaning()
    elif choice == "3":
        DB.Display_all_words()
    elif choice == "4":
        DB.Update_meaning()
    elif choice == "5":
        DB.Delete_word()
    elif choice == "6":
        # if DB.Exit():
        print("Thank you ! Exiting...")
        break
        