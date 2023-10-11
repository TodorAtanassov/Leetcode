# def f(a):
#     if a <= 0:
#         return 0
#     return a + f(a-1)
#
# print(f(4))

# import calendar
# y = 2023
# m = 11
# print(calendar.month(y,m))


# w1 = 'codewars'
# w2 = 'hackerrank'
# a = 0
# for i in w1:
#     if i not in w2:
#         a += 1
# for j in w2:
#     if j not in w1:
#         a += 1
#
# print(a)


# def f(a):
#     if a <= 0:
#         return 0
#     return a + f(a-1)
#
# print(f(4))


# from string import ascii_lowercase
#
# for i in ascii_lowercase:
#     for j in ascii_lowercase:
#         for k in ascii_lowercase:
#             for l in ascii_lowercase:
#                 print(i, j, k, l)


# for i in range(10):
#     for j in range(10):
#         for k in range(10):
#             for l in range(10):
#                 print(i, j, k, l)
# import sys
#
# prices = [7, 1, 5, 3, 6, 4]
#
# for idx, price in enumerate(prices):
#     if price < prices[idx - 1]:
#         starting_price = price
#         break
#     for i in prices[idx,len(prices-1)]:
#         print(i)

# print(starting_price)

n1 = [1, 2, 3, 1, 1, 3, 4, 6, 12]

# def numIdenticalPairs(nums):
#     count = 0
#     for idx1, i in enumerate(nums):
#         for j in nums[idx1::]:
#             if i == j:
#                 count += 1
#     return count
#
#
# print((numIdenticalPairs(n1)))

# for idx1,i in enumerate(n1):
#     for j in n1[idx1::]:
#         print(j,end=' ')
#     print()

print([i for i in n1 if not i % 2])
