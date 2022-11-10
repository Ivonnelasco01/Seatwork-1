list=[10, 20, 45, 6, 78, 11, 5, 12, 18, 15]
def menu():
    print("This is the array", list)
    print("MENU:")
    print("1. Add an element")
    print("2. Insert an element")
    print("3. Modify an element")
    print("4. Delete an element")
    print("5. Arrange in ascending order")
    print("6. Arrange in descending order")
menu()

while True:
    select = int(input("Select a number >> "))
    if select == 1:
        add_num = int(input("What number do you want to add? "))
        result = list.append(add_num)
        print("Your number has been added, new array :", list)
        break
    elif select == 2:
        insert_num2 = int(input("What number do you want to insert?"))
        insert_num3 = int(input("Where do you want to insert?"))
        result_2 = list.insert(insert_num3 - 1, insert_num2)
        print("Your number has been insert, new array :", list)
        break
    elif select == 3:
        insert_num4 = int(input("From the arrangement 1-10, modify a number:"))
        insert_num5 = int(input("Insert your number:"))
        result_3 = list.pop(insert_num4 -1)
        list.insert(insert_num4 -1, insert_num5)
        print("Your number has been modified, new array :", list)
        break
    elif select == 4:
        insert_num6 = int(input("What number do you want to delete?"))
        result_4 = list.remove(insert_num6)
        print("Your number has been deleted, new array :", list)
        break
    elif select == 5:
        result_5 = list.sort()
        print("Arrangement in ascending order, new array :", list)
        break
    elif select == 6:
        result_6 = list.sort(reverse=True)
        print("Arrangement in descending order, new array ", list)
        break
    else:
        print("THATS NOT IN THE MENU, PICK ANOTHER ONE!")
        menu()
