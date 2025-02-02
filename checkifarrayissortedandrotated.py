class Solution(object):
    def check(self, nums):
        nums1=nums
        nums2=sorted(nums)
        a=nums[0]
        b=nums[-1]
        def leftrotate(nums1,a):        
            for i in range(len(nums1)):
                if i==len(nums1)-1:
                    nums1[i]=a
                else:
                    nums1[i]=nums1[i+1]
            return nums1  


        def rightrotate(nums1,b):
            for i in range(len(nums1)-1,-1,-1):
                if i==0:
                    nums1[i]=b
                else:
                    nums1[i]=nums1[i-1]
            return nums1

        for i in range(len(nums)):
            nums1=rightrotate(nums1,b)
            b=nums1[-1]
            if nums1==nums2:
                        return True 

        nums1=nums  

        for i in range(len(nums)):
            nums1=leftrotate(nums1,a)
            a=nums1[0]
            if nums1==nums2:
                        return True 
        return False                          
