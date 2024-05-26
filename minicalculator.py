print("Mini Calculator")
num1 = float(input("enter the first number here: "))
num2 = float(input("enter the second number here: "))
print("press 1  for addition \npress  2 for subtraction \npress 3 for multiplication \npress 4 for division")
choice = int(input("enter your choice"))
if choice ==1:
    print("the addition  of the gven two number is",num1 + num2)
elif choice ==2:
    print("the subtraction  of the gven two number is",num1 - num2)
elif choice == 3:
  print("the multiplication  of the gven two number is",num1 * num2)
elif choice == 4:
  print("the division of the gven two number is",num1 / num2)
