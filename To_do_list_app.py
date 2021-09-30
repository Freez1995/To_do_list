import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

list_of_tasks = list()


def clear_text():
    task_entry.delete(0, 'end')
    del_task_entry.delete(0, 'end')


def add_task():
    task_counter = 0
    entered_task = task_entry.get()
    if len(entered_task) == 0:
        list_of_tasks.append(" ")
    else:
        list_of_tasks.append(entered_task)
    task = ""
    for x in range(len(list_of_tasks)):
        task_counter += 1
        task = str(task_counter) + ".    " + list_of_tasks[x][0].upper() + list_of_tasks[x][1:] + "\n"
    clear_text()
    tablica.insert("end", task)


def delete_task():
    task_counter_del = 0
    number = del_task_entry.get()
    try:
        if_number = int(number)
        list_of_tasks.pop(if_number-1)
        clear_text()
        tablica.delete(0, "end")
        for x in range(len(list_of_tasks)):
            task_counter_del += 1
            task = str(task_counter_del) + ".    " + list_of_tasks[x][0].upper() + list_of_tasks[x][1:] + "\n"
            tablica.insert("end", task)
    except:
        clear_text()
        messagebox.showerror("Error", "Please input task number '1' or check if list is empty")


def open_text():
    text_file = filedialog.askopenfilename(initialdir='::{20D04FE0-3AEA-1069-A2D8-08002B30309D}',
                                           title='Select file',
                                           filetypes=(('Text Document', '*.txt'), ))
    text_file = open(text_file, 'r')
    for line in text_file:
        list_of_tasks.append(line.strip())
    task_counter_open = 0
    for x in range(len(list_of_tasks)):
        task_counter_open += 1
        if list_of_tasks[x] == "":
            task = str(task_counter_open) + "."
        else:
            task = str(task_counter_open) + ".    " + list_of_tasks[x][0].upper() + list_of_tasks[x][1:] + "\n"
        tablica.insert("end", task)
    text_file.close()


def save_text():
    text_file_save = tk.filedialog.asksaveasfile(mode='w', defaultextension=".txt")
    if text_file_save is None:
        return
    for x in range(len(list_of_tasks)):
        text_file_save.writelines(str(list_of_tasks[x][0]).upper() + str(list_of_tasks[x][1:]) + "\n")
    text_file_save.close()


def quit_program():
    quit_option = messagebox.askquestion("Confirm exit", "Are you sure you want to exit without saving")
    if quit_option == 'yes':
        root.quit()
    else:
        return


def clear_all():
    list_of_tasks.clear()
    tablica.delete(0, "end")


def clear_search_del(event):
    del_task_entry.delete(0, "end")
    return


def clear_search_add(event):
    task_entry.delete(0, "end")
    return


root = tk.Tk()
HEIGHT = 350
WIDTH = 450
#   naziv aplikacije, prozor nije razluciv:
root.title("Task_reminder")
root.resizable(False, False)

#   ikona programa:
root.iconbitmap("app.ico")

#   velicina prozora:
prozor = tk.Canvas(root, height=HEIGHT, width=WIDTH)
prozor.pack()

#   window icon, Setting icon of master window:
p1 = tk.PhotoImage(file='Window_icon.png')
root.iconphoto(False, p1)

#  background image:
pozadina_image = tk.PhotoImage(file="background.png")
pozadina = tk.Label(root, image=pozadina_image)
pozadina.place(x=0, y=0)

#   unutarnji okvir:
okvir = tk.Frame(root, bg="#8f9294", bd=2)
okvir.place(relx=0.5, rely=0.025, relwidth=0.95, relheight=0.075, anchor="n")

#   naziv input result prozora:
name_label = tk.Label(okvir, text="To do list", bg="#8599a6", font="Arial 13 bold italic", anchor="w")
name_label.place(relx=0.01, rely=0.1, relwidth=0.981, relheight=0.8)

#   quit button:
quit_button = tk.Button(okvir, text="Quit", bg="#db5858", padx=15, font="Arial 10 bold", command=quit_program)
quit_button.place(relx=0.89, rely=0.1, relwidth=0.10, relheight=0.8)

#   save button:
save_button = tk.Button(okvir, text="Save", bg="#1aa80d", padx=15, font="Arial 10 bold", command=save_text)
save_button.place(relx=0.77, rely=0.1, relwidth=0.10, relheight=0.8)

#   open button:
open_button = tk.Button(okvir, text="Open", bg="#1aa80d", padx=15, font="Arial 10 bold", command=open_text)
open_button.place(relx=0.65, rely=0.1, relwidth=0.10, relheight=0.8)

#   unutarnji okvir2 and scroll:
okvir_donji = tk.Frame(root, bg="#8f9294", bd=5)
task_scroll_vertical = tk.Scrollbar(okvir_donji, orient="vertical")
task_scroll_horizontal = tk.Scrollbar(okvir_donji, orient="horizontal")
okvir_donji.place(relx=0.475, rely=0.14, relwidth=0.9, relheight=0.5, anchor="n")

#   tablica zadataka u unutarnjem okviru2 with scrollbar config:
tablica = tk.Listbox(okvir_donji, yscrollcommand=task_scroll_vertical.set, xscrollcommand=task_scroll_horizontal.set,
                     font="Arial 9 bold")
task_scroll_vertical.config(command=tablica.yview)
task_scroll_horizontal.config(command=tablica.xview)
task_scroll_vertical.pack(side="right", fill="y")
task_scroll_horizontal.pack(side="bottom", fill="x")
tablica.pack(fill="both", expand=1)

#   button add task:
add_task_button = tk.Button(root, text="Add task", bg="#1aa80d", padx=15, font="Arial 10 bold", command=add_task)
add_task_button.place(relx=0.1, rely=0.7, relwidth=0.15, relheight=0.05)

#   button add entry:
task_entry = tk.Entry(root, font="Arial 10", bd=2)
task_entry.insert(0, "Enter your task")
task_entry.bind("<Button-1>", clear_search_add)
task_entry.place(relx=0.3, rely=0.69, relwidth=0.4, relheight=0.06)

#   button delete task:
delete_task_button = tk.Button(root, text="Delete task", bg="#db5858", padx=15, font="Arial 10 bold",
                               command=delete_task)
delete_task_button.place(relx=0.05, rely=0.8, relwidth=0.2, relheight=0.05)

#   button delete entry:
del_task_entry = tk.Entry(root, font="Arial 10 ", bd=2)
del_task_entry.place(relx=0.3, rely=0.80, relwidth=0.1, relheight=0.06)
del_task_entry.insert(0, "1")
del_task_entry.bind("<Button-1>", clear_search_del)

#   clear all button:
clear_all_button = tk.Button(root, text="Clear\n all", bg="#db5858", padx=15, font="Arial 10 bold", command=clear_all)
clear_all_button.place(relx=0.75, rely=0.85, relwidth=0.2, relheight=0.1)

root.mainloop()
