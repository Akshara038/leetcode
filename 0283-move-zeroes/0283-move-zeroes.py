class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        zero=[]
        nonzero=[]
        for i in nums:
            if(i==0):
                zero.append(i)
            else:
                nonzero.append(i)
        nums[:]=nonzero+zero