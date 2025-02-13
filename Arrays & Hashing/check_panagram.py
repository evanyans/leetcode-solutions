class Solution:
    # Attempted 2/12/2025
    # AHA: set is pretty efficient here instead of marking seen.
    def checkIfPangram(self, sentence: str) -> bool:
        alph = list(map(chr, range(97, 123)))
        my_set = set(alph)
        for i in range(len(sentence)):
            if sentence[i] in my_set:
                my_set.remove(sentence[i])
        return len(my_set) == 0
        
