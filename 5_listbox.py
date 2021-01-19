from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

listbox = Listbox(root, selectmode="extended", height=0)
listbox.insert(0, "apple")
listbox.insert(1, "strawberry")
listbox.insert(2, "banana")
listbox.insert(END, "watermelon")
listbox.insert(END, "grape")
listbox.pack()


def btncmd() :
    #listbox.delete(END)

    #print(listbox.size())

    #print(listbox.get(0, 2)) #start idx, end idx

    print(listbox.curselection())

btn = Button(root, text="CLICK!!!", command=btncmd)
btn.pack()

root.mainloop()