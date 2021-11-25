class Solution:
    def sortedSquares(self, nums):
        sub = []
        ans = []
        left = 0
        right = len(nums) - 1
        while left <= right:
            #print(left,right)
            if nums[left]**2 < nums[right]**2:
                sub.append(nums[right]**2)
                right -= 1
            if nums[left]**2 >= nums[right]**2:
                sub.append(nums[left]**2)
                left += 1
        for i in range(len(sub) - 1, -1, -1):
            ans.append(sub[i])
        return ans


if __name__ == '__main__':
    nums = [-3,0,2]
    s = Solution()
    print(s.sortedSquares(nums))