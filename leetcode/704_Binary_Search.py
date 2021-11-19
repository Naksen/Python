class Solution:
    def sub_search(self, nums, target, left, right):
        if right < left:
            return -1
        mid = (right + left) // 2
        if target == nums[mid]:
            return mid
        elif target > nums[mid]:
            return self.sub_search(nums, target, mid + 1, right)
        elif target < nums[mid]:
            return self.sub_search(nums, target, left, mid - 1)

    def search(self, nums, target):
        left = 0
        right = len(nums) - 1
        pos = self.sub_search(nums, target, left, right)
        return pos


if __name__ == '__main__':
    nums = [-1, 0, 2, 3, 5, 9, 12]
    target = 2
    s = Solution()
    print(s.search(nums, target))
