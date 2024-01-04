print("Please enter 'q' as an operator to quit.")

zero = 0

# starting while loop so the user can use the calculator as long as they want
while zero < 1:

    try:
        value_one = input('Please insert a value: ')
        value_two = input('Please insert another value: ')
        operator = input('Please select an operator: ')
        
        # Processing the calculation 
        if operator == '+':
            print(int(value_one) + int(value_two))
        elif operator == '-':
            print(int(value_one) - int(value_two))
        elif operator == '*':
            print(int(value_one) * int(value_two))
        elif operator == '/':
            print(int(value_one) / int(value_two))
        elif operator == '%':
            print(int(value_one) % int(value_two))

        # Quit the program or calculator
        elif operator.lower() == 'q':
            break

        # if operator is wrong or unexpected
        else:
            print('Please insert a correct operator.')

    except ValueError:

        # if value is wrong or not an integer 
        print('Something went wrong.\nPlease make sure your entered values and operators are correct.')
