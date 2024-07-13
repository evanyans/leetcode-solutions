class Solution:
    def rob(self, nums: List[int]) -> int:
        max_accum = {}
        def rob_solver(max_accum, nums, index):
            if index == 0:
                return nums[0]
            if index == 1:
                return max(nums[0], nums[1])
            if index in max_accum:
                return max_accum[index]
                
            max_accum[index] = max(rob_solver(max_accum, nums, index - 2) + nums[index], rob_solver(max_accum, nums, index - 1))
            return max_accum[index]
        return rob_solver(max_accum, nums, len(nums) - 1)
    

