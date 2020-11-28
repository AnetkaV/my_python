import tkinter as tk

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

frame_a = tk.Frame()
label_a = tk.Label(master=frame_a, text = "I'm in Frame A")
label_a.pack()

frame_b = tk.Frame()
label_b = tk.Label(master=frame_a, text = "I'm in Frame B")
label_b.pack()

frame_b.pack()
frame_a.pack()

window = tk.Tk()

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

window = tk.Tk()

events_list = []
def handle_keypress(event):
    print(event.char)

window.bind("<Key>", handle_keypress)

while True:
    if events_list == []:
        continue
    event = events_list[0]
    
    if event.type == "keypress":
        handle_keypress(event)

window.mainloop()

def increase():
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value + 1}"

def decrease():
    value = int(lbl_value["text"])
    lbl_value["text"] = f"{value - 1}"

window = tk.Tk()

window.rowconfigure(0, minsize=50, weight=1)
window.columnconfigure([0, 1, 2], minsize=50, weight=1)

btn_decrease = tk.Button(master=window, text="-", command=decrease)
btn_decrease.grid(row=0, column=0, sticky="nsew")

lbl_value = tk.Label(master=window, text="0")
lbl_value.grid(row=0, column=1)

btn_increase = tk.Button(master=window, text="+", command=increase)
btn_increase.grid(row=0, column=2, sticky="nsew")

window.mainloop()


def fahrenheit_to_celsius():
    fahrenheit = ent_temperature.get()
    celsius = (5/9) * (float(celsius) - 32)
    lbl_result["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"

window = tk.Tk()

window.title("Temperature Converter")

frm_entry = tk.Frame(master=window)
ent_temperature = tk.Entry(master=frm_entry, width=10)
lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")

ent_temperature.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0, column=1, sticky="w")

btn_convert = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=fahrenheit_to_celsius
)
lbl_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}")

frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
lbl_result.grid(row=0, column=2, padx=10)

window.mainloop()
