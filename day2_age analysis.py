print("welcome to age analysis")
while True:
    try:
        age = int(input("enter your age "))
        if age<13:

            print("your a child")
        elif age<20:
            print("your a teenager")
        else :
            print("your a adult")
        break
    except:
            print ("only numbers my friend")
