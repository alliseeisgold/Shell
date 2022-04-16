from tkinter import *

window = Tk()
window.title('Tkinter Intro')
window.geometry('800x400')
lbl = Label(window, text='Welcome to my own Shell', bg='black', fg='white')
    lbl.grid()
    username = os.getlogin()
    hostname = socket.gethostname()
    user = username + '@' + hostname + ':~'
    lbl2 = Label(window, text=user, bg='black', fg='white', font=('times new roman', 12, 'bold'))
    lbl2.grid()
    lbl2.grid()
    lbl2.grid()
    lbl2.grid()
    lbl2.grid()

window.mainloop()