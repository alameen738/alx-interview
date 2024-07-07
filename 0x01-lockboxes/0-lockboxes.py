#!/usr/bin/env python3
def canUnlockAll(boxes):
    n = len(boxes)
    visited = [False] * n
    visited[0] = True  # The first box is unlocked by default

    queue = [0]  # Start with the first box
    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if 0 <= key < n and not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)
