class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        last_number = None
        for i in range(len(numbers)):
            is_true = False
            end_index = None
            if last_number == numbers[i]:
                continue
            for j in range(i + 1, len(numbers)):
                if target == (numbers[i] + numbers[j]):
                    end_index = j + 1
                    is_true = True
                    break

                if target < (numbers[i] + numbers[j]):
                    break

            if is_true:
                return [i + 1, end_index]

            last_number = numbers[i]


solve = Solution()
print(solve.twoSum([-1,0], -1))