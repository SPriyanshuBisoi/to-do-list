import tkinter
from tkinter import *
root=Tk()
root.title("To_Do_List")
root.geometry("400x650+400+100")
root.resizable(False,False)
root.configure(bg="#92D5C2") 
task_list=[]
def addTask():
    task = task_entry.get()
    task_entry.delete(0,END)

    if task:
        with open("E:/pip/to do list/file.txt",'a')as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END,task)
def deletetask():
    global task_list
    task=str(listbox.get(ANCHOR))
    if task in task_list:
        task_list.remove(task)
        with open("to do list/file.txt",'w')as taskfile:
            for task in task_list:
                taskfile.write(task+"\n")
        listbox.delete(ANCHOR)
        
def openTaskFile():
    try:
        global task_list
        with open("E:/pip/to do list/file.txt","r")as taskfile:
            tasks=taskfile.readlines()

        for task in tasks:
            if task !='\n':
                task_list.append(task)
                listbox.insert(END,task)
    except:
        file=open("E:/pip/to do list/file.txt","w")
        file.close()

Image_icon=PhotoImage(file="to do list/task.png")
root.iconphoto(False,Image_icon)
TopImage=PhotoImage(file="E:/pip/to do list/topbar.png")
Label(root,image=TopImage,bg="#92D5C2").pack()
dockImage=PhotoImage(file="to do list/dock.png")
Label(root,image=dockImage,bg="#3c345c").place(x=28,y=28)
noteImage=PhotoImage(file="to do list/task.png")
Label(root,image=noteImage,bg="#3c345c").place(x=330,y=25)
heading=Label(root,text="WHAT TO DO",font="arial 20 bold",fg="white",bg="#3c345c")
heading.place(x=110,y=20)

frame= Frame(root,width=400,height=50,bg="white")
frame.place(x=0,y=85)
task=StringVar()
task_entry=Entry(frame,width=18,font="areal 20",bd=0)
task_entry.place(x=10,y=7)
task_entry.focus()

button=Button(frame,text="ADD",font="arial 20 bold",width=6,bg="#3c345c",fg="#FF9B9B",bd=0,command=addTask)
button.place(x=300,y=0)

frame1=Frame(root,bd=3,width=700,height=280,bg="#3c345c")
frame1.pack(pady=(60,0))
listbox=Listbox(frame1,font="arial 14 bold",width=33,height=18,bg="#3c345c",fg="#FF9B9B",cursor="hand2",selectbackground="#3c345c")
listbox.pack(side=LEFT,fill=BOTH,padx=2)
Scrollbar=Scrollbar(frame1)
Scrollbar.pack(side=RIGHT,fill=BOTH)
listbox.config(yscrollcommand=Scrollbar.set)
Scrollbar.config(command=listbox.yview)

openTaskFile()
Delete_icon=PhotoImage(file="to do list/delete.png")
Button(root,image=Delete_icon,bg="#92D5C2",bd=0,command=deletetask).pack(side=BOTTOM,pady=13)

root.mainloop()