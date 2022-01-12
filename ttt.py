import numpy as np
import os, time
from tkinter import ttk
from tkinter import font
from functools import partial
import tkinter as tk
import numpy as np

# tick tac toe game with GUI

root = tk.Tk()
root.configure(bg='black')

style = ttk.Style(root)
style.theme_use('alt')

bfont = font.Font(family='Courier', size=60)
lfont = font.Font(family='Courier', size=20)

buttons = np.empty((9), dtype=tk.Button)
pad = 60
turn = "O"

def ini(pad = pad):
    global buttons
    global turn
    global board
    turn = "O"
    board = np.zeros((9), dtype=str)
    for i in range(9):
        buttons[i]= (tk.Button(root,
                               text = " ",
                               padx= pad,
                               pady= pad,
                               bg = 'black',
                               fg = 'white',
                               command = partial(click, i),
                               font = bfont,
                               state = 'normal'
                               )
                    )
    draw()

def winner(arr):
    arr = np.reshape(arr, (3,3))
    def checkRows(arr_):  #loops through the rows, returns true if all are "O" or "X" in the row
        for i in arr_:
            if np.all(i == "X") or np.all(i == "O"):
                return True
    def checkDiagonals(arr_):
        return(
        np.all(arr.diagonal()=="O") or
        np.all(arr.diagonal()=="X") or
        np.all(np.fliplr(arr).diagonal()=="O") or
        np.all(np.fliplr(arr).diagonal()=="X"))

    return (
            checkRows(arr) or
            checkRows(arr.T) or #transpose (array.T) "turns" the array 90 degrees so that rows become columns
            checkDiagonals(arr)
            )

def click(i, pad = pad):
    global turn
    global board
    board[i] = turn
    print("click" + str(i))
    buttons[i].config(text = turn, state = 'disabled')
    if turn == "X":
        turn = "O"
    else:
        turn = "X"

    if winner(board):
        print("winner")
        txt = tk.Label(root, text="Winner!!!", bg = 'black', fg = 'white', padx = 24, font = lfont)
        txt.grid(row=4, column=1)

        again = tk.Button(root, text="Again?", font = lfont, bg = 'black', fg = 'white', command = ini)
        again.grid(row=5, column=1)
        for i in buttons:
            i.config(state = 'disabled')
    elif all(board):
        print("draw")
        txt = tk.Label(root, text="Draw!!!", bg = 'black', fg = 'white', padx = 24, font = lfont)
        txt.grid(row=4, column=1)

        again = tk.Button(root, text="Again?", font = lfont, bg = 'black', fg = 'white', command = ini)
        again.grid(row=5, column=1)
        for i in buttons:
            i.config(state = 'disabled')

    draw()

def draw(buttons = buttons):
    turn_txt = tk.Label(root, text="Turn: {}".format(turn),  bg = 'black', fg = 'white', padx = 30, font = lfont)
    turn_txt.grid(row = 0, column=1, )

    buttons = np.reshape(buttons, (3,3))
    for i in range(3):
        for j in range(3):
            buttons[i][j].grid(row=(i + 1), column=(j))
    buttons = np.reshape(buttons, (9))

ini()
root.mainloop()

