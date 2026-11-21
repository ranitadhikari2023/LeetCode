from typing import List

class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)

        # Original tree children
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)

        new_parent = parent[:]
        last = [-1] * 26

        # Iterative DFS on original tree
        # stack item: (node, state, saved_last)
        # state 0 = enter, state 1 = exit
        stack = [(0, 0, -1)]

        while stack:
            u, state, saved = stack.pop()
            c = ord(s[u]) - ord('a')

            if state == 0:
                saved = last[c]

                if u != 0:
                    if saved != -1:
                        new_parent[u] = saved
                    else:
                        new_parent[u] = parent[u]

                last[c] = u

                stack.append((u, 1, saved))

                for v in reversed(children[u]):
                    stack.append((v, 0, -1))

            else:
                last[c] = saved

        # Build final tree
        new_children = [[] for _ in range(n)]
        for v in range(1, n):
            new_children[new_parent[v]].append(v)

        # Postorder traversal of final tree
        order = []
        stack = [0]

        while stack:
            u = stack.pop()
            order.append(u)

            for v in new_children[u]:
                stack.append(v)

        size = [1] * n

        for u in reversed(order):
            p = new_parent[u]
            if p != -1:
                size[p] += size[u]

        return size