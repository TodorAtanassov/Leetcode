# in [-1,0,1,2,-1,-4]
# out [[-1,-1,2],[-1,0,1]]

n = input()


def three_sum(list):
    for i, a in enumerate(list):
        for j, b in enumerate(list):
            for k, c in enumerate(list):
                if a != b != c and a + b + c == 0:
                    return i, j, k


print(three_sum(n))
# target = 0
# for i in range(len(nums)):
#    for j in range(len(nums)):
#           if i != j != k and i + j + k == target:
#               print(i, j, k)


# n = [1, 2, 3, 4, 5]


# def mult_arr(a):
#    b = 1
#   for i in a:
#      b *= i
# print(b)


# mult_arr(n)
