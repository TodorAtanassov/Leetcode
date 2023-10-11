class Solution:
    def twosum(self, nums, target):
        for idx1, i in enumerate(nums):
            for idx2, j in enumerate(nums):
                if i + j == target and idx1 != idx2:
                    return [i, j]


###


class Solution:
    def twosum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            if target - num in seen:
                return [seen[target - num], i]
            else:
                seen[num] = i
