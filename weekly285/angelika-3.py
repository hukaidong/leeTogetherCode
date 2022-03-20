class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        solution = [0 for idx in range(12)]
        maxScore = 0
        for mask in range(1, 1 << 12):
            score = sum([idx if (1 << idx) & mask else 0 for idx in range(12)])
            arrows = [aliceArrows[idx] + 1 if (1 << idx) & mask else 0 for idx in range(12)]
            if score > maxScore and sum(arrows) <= numArrows:
                solution = arrows
                maxScore = score
                
        solution[0] += numArrows - sum(solution)
        return solution