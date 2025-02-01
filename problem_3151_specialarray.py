class Solution(object):
    def isArraySpecial(self, nums):
        value=True
        for i in range(len(nums)-1):
            if nums[i]%2==0:
                if nums[i+1]%2==0:
                     value=False
                     break
            else:
                if nums[i+1]%2!=0:
                    value=False
                    bre
