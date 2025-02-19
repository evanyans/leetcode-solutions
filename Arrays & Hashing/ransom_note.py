class Solution:
    #Attempted 2/19/2025
    # AHA: really easy, just read the question.
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_dict = defaultdict(int)
        for c in magazine:
            mag_dict[c] += 1
        
        for c in ransomNote:
            if c in mag_dict:
                mag_dict[c] -= 1
            if c not in mag_dict or mag_dict[c] < 0:
                return False
        print(mag_dict)
        return True
            
