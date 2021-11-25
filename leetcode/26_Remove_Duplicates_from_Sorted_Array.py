class Solution:
    def removeDuplicates(self, nums):
        k = 0
        for i in range(len(nums)):
            if nums[i] != nums[k]:
                k += 1
                nums[k] = nums[i]
        #print(k + 1)
        #print(nums)
        return k + 1
if __name__ == '__main__':
    nums = [0,0,1,1,1,2,2,3,3,4]
    t = Solution()
    t.removeDuplicates(nums)
