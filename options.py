def resize_window(root, wight, height):
    size = [wight, height]
    w = root.winfo_screenwidth()
    h = root.winfo_screenheight()
    w = w // 2
    h = h // 2
    w = w - (size[0] // 2)
    h = h - (size[1] // 2)
    root.geometry('{}x{}+{}+{}'.format(size[0], size[1], w, h))
    #

# socet *10