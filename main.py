import tkinter as tk
from tkinter import ttk
import random
import time

# -----------------------------
# Draw data bars on canvas
# -----------------------------
def draw_data(data, color_array):
    canvas.delete("all")
    c_height = 400
    c_width = 880
    x_width = c_width / (len(data) + 1)
    offset = 10
    spacing = 5
    normalized_data = [i / max(data) for i in data]
    for i, height in enumerate(normalized_data):
        x0 = i * x_width + offset + spacing
        y0 = c_height - height * 350
        x1 = (i + 1) * x_width + offset
        y1 = c_height
        canvas.create_rectangle(x0, y0, x1, y1, fill=color_array[i])
    root.update_idletasks()

# -----------------------------
# Sorting Algorithms
# -----------------------------
def bubble_sort(data, draw_data, speed):
    for i in range(len(data) - 1):
        for j in range(len(data) - i - 1):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                draw_data(data, ['#00C853' if x == j or x == j + 1 else '#007ACC' for x in range(len(data))])
                time.sleep(speed)
    draw_data(data, ['#00C853' for x in range(len(data))])

def insertion_sort(data, draw_data, speed):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and key < data[j]:
            data[j + 1] = data[j]
            j -= 1
            draw_data(data, ['#FF5722' if x == j or x == j + 1 else '#007ACC' for x in range(len(data))])
            time.sleep(speed)
        data[j + 1] = key
    draw_data(data, ['#00C853' for x in range(len(data))])

def selection_sort(data, draw_data, speed):
    for i in range(len(data)):
        min_idx = i
        for j in range(i + 1, len(data)):
            if data[min_idx] > data[j]:
                min_idx = j
            draw_data(data, ['#FFEB3B' if x == min_idx else '#007ACC' for x in range(len(data))])
            time.sleep(speed)
        data[i], data[min_idx] = data[min_idx], data[i]
    draw_data(data, ['#00C853' for x in range(len(data))])

def merge_sort(data, draw_data, speed):
    merge_sort_alg(data, 0, len(data) - 1, draw_data, speed)
    draw_data(data, ['#00C853' for _ in range(len(data))])

def merge_sort_alg(data, left, right, draw_data, speed):
    if left < right:
        middle = (left + right) // 2
        merge_sort_alg(data, left, middle, draw_data, speed)
        merge_sort_alg(data, middle + 1, right, draw_data, speed)
        merge(data, left, middle, right, draw_data, speed)

def merge(data, left, middle, right, draw_data, speed):
    left_part = data[left:middle + 1]
    right_part = data[middle + 1:right + 1]
    left_idx = right_idx = 0
    for data_idx in range(left, right + 1):
        if left_idx < len(left_part) and right_idx < len(right_part):
            if left_part[left_idx] <= right_part[right_idx]:
                data[data_idx] = left_part[left_idx]
                left_idx += 1
            else:
                data[data_idx] = right_part[right_idx]
                right_idx += 1
        elif left_idx < len(left_part):
            data[data_idx] = left_part[left_idx]
            left_idx += 1
        else:
            data[data_idx] = right_part[right_idx]
            right_idx += 1
        draw_data(data, ['#FF4081' if x >= left and x <= right else '#007ACC' for x in range(len(data))])
        time.sleep(speed)

def quick_sort(data, draw_data, speed):
    quick_sort_alg(data, 0, len(data) - 1, draw_data, speed)
    draw_data(data, ['#00C853' for _ in range(len(data))])

def quick_sort_alg(data, low, high, draw_data, speed):
    if low < high:
        pi = partition(data, low, high, draw_data, speed)
        quick_sort_alg(data, low, pi - 1, draw_data, speed)
        quick_sort_alg(data, pi + 1, high, draw_data, speed)

def partition(data, low, high, draw_data, speed):
    pivot = data[high]
    i = low - 1
    for j in range(low, high):
        if data[j] < pivot:
            i += 1
            data[i], data[j] = data[j], data[i]
        draw_data(data, ['#FF9800' if x == j else '#007ACC' for x in range(len(data))])
        time.sleep(speed)
    data[i + 1], data[high] = data[high], data[i + 1]
    return i + 1

# -----------------------------
# UI Logic
# -----------------------------
def generate():
    global data
    data = [random.randint(10, 150) for _ in range(40)]
    draw_data(data, ['#007ACC' for x in range(len(data))])

def start_sort():
    global data
    speed = speed_scale.get() / 100
    algo = algo_menu.get()

    if algo == 'Bubble Sort':
        bubble_sort(data, draw_data, speed)
    elif algo == 'Insertion Sort':
        insertion_sort(data, draw_data, speed)
    elif algo == 'Selection Sort':
        selection_sort(data, draw_data, speed)
    elif algo == 'Merge Sort':
        merge_sort(data, draw_data, speed)
    elif algo == 'Quick Sort':
        quick_sort(data, draw_data, speed)

# -----------------------------
# Tkinter Setup
# -----------------------------
root = tk.Tk()
root.title("Visual Sorting")
root.geometry("900x600")
root.config(bg="#1E1E1E")

ui_frame = tk.Frame(root, width=880, height=150, bg="#2C2C2C")
ui_frame.pack(padx=10, pady=5)

canvas = tk.Canvas(root, width=880, height=400, bg="white")
canvas.pack(padx=10, pady=5)

# Dropdown menu
tk.Label(ui_frame, text="Algorithm:", bg="#2C2C2C", fg="white").grid(row=0, column=0, padx=10, pady=5, sticky="w")
algo_menu = ttk.Combobox(ui_frame, values=["Bubble Sort", "Insertion Sort", "Selection Sort", "Merge Sort", "Quick Sort"])
algo_menu.grid(row=0, column=1, padx=5, pady=5)
algo_menu.current(0)

# Speed control
tk.Label(ui_frame, text="Speed:", bg="#2C2C2C", fg="white").grid(row=0, column=2, padx=10, pady=5, sticky="w")
speed_scale = tk.Scale(ui_frame, from_=1, to=100, length=150, orient=tk.HORIZONTAL, bg="#2C2C2C", fg="white")
speed_scale.grid(row=0, column=3, padx=5, pady=5)
speed_scale.set(30)

# Buttons
tk.Button(ui_frame, text="Generate Array", bg="#007ACC", fg="white", width=15, command=generate).grid(row=0, column=4, padx=10, pady=5)
tk.Button(ui_frame, text="Start Sorting", bg="#00C853", fg="white", width=15, command=start_sort).grid(row=0, column=5, padx=10, pady=5)

data = []
import time
from tkinter import messagebox

def compare_algorithms():
    global data
    size = len(data)
    if size == 0:
        messagebox.showwarning("Warning", "Please generate an array first!")
        return

    algorithms = {
        "Bubble Sort": bubble_sort,
        "Insertion Sort": insertion_sort,
        "Selection Sort": selection_sort,
        "Merge Sort": merge_sort,
        "Quick Sort": quick_sort
    }

    results = []
    original_data = data[:]

    for name, func in algorithms.items():
        data = original_data[:]  # copy array
        start = time.time()
        func(draw_data, speed_scale)
        end = time.time()
        results.append((name, round(end - start, 3)))

    result_text = "\n".join([f"{name}: {t} sec" for name, t in results])
    messagebox.showinfo("Algorithm Comparison", result_text)

# Add new Compare button in UI
tk.Button(ui_frame, text="Compare Algorithms", bg="#FF9800", fg="white", width=18, command=compare_algorithms)\
    .grid(row=0, column=6, padx=10, pady=5)

root.mainloop()
