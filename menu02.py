student_list = []
while True:
    print("1)add name")
    print("2)show list")
    print("3)remove name")
    print("4)cont list")
    print("0)exit")
    option = int(input("your option:"))
    if option == 1:
        name = input("enter student name:")
        student_list.append(name)
    elif option == 2:
        print("student list:",student_list)
    elif option == 3:
        remove_student_name = input("enter remove student name:")
        if remove_student_name in student_list:
            print("ok")
            student_list.remove(remove_student_name)
        else:
             print("error 404!")
    elif option == 4:
        co = len(student_list)
        print("cont list:",co)
    elif option == 0:
        break
    else:
        print("invalid option")