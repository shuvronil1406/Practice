#LC 347

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            h_map = {}
            res = []
            for i in nums:
                count = 1
                if i not in h_map:
                    h_map.update({i:count})
                else:
                    h_map[i] +=1
            sorted_items = sorted(h_map.items(), key = lambda x: x[1], reverse = True)
            for i in range(k):
                res.append(sorted_items[i][0])
            return res
            