import tkinter as tk

def safe_eval(expression):
    """Safely evaluates a math expression."""
    try:
        allowed_chars = "0123456789+-*/.() "
        for char in expression:
            if char not in allowed_chars:
                return "Invalid input"
        result = eval(expression)
        return result
    except ZeroDivisionError:
        return "Can't divide by 0"
    except Exception:
        return "Invalid expression"

def click(event):
    text = event.widget.cget("text")

    if text == "=":
        expr = entry.get()
        result = safe_eval(expr)
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    elif text == "C":
        entry.delete(0, tk.END)
    elif text == "⌫":
        current = entry.get()
        entry.delete(0, tk.END)
        entry.insert(tk.END, current[:-1])
    else:
        entry.insert(tk.END, text)

def handle_key(event):
    if event.char.isdigit() or event.char in "+-*/().":
        entry.insert(tk.END, event.char)
    elif event.keysym == "Return":
        result = safe_eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, result)
    elif event.keysym == "BackSpace":
        current = entry.get()
        entry.delete(0, tk.END)
        entry.insert(tk.END, current[:-1])

# --- UI Setup ---
root = tk.Tk()
root.title("Python Calculator")

entry = tk.Entry(root, font="Arial 20", borderwidth=5, relief="solid", justify="right")
entry.pack(fill="both", padx=10, pady=10)
entry.focus_set()

# Bind keyboard input
root.bind("<Key>", handle_key)

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['C', '0', '=', '+'],
    ['⌫']  # Add remove (backspace) button in a new row
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    for btn in row:
        b = tk.Button(frame, text=btn, font="Arial 18", height=2, width=4)
        b.pack(side="left", expand=True, fill="both")
        b.bind("<Button-1>", click)

root.mainloop()
