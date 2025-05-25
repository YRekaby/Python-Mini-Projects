# This program says hello and asks for your name

print('Hello World!')

print('What is your name?') # ask for name
myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is:')
print(len(myName)) # len evaluates the number of integers in a string

print('What is your age?') #ask for age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year. ') #int will convert the value in myAge to a number(integer) then so it can do the math and adds + 1, Then the Str function will convert this number into a string so it can add it to the other strings beside it and give us the sentence

