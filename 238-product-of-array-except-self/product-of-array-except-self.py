class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        zero_count = nums.count(0)

        # Case 1: more than one zero → all products are 0
        if zero_count > 1:
            return [0] * len(nums)

        # Case 2: exactly one zero
        if zero_count == 1:
            total = 1
            for n in nums:
                if n != 0:
                    total *= n
            return [total if n == 0 else 0 for n in nums]

        # Case 3: no zeros → safe to divide
        total = 1
        for n in nums:
            total *= n
        return [total // n for n in nums]


# import math
# class Solution:
#     def productExceptSelf(self, nums: List[int]) -> List[int]:
#         answer=[]
#         answer = [math.prod(nums[:i] + nums[i+1:]) for i in range(len(nums))]
#         return answer    

    