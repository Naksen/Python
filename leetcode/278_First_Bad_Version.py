class Solution:
    def isBadVersion(self, x):
        if x >= 15:
            return True
        else:
            return False

    def sub_search(self, left, right):
        if left == right:
            return left
        mid = (left + right) // 2
        if self.isBadVersion(mid):
            return self.sub_search(left, mid)
        else:
            return self.sub_search(mid + 1, right)

    def firstBadVersion(self, n):
        ans = self.sub_search(0, n)
        return ans


if __name__ == '__main__':
    n = 25
    s = Solution()
    print(s.firstBadVersion(n))
