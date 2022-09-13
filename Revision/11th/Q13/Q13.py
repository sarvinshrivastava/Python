def fname(gender, name):
    if gender == 'M':
        print('Mr.', name)
    elif gender == 'F':
        print('Ms.', name)
    else:
        print('Please enter a valid gender')

name = str(input('Enter you name:'))
gender = str(input('ENter you gender:'))
fname(gender, name)
