list = [2, 5, 6, 8, 9, 11, 15, 1, 85, 95, 10]
print("------------------------")
print("Array:", list)
print("")
print("Menu:")
print("1 -> Add an element")
print("2 -> Insert an element")
print("3 -> Modify an element")
print("4 -> Delete an elementt")
print("5 -> Arrange in ascending order")
print("6 -> Arrange in descending order")
print("-----------------------")
print()
op = int(input("What do you want to do? Pick a number from 1-6 >>"))
def num1():
    if op == 1:
        insert_num = int(input("What number do you want to add? "))
        result = list.append(insert_num)
        print("Your number has been added")
        return result
    elif op == 2:
        insert_num2 = int(input("What number do you want to insert?"))
        insert_num3 = int(input("Where do you want to insert?"))
        result_2 = list.insert(insert_num3, insert_num2)
        print("The element has been Insert")
        return result_2    
    elif op == 3:
        insert_num4 = int(input("What number do yoy want to modify?"))
        insert_num5 = int(input("Insert your number:"))
        result_3 = list.pop(insert_num4)
        list.insert(insert_num4, insert_num5)
        print("The element has been Modify")
        return result_3
    elif op == 4:
        insert_num6 = int(input("What number do you want to delete?"))
        result_4 = list.remove(insert_num6)
        return result_4
    elif op == 5:
        result_5 = list.sort()
        print("The element has been arrange to ascending order")
        return result_5
    elif op == 6:
        result_6 = list.reverse()
        print("The element has been arrange to descending order")
        return result_6
num1()
print()
print(f"This is the new array: Array : {list}")