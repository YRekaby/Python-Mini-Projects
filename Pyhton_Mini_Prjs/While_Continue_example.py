spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue #if the condition is met, Continue will jump to the start of the program and the lines after it wont be executed.
    print('spam is ' + str(spam))
