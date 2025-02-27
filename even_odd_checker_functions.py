def check_number_type(number):
    if number % 2 == 0:
        print(f"{number} is an Even number.")
    else:
        print(f"{number} is an Odd number.")

num = int(input("Enter an integer: "))
check_number_type(num)
