class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_set = {}
        array = set()
        for num in nums:
            hash_set[num]= hash_set.get(num,0)+1
        
        for i in range(0,k):
            max=1
            max_num=nums[0]
            for num in nums:
                if hash_set[num] >= max:
                    max=hash_set[num]
                    max_num=num
            array.add(max_num)
            hash_set[max_num]=0
        
        return list(array)

