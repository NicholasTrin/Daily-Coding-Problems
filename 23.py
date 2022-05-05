# You are given an M by N matrix consisting of booleans that represents a board. Each True boolean represents a wall.
# Each False boolean represents a tile you can walk on.
# Given this matrix, a start coordinate, and an end coordinate, return the minimum number of steps required to reach the end coordinate from the start.
# If there is no possible path, then return null. You can move up, left, down, and right. You cannot move through walls. You cannot wrap around the edges of the board.
f = False
t = True


def min_distance(map, start, end) -> int:
    open = [[start]]
    visited = set()
    while len(open):
        current_path = open.pop()
        evaluate_coordinate = current_path[-1]
        if is_goal(evaluate_coordinate, end):
            return len(current_path) - 1
        for move in get_valid_moves(map, evaluate_coordinate):
            if move not in visited:
                new_path = list(current_path)
                new_path.append(move)
                open.append(new_path)
                visited.add(move)
    return None


def is_goal(coordinate, end):
    if coordinate == end:
        return True
    else:
        return False


def get_valid_moves(map, coordinate):
    x, y = coordinate
    map_width, map_height = len(map[0]), len(map)
    north = (x, y - 1)
    south = (x, y + 1)
    west = (x - 1, y)
    east = (x + 1, y)
    cardinal_directions = [north, east, west, south]
    for move in list(cardinal_directions):
        x, y = move
        if -1 < x < map_width and -1 < y < map_height:
            if map[y][x]:
                cardinal_directions.remove(move)
        else:
            cardinal_directions.remove(move)
    return cardinal_directions


map = [[f, f, f, f],
       [t, t, f, t],
       [f, f, f, f],
       [f, f, f, f]]
start = (3, 0)
end = (0, 0)
print(min_distance(map, start, end))
