import tkinter as tk

# Canvas size and grid properties
CELL_SIZE = 30
GRID_WIDTH = 10
GRID_HEIGHT = 10

# Function to draw the grid of blue cells
def draw_grid(canvas):
    for row in range(GRID_HEIGHT):
        for col in range(GRID_WIDTH):
            x1 = col * CELL_SIZE
            y1 = row * CELL_SIZE
            x2 = x1 + CELL_SIZE
            y2 = y1 + CELL_SIZE
            canvas.create_rectangle(x1, y1, x2, y2, fill="blue", outline="black")

# Eraser functionality
def start_eraser(event):
    global eraser_dragging
    eraser_dragging = True
    erase(event)

def stop_eraser(event):
    global eraser_dragging
    eraser_dragging = False

def erase(event):
    if eraser_dragging:
        x = event.x // CELL_SIZE
        y = event.y // CELL_SIZE
        if 0 <= x < GRID_WIDTH and 0 <= y < GRID_HEIGHT:
            cell_id = x + y * GRID_WIDTH
            canvas.itemconfig(cell_ids[cell_id], fill="white")

# Set up the Tkinter window
root = tk.Tk()
root.title("Canvas with Eraser")

# Create canvas
canvas = tk.Canvas(root, width=GRID_WIDTH * CELL_SIZE, height=GRID_HEIGHT * CELL_SIZE)
canvas.pack()

# Draw grid
cell_ids = []
for row in range(GRID_HEIGHT):
    for col in range(GRID_WIDTH):
        x1 = col * CELL_SIZE
        y1 = row * CELL_SIZE
        x2 = x1 + CELL_SIZE
        y2 = y1 + CELL_SIZE
        cell_id = canvas.create_rectangle(x1, y1, x2, y2, fill="blue", outline="black")
        cell_ids.append(cell_id)

# Create eraser (this will be a small rectangle on the canvas)
eraser = canvas.create_rectangle(0, 0, CELL_SIZE, CELL_SIZE, fill="gray", outline="black")

# Bind mouse events for erasing
canvas.bind("<ButtonPress-1>", start_eraser)
canvas.bind("<B1-Motion>", erase)
canvas.bind("<ButtonRelease-1>", stop_eraser)

root.mainloop()
