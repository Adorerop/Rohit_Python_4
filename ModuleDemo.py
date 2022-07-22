import udf

while True:
    print("*"*50)
    print("1. Rohit Kumavat")
    print("2. Utsav")
    print("3. Dev")
    print("4. Nishu")
    print("5. Mrudani")
    print("6. Dhruvi")
    print("7. Priyal")
    print("8. Vedant")
    print("9. Axay")
    print("10. Raji")
    print("11. Dhruvish")
    print("12. Rohit Nanera")
    print("13. Haider")
    print("14. Break")
    print("*"*50)
    choice=int(input("Enter Your Choice : "))
    print("*"*50)
    if choice==1:
        udf.rohit(10)
        print("*"*50)
    elif choice==2:
        udf.utsav(10,20)
        print("*"*50)
    elif choice==3:
        udf.dev(1,2,3)
        print("*"*50)
    elif choice==4:
        udf.nishu(100)
        print()
        print("*"*50)
    elif choice==5:
        udf.mrudani(21)
        print("*"*50)
    elif choice==6:
        udf.dhruvi(10)
        print("*"*50)
    elif choice==7:
        udf.priyal(10)
        print("*"*50)
    elif choice==8:
        udf.vedant(10)
        print("*"*50)
    elif choice==9:
        udf.axay(10)
        print("*"*50)
    elif choice==10:
        udf.raji(10)
        print("*"*50)
    elif choice==11:
        udf.dhruvish(10)
        print("*"*50)
    elif choice==12:
        udf.rohitNanera(10)
        print("*"*50)
    elif choice==13:
        udf.haidar(10)
        print("*"*50)
    else:
        break
