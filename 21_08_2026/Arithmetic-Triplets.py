#LC 2367
#Solution:
class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        visited = set(nums)
        count = 0
        for i in nums:
            if i + diff in visited and i + 2* diff in visited:
                count += 1
        return count