class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_set = set()
        l = 0
        cur_max = 0

        s_len = len(s)
        for i in range(s_len):
            while s[i] in my_set:
                my_set.remove(s[l])
                l += 1
            my_set.add(s[i])
            cur_max = max(cur_max, i - l + 1)


        return cur_max
                