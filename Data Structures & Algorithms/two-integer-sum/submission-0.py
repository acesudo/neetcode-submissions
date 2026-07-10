class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i ,n in enumerate(nums):
            k= target -n
            if k in d:
                return [d[k],i]
            d[n]=i    