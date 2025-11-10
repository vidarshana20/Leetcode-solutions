class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')   # smallest number so far
        second = float('inf')  # second smallest number so far

        for n in nums:
            if n <= first:
                first = n        # new smallest number
            elif n <= second:
                second = n       # new second smallest
            else:
                # n > first and n > second → triplet found
                return True

        return False
