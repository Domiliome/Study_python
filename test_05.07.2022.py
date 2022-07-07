from tkinter import *


def resize_window(window, wight, height):
    size = [wight, height]
    w = window.winfo_screenwidth()
    h = window.winfo_screenheight()
    w = w // 2
    h = h // 2
    w = w - (size[0] // 2)
    h = h - (size[1] // 2)
    window.geometry('{}x{}+{}+{}'.format(size[0], size[1], w, h))

btns = []
status = "X"

root = Tk()
resize_window(root, 400, 400)

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)

def move_x(btn):
    btn["text"] = "X"

def move_o(btn):
    btn["text"] = "O"

def start(btn):
    global status
    match status:
        case "X":
            move_x(btn)
            status = "O"
            check_win()
        case "O":
            move_o(btn)
            status = "X"
            check_win()

def check_win():
    result = []
    for i in range(len(btns)):
        arr = []
        for j in range(len(btns[i])):
            arr += btns[i][j]["text"]
        result.append(arr)
        if len(set(result[i])) == 1 and set(result[i]) != {' '}:
            print("good")
    for i in range(3):
        if len({result[0][i], result[1][i], result[2][i]}) == 1 and {result[0][i], result[1][i], result[2][i]} != {" "}:
            print("good")
    if len({result[0][0], result[1][1], result[2][2]}) == 1 and {result[0][i], result[1][i], result[2][i]} != {" "}:
        print("good")
    if len({result[0][2], result[1][1], result[2][0]}) == 1 and {result[0][i], result[1][i], result[2][i]} != {" "}:
        print("good")
    print(result)

for i in range(3):
    btns.append([])
    for j in range(3):
        btn = Button(root, text=" ")
        btn.grid(row=i, column=j, sticky="nwse")
        btn["command"] = lambda b=btn: start(b)
        btns[i].append(btn)

root.mainloop()
