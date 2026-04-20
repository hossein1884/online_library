# from classes import *
# import tkinter as tk
# from tkinter import ttk

# def genre_insert():
#     GenresDataAdapter.insert(Genre(0, entry1.get()))

# window = tk.Tk()
# window.configure(bg="lightblue")
# window.title("my window")


# # Label
# label1 = tk.Label(window, text="enter genre name:", fg="black", bg="lightblue", font=("Arial", 18))
# label1.grid(row=0, column=0)

# # Entry
# entry1 = tk.Entry(window, bd=6, font=("Arial", 15))
# entry1.grid(row=0, column=1, sticky="ew", padx=10, pady=10)

# # Button
# button1 = tk.Button(window, text="ok", width=8, command=genre_insert)
# button1.grid(row=2, column=0, columnspan=2, pady=20)

# listbox1 = tk.Listbox(window)
# listbox1.grid(row=1, column=0)
# genres=""
# for genre in GenresDataAdapter.get_all():
#     genres+=str(genre)+"\n"

# listbox1.insert("end",genre)

# # listbox1.insert(f"{GenresDataAdapter.get_all()}")

# window.grid_columnconfigure(0, weight=0)
# window.grid_columnconfigure(1, weight=1)
# window.grid_rowconfigure(0, weight=1)

# window.mainloop()



















from classes import *
import tkinter as tk
from tkinter import ttk
cn = sqlite3.connect("books.db")
cur=cn.cursor()

def refresh_listbox():
    listbox1.delete(0, tk.END)  
    for genre in GenresDataAdapter.get_all():
        listbox1.insert("end", f"{genre.id} , {genre.name}")

def genre_insert():
    GenresDataAdapter.insert(Genre(0, entry1.get()))
    entry1.delete(0, tk.END)
    refresh_listbox() 

def on_select(event):
    if not listbox1.curselection():
        return

    index = listbox1.curselection()[0]
    value = listbox1.get(index)

    entry1.delete(0, tk.END)   
    entry1.insert(0, value)    


def update_genre():
    
    values = entry1.get().strip().split(',')
    genre=Genre(values[0],values[1])
    GenresDataAdapter.update(genre)
    
    

    refresh_listbox() 

window = tk.Tk()
window.configure(bg="lightblue")
window.title("my window")

label1 = tk.Label(window, text="enter genre name:", fg="black", bg="lightblue", font=("Arial", 18))
label1.grid(row=0, column=0, padx=10, pady=10)

entry1 = tk.Entry(window, bd=6, font=("Arial", 15))
entry1.grid(row=0, column=1, sticky="ew", padx=10, pady=10)

button1 = tk.Button(window, text="ok", width=8, command=update_genre)
button1.grid(row=2, column=0, columnspan=2, pady=20)

listbox1 = tk.Listbox(window, width=40, height=10, font=("Arial", 11))
listbox1.grid(row=1, column=0, columnspan=2, sticky="ew", padx=10, pady=10)
listbox1.bind("<<ListboxSelect>>", on_select)

refresh_listbox()

window.grid_columnconfigure(0, weight=0)
window.grid_columnconfigure(1, weight=1)
window.grid_rowconfigure(0, weight=1)

window.mainloop()

