import tkinter


class CustomButton(tkinter.Frame):
    def __init__(self, text="", hover=True, imageset=None, custom_bg="black", function=None, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.imageset = imageset
        self.pressed = False
        self.function = function

        self.configure(bg=custom_bg)

        if imageset is None:
            self.label = tkinter.Label(self, text=text, bg=custom_bg, fg="lightgray", font=("Avenir", 32))
            self.label.place(relx=0.5, rely=0.55, anchor="center")
        else:
            self.label = tkinter.Label(self, image=self.imageset[0], bg=custom_bg)
            self.label.place(x=0, y=0)

        if hover is True:
            self.bind("<Enter>", self.on_enter)
            self.bind("<Leave>", self.on_leave)
            self.bind("<Button-1>", self.clicked)
            self.label.bind("<Button-1>", self.clicked)

    def on_enter(self, event):
        if self.imageset is None:
            self.label.configure(fg="white")
        else:
            if self.pressed is False:
                self.label.configure(image=self.imageset[1])
            if self.pressed:
                self.label.configure(image=self.imageset[3])

    def on_leave(self, enter):
        if self.imageset is None:
            self.label.configure(fg="lightgray")
        else:
            if self.pressed is False:
                self.label.configure(image=self.imageset[0])
            if self.pressed:
                self.label.configure(image=self.imageset[2])

    def clicked(self, event):
        if self.function:
            self.function()

        if self.imageset is None:
            self.label.configure(fg="lightgray")
        else:
            if self.pressed is False:
                self.pressed = True
                self.label.configure(image=self.imageset[3])
            else:
                self.pressed = False
                self.label.configure(image=self.imageset[1])
