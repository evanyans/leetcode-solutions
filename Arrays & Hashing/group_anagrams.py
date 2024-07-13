class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            standard_s = ''.join(sorted(s))
            if standard_s in anagrams:
                anagrams[standard_s].append(s)
            else:
                anagrams[standard_s] = [s]

        return anagrams.values()
