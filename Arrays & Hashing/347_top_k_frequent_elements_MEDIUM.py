class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # - nums in UNSORTED
        # - we can return in any order
        # - we return an array containing the k most frequent elements
        # - assume unique solution

        count_occ = {}
        frequency = [[] for i in range(len(nums) + 1)] # + 1 accounts for 0 occurences

        for n in nums:
            count_occ[n] = 1 + count_occ.get(n, 0)
        for n, c in count_occ.items():
            frequency[c].append(n)
        output = []
        for i in range(len(frequency) - 1, 0, -1):
            for num in frequency[i]:
                output.append(num)
                if (len(output) == k):
                    return output
        



        

            
        


