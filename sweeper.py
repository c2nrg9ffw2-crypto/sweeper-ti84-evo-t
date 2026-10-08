# Minesweeper for the TI-84 Evo
# Keys: arrows = move, enter = open, 2nd or mode = flag, clear = quit
import random
from ti_draw import clear, set_color, draw_text
from ti_draw import fill_rect as ti_fill_rect
try:
    from ti_draw import get_screen_dim
    SW, SH = get_screen_dim()
except:
    SW, SH = 320, 240

# Keep every box inside the screen and never stop the game over one box
# (the Evo gave "Height cannot be negative" for a box near the edge).
# The Evo draws boxes 1 pixel too small, so we ask for 1 pixel more.
def fill_rect(x, y, w, h):
    if x < 0:
        w, x = w + x, 0
    if y < 0:
        h, y = h + y, 0
    w, h = min(w, SW - x), min(h, SH - y)
    if w > 0 and h > 0:
        try:
            ti_fill_rect(x, y, w + 1, h + 1)
        except:
            pass
# Draw in a hidden buffer and show the finished picture at once: no flicker
try:
    from ti_draw import use_buffer, paint_buffer
    use_buffer()
except:
    paint_buffer = None
try:
    from ti_system import get_key as read_key
except:
    from ti_system import getKey as read_key
# On the Evo get_key wants one number. Find out once at the start.
try:
    read_key()
    key = read_key
except TypeError:
    def key():
        return read_key(0)
try:
    from ti_system import store_list, recall_list
except:
    store_list = recall_list = None
try:
    from time import sleep
except:
    from ti_system import sleep

# Key numbers (the Evo uses the second number in each pair)
LEFT = (2, 24)
RIGHT = (1, 26)
UP = (3, 25)
DOWN = (4, 34)
OPEN = (5, 105)               # enter
FLAG = (21, 22)               # 2nd, mode
QUIT = (9, 45)                # clear

GW, GH, MINES = 12, 8, 17     # board size and number of mines
C = 20                        # cell size in pixels
TOP = 34                      # height of the top bar
X0 = (SW - GW * C) // 2
Y0 = TOP + (SH - TOP - GH * C) // 2
NUM_COLORS = [(0, 0, 0), (0, 0, 230), (0, 140, 0), (220, 0, 0),
              (0, 0, 120), (130, 0, 0), (0, 130, 130), (0, 0, 0),
              (100, 100, 100)]

mine = bytearray(GW * GH)     # 1 = mine
near = bytearray(GW * GH)     # number of mines around
opened = bytearray(GW * GH)
flag = bytearray(GW * GH)

def paint():
    if paint_buffer:
        paint_buffer()

# Wipe the whole bar (tall letters leave nothing behind), then write
def bar(s):
    set_color(0, 0, 0)
    fill_rect(0, 0, SW, TOP - 2)
    set_color(255, 255, 255)
    draw_text(4, 22, s)

def wait_for(keys):
    paint()
    while True:
        k = key()
        if k in keys:
            return k
        sleep(0.05)

# Wins and games live in the calculator list MINES, so they stay after quitting
def load_stats():
    try:
        l = recall_list("MINES")
        return int(l[0]), int(l[1])
    except:
        return 0, 0

def save_stats(wins, games):
    try:
        store_list("MINES", [wins, games])
    except:
        pass

def neighbours(x, y):
    out = []
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            nx, ny = x + dx, y + dy
            if (dx or dy) and 0 <= nx < GW and 0 <= ny < GH:
                out.append((nx, ny))
    return out

# Place mines after the first open, never on or next to that square
def place_mines(sx, sy):
    safe = neighbours(sx, sy) + [(sx, sy)]
    n = 0
    while n < MINES:
        x, y = random.randrange(GW), random.randrange(GH)
        if not mine[y * GW + x] and (x, y) not in safe:
            mine[y * GW + x] = 1
            n += 1
    for y in range(GH):
        for x in range(GW):
            near[y * GW + x] = sum(mine[b * GW + a] for a, b in neighbours(x, y))

# Digits 1-8 as 3 x 5 block pictures ("#" = block). We draw them ourselves,
# because draw_text on the Evo puts text too high: it spilled into the square above.
DIGITS = {1: [".#.", "##.", ".#.", ".#.", "###"],
          2: ["##.", "..#", ".#.", "#..", "###"],
          3: ["##.", "..#", ".#.", "..#", "##."],
          4: ["#.#", "#.#", "###", "..#", "..#"],
          5: ["###", "#..", "##.", "..#", "##."],
          6: [".##", "#..", "###", "#.#", "###"],
          7: ["###", "..#", ".#.", ".#.", ".#."],
          8: ["###", "#.#", "###", "#.#", "###"]}
P = 3                         # size of one block in pixels

def draw_digit(n, x, y):
    for r in range(5):
        row = DIGITS[n][r]
        c = 0
        while c < 3:          # draw each run of blocks as one box
            if row[c] == "#":
                e = c
                while e < 3 and row[e] == "#":
                    e += 1
                fill_rect(x + c * P, y + r * P, (e - c) * P, P)
                c = e
            else:
                c += 1

def draw_cell(x, y, cursor=False):
    i = y * GW + x
    px, py = X0 + x * C, Y0 + y * C
    if opened[i]:
        set_color(*((230, 0, 0) if mine[i] else (210, 210, 210)))
        fill_rect(px, py, C - 1, C - 1)
        if mine[i]:
            set_color(0, 0, 0)
            fill_rect(px + 5, py + 5, C - 11, C - 11)
        elif near[i]:
            set_color(*NUM_COLORS[near[i]])
            draw_digit(near[i], px + 5, py + 2)
    else:
        set_color(110, 110, 110)
        fill_rect(px, py, C - 1, C - 1)
        if flag[i]:
            set_color(230, 0, 0)
            fill_rect(px + 6, py + 4, 7, 6)        # flag
            set_color(0, 0, 0)
            fill_rect(px + 6, py + 4, 2, 12)       # pole
    if cursor:                                     # thick yellow frame
        set_color(255, 220, 0)
        fill_rect(px, py, C - 1, 4)
        fill_rect(px, py + C - 5, C - 1, 4)
        fill_rect(px, py, 4, C - 1)
        fill_rect(px + C - 5, py, 4, C - 1)

# Open a square. Empty squares (0 mines around) open their neighbours too.
def open_at(x, y):
    todo = [(x, y)]
    count = 0
    while todo:
        x, y = todo.pop()
        i = y * GW + x
        if opened[i] or flag[i]:
            continue
        opened[i] = 1
        count += 1
        draw_cell(x, y)
        if not mine[i] and near[i] == 0:
            todo += neighbours(x, y)
    return count

def show_bar(flags, wins, games):
    bar("Flags " + str(flags) + "/" + str(MINES) + "   Wins " + str(wins) + "/" + str(games))

def start_screen(wins, games):
    clear()
    set_color(0, 0, 0)
    fill_rect(0, 0, SW, SH)
    x = SW // 2 - 80
    set_color(230, 0, 0)
    draw_text(x + 20, 20, "MINESWEEPER")
    set_color(255, 255, 255)
    draw_text(x, 45, "Wins " + str(wins) + " of " + str(games))
    help = ["ARROWS: move", "ENTER: open", "2ND: flag a mine",
            "Numbers = mines", "around that square", "CLEAR: quit"]
    for i in range(len(help)):
        draw_text(x, 72 + i * 20, help[i])
    set_color(230, 200, 0)
    draw_text(x, 195, "ENTER: start")
    return wait_for(OPEN + QUIT) in OPEN

# Returns "win", "lose" or "quit"
def game(wins, games):
    for i in range(GW * GH):
        mine[i] = near[i] = opened[i] = flag[i] = 0
    clear()
    set_color(0, 0, 0)
    fill_rect(0, 0, SW, SH)
    for y in range(GH):
        for x in range(GW):
            draw_cell(x, y)
    cx, cy = GW // 2, GH // 2
    draw_cell(cx, cy, True)
    flags, left, first = 0, GW * GH - MINES, True
    show_bar(flags, wins, games)
    paint()
    while True:
        k = key()
        if not k:
            sleep(0.03)
            continue
        if k in QUIT:
            return "quit"
        ox, oy = cx, cy
        if k in LEFT:
            cx = max(0, cx - 1)
        elif k in RIGHT:
            cx = min(GW - 1, cx + 1)
        elif k in UP:
            cy = max(0, cy - 1)
        elif k in DOWN:
            cy = min(GH - 1, cy + 1)
        elif k in FLAG:
            i = cy * GW + cx
            if not opened[i]:
                flag[i] = 1 - flag[i]
                flags += 1 if flag[i] else -1
                show_bar(flags, wins, games)
        elif k in OPEN:
            i = cy * GW + cx
            if not flag[i] and not opened[i]:
                if first:
                    place_mines(cx, cy)
                    first = False
                if mine[i]:
                    for j in range(GW * GH):       # show all mines
                        if mine[j]:
                            opened[j] = 1
                            draw_cell(j % GW, j // GW)
                    return "lose"
                left -= open_at(cx, cy)
                if left == 0:
                    return "win"
        draw_cell(ox, oy)
        draw_cell(cx, cy, True)
        paint()

# --- start ---
wins, games = load_stats()
if start_screen(wins, games):
    while True:
        result = game(wins, games)
        if result == "quit":
            break
        games += 1
        if result == "win":
            wins += 1
        save_stats(wins, games)
        bar(("YOU WIN!" if result == "win" else "BOOM!") + "  ENTER: again")
        if wait_for(OPEN + QUIT) in QUIT:
            break
paint()
