# practice 5
# create the multiplication table based on user input
print("hello there! we want to create a multiplication table\n"
      "based on the numbers that you will provide. all we ask\n"
      "you to do is to give us two numbers below :)")

while True:
    print("")
    number1 = input("1/ please provide a number here: ")
    number2 = input("2/ please provide a number here: ")

    if number1.isdigit() and number2.isdigit():
        if int(number1) < int(number2):
            num1 , num2 = int(number1), int(number2)
            print("")
            print("  ", end="")
            for i in range (num1, num2 + 1):
                print (i, end=" ")
            print("")
            for j in range (num1, num2 + 1):
                print(j, end=" ")
                for n in range (num1, num2 + 1):
                    print(j * n, end=" " )
                print("")
            break
        else:
            print("")
            print("the first number is either bigger or equal to the second number.\n"
                  "that is not acceptable, so please try again.")
    else:
        print("")
        print("the values provided do not follow the rules.\n"
              "please try again.")