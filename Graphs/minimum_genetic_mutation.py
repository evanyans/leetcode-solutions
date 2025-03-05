class Solution:
    # Attempted 3/4/2025
    # AHA: i used startNode[i] instead of node[i] in neighbors function and it broke, dumb mistake
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        dna_to_num = {
            'A': 0,
            'C': 1,
            'G': 2,
            'T': 3
        }
        num_to_dna = ['A', 'C', 'G', 'T']
        def neighbors(node):
            ans = []
            for i in range(8):
                num = dna_to_num[node[i]]
                for change in [1, 2, 3]:
                    x = (num + change) % 4
                    ans.append(node[:i] + num_to_dna[x] + node[i + 1:])
            return ans

        queue = deque([(startGene, 0)])
        seen = set()
        valid = set(bank)
        seen.add(startGene)
        while queue:
            node, steps = queue.popleft()
            if node == endGene:
                return steps
            for neighbor in neighbors(node):
                if neighbor not in seen and neighbor in valid:
                    seen.add(neighbor)
                    queue.append((neighbor, steps + 1))

        return -1
