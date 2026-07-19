#LC 1:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h_map = {}
        for j, num in enumerate(nums):
            diff = target - num
            if diff in h_map:
                return [h_map[diff], j]
            h_map[num] = j

