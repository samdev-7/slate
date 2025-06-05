# Install dependecies from local-requirements.txt

import pygame
import displayio
from blinka_displayio_pygamedisplay import PyGameDisplay
from adafruit_display_text import label
from adafruit_bitmap_font import bitmap_font
from adafruit_display_shapes.rect import Rect
from displayio import Bitmap

DISPLAY_WIDTH = 296
DISPLAY_HEIGHT = 128

BLACK = 0x000000
WHITE = 0xFFFFFF
RED = 0xFF0000

# Change text colors, choose from the following values:
# BLACK, RED, WHITE

BACKGROUND_COLOR = WHITE

display = PyGameDisplay(width=DISPLAY_WIDTH, height=DISPLAY_HEIGHT)

font = bitmap_font.load_font("IBMPlexSans-Regular-25.pcf", Bitmap)
font_bold = bitmap_font.load_font("IBMPlexSans-Medium-36.pcf", Bitmap)
font_small = bitmap_font.load_font("IBMPlexSans-Regular-18.pcf", Bitmap)
img = displayio.OnDiskBitmap("img.bmp")

# Create a display group for our screen objects
g = displayio.Group()

# Set a background
background_bitmap = displayio.Bitmap(DISPLAY_WIDTH, DISPLAY_HEIGHT, 1)
# Map colors in a palette
palette = displayio.Palette(1)
palette[0] = BACKGROUND_COLOR

# Create a Tilegrid with the background and put in the displayio group
t = displayio.TileGrid(background_bitmap, pixel_shader=palette)
g.append(t)

imgt = displayio.TileGrid(
    img,
    pixel_shader=img.pixel_shader,
    x=DISPLAY_WIDTH - img.width - 10,
    y=4,
)
g.append(imgt)
rect = Rect(
    x=DISPLAY_WIDTH - 10 - 22,
    y=4,
    width=22,
    height=22,
    fill=BACKGROUND_COLOR,
)
g.append(rect)

# Draw simple text using the built-in font into a displayio group
name_group = displayio.Group(scale=1, x=12, y=25)
first_name = label.Label(font_bold, text="Sam", color=RED, scale=1)
name_group.append(first_name)  # Add this text to the text group
last_name = label.Label(font, text="Liu", color=RED)
last_name.y = 30
name_group.append(last_name)  # Add this text to the text group
pronoun = label.Label(font_small, text="(he/him)", color=RED)
pronoun.y = 32
pronoun.x = 45
name_group.append(pronoun)  # Add this text to the text group
g.append(name_group)

desc_group = displayio.Group(scale=1, x=12, y=88)
desc = label.Label(font_small, text="I build things!", color=BLACK)
desc_group.append(desc)  # Add this text to the text group
desc2 = label.Label(font_small, text="https://samliu.dev", color=BLACK)
desc2.y = 20
desc_group.append(desc2)  # Add this text to the text group
g.append(desc_group)

# Place the display group on the screen
display.root_group = g

while True:
    if display.check_quit():
        break
