#worst task ever... Probieren ist nicht Programmieren. Mr.Google... >GGs









#import tkinter
#from tkinter import *                               #Import Library für Fenster
#window = Tk()                                       #definition name - window = Tk
#window.title("Haas_To_Do")                          #benennung des Fensters
#window.geometry("400x800")                          #größe des Fensters



#button1 = Button(window, text="Add Task")           #button1 mit funktion Button einfügen, definition wo, dann "text", geht auch ohne "window"
#button1.geometry("30x10")                          #WARUM FEHLER? Funktion mit width oder height fehlanzeige.
#button1.pack()
# = open(r'D:\OneDrive - Blue Air Systems GmbH\Desktop\Tasks.txt')  #Daten werden von Dateipfad geöffnet, r sollte read sein.


#button2 = Button(window, text="Delete Task")         # selbes spiel wie button 1
#button2.pack()

#button3 = Button(window, text="Finished Task")      # and again
#button3.pack()


import tkinter as tk
import tkinter.font as tkFont

app = tk.Tk()
app.geometry("400x800")

button1 = tk.Button(app,
                    text="Add",
                    width=10,               #Fenster zeigt mit sicherheit nicht 10x10, eher 20x40
                    height=10)              #Gleiches spiel hier

button2 = tk.Button(app,
                    text="Delete",
                    width=10,
                    height=10)

button1.pack(side=tk.LEFT)
button2.pack(side=tk.RIGHT)

app.mainloop()                      #mainloop alleine geht nicht. WARUM??









