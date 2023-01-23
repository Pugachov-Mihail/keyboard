from config import app, TEXT
from tkinter import Label


def find_but(event, find):
    if find == event:
        label_text("ОК", background="green")
    else:
        label_text("Мимо", background="red")


def press(event):
    return event.keysym


def label_text(text, background):
    label = Label(text=text, background=background)
    label.pack()


def main():



if __name__ == '__main__':
    main()
    app.bind_all("<Key>", press)
    app.mainloop()
