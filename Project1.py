# height checker program
print("hello world")
height = int(input("what is your height:"))
if height > 120:
    print("you can ride")
    age = int(input("what is your age:"))
    if age >= 18:
        bill = 12
        print(f"your bill is ${bill}")
    elif age < 12:
        bill = 5
        print(f"your bill is ${bill}")
    else:
        bill = 7
        print(f"your bill is ${bill}")
    want_photos = input("do u need some photos sir, respond with y or n: ")
    if want_photos == "y":
        bill += 3
    print(f"your total bill is ${bill}")
else:
    print("you can't ride")
