
from tkinter import *
import tkinter.messagebox
import csv

# Funktionen beim Öffnen

def einlesen():
    reader = csv.reader(open("liste.csv", "r"), delimiter=",")
    tasks = []
    for row in reader:
        tasks.append(row)
    return tasks

def alteanzeigen(tasks):
    for task in tasks:
        text = str(task).strip("['")                            #strip ist notwendig, damit die blöden ['...'] weggehen
        listbox_task.insert(END, text.strip("']"))
    return



# Funktionen für Buttons

def entertask():
    input_text = ""

    def add():
        input_text = entry_task.get(1.0, "end-1c")
        if input_text == "":
            tkinter.messagebox.showwarning(title="Warning!", message="Verkackt")
        else:
            listbox_task.insert(END, input_text)
            # close the root1 window
            root1.destroy()
        return

    root1 = Tk()
    root1.title("Add task")
    entry_task = Text(root1, width=40, height=4)
    entry_task.pack()
    button_temp = Button(root1, text="Add task", command=add)
    button_temp.pack()
    root1.mainloop()
    return



def deletetask():
    selected = listbox_task.curselection()
    listbox_task.delete(selected[0])
    return

def markcompleted():
    marked = listbox_task.curselection()
    temp = marked[0]
    temp_marked = listbox_task.get(marked)
    if "  - Done" in temp_marked:
        temp_marked = temp_marked.replace("  - Done", "")
    else:
        temp_marked += "  - Done"

    listbox_task.delete(temp)
    listbox_task.insert(temp, temp_marked)
    return


def speichern():
    taskliste = listbox_task.get(0, listbox_task.size())
    speicherliste = []
    for text in taskliste:
        aufgabe = [text]
        speicherliste.append(aufgabe)
    writer = csv.writer(open("liste.csv", "w"))
    writer.writerows(speicherliste)

def deletealltasks():
    listbox_task.delete(0, END)
    return

#Fenster

window = Tk()
window.title("Haas_ToDo")

frame_task = Frame(window)
frame_task.pack()

listbox_task = Listbox(frame_task, bg="Lightblue", fg="black", height=15, width=50, font="Arial")
listbox_task.pack(side=tkinter.LEFT)

# Scrollbar
scrollbar_task = Scrollbar(frame_task)
scrollbar_task.pack(side=tkinter.RIGHT, fill=tkinter.Y)
listbox_task.config(yscrollcommand=scrollbar_task.set)
scrollbar_task.config(command=listbox_task.yview)

# Buttons
entry_button = Button(window, text="Add task", width=50, command=entertask)
entry_button.pack(pady=3)

delete_button = Button(window, text="Delete selected task", width=50, command=deletetask)
delete_button.pack(pady=3)

mark_button = Button(window, text="Mark as completed ", width=50, command=markcompleted)
mark_button.pack(pady=3)

mark_button = Button(window, text="Save", width=50, command=speichern)
mark_button.pack(pady=3)

deleteall_button = Button(window, text="Delete all tasks", width=50, command=deletealltasks)
deleteall_button.pack(pady=3)



# Anzeigen der Einträge beim Öffnen

old = einlesen()
alteanzeigen(old)

window.mainloop()
