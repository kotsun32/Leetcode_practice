#1 on leetcode
#2sum
#O(n) solution
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ht ={} 
        for i,n in enumerate(nums):
            val = target - n
            if val in ht:
                return [ht[val],i]
            ht[n]=i
