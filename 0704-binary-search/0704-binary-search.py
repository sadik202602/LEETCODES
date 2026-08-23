class Solution:
    def search(self, nums: List[int], target: int) -> int:

        beginning_index = 0
        ending_index = len(nums) - 1
        
        while beginning_index <= ending_index:
            midpoint = beginning_index + (ending_index - beginning_index) // 2
            midpoint_value = nums[midpoint]
            
            if midpoint_value == target:
                return midpoint
            elif midpoint_value > target:
                ending_index = midpoint - 1
            else:
                beginning_index = midpoint + 1
        return -1