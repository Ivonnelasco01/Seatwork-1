#list 
list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#menu
def menu():
    print("----------------------")
    print("Array:", list1)
    print("Menu:")
    print("1. Add an element")
    print("2. Insert an element")
    print("3. Modify an element")
    print("4. Delete an element")
    print("5. Arrange in descending order")
    print("6. Arrange in accending order")
    print("----------------------")
menu()

#option
option  = input("What do you want to do? Please pick a number from 1-6. >>")

if option == "1":
    print("What do you want to add? >>")
elif option == "2":
    print("What do you want to insert? >>")
elif option == "3":
    print("What do you want to modify? >>")
elif option == "4":
    print("What do you want to delete? >>")
elif option == "5":
    print("")
elif option == "6":
    print("")
else:
    print("Thats not in the menu, Please pick another!")