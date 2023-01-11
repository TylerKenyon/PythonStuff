score = 0
number = int(input("Enter a timestable: "))
for x in range (1,11):
    print(number,"*" ,x,"=__________)")
    user = int(input("Enter the answer: "))
    answer = number * x
    if user == answer:
        print("Correct")
        score = score + 1
    else:
        print("Incorrect")

print("Your score is:",score)
