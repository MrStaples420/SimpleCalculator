

def main():
    print("1.add\n2.sub\n3.mult\n4.div")

    op = int(input("enter a number between 1-4: "))
    num1 = int(input("enter a number: "))
    num2 = int(input("enter another number: "))

    if op == 1:
        print(num1 + num2)
    elif op == 2:
        print(num1 - num2)
    elif op == 3:
        print(num1 * num2)
    elif op == 4:
        print(num1 / num2)
    else:
        print("you didn't choose numbers 1-4 pls do so!")


def redo():

    restart = (int(input("do you want to continue 1 for yes 2 for no: ")))

    while restart == 1:
        main()
        redo()
    exit()


main()
redo()
