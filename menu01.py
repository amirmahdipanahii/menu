number_list = []
name_list = []
while True:
    print("1)add number")
    print("2)show number list")
    print("3)add name")
    print("4)show name list")
    print("5)removed name")
    print("0)exit")
    option = int(input("your option:"))
    if option == 1:
        number = int(input("your number:"))
        number_list.append(number)
    elif option == 2:
        number_list.sort(reverse=True)
        print(number_list)
    elif option == 3:
        name = input("your name:").upper()
        name_list.append(name)
    elif option == 4:
        print(name_list)
    elif option == 5:
        removed_name = input("your removed name:").upper()
        name_list.remove(removed_name)
    elif option == 0:
        break
    else:
        print("eror 404!")
print("name_list:",name_list)
print("number_list:",number_list)