#
#

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l1 = []
        res = []
        for x in s:
            if x in l1:
                l1.pop()
            l1.append(x)



# if __name__ == '__main__':
#     s1 = "zaaasdasd"
#     # for x in s1:
#     #     print(x)
#     s1 = s1+"2"
#     print(s1)
