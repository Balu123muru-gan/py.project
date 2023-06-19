from tkinter import*
import mysql.connector
from tkinter import messagebox
import sys

root=Tk()
root.title("webpage")
root.geometry("800x600")
##root.iconbitmap("sp.ico")
root.state("zoom")
h=root.winfo_screenheight()
w=root.winfo_screenwidth()

root.configure(bg="orange")


#frame
frm=Frame(root,bg="green")
frm.place(x=250,y=90,height=550,width=1000)
frm1=Frame(frm,bg="#0FF0F0")
frm1.place(x=0,y=0,height=600,width=1000)


#label
user=Label(frm,text="user name :",font=('bold',30))
user.place(x=150,y=150)
user=Entry(frm,font=('timesnewroman',30),bg="red")
user.place(x=450,y=150)




password=Label(frm,text="password :",font=('bold',30))
password.place(x=150,y=300)
password=Entry(frm,font=('timesnewroman',30),bg="red")
password.place(x=450,y=300)


def login():
    con=mysql.connector.connect(host="localhost",user='root',password='1234',database='live')
    u_name=user.get()
    p_word=password.get()
##    u_name=us_name.strip()
##    p_word=ps_word.strip()
    n=len(u_name)
    l=len(p_word)
    if l==0 or n==0:
        messagebox.showwarning("warning","USERNAME OR PASSWORD SHOULD NOT BE EMPTY")
        return
    cur=con.cursor()
    cur.execute("select * from wire")
    alldata=cur.fetchall()
    for i in alldata:
        if u_name==i[0]:
            if p_word==i[1]:
                messagebox.showinfo('RESULT','Login Successful')
                clearfun()
                break
            else:
                messagebox.showerror('Result',"Incorrect Password")
                up_tb.delete(0,'end')
                break
    else:
        messagebox.showerror('Result',"Invalid Username")
        clearfun()
    con.commit()
  
def signup(): 
    con=mysql.connector.connect(host="localhost",user='root',password='1234',database='live')
    us_name=user.get()
    ps_word=password.get()
    u_name=us_name.strip()
    print(u_name)
    p_word=ps_word.strip()
    n=len(u_name)
    l=len(p_word)
    if l==0 or n==0:
        messagebox.showwarning("warning","USERNAME OR PASSWORD SHOULD NOT BE EMPTY")
        return
    elif not(u_name.isupper()):
        messagebox.showwarning('Warning',"Please Use Only Capital Letters \n in UserName")
        return
    elif not(l>=8 and l<=12):
        messagebox.showwarning('Warning',"Password Must contain 8 to 12 characters")
        return
    else:
        pass

    a,b,c,d=0,0,0,0
    for j in p_word:
        if j>='A' and j<='Z':
            a=1
            continue
        if j>='a' and j<='z':
            b=1
            continue
        if j>='0' and j<='9':
            c=1
            continue
        if not((j>='A' and j<='Z') and (j>='a' and j<='z') and (j>='0' and j<='9')):
            d=1
            continue
    if a==1 and b==1 and c==1 and d==1:
        cur=con.cursor()
        cur.execute("select * from wire")
        alldata=cur.fetchall()

        for k in alldata:
            if u_name==k[0] or (u_name==k[0] and p_word==k[1]):
                    messagebox.showwarning('Result',"Same Username and Password\n is already exist")
                    messagebox.showinfo('Suggestion',"Please choose another Username")
                    
                    clearfun()
                    break
        else:
            cur=con.cursor()
            cur.execute("insert into wire values('%s','%s')"%(u_name,p_word))
            messagebox.showinfo('Result',"Signup Successful")
        con.commit()
    else:
        messagebox.showwarning('Warning',"weak password,Please use strong password")
        up_tb.delete(0,"end")





            
def clearfun():
    user.delete(0,'end')
    password.delete(0,"end")
    password.focus()

def Exit():
    wayOut = messagebox.askyesno("Login System", "Do you want to exit the system")
    if wayOut > 0:
        root.destroy()
        return
                                   

title=Label(root,text="Signup/Login Page",bg='blue',font=('Times',45),fg='red')
title.place(x=525,y=0)
#BTN
login=Button(frm,text="Login",height="1",width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="white",
                   bg="blue",command=login)
login.place(x=450,y=450)
#BTN2
login=Button(frm,text="Signup",height="1",width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="white",
                   bg="blue",command=signup)
login.place(x=700,y=450)

exity=Button(frm,text='Exit', height="1",width="10", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="white",
                   bg="blue",command=Exit)
exity.place(x=520,y=500)
    
root.mainloop()

#---------------------------------------------------------------------------------->
##from tkinter import *
##import tkinter.messagebox
##import mysql.connector
##
##
###connecting to the database
##connectiondb = mysql.connector.connect(host="localhost",user="root",passwd="1234",database="live")
##cursordb = connectiondb.cursor()
##
##
##def login():
##    global root2
##    root2 = Toplevel(root)
##    root2.title("Account Login")
##    root2.geometry("450x300")
##    root2.config(bg="white")
##
##    global username_verification
##    global password_verification
##    Label(root2, text='Please Enter your Account Details', bd=5,font=('arial', 12, 'bold'), relief="groove", fg="white",
##                   bg="blue",width=300).pack()
##    username_verification = StringVar()
##    password_verification = StringVar()
##    Label(root2, text="").pack()
##    Label(root2, text="Username :", fg="black", font=('arial', 12, 'bold')).pack()
##    Entry(root2, textvariable=username_verification).pack()
##    Label(root2, text="").pack()
##    Label(root2, text="Password :", fg="black", font=('arial', 12, 'bold')).pack()
##    Entry(root2, textvariable=password_verification, show="*").pack()
##    Label(root2, text="").pack()
##    Button(root2, text="Login", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'),command=login_verification).pack()
##    Label(root2, text="")
##
##def logged_destroy():
##    logged_message.destroy()
##    root2.destroy()
##
##def failed_destroy():
##    failed_message.destroy()
##
##def logged():
##    global logged_message
##    logged_message = Toplevel(root2)
##    logged_message.title("Welcome")
##    logged_message.geometry("500x100")
##    Label(logged_message, text="Login Successfully!... Welcome {} ".format(username_verification.get()), fg="green", font="bold").pack()
##    Label(logged_message, text="").pack()
##    Button(logged_message, text="Logout", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'), command=logged_destroy).pack()
##
##
##def failed():
##    global failed_message
##    failed_message = Toplevel(root2)
##    failed_message.title("Invalid Message")
##    failed_message.geometry("500x100")
##    Label(failed_message, text="Invalid Username or Password", fg="red", font="bold").pack()
##    Label(failed_message, text="").pack()
##    Button(failed_message,text="Ok", bg="blue", fg='white', relief="groove", font=('arial', 12, 'bold'), command=failed_destroy).pack()
##
##
##def login_verification():
##    user_verification = username_verification.get()
##    pass_verification = password_verification.get()
##    sql = "select * from wire where username = %s and password = %s"
##    cursordb.execute(sql,[(user_verification),(pass_verification)])
##    results = cursordb.fetchall()
##    if results:
##        for i in results:
##            logged()
##            break
##    else:
##        failed()
##
##def Exit():
##    wayOut = tkinter.messagebox.askyesno("Login System", "Do you want to exit the system")
##    if wayOut > 0:
##        root.destroy()
##        return
##
##def main_display():
##    global root
##    root = Tk()
##    root.config(bg="white")
##    root.title("Login System")
##    root.geometry("500x500")
##    Label(root,text='Welcome to Log In System',  bd=20, font=('arial', 20, 'bold'), relief="groove", fg="white",
##                   bg="blue",width=300).pack()
##    Label(root,text="").pack()
##    Button(root,text='Log In', height="1",width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="white",
##                   bg="blue",command=login).pack()
##    Label(root,text="").pack()
##    Button(root,text='Exit', height="1",width="20", bd=8, font=('arial', 12, 'bold'), relief="groove", fg="white",
##                   bg="blue",command=Exit).pack()
##    Label(root,text="").pack()
##
##main_display()
##root.mainloop()
