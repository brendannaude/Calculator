#This is the code for a basic calculator programme.
import os

class Operations:

    def add(m, n):
        '''Returns result = m + n '''
        return m + n
        
    def subtract(m, n):
        '''Returns ans = m - n '''
        return m - n
    
    def multiply(m, n):
        '''Returns ans = m * n '''
        return m * n
    
    def divide(m, n):
        '''Returns ans = m / n '''
        if n == 0:
            print("Undefined")
            return "Undefined"
        else:
            return m / n
    
    def exponent(m, n):
        '''Returns m to the power of n'''
        return m ** n

    dictionary = {
        "+": add,
        "-": subtract,
        "*": multiply,
        "/": divide,
        "^": exponent
    }
    options_string = "\n'+'\n'-'\n'*'\n'/'\n'^'\n"


def run_calculation(m, calculation_history):
    print(f"First input --> {m}:\n")
    
    operation = get_operation()
    n = get_second_number(operation)
    
    result = Operations.dictionary[operation](m, n)
    calculation_string = f"{m} {operation} {n} = {result}\n"
    calculation_history += calculation_string
    
    print(f"Result: {calculation_string}\n")
    print(calculation_history)
    return result, calculation_history


def get_first_number():
    '''Prompts the user to input the first number, returns False if "exit" is selected'''
    answer = input("Enter first number (or 'exit'): ")
    
    if answer == "exit":
       return False
    else:
        return float(answer)
    return
    

def get_operation():
    '''`Prompts the user to input the operation type'''
    answer = input(f"Choose operation: {Operations.options_string}")
    
    while not answer in Operations.dictionary:
        answer = input(f"Invalid input. Choose operation: {Operations.options_string}")
    print(f"\n\"{answer}\" selected.\n")
    return answer


def get_second_number(operation):
    '''Prompts the user to input the second number'''
    answer = float(input("Enter second number: "))
    while operation == "/" and answer == 0:
        answer = float(input("Division by zero is not defined. Enter non-zero number: "))
    return answer
    

def prompt_keep_going(result):
    continue_dict = {"yes": True, "no": False}
    yes_string = "Answer \"yes\" to proceed with"
    no_string = "as the input, or \"no\" to clear."

    answer = input(f"Proceed with {result} as input? {yes_string} {no_string} : ").lower()
    
    while not answer in continue_dict:
        answer = input(f"Invalid input. {yes_string} {result} {no_string}")

    os.system("clear")
    if answer == "no":
        print("Existing input cleared.\n")
    
    return continue_dict[answer]
    

def calculator():
    calculation_history = f"\nCalculation history:\n"
    print("Calculator:\n")

    m = get_first_number()
    #Check if user chose to exit
    if type(m) == bool:
        os.system("clear")
        print("Goodbye!")
        return
    else:
        result, calculation_history = run_calculation(m, calculation_history)
    
    #Further calculations
    while prompt_keep_going(result):
        result, calculation_history = run_calculation(result, calculation_history)      

    #User chooses to clear so calculator is restarted
    calculator()
    return


#run calculator    
calculator()

 
