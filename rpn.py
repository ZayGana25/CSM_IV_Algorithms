# Isaiah Lugo
# CSM IV - Algorithms
# RPN Calculator - stack implementation


def rpn_calculator(expression): # define rpn funciton
    stack = [] # stack initialization
    tokens = expression.split() # expression split into tokens
    
    for token in tokens:
        if token.isdigit(): # if number, push onto stack
            stack.append(int(token))
        elif token in {"+", "-", "*", "/"}: # if an operator
            if len(stack) < 2:
                raise ValueError("Invalid RPN expression: not enough operands for operation.")
            b = stack.pop() # pop second operand
            a = stack.pop() # pop first operand
            
            # perform operation based on token
            if token == "+":
                stack.append(a + b)
            elif token == "-":
                stack.append(a - b)
            elif token == "*":
                stack.append(a * b)
            elif token == "/":
                if b == 0:
                    raise ZeroDivisionError("Division by zero is not allowed.")
                stack.append(a // b)  # integer division
        else:
            raise ValueError(f"Invalid token in expression: {token}")
    
    if len(stack) != 1:
        raise ValueError("Invalid RPN expression: too many values left in stack.")
    
    return stack[0] # return the final result


# example test cases
if __name__ == "__main__":
    print("Answer: ", rpn_calculator("2 3 +"))  # 5
    print("Answer: ", rpn_calculator("3 4 + 2 *"))  # 14
    print("Answer: ", rpn_calculator("5 1 2 + 4 * + 3 -"))  # 14
    print("Answer: ", rpn_calculator("15 7 1 - 1 - /"))  # 3
