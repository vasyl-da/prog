from tkinter import *
from tkinter.filedialog import *
root = Tk()
root.title('DCD TSu')
root.geometry("1310x510")
root.configure(background='#0000ff')
def f():
    l.delete("1.0","end")
    s = e.get("1.0","end-1c")
    SEP = "|*|"
    TRASH = "X}f"
    ANSWERS = [["A.","EЖ%¦"],["B.","DД$¤"],["C.","Cµ#•"],["D.",'B"'],["E.","AБ!"]]
    PROB = " "
    while any(SEP+trash in s or trash+SEP in s for trash in TRASH):
        for trash in TRASH:
            s = s.replace(trash+SEP, SEP).replace(SEP+trash, SEP)
    s = s.replace("	",PROB)
    s = s.replace(SEP+PROB,SEP).replace(PROB+SEP,SEP)
    s=s.replace("A.","A ").replace("B.","B ").replace("C.","C ").replace("D.","D ").replace("E.","E ")
    while "  " in s:
        s = s.replace(PROB*2,PROB)
    for answer, wrongs in ANSWERS:
        for wrong in wrongs:
            s = s.replace(SEP+wrong+SEP, SEP+answer+SEP)
    s = s.replace(SEP*4, SEP).replace(SEP, '\n')
    s = s.replace(PROB+'\n','\n').replace('\n'+PROB,'\n')
    l.insert(INSERT,s)

def d():
    e.delete("1.0","end")
    l.delete("1.0","end")

def outText():

    name = asksaveasfilename(
    filetypes = (("TXT files", "* .txt"),("Docx files","* .doc")))
    if (str(name)!=""):
        f = open(name, 'w')
        f.close()
        s = e.get("1.0",'end')
        SEP = "|*|"
        TRASH = "X}f"
        ANSWERS = [["A.","EЖ%¦"],["B.","DД$¤"],["C.","Cµ#•"],["D.",'B"'],["E.","AБ!"]]
        PROB = " "
        while any(SEP+trash in s or trash+SEP in s for trash in TRASH):
            for trash in TRASH:
                s = s.replace(trash+SEP, SEP).replace(SEP+trash, SEP)
        s = s.replace("	",PROB)
        s = s.replace(SEP+PROB,SEP).replace(PROB+SEP,SEP)
        s=s.replace("A.","A ").replace("B.","B ").replace("C.","C ").replace("D.","D ").replace("E.","E ")
        while PROB*2 in s:
            s = s.replace(PROB*2,PROB)
        for answer, wrongs in ANSWERS:
            for wrong in wrongs:
                s = s.replace(SEP+wrong+SEP, SEP+answer+SEP)
        s = s.replace(SEP*4, SEP).replace(SEP, '\n')
        s = s.replace(PROB+'\n','\n').replace('\n'+PROB,'\n')
        while '\n'*2 in s:
            s=s.replace('\n'*2,'\n')
        d = open(name,'a')
        d.write(s)
        d.close()

cart = Canvas (root, width=95,height=145)
im=PhotoImage(file="symv.png")
cart.create_image(0,0,anchor="nw",image=im)
cart.place(x=0,y=0)

b = Button(root,text = 'Розшифрувати', font = "Arial 10", command = f)
b.place(x=0,y=155,width=100,height=85)

b2 = Button(root,text = 'Зберегти', font = "Arial 10", command = outText)
b2.place(x=0,y=245,width=100,height=85)

d = Button(root,text = 'Очистити', font = "Arial 10", command = d,)
d.place(x=0,y=335,width=100,height=85)

escr = Scrollbar(root)
escr.place(x=680,y=55,width=25, height=455 )

e = Text(root,font = "Calibri 11", yscrollcommand = escr.set )
e.place(x=105,y=55,width=580, height=455)

escr.config( command = e.yview )

lscr = Scrollbar(root)
lscr.place(x=1285,y=55,width=25, height=455 )

l = Text(root, font = "Calibri 11",yscrollcommand = lscr.set)
l.place(x=710,y=55,width=575, height=455)

lscr.config( command = l.yview )

t1 = Label(root, text='Зашифровані тести', font = "Times 24")
t1.place(x=105,y=0,width=600, height=50,)

t2 = Label(text = 'Розшифровані тести',  font = "Times 24")
t2.place(x=710,y=0,width=600, height=50)





root.mainloop()
