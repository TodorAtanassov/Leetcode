nums, target = input()
class Solution:
    def twoSum(a, b ,target):
        for i in nums:
            for j in nums:
                if i + j == target:
                    return [nums.index(i), nums.index(j)]
