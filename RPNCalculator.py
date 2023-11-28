class RPNCalculator:
    def __init__(self):
        self.stack = []

    def calculate_rpn(self, expression):
        tokens = expression.split()
        for token in tokens:
            if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
                self.stack.append(int(token))
            elif token in ('+', '-', '*', '/'):
                operand2 = self.stack.pop()
                operand1 = self.stack.pop()
                result = self.perform_operation(operand1, operand2, token)
                self.stack.append(result)
            else:
                raise ValueError(f"Invalid token: {token}")

        if len(self.stack) == 1:
            return self.stack[0]
        else:
            raise ValueError("Invalid expression")

    def perform_operation(self, operand1, operand2, operator):
        if operator == '+':
            return operand1 + operand2
        elif operator == '-':
            return operand1 - operand2
        elif operator == '*':
            return operand1 * operand2
        elif operator == '/':
            if operand2 == 0:
                raise ValueError("Division by zero")
            return operand1 / operand2

# Example usage:
rpn_calculator = RPNCalculator()
result = rpn_calculator.calculate_rpn("3 4 + 5 *")
print(result)
