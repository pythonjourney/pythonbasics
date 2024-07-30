try:

    num = int(input("Enter a number:"))
    result = 10/num
except ZeroDivisionError as e:
     print(e)

else:
     
     print("program executed succesfully without exceeptions")