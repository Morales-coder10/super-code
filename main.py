# Python program to create a table
import  tkinter as tk
from tkinter import *


root = Tk()
root.title("entry boxes")





grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0]]

answ = [[3 ,1 ,6 ,5, 7 ,8, 4, 9 ,2],
        [5 ,2 ,9 ,1, 3 ,4 ,7, 6, 8],
        [4 ,8, 7 ,6 ,2, 9, 5, 3, 1],
        [2, 6 ,3, 4 ,1, 5, 9 ,8 ,7],
        [9,7, 4, 8, 6, 3, 1, 2, 5],
        [8,5, 1, 7, 9, 2, 6, 4, 3],
          [1, 3, 8 ,9 ,4 ,7 ,2 ,5 ,6],
          [6, 9, 2, 3, 5, 1, 8, 7, 4],
          [7 ,4 ,5, 2, 8 ,6 ,3 ,1 ,9]]



lis=[]


def tomar ():
    data = ''
    for num in lis:
        data += data + str(num.get())

        showData.config(text=data)

class tabla():
    def __init__(self,box):
        self.box = box
    for i in range(9):
        for j in range(9):
           box = Entry(root,width=3)
           box.insert(j,grid[i][j])
           box.grid(row=i, column=j, pady=20, padx=5)

tabla(lis)


revisar = Button(root,text='revisar',command=tomar)
revisar.grid(row=1,column=30,pady=5)




showData = Label(root,text='')
showData.grid(row=30,column=0,pady=10)




root.mainloop()
