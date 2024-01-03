class Solution:
    def concatenatedBinary(self, n: int) -> int:
        MOD = 10**9 + 7
        result = 0

        for i in range(1, n + 1):
            binary_str = bin(i)[2:]
            result = (result << len(binary_str)) + i
            result %= MOD

        return result

solution = Solution()
n = 12
result = solution.concatenatedBinary(n)
print(result)