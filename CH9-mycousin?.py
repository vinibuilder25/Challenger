print ('-='*30,'\nMycousin?\n','-='*30)
number = int(input('Enter a number: '))
counter = 2
while True:
    if number % counter == 0:
        print("It's not prime")
        break
    if counter == number - 1:
        print('its prime')
        break
    counter += 1
