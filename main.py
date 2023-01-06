import tkinter
from tkinter import  ttk
from tkinter import *
from PIL import ImageTk, Image


def raise_frame(frame):
    frame.tkraise()

root = Tk()


x = root.winfo_screenwidth()  # размер  по горизонтали монитора пользователя
y = root.winfo_screenheight() # размер по вертикали монитора пользователя
root.geometry('{}x{}'.format(int(x*1), int(y*1))) # размер приложения

f1 = Frame(root) # создание 1 рамки
f2 = Frame(root) # создание 2 рамки
f3 = Frame(root) # создание 3 рамки
f4 = Frame(root) # создание 4 рамки


image = Image.open("image.png") # открытие изображения
photo = ImageTk.PhotoImage(image.resize((1600, 600), Image.ANTIALIAS))
background_label1 = Label(f1, image=photo)
background_label1.pack(side="top", fill="both", expand="no")
background_label2 = Label(f2, image=photo)
background_label2.pack(side="top", fill="both", expand="no")
background_label3 = Label(f3, image=photo)
background_label3.pack(side="top", fill="both", expand="no")
background_label4 = Label(f4, image=photo)
background_label4.pack(side="top", fill="both", expand="no")




def openNewWindow():
    newWindow = Toplevel(root)

    newWindow.title("Расписание")

    newWindow.geometry('{}x{}'.format(int(x*0.4), int(y*0.4)))

    Label(newWindow, text="Зесь будет расписание").pack()


for frame in (f1, f2, f3, f4):
    frame.grid(row=0, column=0, sticky='news')


btn_mov1 = Button(f1, text='Перейти на 2 этаж', command=lambda:raise_frame(f2))
btn_mov1.pack()
Label(f1, text='Этаж 1').pack()
btn_tim1 = Button(f1, text ="расписание", command=openNewWindow)
btn_tim1.pack()
btn_tim1.columnconfigure(1, weight=1)
btn_tim1.rowconfigure(1, weight=1)
btn_tim1.lift()

btn_mov2 = Button(f2, text='Перейти на 3 этаж', command=lambda:raise_frame(f3))
btn_mov2.pack()
Label(f2, text='Этаж 2').pack()
btn_tim2 = Button(f2, text ="Р2", command=openNewWindow)
btn_tim2.place(x=400, y=550)
btn_tim2 = Button(f2, text ="Р3", command=openNewWindow)
btn_tim2.place(x=200, y=550)
btn_tim2.columnconfigure(1, weight=1)
btn_tim2.rowconfigure(1, weight=1)
btn_tim2.lift()

btn_mov3 = Button(f3, text='Перейти на 4 этаж', command=lambda:raise_frame(f4))
btn_mov3.pack()
Label(f3, text='Этаж 3').pack()
btn_tim3 = Button(f3, text ="расписание", command=openNewWindow)
btn_tim3.pack()
btn_tim3.columnconfigure(1, weight=1)
btn_tim3.rowconfigure(1, weight=1)
btn_tim3.lift()

btn_mov4 = Button(f4, text='Перейти на 1 этаж', command=lambda:raise_frame(f1))
btn_mov4.pack()
Label(f4, text='Этаж 4').pack()
btn_tim4 = Button(f4, text ="расписание", command=openNewWindow)
btn_tim4.pack()
btn_tim4.columnconfigure(1, weight=1)
btn_tim4.rowconfigure(1, weight=1)
btn_tim4.lift()

raise_frame(f1)
root.mainloop()