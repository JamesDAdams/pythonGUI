from tkinter import *

cookie_count = 0


def add_cookie():
    global cookie_count
    cookie_count += 1
    label_counter.config(text=cookie_count)


# creer la fenetre
window = Tk()
window.title("G4-Bank")
window.geometry("720x480")
#window.config(background='#dee5dc')

# Construction d'un simple bouton
qb = Button(window, text='Quitter', command=window.quit)

# creer la frame principale
frame = Frame(window, bg='#dee5dc')


# ajout de la frame au centre
frame.pack(expand=YES)

# affichage
window.mainloop()