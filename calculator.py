"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


def get_user_operation():
    """
        Gets the user's operation to perform

    """


    user_question = input("Enter your equation or press 'q' to exit >  ")

    answer_tokenized = user_question.split(" ")
    return answer_tokenized



def two_tokens_calculation(operation, number):
    """
        Perform the calculation for two numbers operations

    """

    
    result = None
    
    if operation == "square":
        result = square(float(number))
                
    elif operation == "cube":
        result = cube(float(number))

    return result



def tree_tokens_calculation(operator, first_number, second_number):
    """
        Performs a 3 numbers calculation using the numbers provided from user.

    """

    result = None

    if operator == "+":              
        result = add(float(first_number), float(second_number))

    elif operator == "-":
        result = subtract(float(first_number), float(second_number))

    elif operator == "*":
        result = multiply(float(first_number), float(second_number))

    elif operator == "/":
        result = divide(float(first_number), float(second_number))

    elif operator == "pow":
        result = power(float(first_number), float(second_number))

    elif operator == "mod":
        result = mod(float(first_number), float(second_number))    

    return result    


def calculator():
    """
        Perform the calculation using the numbers provided from user

    """


    perform_calulation = True    

    while perform_calulation:

        result = None
        tokens_from_user = get_user_operation()
        operator = tokens_from_user[0]
        

        valid_operators = ["+", "-", "/", "*", "square", "cube", "pow", "mod", "q"]

        if operator not in valid_operators:
            print("Not a valid operator")
            continue
        elif operator == "q":         
            return "You are going to exit. Bye"   
             
                 
        first_number = tokens_from_user[1]
        two_numbers_operations = ["square", "cube"]        

        if len(tokens_from_user) <= 2 and operator not in two_numbers_operations:
            print("You have to provided the correct amount of tokens.")  
            continue

        elif len(tokens_from_user) == 2:
            result = two_tokens_calculation(operation = operator, number = first_number)
            print(result)

        elif len(tokens_from_user) == 3:            
            second_number = tokens_from_user[2] 

            if not str(first_number).isnumeric() or not str(second_number).isnumeric():
                print("You should provide numbers.")
                continue

            else:
                result = tree_tokens_calculation(operator = operator, first_number = first_number, second_number = second_number)
                print(result)
                continue                   

        return result   
        

print(calculator())