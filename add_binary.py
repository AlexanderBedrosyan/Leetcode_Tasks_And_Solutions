# Given two binary strings a and b, return their sum as a binary string.

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ""
        carry = 0
        i = len(a) - 1
        j = len(b) - 1

        while i >= 0 or j >= 0:
            sum_bits = carry

            if i >= 0:
                sum_bits += int(a[i])
                i -= 1

            if j >= 0:
                sum_bits += int(b[j])
                j -= 1

            result = str(sum_bits % 2) + result
            carry = sum_bits // 2

        if carry > 0:
            result = str(carry) + result

        return result
