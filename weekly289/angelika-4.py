from typing import List

def traverse(node, children, label, optimal):
    if node is None or not node in label:
        return (1, None)
    if not node in children or len(children[node]) < 1:
        return (1, label[node])
    diff = list(reversed(sorted(filter(lambda result: result[1] != label[node], [traverse(child, children, label, optimal) for child in children[node]]))))
    if len(diff) > 1:
        optimal['path'] = max(optimal['path'], diff[0][0] + diff[1][0] + 1)

    if len(diff) > 0:
        optimal['path'] = max(optimal['path'], diff[0][0] + 1)
        return (diff[0][0] + 1, label[node])
    else:
        return (1, label[node])

def longestPath(parent: List[int], s: str) -> int:
    children = dict()
    label = dict()
    root = None
    for node in range(len(parent)):
        label[node] = s[node]
        pa = parent[node]
        if pa > -1 and pa in children:
            children[pa].append(node)
        elif pa > -1 and not pa in children:
            children[pa] = [node]
        elif pa == -1:
            root = node

    optimal = {'path': 1}
    path, label = traverse(root, children, label, optimal)
    return optimal['path']

print(longestPath([-1,0,0,1,1,2], "abacbe"))
print(longestPath([-1,0,0,1,1,2], "ebacbe"))
print(longestPath([-1,0,0,0], "aabc"))
print(longestPath([-1,0], "aa"))