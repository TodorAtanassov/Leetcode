class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for idx1, i in enumerate(nums):
            for idx2, j in enumerate(nums):
                if i + j == target and idx2 != idx1:
                    return idx1, idx2
