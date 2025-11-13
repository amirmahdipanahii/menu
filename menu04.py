user_name = "amir"
password = "amir12"
u_s = input("user name:")
pas = input("password:")
if user_name == u_s and password == pas:
    print("welcome")
else:
    exit("nooo")
mmd_score_list = []
amir_score_list = []
ali_score_list = []
while True:
    print("1)add score")
    print("2)average score")
    print("3)show maximum score")
    print("4)show minimum score")
    print("5)remove score")
    print("6)show scor < 10 ")
    print("7)show lists")
    print("0)exit")
    option = int(input("your option:"))
    if option == 1:
        student_name = input("enter student name:")
        if student_name == "mmd":
            mmd_score = float(input("score:"))
            mmd_score_list.append(mmd_score)
        elif student_name == "amir":
            amir_score = float(input("score:"))
            amir_score_list.append(amir_score)
        elif student_name == "ali":
            ali_score = float(input("score:"))
            ali_score_list.append(ali_score)
        else:
            print("invalid name")
    if option == 2:
        student_name1 = input("enter student name:")
        if student_name1 == "mmd":
            print("mmd average score:" , sum(mmd_score_list) /  len(mmd_score_list))
        elif student_name1 == "amir":
            print("amir average score:" , sum(amir_score_list) / len(ali_score_list))
        elif student_name1 == "ali":
            print("ali average score:" , sum(ali_score_list) / len(ali_score_list))
        else:
            print("ivalid name")
    if option == 3:
        student_name2 = input("enter student name:")
        if student_name2 == "mmd":
            print("maximum mmd score:" , max(mmd_score_list))
        elif student_name2 == "amir":
            print("maximum amir score:" , max(amir_score_list))
        elif student_name2 == "ali":
            print("maximum ali score:" , max(ali_score_list))
        else:
            print("invalid name")
    if option == 4:
        student_name3 = input("enter student name:")
        if student_name3 == "mmd":
            print("minimum mmd score:" , min(mmd_score_list))
        elif student_name3 == "amir":
            print("minimum amir score:" , min(amir_score_list))
        elif student_name3 == "ali":
            print("minimum ali score:" , min(ali_score_list))
        else:
            print("invalid namr")
    if option == 5:
        student_name4 = input("enter student name:")
        if student_name4 == "mmd":
            mr_s = float(input("remove score:"))
            if mr_s in mmd_score_list:
                mmd_score_list.remove(mr_s)
                print("ok")
            else:
                print("not ok")
        if student_name4 == "amir":
            amr_s = float(input("rmove score:"))
            if amr_s in amir_score_list:
                amir_score_list.remove(amr_s)
                print("ok")
            else:
                print("not ok")
        if student_name4 == "ali":
            ar_s = float(input("remove score:"))
            if ar_s in ali_score_list:
                ali_score_list.remove(ar_s)
                print("ok")
            else:
                print("not ok")
        else:
            print("invalid name")
    if option == 6:
        student_name5 = input("enter student name:")
        if student_name5 == "mmd":
            for i in mmd_score_list:
                if i < 10:
                    print("mmd score < 10:" , i)
        elif student_name5 == "amir":
            for m in amir_score_list:
                if m < 10:
                    print("amir score < 10:" , m)
        elif student_name5 == "ali":
            for a in ali_score_list:
                if a < 10:
                    print("ali score < 10:" , a)
        else:
            print("invalid name")
    if option == 7:
        print("mmd score list:" , mmd_score_list)
        print("amir score list:" , amir_score_list)
        print("ali score list:" , ali_score_list)
    if option == 0:
        break
    else:
        print("invalid name")