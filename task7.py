from collections import deque

def is_goal(state):
    return state[0] == 2 or state[1] == 2  # looking for 2 liters in either jug

def get_successors(state):
    successors = []
    a, b = state
    max_a, max_b = 4, 3

    # Fill A or B
    successors.append((max_a, b))
    successors.append((a, max_b))

    # Empty A or B
    successors.append((0, b))
    successors.append((a, 0))

    # Pour A -> B
    transfer = min(a, max_b - b)
    successors.append((a - transfer, b + transfer))

    # Pour B -> A
    transfer = min(b, max_a - a)
    successors.append((a + transfer, b - transfer))

    return successors

def bfs():
    start = (0, 0)
    queue = deque([(start, [])])
    visited = set()

    while queue:
        current, path = queue.popleft()
        if current in visited:
            continue
        visited.add(current)

        if is_goal(current):
            return path + [current]

        for next_state in get_successors(current):
            if next_state not in visited:
                queue.append((next_state, path + [current]))

    return None

if __name__ == "__main__":
    result = bfs()
    if result:
        for i, state in enumerate(result):
            print(f"Step {i}: Jug A: {state[0]}L, Jug B: {state[1]}L")
    else:
        print("No solution found.")
