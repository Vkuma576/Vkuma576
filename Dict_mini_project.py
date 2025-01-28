dictionary = {}

while True:
    print("\n Dictionary operation system")
    print("1. Add a word")
    print("2. Search for Meaning")
    print("3. Display all Words")
    print("4. Update Meaning")
    print("5. Delete Word")
    
    choice = input ("Enter your choice: ").strip()

    if choice == '1':
        word = input("Enter the word: ").lower().strip()
        if word in dictionary:
            print(f"The word {word} is already exists")
        else:
            meaning = input("Enter the meaning: ").strip()
            dictionary[word] = meaning
            print(f"word added successfully!!")

    elif choice == '2':
        word = input("Enter the word for searching: ").lower().strip()
        if word in dictionary:
            print(f"Meaning:", dictionary[word])
        else:
            print(f"Word not found")

    elif choice == '3':
        if dictionary:
            print("Word and their meaning:")
            for word, meaning in dictionary.items():
                print(f"{word} : {meaning}")
        else:
            print(f"Dictionary is empty")
        
    elif choice == "4":
            word = input("Entre the word to update meaning: ").lower().strip()
            if word in dictionary:
                New_meaning = input("Enter the new meaning: ").strip()
                print("Are you sure you want to update?")
                check_point_1 = input("Type Y/N: ").lower().strip()
                if check_point_1 == "y":
                    dictionary[word] = New_meaning
                    print("New meaning updates sucessfully!")
                    print("updated_meaning:", dictionary[word])
                elif check_point_1 == "n":
                    print("updation aborted!")
                else:
                    print("Invalid choice")
            else:
                print("word not found in the dictionary!")

    elif choice == "5":
            word = input("Enter a word to delete: ").lower().strip()
            if word in dictionary:
                print("Are you sure you want to delete?")
                check_point_2 = input("Type Y/N: ").lower().strip()
                if check_point_2 == "y":
                    del dictionary[word]
                    print("word deleted successfully!")
                elif check_point_2 == "n":
                    print("Deletion aborted!")
                else:
                    print("Invalid choice!")
            else:
                print("word not found in disctionary")

    elif choice == "6":
            print("Are you sure you want to exit?")
            check_point_3 = input("Type Y/N: ").lower().strip()
            if check_point_3 == "y":
                print("Exiting program..")
                break
            elif check_point_3 == "n":
                print("Welcome Back!")
            else:
                print("Invalid option!")
    else:
        print("Invalid choice! please entre valid option.")
                    









