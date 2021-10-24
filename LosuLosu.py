"""
LosuLosu - Simple Random Picker
Copyright (C) 2021  Palich Szymon

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import random
import tkinter as tk


def get_persons():
    list_of_persons = []
    if ent_p1.get() != "":
        list_of_persons.append(ent_p1.get()[:16])
    if ent_p2.get() != "":
        list_of_persons.append(ent_p2.get()[:16])
    if ent_p3.get() != "":
        list_of_persons.append(ent_p3.get()[:16])
    if ent_p4.get() != "":
        list_of_persons.append(ent_p4.get()[:16])
    return list_of_persons


def retrieve_values():
    time = int(ent_time.get())
    list_of_persons = get_persons()

    if time > MAX_TIME:
        time = MAX_TIME
        ent_time.delete(0, tk.END)
        ent_time.insert(0, MAX_TIME)
    elif time < MIN_TIME:
        time = MIN_TIME
        ent_time.delete(0, tk.END)
        ent_time.insert(0, MIN_TIME)

    return time, list_of_persons


def validate():
    area.config(text="", fg="black", bg="white")

    try:
        int(ent_time.get())
    except ValueError:
        area.config(text="Specify time", fg="red")
        return False

    if len(get_persons()) < 2:
        area.config(text="Input more values", fg="red")
        return False

    return True


def losu():
    if validate():
        time, persons = retrieve_values()
        submit["state"] = "disabled"
        submit["text"] = time
        draw(time * 4, persons)


def draw(time, persons):
    if time % 4 == 0:
        submit["text"] = int(time / 4)

    if time != 0:
        area.config(text=persons[random.randint(0, len(persons) - 1)],
                    fg=COLORS[random.randint(0, len(COLORS) - 1)])
        root.after(250, lambda: draw(time - 1, persons))
    else:
        area.config(text=persons[random.randint(0, len(persons) - 1)],
                    highlightbackground="#04240b", bg="#9ffa43", fg="#420057")
        submit["state"] = "normal"
        submit["text"] = "Start!"


if __name__ == '__main__':
    COLORS = ["blue", "red", "green", "yellow", "magenta", "brown", "black"]
    MAX_TIME = 30
    MIN_TIME = 1

    root = tk.Tk()
    root.title("LosuLosu")
    root.resizable(0, 0)
    root.pack_propagate(0)

    area = tk.Label(root, width=15, height=3, borderwidth=2, relief="solid", bg="white",
                    font="Helvetica 18 bold")
    area.grid(row=1, column=1, columnspan=4, pady=5, padx=(8, 8))

    lab_p1 = tk.Label(root, width=1, height=1, text="1.")
    lab_p1.grid(row=2, column=1, pady=5, padx=(0, 0))
    ent_p1 = tk.Entry(root, width=15, borderwidth=2, relief="groove")
    ent_p1.grid(row=2, column=2, columnspan=4, pady=5, padx=(8, 0))

    lab_p2 = tk.Label(root, width=1, height=1, text="2.")
    lab_p2.grid(row=3, column=1, pady=5, padx=(0, 0))
    ent_p2 = tk.Entry(root, width=15, borderwidth=2, relief="groove")
    ent_p2.grid(row=3, column=2, columnspan=4, pady=5, padx=(8, 0))

    lab_p3 = tk.Label(root, width=1, height=1, text="3.")
    lab_p3.grid(row=4, column=1, pady=5, padx=(0, 0))
    ent_p3 = tk.Entry(root, width=15, borderwidth=2, relief="groove")
    ent_p3.grid(row=4, column=2, columnspan=4, pady=5, padx=(8, 0))

    lab_p4 = tk.Label(root, width=1, height=1, text="4.")
    lab_p4.grid(row=5, column=1, pady=5, padx=(0, 0))
    ent_p4 = tk.Entry(root, width=15, borderwidth=2, relief="groove")
    ent_p4.grid(row=5, column=2, columnspan=4, pady=5, padx=(8, 0))

    lab_time = tk.Label(root, width=5, height=1, text="Time:")
    lab_time.grid(row=6, column=1, pady=5, padx=(0, 0))
    ent_time = tk.Entry(root, width=5, borderwidth=2, relief="groove")
    ent_time.insert(tk.END, '5')
    ent_time.grid(row=6, column=2, columnspan=4, pady=5, padx=(8, 0))

    submit = tk.Button(root, text='Start!', width=15, height=2, command=lambda: losu())
    submit.grid(row=7, column=1, columnspan=4, pady=5, padx=(8, 0))

    root.mainloop()
