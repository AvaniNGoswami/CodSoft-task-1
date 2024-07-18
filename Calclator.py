from tkinter import *

def click_me(event):
    global enter
    global entry
    text = event.widget.cget("text")
    if text=="=":
        if enter.get().isdigit():
            value = int(enter.get())
        else:
            value = eval(entry.get())

        enter.set(value)
        entry.update()
    elif text=="C":
        enter.set("")
        entry.update()
    else:
        enter.set(enter.get()+text)
        entry.update()


root = Tk()
root.geometry("600x500")
root.title("My Calculator")
root.configure(bg="black")

enter = StringVar()
enter.set("")
entry = Entry(root,textvariable=enter,font="lucida 40 bold")
entry.pack(fill=X,pady=10,ipady=10)

f1 = Frame(root,bg="black")
f1.pack(padx=10,pady=10)

b9 = Button(f1,text="9",padx=10,pady=5,font="lucida 20 bold")
b9.pack(side=LEFT,padx=10)
b9.bind("<Button-1>",click_me)
b8 = Button(f1,text="8",padx=10,pady=5,font="lucida 20 bold")
b8.pack(side=LEFT,padx=10)
b8.bind("<Button-1>",click_me)
b7 = Button(f1,text="7",padx=10,pady=5,font="lucida 20 bold")
b7.pack(side=LEFT,padx=10)
b7.bind("<Button-1>",click_me)
b_mul = Button(f1,text="*",padx=10,pady=5,font="lucida 20 bold")
b_mul.pack(side=LEFT,padx=10)
b_mul.bind("<Button-1>",click_me)

f2 = Frame(root,bg="black")
f2.pack(padx=10,pady=10)

b6 = Button(f2,text="6",padx=10,pady=5,font="lucida 20 bold")
b6.pack(side=LEFT,padx=10)
b6.bind("<Button-1>",click_me)
b5 = Button(f2,text="5",padx=10,pady=5,font="lucida 20 bold")
b5.pack(side=LEFT,padx=10)
b5.bind("<Button-1>",click_me)
b4 = Button(f2,text="4",padx=10,pady=5,font="lucida 20 bold")
b4.pack(side=LEFT,padx=10)
b4.bind("<Button-1>",click_me)
b_d = Button(f2,text="/",padx=10,pady=5,font="lucida 20 bold")
b_d.pack(side=LEFT,padx=10)
b_d.bind("<Button-1>",click_me)

f3 = Frame(root,bg="black")
f3.pack(padx=10,pady=10)

b3 = Button(f3,text="3",padx=10,pady=5,font="lucida 20 bold")
b3.pack(side=LEFT,padx=10)
b3.bind("<Button-1>",click_me)
b2 = Button(f3,text="2",padx=10,pady=5,font="lucida 20 bold")
b2.pack(side=LEFT,padx=10)
b2.bind("<Button-1>",click_me)
b1 = Button(f3,text="1",padx=10,pady=5,font="lucida 20 bold")
b1.pack(side=LEFT,padx=10)
b1.bind("<Button-1>",click_me)
b_p = Button(f3,text="%",padx=3,pady=5,font="lucida 20 bold")
b_p.pack(side=LEFT,padx=10)
b_p.bind("<Button-1>",click_me)

f4 = Frame(root,bg="black")
f4.pack(padx=10,pady=10)

b0 = Button(f4,text="0",padx=10,pady=5,font="lucida 20 bold")
b0.pack(side=LEFT,padx=10)
b0.bind("<Button-1>",click_me)
b_sub = Button(f4,text="-",padx=10,pady=5,font="lucida 20 bold")
b_sub.pack(side=LEFT,padx=10)
b_sub.bind("<Button-1>",click_me)
b_add = Button(f4,text="+",padx=10,pady=5,font="lucida 20 bold")
b_add.pack(side=LEFT,padx=10)
b_add.bind("<Button-1>",click_me)
b_eq = Button(f4,text="=",padx=10,pady=1,font="lucida 20 bold")
b_eq.pack(side=LEFT,padx=10)
b_eq.bind("<Button-1>",click_me)

f5 = Frame(root,bg="black")
f5.pack(padx=10,pady=10)

b_c = Button(f5,text="C",padx=10,pady=5,font="lucida 20 bold")
b_c.pack(side=LEFT,padx=10)
b_c.bind("<Button-1>",click_me)
root.mainloop()