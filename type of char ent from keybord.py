s = input('enter the charater:')
if s.isalnum():
    print('it is alphanumiric character..')
    if s.isalpha():
        print('it is alphabet character..')
        if s.islower():
            print('it is lower case charater..')
        else:
            print('it is upper case charater..')
    else:
        print('it is digit..')
elif s.isspace():
    print('it is space charater..')
else:
    print('it is non space,special charater..')        