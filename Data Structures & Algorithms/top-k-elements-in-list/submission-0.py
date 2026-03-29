class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        arr = []

        for num, cnt in freq.items():
            arr.append([num, cnt])
        
        arr.sort(key=lambda x: x[1], reverse=True)

        res = []
        i = 0

        while len(res) < k:
            res.append(arr[i][0])
            i += 1
        
        return res