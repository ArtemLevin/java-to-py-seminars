yourLine = input("Enter your line ---> ") + " "

counter = 1
for i in range(1, len(yourLine)):
    if yourLine[i] == yourLine[i - 1]:
        counter += 1
    else:
        if counter == 1:
            print(yourLine[i - 1])
        else:
            print(yourLine[i - 1] + str(counter), end="")
            counter = 1
