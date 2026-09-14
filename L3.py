n = int(input("Enter the number"))
b = int(input("Enter the number"))


if(b == 0):
 raise ZeroDivisionError("OH FUCKK THIS AIN'T MEANT TO BE HAPPEN")

else:
 print(f"The division is {int(n/b)}")
