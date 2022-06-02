import tkinter as tk


class FileReader:
    def __init__(self, file_directory):
        self.file_directory = file_directory
        try:
            if r_var.get():
                file = open(file_directory, "w")
                file.write(txt_result.get(1.0, tk.END))

            else:

                file = open(file_directory, "r")
                txt_result.insert(1.0, file.read())

            file.close()
        except FileNotFoundError:
            pass


def set_lbl_text():
    txt_result.delete(1.0, tk.END)
    if r_var.get():
        lbl_command["text"] = "Напишите путь к файлу\n который вы хотите скопировать"
    else:
        lbl_command["text"] = "Напишите путь к файлу\n содержимое которого вы хотите прочитать"


def resize_window(window, wight, height):
    size = [wight, height]
    w = window.winfo_screenwidth()
    h = window.winfo_screenheight()
    w = w // 2
    h = h // 2
    w = w - (size[0] // 2)
    h = h - (size[1] // 2)
    window.geometry('{}x{}+{}+{}'.format(size[0], size[1], w, h))


root = tk.Tk()
resize_window(root, 600, 500)
root.update()

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

r_var = tk.BooleanVar()
r_var.set(False)

btn_read = tk.Radiobutton(root, text="read", variable=r_var, value=False, command=set_lbl_text)
btn_read.grid(row=0, column=0, sticky="we")

lbl_command = tk.Label(root, text="Напишите путь к файлу\n содержимое которого вы хотите прочитать")
lbl_command.grid(row=1, column=0, columnspan=2, sticky="we")

btn_write = tk.Radiobutton(root, text="write", variable=r_var, value=True, command=set_lbl_text)
btn_write.grid(row=0, column=2, sticky="we")

lbl_set_command = tk.Label(root, text="Выберите режим")
lbl_set_command.grid(row=0, column=1, sticky="we")

ent_set_command = tk.Entry(root)
ent_set_command.grid(row=1, column=2, sticky="we")

btn_choice = tk.Button(root, text="Выбрать", command=lambda: FileReader(ent_set_command.get()))
btn_choice.grid(row=2, column=0, columnspan=3)

txt_result = tk.Text()
txt_result.grid(row=3, column=0, columnspan=3)

root.mainloop()
