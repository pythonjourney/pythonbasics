run = True

while run:
    answer = input("What is 5 + 7")
    
    if answer == "12":
        print("Correct!")
        run = False
    else:
        print("Try Again...")