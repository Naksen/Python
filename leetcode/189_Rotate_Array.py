class Solution:
    def rotate(self, nums, k):
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]

if __name__ == '__main__':
    nums = [1, 2, 3]
    k = 2
    s = Solution()
    s.rotate(nums, k)
