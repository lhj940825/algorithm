'''
 * User: Hojun Lim
 * Date: 2021-03-16
'''

def solution(numbers, target):
    from collections import deque
    que = deque()

    que.append(0)

    bfs_tree_depth = len(numbers)
    cur_bfs_tree_depth = 0
    i = 0

    while que and cur_bfs_tree_depth < bfs_tree_depth:

        for _ in range(len(que)):
            cur_node = que.popleft()
            que.append(cur_node + numbers[i])
            que.append(cur_node - numbers[i])
        i += 1
        cur_bfs_tree_depth += 1

    solution_cnt = 0
    for solution in que:
        if solution == target: solution_cnt += 1

    return solution_cnt