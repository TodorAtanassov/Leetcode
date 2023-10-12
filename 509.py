class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n <= 2:
            return 1
        return self.fib(n - 1) + self.fib(n - 2)


# s = [1, 66, 2, 4, 12, 23, 7, 13, 9, 10]
# for i in range(len(s) - 1):
#     for j in range(len(s) - 1 - i):
#         if s[j] > s[j + 1]:
#             s[j], s[j + 1] = s[j + 1], s[j]
# print(s)
