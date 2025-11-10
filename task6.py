import heapq

class Node:
    def __init__(self, position, parent=None, g=0, h=0):
        self.position = position
        self.parent = parent
        self.g = g
        self.h = h
        self.f = g + h

    def __lt__(self, other):
        return self.f < other.f

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar(grid, start, goal):
    open_set = []
    heapq.heappush(open_set, Node(start, None, 0, heuristic(start, goal)))
    closed_set = set()
    open_positions = {start: 0}

    while open_set:
        current = heapq.heappop(open_set)

        if current.position == goal:
            path = []
            while current:
                path.append(current.position)
                current = current.parent
            return path[::-1]

        closed_set.add(current.position)

        x, y = current.position
        for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]) and grid[nx][ny] == 0:
                if (nx, ny) in closed_set:
                    continue
                g_cost = current.g + 1
                h_cost = heuristic((nx, ny), goal)
                neighbor = Node((nx, ny), current, g_cost, h_cost)
                # optional: avoid duplicates with worse g
                if open_positions.get((nx, ny), float('inf')) <= g_cost:
                    continue
                open_positions[(nx, ny)] = g_cost
                heapq.heappush(open_set, neighbor)

    return None

if __name__ == "__main__":
    grid = [
        [0,1,0,0,0],
        [0,1,0,1,0],
        [0,0,0,1,0],
        [0,1,1,0,0],
        [0,0,0,0,0]
    ]
    start = (0,0)
    goal = (4,4)
    path = astar(grid, start, goal)
    if path:
        print("Path found:")
        for p in path:
            print(p)
    else:
        print("No path found.")
