print('How many cats do you have?')
numcats = input()
try:
    if int(numcats) >= 4:
        print('That is alot of cats!')
    elif int(numcats) < 0:
        print('Negative cats? Really?')
    else:
        print('Thats not many cats')
except ValueError:
    print('You did not enter a number')

        
