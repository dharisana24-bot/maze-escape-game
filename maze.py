# Maze Escape Game using BFS with Visualization
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from collections import deque

# Define the BFS function
def bfs_with_visualization(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    visited = [[False]*cols for _ in range(rows)]
    parent = {}
    queue = deque([start])
    visited[start[0]][start[1]] = True
    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    frames = []  # store exploration steps for animation

    while queue:
        current = queue.popleft()
        frames.append([row[:] for row in visited])  # snapshot

        if current == goal:
            break

        for d in directions:
            new_row, new_col = current[0] + d[0], current[1] + d[1]
            if (0 <= new_row < rows and 0 <= new_col < cols and 
                maze[new_row][new_col] == 0 and not visited[new_row][new_col]):
                queue.append((new_row, new_col))
                visited[new_row][new_col] = True
                parent[(new_row, new_col)] = current

    # Reconstruct shortest path
    path = []
    node = goal
    while node != start:
        path.append(node)
        node = parent.get(node)
        if node is None:
            print("No path found!")
            return frames, []
    path.append(start)
    path.reverse()
    return frames, path

# Draw the maze and animate BFS exploration
def visualize_bfs(maze, frames, path):
    fig, ax = plt.subplots()
    maze_display = [[1 if cell == 1 else 0 for cell in row] for row in maze]
    img = ax.imshow(maze_display, cmap='gray')

    def update(frame):
        display = [[1 if cell == 1 else 0 for cell in row] for row in maze]
        for r in range(len(frame)):
            for c in range(len(frame[0])):
                if frame[r][c]:
                    display[r][c] = 0.6  # explored area
        img.set_data(display)
        return [img]

    ani = animation.FuncAnimation(fig, update, frames=frames, repeat=False, interval=200)
    plt.title("BFS Maze Exploration")
    plt.show()

    # Show final path
    for r, c in path:
        maze_display[r][c] = 0.3
    plt.imshow(maze_display, cmap='gray')
    plt.title("Shortest Path Found by BFS")
    plt.show()

# Example Maze (0 = path, 1 = wall)
maze = [
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0]
]

start = (0, 0)
goal = (4, 4)

# Run BFS and visualize
frames, path = bfs_with_visualization(maze, start, goal)
print("Shortest Path:", path)
visualize_bfs(maze, frames, path)