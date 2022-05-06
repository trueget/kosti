from tkinter import *
import random, time

def bros():
    x = random.choice(['p1.png','p2.png','p3.png','p4.png','p5.png','p6.png'])
    return x

def img(event):
    global b1,b2
    for i in range(5):
        b1 = PhotoImage(file=(bros()))
        b2 = PhotoImage(file=(bros()))
        lab1['image'] = b1
        lab2['image'] = b2
        root.update()
        time.sleep(0.1)

root = Tk()
root.geometry('800x400')
root.title('Игра в кости. Сделай бросок! ')
root.resizable(height=False, width=False)
# root.iconphoto(True, PhotoImage(file=('photoz.png')))
font = PhotoImage(file=('photo_p.png'))
Label(root, image=font).pack()
lab1 = Label(root)
lab1.place(relx=0.3, rely=0.5, anchor=CENTER)
lab2 = Label(root)
lab2.place(relx=0.7, rely=0.5, anchor=CENTER)
img('event')
root.bind('<1>', img)
root.mainloop()