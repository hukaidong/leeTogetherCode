def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
    res = []
    for query in queries:
        power = 10 ** ((intLength - 1) >> 1)
        order = query + power - 1
        if order >= 10 ** ((intLength + 1) >> 1):
            res.append(-1)
            continue
        part = order
        if intLength & 1 == 1:
            order //= 10
        while order > 0:
            part = part * 10 + order % 10
            order //= 10
        res.append(part)
    return res
