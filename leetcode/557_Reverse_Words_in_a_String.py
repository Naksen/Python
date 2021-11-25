class Solution:
    def reverseString(self, s):
        buf_s = ''
        for i in s.split():
            i = i[::-1]
            buf_s = buf_s + i + ' '
        return buf_s[0:len(buf_s) - 1:1]

if __name__ == '__main__':
    s = "Let's take LeetCode contest"
    t = Solution()
    print(t.reverseString(s))
