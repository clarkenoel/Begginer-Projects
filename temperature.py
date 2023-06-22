fahrenheit = 0
celsius = 0
flag = True


choice = input("What would you like to convert from ? : ")
choice = str(choice.lower())

if choice == 'fahrenheit':
    fahrenheit = input("What is the temperature ? : ")
    fahrenheit = float(fahrenheit)
    celsius = (fahrenheit - 32) * 5/9
    print(str(celsius) + 'C')
elif choice == 'celsius':
    celsius = input("What is the temperature ? : ")
    celsius = float(celsius)
    fahrenheit = (celsius) * (9/5) + 32
    print(str(fahrenheit) + 'F')
