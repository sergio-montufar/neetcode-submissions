class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            match token:
                case "+":
                    stack.append(stack.pop() + stack.pop())
                case "-":
                    oper_1, oper_2 = stack.pop(), stack.pop()
                    stack.append(oper_2 - oper_1)
                case "*":
                    stack.append(stack.pop() * stack.pop())
                case "/":
                    oper_1, oper_2 = stack.pop(), stack.pop()
                    stack.append(int(oper_2 / oper_1))
                case _:
                    stack.append(int(token))
            
        return stack.pop()