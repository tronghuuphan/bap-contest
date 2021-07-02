def checkNumber(number):
    num_cvt = bin(number)
    if int(num_cvt[-1])==0:
        print('Even')
    else:
        print('Odd')

a = int(input('Input number you want to check: '))
checkNumber(a)
