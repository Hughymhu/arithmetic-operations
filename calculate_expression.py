def calculate(expression):

    # Validate the input expression to ensure it only contains digits, operators, and decimal points
    if not all(c.isdigit() or c in '+-*/.' for c in expression):
        raise ValueError("Expression contains invalid characters.")

    stack = []
    num, decimal_divisor = 0, 1
    is_decimal = False
    last_op = '+'

    # Add an extra operator to process the last number
    expression += '+'

    for i, char in enumerate(expression):

        # Handle digits
        if char.isdigit():
            num = num * 10 + int(char)
            if is_decimal:
                decimal_divisor *= 10

        # Start decimal processing
        elif char == '.':
            is_decimal = True

        # Process operators
        elif char in '+-*/' or i == len(expression) - 1:
            if is_decimal:

                # Convert integer number to decimal
                num /= decimal_divisor
            if last_op == '+':
                stack.append(num)
            elif last_op == '-':
                stack.append(-num)
            elif last_op == '*':
                stack[-1] *= num
            elif last_op == '/':
                if num == 0:
                    raise ZeroDivisionError("Division by zero.")

                # Use floating-point division for decimals
                stack[-1] /= num
            num, decimal_divisor = 0, 1
            is_decimal = False
            last_op = char

    return sum(stack)


# Example usage
if __name__ == '__main__':
    try:
        input_expression = "3.92+5*8.9-6/2"
        result = calculate(input_expression)
        print(result)
    except Exception as e:
        print("Error:", e)
      
