# User runs program
# Ask user for operation type and save / cache it
# Ask user for numbers/ floats
# Validate user number
# Perform mathematical operation on user numbers and print result
# Ask user whether s/he'd like to perform an operation
# If yes, restart the loop
# Else, break the loop, and end the program
print("Welcome to Simple CLI Calculator")

is_running = True

while is_running:
    # processing calculations..
    print("Starting Calculator Process")
    user_operation = input("What operation would you like to perform? \n Pick any of ['+','-','*','/','%'] : ")
    
    # Get user numbers
    try: #Try to get user numbers, if theyre valid integers/float
        no1 = float(input("First number: "))
        no2 = float(input("Second number: "))
        
    except: #We get an error while running it
        print("Failed, Invalid numbers..")
        continue
    
    if user_operation == "+":
        # perform addition
        print(no1 + no2)
    
    elif user_operation == "-":
        # perform subtraction
        print(no1 - no2)
        
    elif user_operation == "*":
        # perform multiplication
        print(no1 * no2)
        
    elif user_operation == "/":
        # perform division
        print(no1 / no2)
        
    elif user_operation == "%":
        # perform modulus
        print(no1 % no2)
    else:
        # invalid operation
        print("Invalid Operation entered Try again!")
        
    choice = input("Would you like to run another calculation? ['yes','no']: ")
    if choice == "Yes":
        pass
    
    if choice == "no":
        is_running = False
        # This is the same as a break
        
print("Thanks for using the calculator, Au revoir!...")
    