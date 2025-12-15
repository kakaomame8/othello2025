from sakura import othello

# Generation ID: Hutch_1763374987242_4rxx7lpmh (前半)

def myai(board, color):
    size = len(board)
    opponent = 3 - color
    corners = [(0, 0), (0, size-1), (size-1, 0), (size-1, size-1)]
    adjacent_to_corners = set()

    for cr, cc in corners:
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                nr, nc = cr + dr, cc + dc
                if 0 <= nr < size and 0 <= nc < size and (nr, nc) not in corners:
                    adjacent_to_corners.add((nr, nc))

    def count_flips(row, col, color):
        if board[row][col] != 0:
            return 0

        flips = 0
        directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

        for dr, dc in directions:
            temp_flips = 0
            r, c = row + dr, col + dc

            while 0 <= r < size and 0 <= c < size and board[r][c] == opponent:
                temp_flips += 1
                r += dr
                c += dc

            if 0 <= r < size and 0 <= c < size and board[r][c] == color and temp_flips > 0:
                flips += temp_flips

        return flips

    valid_moves = []
    for r in range(size):
        for c in range(size):
            if board[r][c] == 0:
                flips = count_flips(r, c, color)
                if flips > 0:
                    valid_moves.append((c, r, flips))

    if not valid_moves:
        return None

    corner_moves = [m for m in valid_moves if (m[1], m[0]) in corners]
    if corner_moves:
        return (corner_moves[0][0], corner_moves[0][1])

    non_adjacent_moves = [m for m in valid_moves if (m[1], m[0]) not in adjacent_to_corners]
    non_adjacent_moves.sort(key=lambda x: x[2], reverse=True)

    if non_adjacent_moves:
        return (non_adjacent_moves[0][0], non_adjacent_moves[0][1])

    valid_moves.sort(key=lambda x: x[2], reverse=True)
    return (valid_moves[0][0], valid_moves[0][1])

# Generation ID: Hutch_1763374987242_4rxx7lpmh (後半)


othello.play(myai)
