class Solution:
    def countCollisions(self, directions: str) -> int:
        mapping = dict({'S': 0, 'R': 1, 'L': -1})
        res = 0
        dirs = [ch for ch in directions]
        
        for loc in range(0, len(dirs) - 1):
            val = mapping[dirs[loc]] - mapping[dirs[loc + 1]]
            if val > 0:
                res += val
                dirs[loc] = 'S'
                dirs[loc + 1] = 'S'
                
        for loc in range(len(dirs) - 2, -1, -1):
            val = mapping[dirs[loc]] - mapping[dirs[loc + 1]]
            if val > 0:
                res += val
                dirs[loc] = 'S'
                dirs[loc + 1] = 'S'
                
        return res