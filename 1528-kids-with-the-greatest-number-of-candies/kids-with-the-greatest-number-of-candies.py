class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        output=[]
        for i in range(0,len(candies)):
            if candies[i] + extraCandies >= max(candies[:i] + candies[i+1:]):
                output.append(True)
            else:
                output.append(False)             
        return output


        # max_candy = max(candies)
        # return [c + extraCandies >= max_candy for c in candies]       