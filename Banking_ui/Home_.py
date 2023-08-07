import mysql.connector as con
import acc_creation_ as ac
import Login_ as lg 
import tkinter as tk

# Tkinter Window

HOME = tk.Tk()
HOME.title("Home Screen")
HOME.state('zoomed')
HOME.config(bg='#12aaaa')


def exxit():
    HOME.destroy()
# Menu Buttons

home = tk.Label(HOME, text = 'Welcome' ,font = ('Arial' , 75) , bg='#12aaaa' , fg='black')
home.place(x=450,y=100)

Login = tk.Button(HOME, text = 'Login' ,command=lambda : lg.create_login() ,  font = ('Arial',35) , bg = 'orange' , fg = 'black')
Login.place(x=600,y=500)

acc = tk.Label(HOME , text = "Don't have an account ??" , font=('Arial', 18) , bg = '#12aaaa' , fg='green' )
acc.place(x=430,y=640)

create_acc = tk.Button(HOME, text='Create Account',command=lambda : ac.create_account() , font=('Arial', 19) , bg='yellow' , fg='black')
create_acc.place(x=550, y=680)

ext = tk.Button(HOME , text = "EXIT" , font=('Arial', 20), command = exxit , bg = 'white' , fg='green' )
ext.place(x=50,y=600)

HOME.mainloop()