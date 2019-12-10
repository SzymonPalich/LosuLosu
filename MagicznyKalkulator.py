import tkinter as tk

root = tk.Tk()
root.title("Magiczny Kalkulator")
root.geometry("262x415")
root.resizable(0, 0)
root.pack_propagate(0)

separators = '^*/+-'
calc_area = ""
mem = 0
dot_placed = False


def kolejnosc_dzialan(dzialanie, kolejnosc=0):
    if kolejnosc == 0:
        i = 0
        stop = False
        while i != len(dzialanie) and not stop:
            if dzialanie[i] == "^":
                dzialanie[i - 1] = dzialanie[i - 1] ** dzialanie[i + 1]
                dzialanie.pop(i)
                dzialanie.pop(i)
                stop = True
            i += 1
        if stop:
            kolejnosc_dzialan(dzialanie)
        else:
            kolejnosc_dzialan(dzialanie, kolejnosc + 1)
    elif kolejnosc == 1:
        i = 0
        stop = False
        while i != len(dzialanie) and not stop:
            if dzialanie[i] == "*":
                dzialanie[i - 1] = dzialanie[i - 1] * dzialanie[i + 1]
                dzialanie.pop(i)
                dzialanie.pop(i)
                stop = True
            elif dzialanie[i] == "/":
                dzialanie[i - 1] = dzialanie[i - 1] / dzialanie[i + 1]
                dzialanie.pop(i)
                dzialanie.pop(i)
                stop = True
            i += 1
        if stop:
            kolejnosc_dzialan(dzialanie)
        else:
            kolejnosc_dzialan(dzialanie, kolejnosc + 1)
    elif kolejnosc == 2:
        i = 0
        stop = False
        while i != len(dzialanie) and not stop:
            if dzialanie[i] == "+":
                dzialanie[i - 1] = dzialanie[i - 1] + dzialanie[i + 1]
                dzialanie.pop(i)
                dzialanie.pop(i)
                stop = True
            elif dzialanie[i] == "-":
                dzialanie[i - 1] = dzialanie[i - 1] - dzialanie[i + 1]
                dzialanie.pop(i)
                dzialanie.pop(i)
                stop = True
            i += 1
        if stop:
            kolejnosc_dzialan(dzialanie)
    return dzialanie[0]


def clear():
    global calc_area
    calc_area = ""
    area.config(text=str(calc_area))


def store():
    brak_operatorow = False
    global calc_area
    global mem
    for x in calc_area:
        if x in "*^-+/":
            brak_operatorow = True
            break
    if not brak_operatorow:
        mem = calc_area


def recall():
    global calc_area
    global mem
    if mem != 0:
        clicked(mem)


def calc_area_append(x):
    global calc_area
    calc_area += str(x)


def clicked(but_val):
    global separators
    global dot_placed
    global calc_area
    if str(but_val) in separators:
        try:
            str(calc_area[-1])
        except IndexError:
            if calc_area == "":
                pass
            else:
                dot_placed = False
                calc_area_append(but_val)
                area.config(text=str(calc_area))
        else:
            if calc_area[-1] in separators or calc_area == "":
                pass
            else:
                dot_placed = False
                calc_area_append(but_val)
                area.config(text=str(calc_area))
    elif str(but_val) in '.':
        if not dot_placed and calc_area[-1] not in separators:
            calc_area_append(but_val)
            area.config(text=str(calc_area))
        dot_placed = True
    else:
        calc_area_append(but_val)
        area.config(text=str(calc_area))


def calc(data):
    global separators
    global dot_placed
    if data != '' and data[-1] not in separators:
        global calc_area
        temp = ''
        to_calc = []
        for x in data:
            if x not in separators:
                temp += x
            elif x in separators:
                to_calc.append(float(temp))
                temp = ''
                to_calc.append(x)
        to_calc.append(float(temp))

        wynik = kolejnosc_dzialan(to_calc)
        calc_area = ""
        if wynik.is_integer():
            wynik = int(wynik)
            clicked(wynik)
        else:
            clicked(round(wynik, 5))
            dot_placed = True


area = tk.Label(root, width=28, height=4, borderwidth=2, relief="groove")
area.grid(row=1, column=1, columnspan=4, pady=5, padx=(8, 0))


button7 = tk.Button(root, text='7', width=4, height=3, command=lambda: clicked(7)).grid(row=2, column=1, padx=(10, 0))
button8 = tk.Button(root, text='8', width=4, height=3, command=lambda: clicked(8)).grid(row=2, column=2)
button9 = tk.Button(root, text='9', width=4, height=3, command=lambda: clicked(9)).grid(row=2, column=3)
button_mul = tk.Button(root, text='*', width=4, height=3, command=lambda: clicked('*')).grid(row=2, column=4)

button4 = tk.Button(root, text='4', width=4, height=3, command=lambda: clicked(4)).grid(row=3, column=1, padx=(10, 0))
button5 = tk.Button(root, text='5', width=4, height=3, command=lambda: clicked(5)).grid(row=3, column=2)
button6 = tk.Button(root, text='6', width=4, height=3, command=lambda: clicked(6)).grid(row=3, column=3)
button_div = tk.Button(root, text='/', width=4, height=3, command=lambda: clicked('/')).grid(row=3, column=4)

button1 = tk.Button(root, text='1', width=4, height=3, command=lambda: clicked(1)).grid(row=4, column=1, padx=(10, 0))
button2 = tk.Button(root, text='2', width=4, height=3, command=lambda: clicked(2)).grid(row=4, column=2)
button3 = tk.Button(root, text='3', width=4, height=3, command=lambda: clicked(3)).grid(row=4, column=3)
button_add = tk.Button(root, text='+', width=4, height=3, command=lambda: clicked('+')).grid(row=4, column=4)

button0 = tk.Button(root, text='0', width=4, height=3, command=lambda: clicked(0)).grid(row=5, column=1, padx=(10, 0))
button_dot = tk.Button(root, text='.', width=4, height=3, command=lambda: clicked('.')).grid(row=5, column=2)
button_sub = tk.Button(root, text='-', width=4, height=3, command=lambda: clicked('-')).grid(row=5, column=3)
button_exp = tk.Button(root, text='^', width=4, height=3, command=lambda: clicked('^')).grid(row=5, column=4)


button_cls = tk.Button(root, text='Clear', width=4, height=3, command=lambda: clear()).grid(row=6, column=1, padx=(10, 0))
button_mstore = tk.Button(root, text='MS', width=4, height=3, command=lambda: store()).grid(row=6, column=2)
button_mrecall = tk.Button(root, text='MR', width=4, height=3, command=lambda: recall()).grid(row=6, column=3)
button_ent = tk.Button(root, bg="#52ff5a", text='=', activebackground="#3aba40",
                       width=4, height=3, command=lambda: calc(calc_area)).grid(row=6, column=4)


root.mainloop()
