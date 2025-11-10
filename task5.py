import heapq

GOAL = [[1,2,3],[4,5,6],[7,8,0]]

def flatten(state):
    return tuple(num for row in state for num in row)

def manhattan(state):
    dist = 0
    for i in range(3):
        for j in range(3):
            val = state[i][j]
            if val != 0:
                target_x = (val - 1) // 3
                target_y = (val - 1) % 3
                dist += abs(i - target_x) + abs(j - target_y)
    return dist

def get_blank_pos(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def neighbors(state):
    x, y = get_blank_pos(state)
    moves = [(-1,0),(1,0),(0,-1),(0,1)]
    results = []
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            results.append(new_state)
    return results

def solve(start):
    queue = []
    start_h = manhattan(start)
    heapq.heappush(queue, (start_h, 0, start, []))
    visited = set()

    while queue:
        est, cost, state, path = heapq.heappop(queue)
        flat = flatten(state)
        if flat in visited:
            continue
        visited.add(flat)

        if state == GOAL:
            return path + [state]

        for neighbor in neighbors(state):
            nflat = flatten(neighbor)
            if nflat not in visited:
                heapq.heappush(queue, (cost + 1 + manhattan(neighbor), cost + 1, neighbor, path + [state]))
    return None

if __name__ == "__main__":
    start_state = [[1,2,3],[4,0,6],[7,5,8]]
    result = solve(start_state)
    if result:
        for i, step in enumerate(result):
            print(f"Step {i}:")
            for row in step:
                print(row)
            print("---")
    else:
        print("No solution found.")
