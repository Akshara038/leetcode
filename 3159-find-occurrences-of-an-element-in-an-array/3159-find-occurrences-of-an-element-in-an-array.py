class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:

        positions = []

        for i in range(len(nums)):
            if nums[i] == x:
                positions.append(i)

        result = []

        for q in queries:
            if q <= len(positions):
                result.append(positions[q - 1])
            else:
                result.append(-1)

        return result