from random import randint, choice


def choose_dir():
    return choice(['N', 'E', 'S', 'W'])


def get_new_location(row, col, dir):
    # North
    if dir == 'W':
        col -= 1
    elif dir == 'E':
        col += 1
    elif dir == 'S':
        row += 1
    elif dir == 'N':
        row -= 1
    return row, col


def valid_location(row, col, max_row):
    if row < 0 or col < 0:
        return False
    elif row > max_row-1:
        return False
    else:
        return True


def has_enough_rooms(map, n):
    # +2 to add end/start rooms
    count = sum(row.count('R') for row in map) + 2
    print("# of rooms: {}".format(count))
    if count >= n:
        return True
    else:
        return False


def generate_random_map(max_row=1, max_col=1, min_num_of_rooms=1):
    row = 0
    col = 0
    map = [['' for _ in range(max_col)] for _ in range(max_row)]

    while True:
        direction = choose_dir()
        temp_row, temp_col = get_new_location(row, col, direction)
        if valid_location(temp_row, temp_col, max_row):
            # Reached far end
            if col == max_col-1:
                map[row][col] = 'E'
                map[0][0] = 'S'
                if has_enough_rooms(map, min_num_of_rooms):
                    break
                else:
                    return generate_random_map(max_row, max_col, min_num_of_rooms)
            else:
                row, col = temp_row, temp_col
                map[row][col] = 'R'

        else:
            continue
    return map