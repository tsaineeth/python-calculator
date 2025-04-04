import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(str(entry.get())))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    elif text == "Del":
        entry.delete(len(entry.get()) - 1, tk.END)
    else:
        entry.insert(tk.END, text)

root = tk.Tk()
root.title("Simple Calculator")

entry = tk.Entry(root, font="Arial 20")
entry.pack(fill=tk.BOTH, ipadx=8, pady=10)

buttons = [
    ["C", "%", "Del", "="],
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["00", "0", ".", "+"]
]

for row in buttons:
    f = tk.Frame(root)
    f.pack()
    for b in row:
        btn = tk.Button(f, text=b, font="Arial 18", width=5)
        btn.pack(side=tk.LEFT, padx=5, pady=5)
        btn.bind("<Button-1>", click)

root.mainloop()
