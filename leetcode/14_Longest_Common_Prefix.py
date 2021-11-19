class Solution:
    def longestCommonPrefix(self, strs):
        ans = ""
        check = 0
        pos = 0
        for i in range(len(strs[0])):
            if pos != i:
                break
            for j in range(1, len(strs)):
                if i < len(strs[j]):
                    if strs[0][i] == strs[j][i]:
                        check += 1
            if check == len(strs) - 1:
                ans += strs[0][i]
                check = 0
                pos += 1
        return ans


if __name__ == '__main__':
    strs = ["flower", "flow", "flight"]
    s = Solution()
    print(s.longestCommonPrefix(strs))
