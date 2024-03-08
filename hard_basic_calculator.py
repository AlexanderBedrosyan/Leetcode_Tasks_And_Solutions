# Given a string s representing a valid expression, implement a basic calculator to evaluate it, and return the result
# of the evaluation.
#
# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as
# eval().

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        def calc(operator, num1, num2):
            if operator == '-':
                return num1 - num2
            else:
                return num1 + num2

        statement = s.replace(' ', '')
        if len(statement) == 1:
            return int(statement)


        if '(' in statement:
            starting_index = []
            end_index = 0
            index = 0

            while '(' in statement:
                if statement[index] == '(':
                    starting_index.append(index)
                elif statement[index] == ')':
                    end_index = index
                    strt_index = starting_index.pop()
                    result = ''
                    second_number = ''
                    operator = None
                    for i in range(strt_index + 1, end_index):
                        if operator is not None:
                            second_number += statement[i]
                            if statement[i + 1].isdigit():
                                continue
                            if not result:
                                result = '0'
                            result = calc(operator, int(result), int(second_number))
                            second_number = ''
                            operator = None
                            continue
                        if statement[i].isdigit():
                            result += statement[i]
                            continue
                        operator = statement[i]

                    statement = statement[0:strt_index] + str(result) + statement[end_index + 1:]
                    index = strt_index
                    continue
                index += 1

        result = ''
        second_number = ''
        operator = None
        for i in range(len(statement)):
            if operator:
                second_number += statement[i]
                if i == len(statement) - 1:
                    if result == '':
                        result = '0'
                    result = calc(operator, int(result), int(second_number))
                    break
                if statement[i + 1].isdigit():
                    continue
                if result == '':
                    result = '0'
                result = calc(operator, int(result), int(second_number))
                operator = None
                second_number = ''
                continue
            if not statement[i].isdigit():
                operator = statement[i]
                continue
            result += statement[i]

        return int(result)



solve = Solution()
# print(solve.calculate("(1+(4+5+2)-3)+(6+8)"))
# print(solve.calculate("1 + 1"))
# print(solve.calculate(" 2-1 + 2 "))
print(solve.calculate('0'))
# print(solve.calculate('(1)'))
# print(solve.calculate("- (3 + (4 + 5))"))