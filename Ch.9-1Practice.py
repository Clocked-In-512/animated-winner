##Robert Fernandez
##Complete
##This program uses a dictionary to track what users choose to do
##and then prints the results

#Global constants for menu choices
LOOK_UP = 1
ADD = 2
CHANGE = 3
DELETE = 4
QUIT = 5

#main function

import sys

# Define the dictionary to store data
my_dict = {}
# Read the input file
def display_menu():
    print("Menu:")
    print("1. Look up a word")
    print("2. Add a word")
    print("3. Change a word")
    print("4. Delete a word")
    print("5. Display entire dictionary")
    print("6. Exit")

def look_up_word():
    word = input("Enter the word to look up: ")
    if word in my_dict:
        print(f"{word}: {my_dict[word]}")
    else:
        print(f"{word} not found in dictionary.")

def add_word():
    word = input("Enter the word to add: ")
    meaning = input("Enter the meaning of the word: ")
    my_dict[word] = meaning
    print(f"{word} added to dictionary.")

def change_word():
    word = input("Enter the word to change: ")
    if word in my_dict:
        new_meaning = input("Enter the new meaning of the word: ")
        my_dict[word] = new_meaning
        print(f"{word} updated in dictionary.")
    else:
        print(f"{word} not found in dictionary.")

def delete_word():
    word = input("Enter the word to delete: ")
    if word in my_dict:
        del my_dict[word]
        print(f"{word} deleted from dictionary.")
    else:
        print(f"{word} not found in dictionary.")

def display_dictionary():
    if my_dict:
        for word, meaning in my_dict.items():
            print(f"{word}: {meaning}")
    else:
        print("Dictionary is empty.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            look_up_word()
        elif choice == '2':
            add_word()
        elif choice == '3':
            change_word()
        elif choice == '4':
            delete_word()
        elif choice == '5':
            display_dictionary()
        elif choice == '6':
            print("Exiting program.")
            sys.exit()
        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
