class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for string in strs:
            anagram = ''.join(sorted(string))
            if anagram in hashmap:
                hashmap[anagram].append(string)
            else:
                hashmap[anagram] = [string]
        return hashmap.values()
