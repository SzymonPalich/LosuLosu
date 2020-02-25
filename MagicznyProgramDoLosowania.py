import tkinter as tk
import random


root = tk.Tk()
root.title("Losu Losu")
root.geometry("218x335")
root.resizable(0, 0)
root.pack_propagate(0)


def losu():
    ust_czas = 0
    lista_ludzi = []
    area.config(text="", fg="black", bg="white")
    if czas.get("1.0", "end-1c") == "":
        area.config(text="Wprowadź czas", fg="red")
    else:
        ust_czas = int(czas.get("1.0", "end-1c"))*4
    if p1.get("1.0", "end-1c") != "":
        if len(p1.get("1.0", "end-1c")) <= 15:
            lista_ludzi.append(p1.get("1.0", "end-1c"))
        else:
            area.config(text="Popraw pole 1", fg="red")
    if p2.get("1.0", "end-1c") != "":
        if len(p2.get("1.0", "end-1c")) <= 15:
            lista_ludzi.append(p2.get("1.0", "end-1c"))
        else:
            area.config(text="Popraw pole 2", fg="red")
    if p3.get("1.0", "end-1c") != "":
        if len(p3.get("1.0", "end-1c")) <= 15:
            lista_ludzi.append(p3.get("1.0", "end-1c"))
        else:
            area.config(text="Popraw pole 3", fg="red")
    if p4.get("1.0", "end-1c") != "":
        if len(p4.get("1.0", "end-1c")) <= 15:
            lista_ludzi.append(p4.get("1.0", "end-1c"))
        else:
            area.config(text="Popraw pole 4", fg="red")
    losowanie(ust_czas, lista_ludzi)


def losowanie(pozostaly_czas, ludzie):
    lista_kolorow = ["blue", "red", "green", "yellow", "magenta", "brown", "black"]
    if pozostaly_czas != 0 and len(ludzie) != 0:
        print(pozostaly_czas)
        if pozostaly_czas == 1 and len(ludzie) != 0:
            area.config(text=ludzie[random.randint(0, len(ludzie) - 1)], highlightbackground="#04240b",
                        bg="#9ffa43", fg="#420057")
        elif pozostaly_czas != 0 and len(ludzie) != 0:
            area.config(text=ludzie[random.randint(0, len(ludzie) - 1)], fg=lista_kolorow[random.randint(0, 6)])
            root.after(250, lambda: losowanie(pozostaly_czas-1, ludzie))


area = tk.Label(root, width=15, height=3, borderwidth=2, relief="solid", bg="white", font="Helvetica 18 bold")
area.grid(row=1, column=1, columnspan=4, pady=5, padx=(8, 0))

t1 = tk.Label(root, width=1, height=1, text="1.")
t1.grid(row=2, column=1, pady=5, padx=(0, 0))
p1 = tk.Text(root, width=15, height=1, borderwidth=2, relief="groove")
p1.grid(row=2, column=2, columnspan=4, pady=5, padx=(8, 0))

t2 = tk.Label(root, width=1, height=1, text="2.")
t2.grid(row=3, column=1, pady=5, padx=(0, 0))
p2 = tk.Text(root, width=15, height=1, borderwidth=2, relief="groove")
p2.grid(row=3, column=2, columnspan=4, pady=5, padx=(8, 0))

t3 = tk.Label(root, width=1, height=1, text="3.")
t3.grid(row=4, column=1, pady=5, padx=(0, 0))
p3 = tk.Text(root, width=15, height=1, borderwidth=2, relief="groove")
p3.grid(row=4, column=2, columnspan=4, pady=5, padx=(8, 0))

t4 = tk.Label(root, width=1, height=1, text="4.")
t4.grid(row=5, column=1, pady=5, padx=(0, 0))
p4 = tk.Text(root, width=15, height=1, borderwidth=2, relief="groove")
p4.grid(row=5, column=2, columnspan=4, pady=5, padx=(8, 0))

t_czas = tk.Label(root, width=5, height=1, text="Czas:")
t_czas.grid(row=6, column=1, pady=5, padx=(0, 0))
czas = tk.Text(root, width=5, height=1, borderwidth=2, relief="groove")
czas.grid(row=6, column=2, columnspan=4, pady=5, padx=(8, 0))

submit = tk.Button(root, text='Losu Losu', width=12, height=2, command=lambda: losu())
submit.grid(row=7, column=1, columnspan=4, pady=5, padx=(8, 0))

root.mainloop()
