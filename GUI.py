# Chargement du module tkinter
from tkinter import * # pour Python2 ce serait Tkinter
from tkinter import ttk

# Construction de la fenêtre principale «root»
def main():
    root = Tk()
    root.title('G4 Bank')
    root.geometry("720x480")
    numpad = NumPad(root)
    buttonTest = ButtonTest(root)
    root.mainloop()

identifiant = "default"
password = ""

def setPassword(b):
    global password
    global identifiant
    if(b == "V"):
        identifiant = entryIdentifiant.get()
    elif(b == "X"):
        password = ""
        print(password)
    else:
        password = password + b
        print(password)

class ButtonTest(ttk.Frame):
    def __init__(self, root):
        ttk.Frame.__init__(self, root)
        self.grid()
        self.button_create()

    def button_create(self):
        #Label et entry identifiant
        labelIdentifiant = Label(self, text="n°identifiant:")
        labelIdentifiant.pack()
        entryIdentifiant = Entry(self,)
        entryIdentifiant.pack()

        #Label et entry password
        labelPassword = Label(self, text="password:")
        labelPassword.pack()
        entryPassword = Entry(self, )
        entryPassword.pack()

        # Construction d'un simple bouton
        qb = Button(self, text='Quitter', command=self.quit)
        qb.pack()

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
        '1',  '2',  '3', '0', 'X', 'V']
        for b in btn_list:
            cmd= lambda b=b: setPassword(b)
            self.b= ttk.Button(self, text=b,width=5,command=cmd).grid(row=r,column=c)
            c += 1
            if c > 4:
                c = 0
                r += 1

# Lancement de la «boucle principale»
main()
root.mainloop()

