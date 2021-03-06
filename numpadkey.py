from tkinter import *
from tkinter import ttk

def main():
    root = Tk()
    numpad = NumPad(root)
    root.mainloop()

class NumPad(ttk.Frame):
    def __init__(self, root):
        ttk.Frame.__init__(self, root)
        self.grid()
        self.numpad_create()

    def numpad_create(self):
        r = 1
        c = 0
        btn_list = [
        '7',  '8',  '9',
        '4',  '5',  '6',
        '1',  '2',  '3', '0']
        for b in btn_list:
            cmd= lambda: print(b)
            self.b= ttk.Button(self, text=b,width=5,command=cmd).grid(row=r,column=c)
            print(b)
            c += 1
            if c > 4:
                c = 0
                r += 1

main()