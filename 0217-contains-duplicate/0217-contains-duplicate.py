class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        let = set(nums)
        return not (len(let) == len(nums))
        