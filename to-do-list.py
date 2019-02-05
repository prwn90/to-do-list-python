# To do list in Python! :)

import tkinter 
import random
from tkinter import messagebox

#Root window
root = tkinter.Tk()

# Root configure
root.configure(bg="snow")
root.title("My Super To Do List!")
root.geometry("400x300")

tasks = []


#FUNCTIONS

def update_listbox():
	clear_listbox()
	
	for task in tasks:
		lb_tasks.insert("end", task)
	
def clear_listbox():
	lb_tasks.delete(0, "end")
	
def add_task():
	task = txt_input.get()
	#Task is not empty
	if task !="":
			tasks.append(task)
			update_listbox()
	else:
			messagebox.showwarning("Warning", "Enter a task! :).")
	txt_input.delete(0, "end")
	

def del_all():
	confirmed = messagebox.askyesno("Please Confirm", "Do you want to delete all tasks? :)")
	if confirmed == True:
		global tasks
		tasks = []
		
		update_listbox()
	

def del_one():
	task = lb_tasks.get("active")
	
	if task in tasks:
		tasks.remove(task)

	update_listbox()

def sort_asc():
	tasks.sort()

	update_listbox()

def sort_desc():
	tasks.sort()
	tasks.reverse()

	update_listbox()

def choose_random():
	task = random.choice(tasks)
	lbl_display["text"]=task

def show_number_of_tasks():
	number_of_tasks = len(tasks)
	msg = "Number of tasks: %s" %number_of_tasks
	lbl_display["text"]=msg


lbl_title = tkinter.Label(root, text="TO DO LIST !", fg="#2c77c1", font="Halvetica 18 bold", bg="snow")
lbl_title.grid(row=0,column=0)

lbl_display = tkinter.Label(root, text="", bg="white")
lbl_display.grid(row=0,column=1)

txt_input = tkinter.Entry(root, width=25)
txt_input.grid(row=1,column=1)

btn_add_task = tkinter.Button(root, text="Add task", fg="snow", font="Halvetica 10 bold", bg="#22a30e", command=add_task)
btn_add_task.grid(row=1,column=0)

btn_del_all = tkinter.Button(root, text="Delete All", fg="snow", font="Halvetica 10 bold", bg="#d81c0f", command=del_all)
btn_del_all.grid(row=2,column=0)

btn_del_one = tkinter.Button(root, text="Delete", fg="snow", font="Halvetica 10 bold", bg="#ba190e", command=del_one)
btn_del_one.grid(row=3,column=0)

btn_sort_asc = tkinter.Button(root, text="Sort ascending", fg="snow", font="Halvetica 10 bold", bg="#1a4489", command=sort_asc)
btn_sort_asc.grid(row=4,column=0)

btn_sort_desc = tkinter.Button(root, text="Sort descending", fg="snow", font="Halvetica 10 bold", bg="#1a4489", command=sort_desc)
btn_sort_desc.grid(row=5,column=0)

btn_choose_random = tkinter.Button(root, text="Random", fg="snow", font="Halvetica 10 bold", bg="#1a4489", command=choose_random)
btn_choose_random.grid(row=6,column=0)

btn_number_of_tasks = tkinter.Button(root, text="Number of Tasks", fg="snow", font="Halvetica 10 bold", bg="#1a4489", command=show_number_of_tasks)
btn_number_of_tasks.grid(row=7,column=0)

btn_exit = tkinter.Button(root, text="Exit", fg="#181819", font="Halvetica 10 bold", bg="#e5e516", command=exit)
btn_exit.grid(row=8,column=0)

lb_tasks = tkinter.Listbox(root)
lb_tasks.grid(row=2,column=1, rowspan=7)


root.mainloop()