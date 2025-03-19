class Solution:
    # Attempted 3/18/2025
    # AHA: clever trick, discrimnant, window_len - max_freq is leftover characters
    # use max frequency, which determines the dominatn character in a subarray to not be flipped
    def characterReplacement(self, s: str, k: int) -> int:
        left = curr = ans = 0
        # since it is flip k characters, instead think of the problem
        # as, find max conseuctive subarray with at most k of those characters
        # because we can just flip those characters to get max conseuctive chars

        #I.E. max consecutive characters with at most k gap
        # how do know which character?
        freq = defaultdict(int)
        max_freq = 0
        window_len = 0
        for right in range(len(s)):
            # logic to update curr progress right
            freq[s[right]] += 1
            max_freq = max(max_freq, freq[s[right]])
            # current window size
            window_len  = right - left + 1

            #window len - max_freq represents the leftover characters
            while window_len - max_freq > k:
                freq[s[left]] -= 1
                left += 1
                window_len = right - left + 1
            ans = max(ans, window_len)

        return ans

