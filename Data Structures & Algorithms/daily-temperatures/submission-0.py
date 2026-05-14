class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            # print(stack, result, i)
            while stack and temp > stack[-1][0]:
                stackTemp, stackIndex = stack.pop()
                result[stackIndex] = i - stackIndex
                print(result, i, stackIndex)
            stack.append((temp, i))
            # print(stack, result, i)

        return result