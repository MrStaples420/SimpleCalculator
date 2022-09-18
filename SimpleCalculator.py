print("1.Addition\n"
      "2.Subtraction\n"
      "3.Multiplication\n"
      "4.Division\n")
# you get to choose what operator you want to use
Op = int(input("What would you want to do. Choose Numbers 1-4: "))
num1 = int(input("Enter number: "))
num2 = int(input("Enter another number: "))

# setting the algorithm you want to use
if Op == 1:
    print(num1 + num2)
elif Op == 2:
    print(num1 - num2)
elif Op == 3:
    print(num1 * num2)
elif Op == 4:
    print(num1 / num2)
else:
    print("Invalid Option. Choose between 1-4: ")
