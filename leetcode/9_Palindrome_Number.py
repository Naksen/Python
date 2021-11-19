class Solution:
    def isPalindrome(self, x):
        if x < 0:
            return False
        if x == 0:
            return True
        else:
            s = str(x)
            arr = list(s)
            # print(mid)
            if len(s) % 2 != 0:
                mid = len(s) // 2
                for i in range(0, mid):
                    # print(i)
                    if arr[mid - 1 - i] != arr[mid + 1 + i]:
                        return False
                return True
            else:
                mid = len(s) // 2
                for i in range(0, mid):
                    if arr[i] != arr[len(s) - i - 1]:
                        return False
                return True


if __name__ == '__main__':
    x = 121
    s = Solution()
    print(s.isPalindrome(x))
