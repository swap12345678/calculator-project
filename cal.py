import tkinter as tk

# Function to handle button click
def click(event):
    text = event.widget.cget("text")

    if text == "=":
        try:
            expression = entry_var.get().replace('%', '/100')
            result = str(eval(expression))
            entry_var.set(result)
        except:
            entry_var.set("Error")

    elif text == "C":
        entry_var.set("")

    else:
        entry_var.set(entry_var.get() + text)

# Main window setup
root = tk.Tk()
root.title("Basic Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Entry field
entry_var = tk.StringVar()
entry = tk.Entry(root, textvar=entry_var, font="Arial 20", bd=10, relief=tk.SUNKEN, justify="right")
entry.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

# Button layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["%", "0", "=", "+"],
    ["C"]
]

# Creating buttons
for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    for btn_text in row:
        button = tk.Button(frame, text=btn_text, font="Arial 18", height=2, width=6)
        button.pack(side=tk.LEFT, expand=True, fill="both")
        button.bind("<Button-1>", click)

root.mainloop()