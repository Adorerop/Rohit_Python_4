from tkinter import *
import mysql.connector
import tkinter.messagebox as msg

def creat_conn():
    return mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="",
            database="game"
        )

def register_data():
    if e_email.get()=="" or e_name.get()=="" or e_mobile.get()=="" or e_password.get()=="":
        msg.showinfo("Registration Error","All Fields are mendetory")
    else:
        conn=creat_conn()
        cursor=conn.cursor()
        query="insert into genshin_impact(Email,Name,Mobile,Password) values(%s,%s,%s,%s)"
        args=(e_email.get(),e_name.get(),e_mobile.get(),e_password.get())
        cursor.execute(query,args)
        conn.commit()
        conn.close()
        e_email.delete(0,"end")
        e_name.delete(0,"end")
        e_mobile.delete(0,"end")
        e_password.delete(0,"end")
        msg.showinfo("Registration","Job well done")

def calcle_data():
    if e_email.get()=="" or e_name.get()=="" or e_mobile.get()=="" or e_password.get()=="":
        msg.showinfo("Error","First Write Something")
    else:
        e_email.delete(0,"end")
        e_name.delete(0,"end")
        e_mobile.delete(0,"end")
        e_password.delete(0,"end")
        msg.showinfo("Yoo","Job well done")

root=Tk()
root.geometry("350x350")
root.configure(bg="#483F3D")
root.title("Genshin Impact")
root.resizable(width=False,height=False)

l_email=Label(root,text="Email",font=("Ink Free",10),bg="#180602",fg="#FFFFFF")
l_email.place(x=50,y=50 )

l_name=Label(root,text="Name",font=("Ink Free",10),bg="#180602",fg="#FFFFFF")
l_name.place(x=50,y=100 )

l_mobile=Label(root,text="Mobile",font=("Ink Free",10),bg="#180602",fg="#FFFFFF")
l_mobile.place(x=50,y=150 )

l_password=Label(root,text="Password",font=("Ink Free",10),bg="#180602",fg="#FFFFFF")
l_password.place(x=50,y=200 )

e_email=Entry(root)
e_email.place(x=150,y=50)

e_name=Entry(root)
e_name.place(x=150,y=100)

e_mobile=Entry(root)
e_mobile.place(x=150,y=150)

e_password=Entry(root)
e_password.place(x=150,y=200)

register=Button(root,text=("Register") ,bg="#180602",fg="#FFFFFF",activebackground="#1FED1C",font=("Ink Free",15),command=register_data)
register.place(x=75,y=270)

calcle=Button(root,text=("Cancle") ,bg="#180602",fg="#FFFFFF",activebackground="#1FED1C",font=("Ink Free",15),command=calcle_data)
calcle.place(x=185,y=270)


root.mainloop()