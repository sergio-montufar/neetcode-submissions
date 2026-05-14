class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]
        for token in tokens:
            if token in operators:
                operand_1 = stack.pop()
                operand_2 = stack.pop()
                result = 0
                match token:
                    case "+":
                        result = operand_2 + operand_1
                    case "-":
                        result = operand_2 - operand_1
                    case "*":
                        result = operand_2 * operand_1
                    case "/":
                        result = int(operand_2 / operand_1)
                stack.append(result)
            else:
                stack.append(int(token))
        return stack.pop()