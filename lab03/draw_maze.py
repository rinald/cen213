symbols = ['##', '  ', ' D', ' K']


def draw_maze(maze):
    n = len(maze)
    m = len(maze[0])

    for i in range(n):
        for j in range(m):
            print(symbols[maze[i][j]], end='')  # print inline
        print()


if __name__ == '__main__':
    maze = \
        [[0, 0, 0, 1, 0],
         [0, 1, 1, 1, 2],
         [0, 1, 0, 0, 0],
         [0, 1, 3, 1, 0],
         [0, 0, 0, 0, 0]]

    draw_maze(maze)
