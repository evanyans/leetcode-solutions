class Solution:
    # Attempted 2nd time at 2/9/2025
    # aha: i forgot to check max, this is a basic sliding window format
    def lengthOfLongestSubstring(self, s: str) -> int:
        # my logic, whenever we hit a repeated character, progress p1 up by 1
        # - when we progress p1 up by 1, deduct 1 it from current length
        # - remove p1 from the set
        # - continue
        # - repeat until we reach the end and we should have the largest.
        my_set = set()
        my_max = 0
        cur_len = 0
        p1 = 0
        p2 = 0
        while p1 < len(s) and p2 < len(s):
            if s[p2] in my_set:
                my_max = max(my_max, cur_len)
                my_set.remove(s[p1])
                p1 += 1
                cur_len = cur_len - 1
                continue
            my_set.add(s[p2])
            cur_len += 1
            p2 += 1
            my_max = max(my_max, cur_len)
        return my_max


# old attempt from summer 2024
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
                
