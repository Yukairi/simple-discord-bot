import random
import re
import numpy as np

def get_response(message: str) -> str:
    p_message = message.lower()
    user_message = message.lower()

    if p_message == 'hello':
        return ' I am the hydro archon of Fontaine, :sparkles: Focalors :sparkles: The god of justice who is loved and adored by many...'

    if user_message == '!dice':
        return str(random.randint(1, 6))

    if p_message == '!help':
        return "This is a help message you can modify."

    # Check for math-related commands
    math_result = calculate_math_expression(user_message)
    if math_result:
        return math_result

    # Check for vector commands
    if p_message.startswith('vector '):
        vector_command = user_message[len('vector '):]
        result = calculate_vector_command(vector_command)
        return f"Vector result: {result}"

    return "I'm sorry, I don't understand your message."


def calculate_math_expression(expression):
    # Define a regular expression pattern to match valid math commands
    math_pattern = r'^(?:(?!(!add\s+-\s+))(!add|!sub|!mul|!div))\s+(-?\d+(?:\.\d+)?)\s*([-+*/])\s*(-?\d+(?:\.\d+)?)$'

    math_match = re.match(math_pattern, expression)
    if math_match:
        operator = math_match.group(2)
        num1 = float(math_match.group(3))
        operation = math_match.group(4)
        num2 = float(math_match.group(5))

        # Ensure both the command and operation are valid
        valid_commands = {'!add', '!sub', '!mul', '!div'}
        valid_operations = {'+', '-', '*', '/'}

        if operator in valid_commands and operation in valid_operations:
            result = 0

            if operator == '!add':
                if operation == '+':
                    result = num1 + num2
                else:
                    return "Invalid operation for addition. Please use '+'."

            elif operator == '!sub':
                if operation == '-':
                    result = num1 - num2
                else:
                    return "Invalid operation for subtraction. Please use '-'."

            elif operator == '!mul':
                if operation == '*':
                    result = num1 * num2
                else:
                    return "Invalid operation for multiplication. Please use '*'."

            elif operator == '!div':
                if operation == '/':
                    if num2 != 0:
                        result = num1 / num2
                    else:
                        return "Error: Division by zero"
                else:
                    return "Invalid operation for division. Please use '/'."

            return f"The result of {num1} {operation} {num2} is: {result}"
        else:
            return "Invalid command or operation. Please use valid commands: !add, !sub, !mul, !div with the correct operations."

def calculate_vector_command(command):
    parts = command.split()
    if len(parts) < 3:
        return "Invalid input. Please provide a valid vector operation."

    if parts[0] == 'add':
        vectors = [list(map(float, v.split(','))) for v in parts[1:]]
        result_vector = np.array(vectors[0])
        for vector in vectors[1:]:
            result_vector += np.array(vector)
        return result_vector

    elif parts[0] == 'subtract':
        vectors = [list(map(float, v.split(','))) for v in parts[1:]]
        result_vector = np.array(vectors[0])
        for vector in vectors[1:]:
            result_vector -= np.array(vector)
        return result_vector

    elif parts[0] == 'scale':
        scalar = float(parts[1])
        vector = list(map(float, parts[2].split(',')))
        result_vector = np.array(vector) * scalar
        return result_vector

    return "Invalid input. Please provide a valid vector operation."

'''Example usage:

message = !add 1 + 1
response = get_response(message)
print(response)

message = "vector add 2,3,4 1,1,1"
response = get_response(message)
print(response)

message = "vector subtract 5,5,5 1,1,1"
response = get_response(message)
print(response)

message = "vector scale 2 3,4,5"
response = get_response(message)
print(response)
'''
