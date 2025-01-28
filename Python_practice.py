# items = [["Apple", 99], ["Banana", 99], ["Milk", 49]]
# print(f"item{" "*8}price")
# print("-"*20)
# print(f"{items[0][0]}{" "*8}{float(items[0][1])}")
# print(f"{items[1][0]}{" "*7}{float(items[1][1])}")
# print(f"{items[2][0]}{" "*9}{float(items[2][1])}")
# print("-"*20)
# print(f"Total{" "*8}{float(float(items[0][1])+float(items[1][1])+float(items[2][1]))}")

dictionary = {}

while True:
            print("\nDictionary Management System")
            print("1. Add a Word")
            print("2. Search for Meaning")
            print("3. Display All Words")
            print("4. Update Meaning")
            print("5. Delete Word")
            print("6. Exit")

            choice = input("Enter your choice: ").strip()

            if choice == '1':
                word = input("Enter the word: ").lower().strip()
                if word in dictionary:
                    print(f"The given word '{word}' is already exists in the dictionary")
                else:
                    meaning = input("Enter the meaning: ").strip()
                    dictionary[word] = meaning
                    print("Word added successfully!")            

            elif choice == '2':
                word = input("Enter the word to search: ").lower().strip()
                if word in dictionary:
                    print("Meaning:", dictionary[word])
                else:
                    print("Word not found in the dictionary.")
    elif choice == '3':
        if dictionary:
            print("Words and their meanings:")
            for word, meaning in dictionary.items():
                print(f"{word}: {meaning}")
        else:   
            print("Dictionary is empty.")     