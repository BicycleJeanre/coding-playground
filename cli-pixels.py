import tkinter as tk

# --- STEP 1: Constants ---
# Define the window/canvas size in pixels.
WIDTH, HEIGHT = 800, 600

# --- STEP 2: Create the root window ---
# tk.Tk() is the main application window. Everything lives inside it.
# This does NOT show the window yet — that happens at mainloop().
print("Creating root window...")
root = tk.Tk()
root.title("Pixels")

# --- STEP 3: Create the canvas ---
# The Canvas is a drawable surface placed inside the root window.
# bg="black"           → starting background colour
# highlightthickness=0 → removes the default border/focus ring around the canvas
print("Creating canvas...")
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="black", highlightthickness=0)

# pack() tells tkinter's layout manager to place the canvas inside the window.
# Without this the canvas exists but is never shown.
canvas.pack()


# --- STEP 4: Define a helper to set individual pixels ---
# tkinter has no native single-pixel API, so we draw a 1×1 rectangle instead.
# x, y   → top-left corner of the "pixel"
# color  → any CSS-style colour string: "#RRGGBB", "red", "white", etc.
def set_pixel(x, y, color):
    # create_rectangle(x1, y1, x2, y2) draws a filled rectangle.
    # x+1, y+1 makes it exactly 1×1 px. outline=color removes the border gap.
    canvas.create_rectangle(x, y, x + 1, y + 1, fill=color, outline=color)


# --- STEP 5: Bulk-fill helper (optional but useful) ---
# Painting pixels one at a time is slow for large areas.
# For a solid rectangle, canvas.create_rectangle is much faster.
def fill_rect(x, y, w, h, color):
    canvas.create_rectangle(x, y, x + w, y + h, fill=color, outline=color)


# --- STEP 6: Draw some pixels before the window opens ---
# All drawing here happens in memory; the screen updates once mainloop starts.
print("Drawing pixels...")

# A single red pixel
set_pixel(100, 100, "#FF0000")

# A cluster of green pixels (small 5×5 block drawn pixel by pixel)
for dy in range(5):
    for dx in range(5):
        set_pixel(200 + dx, 150 + dy, "#00FF00")

# A blue filled rectangle (fast — one canvas object instead of W*H rectangles)
fill_rect(300, 200, 80, 40, "#0000FF")

# A white diagonal line
for i in range(100):
    set_pixel(400 + i, 100 + i, "#FFFFFF")

print("Done drawing. Opening window...")


# --- STEP 8: How to clear / redraw the screen ---
#
# Option A: canvas.delete("all")
#   Removes every object drawn on the canvas, leaving the bg colour.
#   Use this at the start of each frame before redrawing everything.
#
#       canvas.delete("all")
#       set_pixel(x, y, color)   # draw fresh frame
#
# Option B: root.after(delay_ms, callback)
#   Schedules a function to run after `delay_ms` milliseconds, inside
#   the event loop. This is the correct way to animate — never use
#   time.sleep() as it freezes the UI.
#
# The pattern for a game/animation loop:
#
#       frame = 0
#
#       def draw_frame():
#           global frame
#           canvas.delete("all")       # 1. clear previous frame
#           # ... draw new content ... # 2. draw new frame
#           frame += 1
#           root.after(16, draw_frame) # 3. schedule next frame (~60 fps)
#
#       draw_frame()   # kick off the loop (called once before mainloop)
#       root.mainloop()
#
# -----------------------------------------------------------------------
# Live example: an animated white dot bouncing left-right
# -----------------------------------------------------------------------

dot_x = 0
dot_dir = 4  # pixels per frame

def animate():
    global dot_x, dot_dir

    # 1. Clear the whole canvas (wipe previous frame)
    canvas.delete("all")

    # 2. Redraw — fill background manually if you need it opaque after delete
    #    (canvas bg colour stays, so black bg is already there)

    # 3. Draw the moving dot (5×5 white block for visibility)
    fill_rect(dot_x, HEIGHT // 2, 5, 5, "#FFFFFF")

    # 4. Update state for next frame
    dot_x += dot_dir
    if dot_x >= WIDTH - 5 or dot_x <= 0:
        dot_dir = -dot_dir  # reverse direction at edges

    # 5. Schedule this function to run again in ~16 ms (≈ 60 fps)
    #    root.after() queues the call inside the event loop safely.
    root.after(16, animate)


# Start the animation loop, then hand control to tkinter
animate()


# --- STEP 9: Start the event loop ---
# mainloop() renders everything and keeps the window open.
# It blocks here until the window is closed.
# Order of events:
#   1. Window becomes visible with all drawn content
#   2. tkinter listens for events (mouse, keyboard, resize, close)
#   3. When you close the window, mainloop() returns and the script exits
root.mainloop()

print("Window closed. Script done.")