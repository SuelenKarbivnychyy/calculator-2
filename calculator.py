"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code

#tokenize the answer from user
#take the first item and find a match for the operation type
#take the second item and do the calulation with the third item

def get_user_operation():

    user_question = input("Enter your equation or press 'q' to exit >  ")

    answer_tokenized = user_question.split(" ")
    return answer_tokenized


def calculation():

    perform_calulation = True
    

    while perform_calulation:    

        tokens_from_user = get_user_operation()
        calculation_to_perform = tokens_from_user[0]

        if "q" in tokens_from_user:            
            # perform_calulation = False
            print("You are going to exit. Bye")
            break

        first_number = tokens_from_user[1]
        second_number = tokens_from_user[2] 

        if not first_number.isnumeric():
            print("You should provide numbers.")
            continue

        if len(tokens_from_user) < 2:
            print("You have to provided the correct amount of tokens.")  
            continue 


        if calculation_to_perform == "+":
            print(add(float(first_number), float(second_number)))
        elif calculation_to_perform == "-":
            print(subtract(float(first_number), float(second_number)))
        elif calculation_to_perform == "*":
            print(multiply(float(first_number), float(second_number)))
        elif calculation_to_perform == "/":
            print(divide(float(first_number), float(second_number)))
        elif calculation_to_perform == "square":
            print(square(float(first_number)))
        elif calculation_to_perform == "cube":
            print(cube(float(first_number)))
        elif calculation_to_perform == "pow":
            print(power(float(first_number), float(second_number)))
        elif calculation_to_perform == "mod":
            print(mod(float(first_number), float(second_number)))
        else:
            print("Not a valid operation.")    
        

print(calculation())