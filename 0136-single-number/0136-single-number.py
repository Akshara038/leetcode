class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        double = []

        for i in nums:
            if i in double:
                double.remove(i)
            else:
                double.append(i)

        return double[0]