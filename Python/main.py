import tkinter as tk
window = tk.Tk()
label = tk.Label(
     text="Python rocks!",
     foreground="white",
     background="black"
)
label.pack()
window = tk.Tk()
button = tk.Button(
     text="Click me!",
     width=25,
     height=5,
     bg="blue",
     fg="yellow",
 )
button.pack()
label = tk.Label(text = "Name")
entry = tk.Entry(fg="yellow", bg="blue", width=50)
label.pack()
entry.pack()
name = entry.get()
entry.insert(0, "Real Python")

frame = tk.Frame()
label = tk.Label(master=frame)
frame.pack()
 
border_effects = {
    "flat": tk.FLAT,
    "sunken": tk.SUNKEN,
    "raised": tk.RAISED,
    "groove": tk.GROOVE,
    "ridge": tk.RIDGE,
}



for relief_name, relief in border_effects.items():
    frame = tk.Frame(master=window, relief=relief, borderwidth=5)
    frame.pack(side=tk.LEFT)
    label = tk.Label(master=frame, text=relief_name)
    label.pack()


frame_a = tk.Frame()
label_a = tk.Label(master=frame_a, text = "I'm in Frame A")
label_a.pack()

frame_b = tk.Frame()
label_b = tk.Label(master=frame_a, text = "I'm in Frame B")
label_b.pack()

frame_b.pack()
frame_a.pack()





for i in range(3):
    window.columnconfigure(i, weight=1, minsize=75)
    window.rowconfigure(i, weight=1, minsize=50)

    for j in range(0, 3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j, padx=5, pady=5)
        label = tk.Label(master=frame, text=f"row {i}\nColumn {j}")
        label.pack(padx=5, pady=5)

window.mainloop()