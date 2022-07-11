"""
Question:
A robot moves in a plane starting from the original point (0,0). The robot can move toward UP, DOWN, LEFT and RIGHT with a given steps. 
The trace of robot movement is shown as the following:
UP 5
DOWN 3
LEFT 3
RIGHT 2

The numbers after the direction are steps. Please write a program to compute the distance from current position after 
a sequence of movement and original point. If the distance is a float, then just print the nearest integer.

Example:
If the following tuples are given as input to the program:
UP 5
DOWN 3
LEFT 3
RIGHT 2
Then, the output of the program should be: 2

"""

from math import sqrt


def get_movement() -> list[tuple[str]]:
    # Get values (as tuples) from user and make list
    moves = []
    while True:
        move = tuple(map(str,input("Give direction and steps separated with space: ").split()))
        if move:
            moves.append(move)
        else:
            break
    
    return moves


def formatter(moves:list[tuple[str]]) -> list[tuple[str, int]]:
    # Format moves to uppercase and int
    formatted_moves = []
    for move in moves:
        move_dir = move[0].upper()
        move_dist = int(move[1])
        formatted_moves.append((move_dir,move_dist))
    
    return formatted_moves


def robot(moves:list[tuple[str,int]]) -> tuple[int,int]:
    # Move robot from origin and return end position as tuple (x,y)
    x_coord = 0
    y_coord = 0
    for move in moves:
        if move[0] == 'UP':
            y_coord += move[1]
        if move[0] == 'DOWN':
            y_coord -= move[1]
        if move[0] == 'LEFT':
            x_coord -= move[1]
        if move[0] == 'RIGHT':
            x_coord += move[1]

    position = (x_coord, y_coord)
    return position


def calc_dist(position:tuple[int,int]) -> None:
    x = position[0]
    y = position[1]
    distance = int(sqrt(x**2 + y**2))
    print(f'Distance to origin: {distance}')

    
def main():
    #moves = [('UP', '5'), ('DOWN', '3'), ('LEFT', '3'), ('right', '2')]
    moves = get_movement()
    formatted_moves = formatter(moves)
    end_pos = robot(formatted_moves)
    calc_dist(end_pos)


if __name__ == '__main__':
    main()