
# GAME INFO
SIZE = (600, 600)
CAPTION = 'Tic Tac Toe RL'
MARGIN = 200
MARKER_MARGIN = 20
MARKER_SIZE = 160
LINE_MARGIN = (SIZE[0] - 2 * MARGIN)
LINE_WIDTH = 20
BOUNDARIES = [[[x * MARGIN, (x + 1) * MARGIN], [y * MARGIN, (y + 1) * MARGIN]]
              for y in range(3) for x in range(3)]

# IMAGE INFO
X_PATH = 'static/X.png'
O_PATH = 'static/O.png'

# COLORS
WHITE = (255, 255, 255)
GREEN = (124, 252, 0)
ANTIQUE_WHITE = (250, 235, 215)
PURPLE = (128, 0, 128)