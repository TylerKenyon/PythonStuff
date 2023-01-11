#adds a counter varible to say how many times the user attempted the question
awnser = input("What is the capital of France? ")
counter = 1

while awnser != "Paris":
    awnser = input("Incorrect, try again: ")
    counter = counter + 1
print("Correct! you had ",counter,"attempts")
