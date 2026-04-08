class Solution:
    def reverse(self, x: int) -> int:
        num = ""
        for n in str(x)[::-1]:
            if n.isalnum():
                num += n
            else:
                num = n + num

        if -2**31 <= int(num) <= (2**31 - 1):
            return int(num)
        else:
            return 0
            