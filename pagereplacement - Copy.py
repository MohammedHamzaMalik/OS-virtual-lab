import PIL
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from matplotlib import pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)

def Choose_Algo():
    global Root
    Root=Tk()
    Root.geometry("1400x500")
    # Root.attributes('-fullscreen', True)
    Root.config(bg='black')
    Root.title('Select An Algorithem')
    # Enter the number of frames
    # Frame_Image = PhotoImage(file="f2.png",master= Root)
    Frame_Label = Label(Root, text="Enter No. of Frames", font="comicsense 18 bold", bg='cyan').place(x=20, y=10)
    Frame_Entry = Entry(Root, borderwidth=5, width="30", font=20, relief=SUNKEN)
    Frame_Entry.place(x=300, y=10)

    # Reference String
    # Enter string seperated by a space
    # String_Image = PhotoImage(file="rs1.png",master= Root)
    String_Label = Label(Root, text="Enter Reference String", font="comicsense 18 bold", bg='cyan').place(x=840, y=10)
    String_Entry = Entry(Root, borderwidth=5, width="30", font=30, relief=SUNKEN)
    String_Entry.place(x=1150, y=10)


    fifo_image = PhotoImage(master=Root, file='fifo.png')
    FIFO = Button(Root,bg='black', image=fifo_image,
                  command=lambda: FirstInFirstOut(Frame_Entry.get(),String_Entry.get())).place(x=110,y=100)

    lifo_image = PhotoImage(master=Root, file='lifo.png')
    LIFO = Button(Root,bg='black', image=lifo_image,
                  command=lambda: LastInFirstOut(Frame_Entry.get(), String_Entry.get())).place(x=300,y=100)

    lru_image = PhotoImage(master=Root, file='lru.png')
    LRU = Button(Root, bg='black',image=lru_image,
                 command=lambda: LeastRecentlyUsed(Frame_Entry.get(), String_Entry.get())).place(x=490,y=100)


    optimal_image = PhotoImage(master=Root, file='opr.png')
    OPTIMAL = Button(Root,bg='black', image=optimal_image,
                     command=lambda: Optimal(Frame_Entry.get(), String_Entry.get())).place(x=680,y=100)

    mru_image = PhotoImage(master=Root,file='mru.png')
    MRU= Button(Root,bg='black',image=mru_image,
                command=lambda : MostRecentlyUsed(Frame_Entry.get(), String_Entry.get())).place(x=870,y=100)

    ra_image=PhotoImage(master=Root,file='rpr.png')
    RANDOM_RPL= Button(Root,bg='black',image=ra_image,
                       command=lambda : Random_RAlgo(Frame_Entry.get(), String_Entry.get())).place(x=1080,y=100)

    cp_image = PhotoImage(master=Root, file='comparision.png')
    com_Algo=Button(Root,bg='black',image=cp_image,
                    command=lambda :Comp_Algo(Frame_Entry.get(), String_Entry.get())).place(x=1270,y=100)


    Label(Root,bg='black',text="Page Replacement Algorithm",font="algerian 19 bold",fg="lime").place(x=500,y=400)
    Label(Root,bg='black',text="Page Replacement Algorithm decides which page to remove, also called swap out when  a new page needs to be loaded into the main memory.\n Page Replacement happens when a requested page is not present in the main memory and the available space is not sufficient for allocation to the requested page.",font="comicscence 14 italic",fg="white").place(x=10,y=480)
    Label(Root,bg='black',text="When the page that was selected for replacement was paged out, and referenced again, it has to read in from disk,\n and this requires for I/O completion. This process determines the quality of the page replacement algorithm: the lesser the time waiting for page-ins, the better is the algorithm.",font="comicscence 14 italic",fg="white").place(x=10,y=580)
    Label(Root,bg='black',text="A page replacement algorithm tries to select which pages should be replaced so as to minimize the total number of page misses.\n There are many different page replacement algorithms. These algorithms are evaluated by running them on a particular string of memory reference and \ncomputing the number of page faults. The fewer is the page faults the better is the algorithm for that situation.",font="comicscence 14 italic",fg="white").place(x=50,y=680)




    Root.mainloop()

def Concurrency_deadlock():
    pass

def Scheduling_Algo():
    pass


def Parameters(N):
    global frame
    global fault
    global fifo_totalfault
    global lifo_totalfault
    global opr_totalfault
    global lru_totalfault
    global mru_totalfault
    global rpr_totalfault
    global index
    global column
    global count
    global bottom
    global top

    top = -1
    bottom = 0
    fifo_totalfault = 0
    lifo_totalfault=0
    opr_totalfault=0
    lru_totalfault = 0
    mru_totalfault = 0
    rpr_totalfault = 0
    fault = False
    index = 0
    count = 0
    frame = [None]*N
    column=0



def Fault(fault,N):
    global column
    if fault==False:
        Label(root,text="HIT",bg='black',fg='green',font='RALEWAY 10 bold').grid(row=N+4,column=column-1)
    else:
        Label(root,text="FAULT",bg='black',fg="red",font='RALEWAY 10 bold').grid(row=N+4,column=column-1)

def B_Label(frame,RefStr):
    global column
    global root
    row_index=len(frame)+1+2
    for i in frame:
        if i!=None:
            if i == RefStr[count-1]:
                Label(root,text=i,padx=20,pady=10,bd=2,fg='white',bg='#010352',
                      relief=SUNKEN,anchor="center").grid(row=row_index,column=column)
            else:
                Label(root,text=i,padx=20,pady=10,bd=3,fg="white",bg='navy blue',
                      relief=SUNKEN,anchor="center").grid(row=row_index,column=column)
            row_index-=1

def E_label(frame):
    global column
    row_index=len(frame)+1
    for i in range(len(frame)):
        Label(root,text=" ",padx=5,pady=10,bg='black').grid(row=row_index+2,column=column)
        row_index-=1

def Ratio(N,total_fault,len_RefStr):
    global root0
    global column

    hit_ratio=(len_RefStr-total_fault)/len_RefStr
    falult_ratio=1-hit_ratio

    FR=LabelFrame(root0,text="RATIO",bg='black',bd=3,relief=SUNKEN,fg='cyan',pady=30)
    FR.place(x=500,y=500)

    Label(FR,text="PAGE HIT RATIO",fg='cyan',bg='black',relief=SUNKEN,bd=3,anchor='center',
          font=("Lucida Handwriting",15,"bold")).grid(row=0,column=0,padx=30,pady=15)
    Label(FR,text="PAGE FAULT RATIO",fg='cyan',bg='black',relief=SUNKEN,bd=3,anchor='center',
          font=("Lucida Handwriting",15,"bold")).grid(row=1,column=0,padx=30,pady=15)
#     # Label(FR,text="Ekelekekjek ",fg='cyan',bg='black',relief=SUNKEN,bd=3,anchor='center').grid(row=N+8,column=6)
#
    Label(FR,text=f" {round(hit_ratio,3)}",bg='white',fg='green',
          font="comicscence 14 bold",relief=SUNKEN,bd=3).grid(row=0,column=1)
    Label(FR,text=f" {round(falult_ratio,3)}",bg='white',fg='green',
          font="comicscence 15 bold",relief=SUNKEN,bd=3).grid(row=1,column=1)


def FIFO(N,RefStr,root):
    global frame
    global index
    global bottom
    global fifo_totalfault
    global fault
    global column
    global count
    x=0
    q = len(RefStr)
    if count != q:
        column+=1
        x=RefStr[count]
        if None in frame:
            if x not in frame:
                frame[index]=x
                index+=1
                fault=True
                fifo_totalfault+=1
            else:
                fault=False
        elif x in frame:
            fault=False
        else:
            fault=True
            fifo_totalfault+=1
            frame[bottom] = x
            bottom+=1
            if bottom>(N-1):
                bottom=0
        count+=1
        if root!=None:
            B_Label(frame,RefStr)
            column += 1
            E_label(frame)
            Fault(fault,N)
            root.after(2,lambda : FIFO(N,RefStr,root))
        else:
            FIFO(N,RefStr,root)
    else:
        if root!= None:
            Ratio(N,fifo_totalfault,q)





def LIFO(N,RefStr,root):
    global frame
    global index
    global top
    global lifo_totalfault
    global fault
    global column
    global count
    y=0
    x=len(RefStr)
    if count != x:
        column+=1
        y=RefStr[count]
        if None in frame:
            if y not in frame:
                fault=True
                frame[index]=y
                index+=1
                top+=1
                lifo_totalfault+=1
            else:
                fault=False
        elif y in frame:
            fault=False
        else:
            frame[top]=y
            fault=True
            lifo_totalfault+=1
            top-=1
            if top<0:
                top=len(frame)-1
        count+=1
        if root!=None:
            B_Label(frame,RefStr)
            column += 1
            E_label(frame)

            Fault(fault,N)
            root.after(2,lambda : LIFO(N,RefStr,root))
        else:
            LIFO(N,RefStr,root)

    else:
        if root!=None:
            Ratio(N, lifo_totalfault, x)


def OPR(N,RefStr,root):
    global frame
    global index
    global opr_totalfault
    global fault
    global column
    global count

    z = 0
    x = len(RefStr)
    if count != x:
        column += 1
        z = RefStr[count]
        if None in frame:
            if z not in frame:
                fault = True
                frame[index] = z
                index += 1

                opr_totalfault += 1
            else:
                fault = False
        elif z in frame:
            fault = False
        else :
            fault=True
            Dist = []
            for j in range(N):
                l=0
                for i in range(count+1,x):
                    if frame[j]==RefStr[i]:
                        break
                    else:
                        l+=1
                Dist.append(l)

            replace=max(Dist)
            idx=Dist.index(replace)
            frame[idx]=z
            opr_totalfault+=1
        count+=1
        if root!=None:
            B_Label(frame, RefStr)
            column += 1
            E_label(frame)

            Fault(fault, N)
            root.after(2, lambda: OPR(N, RefStr, root))
        else:
            OPR(N,RefStr,root)
    else:
        if root!=None:

            Ratio(N, opr_totalfault,x)



def LRU(N,RefStr,root):
    global frame
    global index
    global lru_totalfault
    global fault
    global column
    global count
    z = 0
    x = len(RefStr)
    if count != x:
        column += 1
        z = RefStr[count]
        if None in frame:
            if z not in frame:
                fault = True
                frame[index] = z
                index += 1
                lru_totalfault += 1
            else:
                fault = False
        elif z in frame:
            fault = False
        else :
            fault=True
            Dist = []
            for j in range(N):
                l=0
                for i in range(count-1,-1,-1):
                    if frame[j]==RefStr[i]:
                        break
                    else:
                        l+=1
                Dist.append(l)

            replace=max(Dist)
            idx=Dist.index(replace)
            frame[idx]=z
            lru_totalfault+=1
        count+=1
        if root!=None:
            B_Label(frame, RefStr)
            column += 1
            E_label(frame)

            Fault(fault, N)
            root.after(2, lambda: LRU(N, RefStr, root))
        else:
            LRU(N,RefStr,root)
    else:
        if(root!=None):
            Ratio(N, lru_totalfault, x)


def MRU(N,RefStr,root):
    global frame
    global index
    global mru_totalfault
    global fault
    global column
    global count
    z = 0
    x = len(RefStr)
    if count != x:
        column += 1
        z = RefStr[count]
        if None in frame:
            if z not in frame:
                fault = True
                frame[index] = z
                index += 1

                mru_totalfault += 1
            else:
                fault = False
        elif z in frame:
            fault = False
        else :
            fault=True
            rpl=RefStr[count-1]
            # print(f"The err {rpl}")
            rpl1=frame.index(rpl)
            # print(rpl1)                7 0 1 2 0 3 0 4 2 3 0 3 2 1 2 0 1
            frame[rpl1]=z

            mru_totalfault+=1
        count+=1
        if root!=None:
            B_Label(frame, RefStr)
            column += 1
            E_label(frame)

            Fault(fault, N)
            root.after(2, lambda: MRU(N, RefStr, root))
        else:
            MRU(N,RefStr,root)
    else:
        if root!=None:
            Ratio(N, mru_totalfault, x)


def RPR(N,RefStr,root):
    from random import randint
    global frame
    global index
    global rpr_totalfault
    global fault
    global column
    global count

    Random_Page = randint(0,N-1)
    z = 0
    x = len(RefStr)
    if count != x:
        column += 1
        z = RefStr[count]
        if None in frame:
            if z not in frame:
                fault = True
                frame[index] = z
                index += 1

                rpr_totalfault += 1
            else:
                fault = False
        elif z in frame:
            fault = False
        else :
            fault=True
            frame[Random_Page]=z
            rpr_totalfault+=1

        count+=1
        if root!=None:
            B_Label(frame, RefStr)
            column += 1
            E_label(frame)

            Fault(fault, N)
            root.after(2, lambda: RPR(N, RefStr, root))
        else:
            RPR(N,RefStr,root)
    else:
        if root!=None:
            Ratio(N, rpr_totalfault, x)


def FirstInFirstOut(n,refStr):
    global root0
    global root
    root0 = Tk()
    # root.attributes('-fullscreen', True)
    root0.configure(bg='black')
    root0.geometry("1400x950")
    canvas = Canvas(root0, bg='black')
    canvas.pack(side=TOP, fill=BOTH, expand=1)
    #
    xscrollbar = ttk.Scrollbar(root0, orient=HORIZONTAL, command=canvas.xview)
    xscrollbar.pack(side=BOTTOM, fill=X)
    #
    canvas.configure(xscrollcommand=xscrollbar.set)
    #
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))
    root = Frame(canvas, bg='black')
    canvas.create_window((0, 0), window=root, anchor="nw")

    # Label(root, text=" ",  bg='black',pady=20).grid(row=1, column=0)
    Label(root, text=" ", bg='black',pady=20).grid(row=0, column=0)
    Label(root,text="First  In  First  Out  Algorithem",borderwidth=3,relief=SUNKEN,bg='black',
          fg='white',pady=20,font="TimesNewRoman 20 bold").grid(row=1,column=0)
    Label(root, text=" ", bg='black', pady=20).grid(row=2, column=0)
    try:

        N = int(n)
        print(f'{N}')
        RefStr = list(map(int, refStr.split()))
    except ValueError as e:
        print('ERROR! Please enter a valid Number')
    k=N
    for i in range(int(n)):
        Label(root,text="Frame "+str(k),pady=10,padx=20,bg='black',fg='cyan',
              borderwidth=3,relief=SUNKEN).grid(row=(i+4),column=0)
        k-=1

    Parameters(N)
    FIFO(N,RefStr,root)
    root.mainloop()




def LastInFirstOut(n,refStr):
    global root0
    global root
    root0 = Tk()
    root0.geometry("1400x950")
    root0.configure(bg="black")
    # root.attributes('-fullscreen', True)
    canvas = Canvas(root0,bg='black')
    canvas.pack(side=TOP, fill=BOTH, expand=1)
    #
    xscrollbar = ttk.Scrollbar(root0, orient=HORIZONTAL, command=canvas.xview)
    xscrollbar.pack(side=BOTTOM, fill=X)
    #
    canvas.configure(xscrollcommand=xscrollbar.set)
    #
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))
    root = Frame(canvas,bg='black')
    canvas.create_window((0, 0), window=root, anchor="nw")

    Label(root,text=" ",bg='black',pady=20).grid(row=0,column=0)
    Label(root, text=" ", bg='black', pady=20).grid(row=2, column=0)
    Label(root,text=" Last In First Out ",bg='black',fg='white',bd=3,relief=SUNKEN,
          pady=20,padx=30,font="TimesNewRoman 20 bold").grid(row=1,column=0)
    try :
        N=int(n)
        RefStr=list(map(int,refStr.split()))
    except EXCEPTION as e:
        print("Invalid Format")

    k=N
    for i in range(int(n)):
        Label(root, text="Frame " + str(k), pady=10, padx=20, bg='black', fg='cyan',
              borderwidth=3, relief=SUNKEN).grid(row=(i + 4), column=0)
        k-=1

    Parameters(N)
    LIFO(N,RefStr,root)
    root.mainloop()


def LeastRecentlyUsed(n,refStr):
    global root0
    global root
    root0=Tk()
    # root.geometry("1000x850")
    root0.configure(bg='black')
    root0.geometry("1400x950")
    # root0.attributes('-fullscreen', True)

    canvas = Canvas(root0, bg='black')
    canvas.pack(side=TOP, fill=BOTH, expand=1)
    #
    xscrollbar = ttk.Scrollbar(root0, orient=HORIZONTAL, command=canvas.xview)
    xscrollbar.pack(side=BOTTOM, fill=X)
    #
    canvas.configure(xscrollcommand=xscrollbar.set)
    #
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))
    root = Frame(canvas, bg='black')
    canvas.create_window((0, 0), window=root, anchor="nw")

    Label(root, text=" ", bg='black', pady=20).grid(row=0, column=0)
    Label(root, text=" Least Recently Used", bg='black', fg='white', font="TimesNewRoman 20 bold", pady=20).grid(
        row=1, column=0)

    try:
        N = int(n)
        RefStr = list(map(int, refStr.split()))
    except EXCEPTION as e:
        print("Invalid Format")

    k = N
    for i in range(int(n)):
        Label(root, text="Frame " + str(k), pady=10, padx=20, bg='black', fg='cyan',
              borderwidth=3, relief=SUNKEN).grid(row=(i + 4), column=0)
        k -= 1
    Parameters(N)
    LRU(N, RefStr, root)
    root.mainloop()


def Optimal(n,refStr):
    global root0
    global root
    root0=Tk()
    # root.geometry("1000x850")
    root0.configure(bg='black')
    # root0.attributes('-fullscreen', True)
    root0.geometry("1400x950")
    canvas = Canvas(root0, bg='black')
    canvas.pack(side=TOP, fill=BOTH, expand=1)
    #
    xscrollbar = ttk.Scrollbar(root0, orient=HORIZONTAL, command=canvas.xview)
    xscrollbar.pack(side=BOTTOM, fill=X)
    #
    canvas.configure(xscrollcommand=xscrollbar.set)
    #
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))
    root = Frame(canvas, bg='black')
    canvas.create_window((0, 0), window=root, anchor="nw")

    Label(root,text=" ",bg='black',pady=20).grid(row=0,column=0)
    Label(root,text=" Optimal Page Replacement",bg='black',fg='white',
          font="TimesNewRoman 20 bold",pady=20).grid(row=1,column=0)

    try :
        N=int(n)
        RefStr=list(map(int,refStr.split()))
    except EXCEPTION as e:
        print("Invalid Format")

    k=N
    for i in range(int(n)):
        Label(root, text="Frame " + str(k), pady=10, padx=20, bg='black', fg='cyan',
              borderwidth=3, relief=SUNKEN).grid(row=(i + 4), column=0)
        k-=1
    Parameters(N)
    OPR(N,RefStr,root)
    root.mainloop()

def MostRecentlyUsed(n,refStr):
    global root0
    global root
    root0 = Tk()
    # root.geometry("1000x850")
    root0.configure(bg='black')
    root0.geometry("1400x950")
    # root.attributes('-fullscreen', True)
    canvas = Canvas(root0, bg='black')
    canvas.pack(side=TOP, fill=BOTH, expand=1)
    #
    xscrollbar = ttk.Scrollbar(root0, orient=HORIZONTAL, command=canvas.xview)
    xscrollbar.pack(side=BOTTOM, fill=X)
    #
    canvas.configure(xscrollcommand=xscrollbar.set)
    #
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))
    root = Frame(canvas, bg='black')
    canvas.create_window((0, 0), window=root, anchor="nw")

    Label(root, text=" ", bg='black', pady=20).grid(row=0, column=0)
    Label(root, text=" Most Recently Used ", bg='black', fg='white', font="TimesNewRoman 20 bold", pady=20).grid(
        row=1, column=0)

    try:
        N = int(n)
        RefStr = list(map(int, refStr.split()))
    except EXCEPTION as e:
        print("Invalid Format")

    k = N
    for i in range(int(n)):
        Label(root, text="Frame " + str(k), pady=10, padx=20, bg='black', fg='cyan',
              borderwidth=3, relief=SUNKEN).grid(row=(i + 4), column=0)
        k -= 1
    Parameters(N)
    MRU(N, RefStr, root)
    root.mainloop()

def Random_RAlgo(n,refStr):
    global root0
    global root
    root0 = Tk()
    # root.geometry("1000x850")
    root0.configure(bg='black')
    root0.geometry("1400x950")
    # root0.attributes('-fullscreen', True)
    canvas = Canvas(root0, bg='black')
    canvas.pack(side=TOP, fill=BOTH, expand=1)
    #
    xscrollbar = ttk.Scrollbar(root0, orient=HORIZONTAL, command=canvas.xview)
    xscrollbar.pack(side=BOTTOM, fill=X)
    #
    canvas.configure(xscrollcommand=xscrollbar.set)
    #
    canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))
    root = Frame(canvas, bg='black')
    canvas.create_window((0, 0), window=root, anchor="nw")

    Label(root, text=" ", bg='black', pady=20).grid(row=0, column=0)
    Label(root, text=" Random Replacement Algorithem ", bg='black', fg='white', font="TimesNewRoman 20 bold",
          pady=20).grid(row=1, column=0)

    try:
        N = int(n)
        RefStr = list(map(int, refStr.split()))
    except EXCEPTION as e:
        print("Invalid Format")

    k = N
    for i in range(int(n)):
        Label(root, text="Frame " + str(k), pady=10, padx=20, bg='black', fg='cyan',
              borderwidth=3, relief=SUNKEN).grid(row=(i + 4), column=0)
        k -= 1
    Parameters(N)
    RPR(N, RefStr, root)
    root.mainloop()

def Comp_Algo(n,refStr):
    global root
    try:
        N = int(n)
        RefStr = list(map(int, refStr.split()))
    except EXCEPTION as e:
        print("Invalid Format")
    Parameters(N)
    FIFO(N,RefStr,None)
    FIFO_Fault = fifo_totalfault / len(RefStr)

    Parameters(N)
    OPR(N, RefStr, None)
    OPR_Fault = opr_totalfault / len(RefStr)

    Parameters(N)
    LIFO(N,RefStr,None)
    LIFO_Fault = lifo_totalfault / len(RefStr)

    Parameters(N)
    LRU(N,RefStr,None)
    LRU_Fault = lru_totalfault / len(RefStr)

    Parameters(N)
    MRU(N,RefStr,None)
    MRU_Fault = mru_totalfault / len(RefStr)

    Parameters(N)
    RPR(N,RefStr,None)
    RPR_Fault = rpr_totalfault / len(RefStr)



    root = Tk()
    root.geometry("1500x900")
    # root.attributes('-fullscreen')
    root.configure(bg='black')

    f0=Frame(root,bg="black" ,bd=3 , relief=SUNKEN)
    # f0.pack(side=LEFT,anchor="n",fill=X)
    f0.place(x=0,y=0)
    # Label(f0, text=" ", bg='black', pady=20).pack()
    Label(f0, text=" Comparision Of Algoritherm", bg='black', fg='magenta', font="TimesNewRoman 20 bold", pady=20).pack(side=LEFT)



    k = N
    # f1=Frame(root,bg='black',bd=3,relief=SUNKEN)
    # f1.pack(side=LEFT,anchor='n',pady=20)
    # # f1.place(x=30,y=100)
    # # f2=Frame(root,bg='black',bd=3,relief=SUNKEN)
    # # f2.place(x=30,y=150)
    # # def Display(val):
    # #     Label(f2,text="This is all about mhy discription \n See YOu Next Time").pack()
    # #
    # # option = ["Description", "Total_Frames", "Total_Fault"]
    # # click=StringVar(f1)
    # # click.set("description")
    #
    #
    # drop=OptionMenu(f1,click,*option,command=Display,font="Comiscence 15 bold")
    # drop.pack(pady=25,padx=25)
    #
    f3=Frame(root,bg='black',bd=3,relief=SUNKEN)
    f3.place(x=600,y=10)



    def Display1(val):

        f4 = Frame(root, bg='black', bd=3, relief=SUNKEN)
        f4.place(x=700, y=100)
        # f5 = Frame(root, bg='black', bd=3, relief=SUNKEN)
        # f5.place(x=900, y=100)
        # print(fifo_totalfault)
        # print(lifo_totalfault)
        FIFO_Hit = 1-FIFO_Fault
        LIFO_Hit = 1- LIFO_Fault
        LRU_Hit = 1- LRU_Fault
        MRU_Hit = 1- MRU_Fault
        OPR_Hit = 1- OPR_Fault
        RPR_Hit = 1- RPR_Fault

        if val=='Hit Ratio':
            if f4 != None:
                # print('NO')
                f4.destroy()
                f4 = Frame(root, bg='black', bd=3, relief=SUNKEN)
                f4.place(x=500, y=100)


            fig = Figure(figsize=(5, 5), dpi=100,facecolor='purple')
            # ax = fig.add_axes([0,0,1,1])
            plot1 = fig.add_subplot(111)
            algo = ['FIFO', 'LIFO', 'LRU',"MRU", 'Optimal', 'Random']
            hit = [FIFO_Hit, LIFO_Hit, LRU_Hit,MRU_Hit, OPR_Hit, RPR_Hit]
            plot1.bar( algo,hit,color='red')

            plot1.set_xlabel('Algorithems')
            plot1.set_ylabel('Hit Ratio')
            canvas = FigureCanvasTkAgg(fig, master=f4)
            canvas.draw()

            # placing the canvas on the Tkinter window
            canvas.get_tk_widget().pack()

            # creating the Matplotlib toolbar
            toolbar = NavigationToolbar2Tk(canvas, f4)
            toolbar.update()

            # placing the toolbar on the Tkinter window
            canvas.get_tk_widget().pack()

            Label(f4, text=f"Here the Maximum Page Hit occured in {algo[hit.index(max(hit))]} "
                           f"\n So {algo[hit.index(max(hit))]} will take less time compare to other algorithem "
                  , bg='black', fg='lightgreen',font="timesnewroman 12 bold").pack(pady=10)




        else:
            if f4!=None:
                # print('NO')
                f4.destroy()
                f4 = Frame(root, bg='black', bd=3, relief=SUNKEN)
                f4.place(x=500, y=100)


            fig = Figure(figsize=(5, 5), dpi=100,facecolor='darkblue')
            # ax = fig.add_axes([0,0,1,1])
            plot1 = fig.add_subplot(111)
            algo = ['FIFO', 'LIFO', 'LRU', "MRU", 'Optimal', 'Random']
            fault = [FIFO_Fault, LIFO_Fault, LRU_Fault, MRU_Fault, OPR_Fault, RPR_Fault]
            plot1.bar(algo,fault ,color='g')
            plot1.set_xlabel('Algorithems')
            plot1.set_ylabel('Fault Ratio')
            canvas = FigureCanvasTkAgg(fig, master=f4)
            canvas.draw()

            # placing the canvas on the Tkinter window
            canvas.get_tk_widget().pack()

            # creating the Matplotlib toolbar
            toolbar = NavigationToolbar2Tk(canvas, f4)
            toolbar.update()

            # placing the toolbar on the Tkinter window
            canvas.get_tk_widget().pack()
            # canvas.get_tk_widget().place(x=0,y=0)
            Label(f4,text=f"Here the Maximum Page Fault occured in {algo[fault.index(max(fault))]} "
                          f"\n So {algo[fault.index(max(fault))]} will take more time compare to other algorithem "
                  , bg='black',fg='lightgreen',font="timesnewroman 12 bold").pack(pady=10)



    click1=StringVar(f3)
    click1.set("Hit_Ratio")
    sel=OptionMenu(f3,click1,'Hit Ratio',"Fault Ratio",command=Display1)
    sel.pack()

    root.mainloop()



root1 = Tk()
root1.config(bg='black')
# root1.maxsize(width=1500,height=900)
# root1.attributes('-fullscreen', True)
#root1.state('zoomed')
root1.geometry('858x500')
root1.maxsize(width=958,height=500)
root1.minsize(width=958,height=500)
root1.title("Operating System")
# root1.geometry("600x400")
file1 = Image.open('Home2.jpg')
# file= ImageTk.PhotoImage(file1)
background_Image=ImageTk.PhotoImage(file1,master=root1)

background_Label = Label(root1,image=background_Image,bg='black').place(x=0,y=0)

#Title
# Title_Image = PhotoImage(file = 'ss1.png',master= root1)
#Title_Image = PhotoImage(file = 'PNG 1.png',master= root1)
Title_Label= Label(root1,text="OPERATING SYSTEM VIRTUAL LAB",font="algerian 26 bold",bg='black',fg='lime').place(x=200,y=10)


Temp_Label = Label(root1,text="",bg='black').grid(row=1,column=0)
#Input
#Enter the number of frames
# Frame_Image = PhotoImage(file="f2.png",master= root1)
# Frame_Label= Label(root1,image=Frame_Image,bg='cyan').place(x=360,y=270)
# Frame_Entry=Entry(root1,borderwidth=5,width="30",font=20,relief=SUNKEN)
# Frame_Entry.place(x=260,y=230)


#Reference String
#Enter string seperated by a space
# String_Image = PhotoImage(file="rs1.png",master= root1)
# String_Label= Label(root1,image=String_Image,bg='cyan').place(x=1050,y=270)
# String_Entry=Entry(root1,borderwidth=5,width="30",font=30,relief=SUNKEN)
# String_Entry.place(x=950,y=230)


#Select an Algo
Select_Image0= Image.open('pr.jpg')
pagerep_Image=ImageTk.PhotoImage(Select_Image0)

Select_Image1= Image.open("cad.jpg")
concded_Image=ImageTk.PhotoImage(Select_Image1)

Select_Image2= Image.open("sa.jpg")
scheduling_Image=ImageTk.PhotoImage(Select_Image2)

Select_Image3= Image.open("ds.jpg")
discsch_Image=ImageTk.PhotoImage(Select_Image3)



Select_Button1 = Button(root1,image=pagerep_Image,borderwidth=0,bg='#021d28',
                        activebackground='#021d28',command=lambda: Choose_Algo())
Select_Button1.place(x=300,y=200)

# Select_Image= PhotoImage(file='selectalgo.png',master=root1)
class Concurrency_Deadlock:
    pass


Select_Button2 = Button(root1,image=concded_Image,borderwidth=0,bg='#021d28',
                        activebackground='#021d28',command=lambda: Concurrency_Deadlock())
Select_Button2.place(x=500,y=200)

# Select_Image= PhotoImage(file='selectalgo.png',master=root1)
class Schduling_Algo:
    pass

import CPUScheduling1
Select_Button3 = Button(root1,image=scheduling_Image,borderwidth=0,bg='#021d28',
                        activebackground='#021d28',command=lambda: CPUScheduling1.app())
Select_Button3.place(x=700,y=200)

import Discscheduling
Select_Button4 = Button(root1,image=discsch_Image,borderwidth=0,bg='#021d28',
                        activebackground='#021d28',command=lambda: Discscheduling.Discscheduling())
Select_Button4.place(x=100,y=200)

root1.mainloop()

# Frame_Entry.get(),String_Entry.get()