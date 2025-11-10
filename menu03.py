while True:
    print("1)sum number")
    print("2)power number")
    print("3)minus number")
    print("4)times number")
    print("0)exit")
    option = int(input("your option:"))
    if option == 1:
        a = int(input("number1:"))
        b = int(input("number2:"))
        c = a + b
        print("sum number:",c)
    elif option == 2:
        d = int(input("number1:"))
        e = int(input("number2:"))
        f = d ** e
        print("power number:",f)
    elif option == 3:
        g = int(input("number1:"))
        h = int(input("number2:"))
        i = g - h
        print("minus number:",i)
    elif option == 4:
        j = int(input("number1:"))
        k = int(input("number2:"))
        l = j * k
        print("times number:",l)
    elif option == 0:
        break
    else:
        print("invalid option")
