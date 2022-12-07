# in [-1,0,1,2,-1,-4]
# out [[-1,-1,2],[-1,0,1]]

nums = input()


def three_sum(list):
    for i in range(len(list)):
        for j in range(len(list)):
            for k in range(len(list)):
                if i != j != k and i + j + k == 0:
                    return list[i, j, k]


print(three_sum(nums))
