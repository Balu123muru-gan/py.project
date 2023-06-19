from tkinter import*
import mysql.connector
from tkinter import messagebox
import sys

root=Tk()
root.title("webpage")
root.geometry("800x600")
##root.iconbitmap("sp.ico")

##h=root.winfo_screenheight()
##w=root.winfo_screenwidth()

root.configure(bg="blue")


#frame
frm=Frame(root,bg="green")
frm.place(x=250,y=90,height=550,width=1000)
frm1=Frame(frm,bg="#e5e4e2")
frm1.place(x=0,y=0,height=600,width=1000)
##frm2=Frame(frm1,bg='#e5e4e2')
##frm2.place(x=510,y=0,height=600,width=500)

#label
user=Label(frm,text="user name :",font=('bold',30))
user.place(x=150,y=150)
user=Entry(frm,font=('timesnewroman',30),bg="red")
user.place(x=450,y=150)
#lABEL2
##def password():
##    frm=Toplevel()
##    frm.title("webpage")
##    frm.geometry("800x600")
##    frm.mainloop()





password=Label(frm,text="password :",font=('bold',30))
password.place(x=150,y=300)
password=Entry(frm,font=('timesnewroman',30),bg="red")
password.place(x=450,y=300)
##word=Button(frm,text="password",font=('timesnewroman',10),bg="red",command=password)
##word.place(x=650,y=350)


    



def login():
         a=user.get()
         b=password.get()
         if a=="" and b=="":
                 messagebox.showinfo("message","some fields are empty")
         elif b=="":
                 messagebox.showinfo("message","fill in the password")

         else:
             try:
                 con=mysql.connector.connect(host="localhost",user="root",password="1234",database="live")
                 cur=con.cursor()
             except:
                 messagebox.showerror("error","connection error try again")
                 return
             cur.execute("select* from wire WHERE username='%s' and password='%s'"%(a,b))
             result=cur.fetchall()
             print(result)
             if len(result)>=1:
                 messagebox.showinfo("message","login success")

##             elif a!=result:
##                 messagebox.showinfo("message","create your signup account")
                 
             else:
                 messagebox.showerror("error","invalid user or password")





def signup():
        
        a=user.get()   
        b=password.get()
        
        if a=="" and b=="":
            messagebox.showinfo("message","All fields are empty")
        elif b=="":
                messagebox.showerror("message","fill in the password")

            
        else:
            try:
            
                conn=mysql.connector.connect(host="localhost",user="root",password="1234",database="live")

                cur=conn.cursor()
                cur.execute("insert into wire values('%s','%s')"%(a,b))
                output=cur.fetchall()
                for i in output:
                    print(i)
                conn.commit()
                messagebox.showinfo("message","account success")
            except:
                data="select *from wire where a=%s"
                cur.execute(data,user.get())

                if data!=None:
                     messagebox.showinfo("message","username already exits")
                
                
##            except:
##                if a==output[i]:
##                    messagebox.showinfo("message"," Alredy this used account ")
##                else:
##                    messagebox.showinfo("message"," signup new account ")
##                    




            

def clearfuc():
    user(0,'end')
    password(0,'end')
    user.focus()
        #input()
                                   

#BTN
login=Button(frm,text="Login",font=('bold',25),bg="green",fg="red",command=login)
login.place(x=450,y=450)



 #BTN2
login=Button(frm,text="Signup",font=('bold',25),bg="green",fg="red",command=signup)
login.place(x=700,y=450)
           





root.mainloop()
