from tkinter import *
import os
import tkinter
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess

compiler = Tk()
compiler.title('Custom IDE                                                              untitled')
file_path = ''
file_name = ''

def set_file_path(path):
    global file_path
    file_path = path

def set_file_name(name):
    global file_name
    file_name = name
    title = "Custom IDE" + "                                                                " + name
    compiler.title(title)

def open_file():
    path = askopenfilename(filetypes=[('Python Files', '*.py')])
    with open(path, 'r') as file:
        code = file.read()
        editor.delete('1.0', END)
        editor.insert('1.0', code)
        set_file_path(path)
        name = os.path.basename(path)
        set_file_name(name)


def save_as():
    if file_path == '':
        path = asksaveasfilename(filetypes=[('Python Files', '*.py')])
    else:
        path = file_path
    with open(path, 'w') as file:
        code = editor.get('1.0', END)
        file.write(code)
        set_file_path(path)
        name = os.path.basename(path)
        set_file_name(name)


def run():
    if file_path == '':
        save_prompt = Toplevel()
        text = Label(save_prompt, text='Please save your code')
        text.pack()
        return
    command = f'python {file_path}'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    code_output.insert('1.0', output)
    code_output.insert('1.0',  error)

def autoCloseBracket():

    return 0

def bracket_parity_check(event):
    if event.char:      
    
        open_list = ["[","{","("]
        close_list = ["]","}",")"]
        stack = []
        textstring=editor.get("1.0","end")
        flag = False
        for i in textstring:
            if i in open_list:
                stack.append(i)
            elif i in close_list:
                if len(stack) > 0:
                    stack.pop()
                else:
                    flag = True
        if flag == True or len(stack)>0:
            print("Unbalanced")
            status_bar.config(text='Mismatched Brackets         ')
        else:
            print("Balanced")
            status_bar.config(text='Ready           ')
    return 0
menu_bar = Menu(compiler)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label='Open', command=open_file)
file_menu.add_command(label='Save', command=save_as)
file_menu.add_command(label='Save As', command=save_as)
file_menu.add_command(label='Exit', command=exit)
menu_bar.add_cascade(label='File', menu=file_menu)

run_bar = Menu(menu_bar, tearoff=0)
run_bar.add_command(label='Run', command=run)
menu_bar.add_cascade(label='Run', menu=run_bar)

compiler.config(menu=menu_bar)

editor = Text()
editor.pack()
editor.bind("<Key>", bracket_parity_check)


code_output = Text(height=10)
code_output.pack()
# editor.bind("<Key>", autoCloseBracket)
status_bar=Label(compiler , text='Ready         ',anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=5)

compiler.mainloop()