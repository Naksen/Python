class Solution:
    def moveZeroes(self, nums):
        j = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1
        while j < len(nums) - 1:
            nums[j] = 0
            j += 1

if __name__ == '__main__':
    t = Solution()
    nums = [0, 1, 0, 3, 12]
    t.moveZeroes(nums)