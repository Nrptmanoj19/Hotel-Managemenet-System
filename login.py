from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import random
import time
import datetime
import mysql.connector
from hotel import HotelManagementSystem
from customer import Cust_win
from room import Roombooking
from details import DetailsRoom


  

def main():
    win=Tk()
    obj=Login_Window(win)
    win.mainloop()

 
class Login_Window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        #self.var_email=StringVar()
        #self.var_pass=StringVar()

        #self.bg=ImageTk.PhotoImage("C:\Users\nrptm\Desktop\dbms h\back1.jpg ")
      
        #lbl_bg=Label(self.root,image=self.bg)
        #lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"C:\Users\nrptm\Desktop\5th sem textbooks\dbms h\login.jpg ")
        img1=img1.resize((90,90),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg="black",borderwidth=0)
        lblimg1.place(x=730,y=170,width=90,height=90)

        get_str=Label(frame,text="Get Started",font=("times now roman",20,"bold"),fg="white",bg="black")
        get_str.place(x=95,y=85)

        #label
        username=lbl=Label(frame,text="Username",font=("times new roman",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=125)

        self.txtuser=ttk.Entry(frame,font=("times new roman",15,"bold"))
        self.txtuser.place(x=40,y=150,width=270)

        password=lbl=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=195)

        self.txtpass=ttk.Entry(frame,font=("times new roman",15,"bold"),show="*")
        self.txtpass.place(x=40,y=220,width=270)

        #icon images
        img2=Image.open(r"C:\Users\nrptm\Desktop\5th sem textbooks\dbms h\username1.png")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg1=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=293,width=25,height=25)

        img3=Image.open(r"C:\Users\nrptm\Desktop\5th sem textbooks\dbms h\password.webp")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg1=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lblimg1.place(x=650,y=365,width=25,height=25)

#Loginbutton

        btn_login=Button(frame,text="Login",command=self.login,font=("times new roman",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        btn_login.place(x=110,y=270,width=120,height=35)

#register button

        registerbtn=Button(frame,text="New User Register",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=15,y=320,width=160)

        #forgot passwordbtn

        registerbtn=Button(frame,text="Forgot Password",command=self.forgot_password_window,font=("times new roman",10,"bold"),borderwidth=0,fg="white",bg="black",activeforeground="white",activebackground="black")
        registerbtn.place(x=10,y=340,width=160)

    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.obj=Register(self.new_window)


    
    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("Error","all fields required")
        elif  self.txtuser.get()=="kapu" and self.txtpass.get()=="ashu":
            messagebox.showinfo("Success","Welcome to the page")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="1234",database="management")
            mycursor=conn.cursor()
            mycursor.execute("select * from register1 where email=%s and password=%s",(
                                                                                        self.txtuser.get(),
                                                                                        self.txtpass.get()

                                                                                    ))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Invalid username and password")
            else:
                open_main=messagebox.askyesno("YesNo","Access only admin")
                if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.obj=HotelManagementSystem(self.new_window)
                else:
                    if not open_main:
                        return
            conn.commit()
            conn.close()

#reset password
    def reset_pass(self):
        if self.combo_secuirty_Q.get()=="Select":
            messagebox.showerror("Error","Select the security question",parent=self.root2)
        elif self.txt_security.get()=="":
            messagebox.showerror("Error","Please enter the answer",parent=self.root2)
        elif self.txt_newpass.get()=="":
            messagebox.showerror("Error","Please enter the new password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="1234",database="management")
            mycursor=conn.cursor()
            query=("select * from register1 where email=%s and securityQ=%s and securityA=%s")
            value=(self.txtuser.get(),self.combo_secuirty_Q.get(),self.txt_security.get(),)
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please enter the correct Answer",parent=self.root2)
            else:
                query=("update register1 set password=%s where email=%s")
                value=(self.txt_newpass.get(),self.txtuser.get())
                mycursor.execute(query,value)
                 
                conn.commit()
                conn.close()
                messagebox.showinfo("Info","Your password has been reset,please login new password",parent=self.root2)
                self.root2.destroy()






#forgot password window
    def forgot_password_window(self):
        if self.txtuser.get()=="":
            messagebox.showerror("Error","Please Enter the Email address to reset password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="1234",database="management")
            mycursor=conn.cursor()
            query=("select * from register1 where email=%s")
            value=(self.txtuser.get(),)
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            #print(row)

            if row==None:
                messagebox.showerror("My Error","Please Enter the valid username")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forgot Password")
                self.root2.geometry("340x450+610+170")

                l=Label(self.root2,text="Forgot Password",font=("times new roman",15,"bold"),fg="red",bg="white")
                l.place(x=0,y=10,relwidth=1)

                security_Q=Label(self.root2,text="Select Security Questions",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_Q.place(x=50,y=80)

                self.combo_secuirty_Q=ttk.Combobox(self.root2,font=("times now roman",15,"bold"),state="readonly")
                self.combo_secuirty_Q["values"]=("Select","Your Birth Place","Your Girlfriend name","Your Pet Name")
                self.combo_secuirty_Q.place(x=50,y=110,width=250)
                self.combo_secuirty_Q.current(0)


                security_A=Label(self.root2,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
                security_A.place(x=50,y=150)

                self.txt_security=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_security.place(x=50,y=180,width=250)


                new_password=Label(self.root2,text="New Password",font=("times new roman",15,"bold"),bg="white",fg="black")
                new_password.place(x=50,y=220)

                self.txt_newpass=ttk.Entry(self.root2,font=("times new roman",15))
                self.txt_newpass.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="Reset",font=("times new roman",15),fg="white",bg="green")
                btn.place(x=100,y=290)




    #reset password

    #def reset_pass(Self):
        #if self.combo_security_Q.get()=="select" or self.txt_security()=="" or self.txt_

class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1600x900+0+0")

        #variables
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_securityQ=StringVar()
        self.var_securityA=StringVar()
        self.var_pass=StringVar()
        self.var_confpass=StringVar()
        #self.var_check=StringVar()

        #bg image
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\nrptm\Desktop\5th sem textbooks\dbms h\login6.png")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)



        #left image

        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\nrptm\Desktop\5th sem textbooks\dbms h\login6.png")
        left_bg1=Label(self.root,image=self.bg1)
        left_bg1.place(x=50,y=100,width=470,relheight=550)

        #main frame
        frame=Frame(self.root,bg="white")
        frame.place(x=520,y=100,width=800,height=550)

        register_lbl=Label(frame,text="REGISTER HERE",font=("times now roman",20,"bold"),fg="darkgreen",bg="white")
        register_lbl.place(x=20,y=20)


        #label and entry

        #row1
        fname=Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=50,y=100)

        self.fname_entry=ttk.Entry(frame,textvariable=self.var_fname,font=("times new roman",15,"bold"))
        self.fname_entry.place(x=50,y=130,width=250)

        l_name=Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="black")
        l_name.place(x=370,y=100)

        self.txt_lname=ttk.Entry(frame,textvariable=self.var_lname,font=("times new roman",15))
        self.txt_lname.place(x=370,y=130,width=250)

        #row2

        contact=Label(frame,text="Contact No",font=("times new roman",15,"bold"),bg="white")
        contact.place(x=50,y=170)

        self.txt_contact=ttk.Entry(frame,textvariable=self.var_contact,font=("times new roman",15))
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame,text="Email",font=("times new roman",15,"bold"),bg="white",fg="black")
        email.place(x=370,y=170)

        self.txt_email=ttk.Entry(frame,textvariable=self.var_email,font=("times new roman",15))
        self.txt_email.place(x=370,y=200,width=250)

        #row3

        security_Q=Label(frame,text="Select Security Questions",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_Q.place(x=50,y=240)

        self.combo_secuirty_Q=ttk.Combobox(frame,textvariable=self.var_securityQ,font=("times now roman",15,"bold"),state="readonly")
        self.combo_secuirty_Q["values"]=("Select","Your Birth Place","Your Girlfriend name","Your Pet Name")
        self.combo_secuirty_Q.place(x=50,y=270,width=250)
        self.combo_secuirty_Q.current(0)


        security_A=Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white",fg="black")
        security_A.place(x=370,y=240)

        self.txt_security=ttk.Entry(frame,textvariable=self.var_securityA,font=("times new roman",15))
        self.txt_security.place(x=370,y=270,width=250)

        #row4

        pswd=Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        pswd.place(x=50,y=310)

        self.txt_pswd=ttk.Entry(frame,textvariable=self.var_pass,font=("times new roman",15,"bold"))
        self.txt_pswd.place(x=50,y=340,width=250)

        confirm_pswd=Label(frame,text="Confrim Password",font=("times new roman",15,"bold"),bg="white",fg="black")
        confirm_pswd.place(x=370,y=310)

        self.txt_confirm=ttk.Entry(frame,textvariable=self.var_confpass,font=("times new roman",15,"bold"))
        self.txt_confirm.place(x=370,y=340,width=250)

        #checkbutton

        self.var_check=IntVar()
        self.checkbtn=Checkbutton(frame,variable=self.var_check,text="i agree the terms and conditions",font=("times now roman",15,"bold"),onvalue=1,offvalue=0)
        self.checkbtn.place(x=50,y=380)

        #buttons
        #icon images
        img=Image.open(r"C:\Users\nrptm\Desktop\5th sem textbooks\dbms h\register.png")
        img=img.resize((200,55),Image.ANTIALIAS)
        self.photoimage=ImageTk.PhotoImage(img)
        b1=Button(frame,image=self.photoimage,command=self.register_data,borderwidth=0,cursor="hand2",font=("times now roman",15,"bold"),fg="white",bg="black")
        b1.place(x=10,y=420,width=200)

        img1=Image.open(r"C:\Users\nrptm\Desktop\5th sem textbooks\dbms h\login6.png")
        img1=img1.resize((200,45),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        b1=Button(frame,image=self.photoimage1,command=self.return_login,borderwidth=0,cursor="hand2",font=("times now roman",15,"bold"),fg="white",bg="black")
        b1.place(x=330,y=420,width=200)

#function declaration

    def register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_securityQ.get()=="Select":
            messagebox.showerror("Error","All fields are required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("Error","password & confirm password must be same")
        elif self.var_check.get()==0:
            messagebox.showerror("Error","Please Agree Our Terms And Condition")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="1234",database="management")
            mycursor=conn.cursor()
            query=("select * from register1 where email=%s")
            value=(self.var_email.get(),)
            mycursor.execute(query,value)
            row=mycursor.fetchone()
            if row!=None:
                messagebox.showerror("Error","User already exist,please try another email")
            else:
                mycursor.execute("insert into register1 values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                        self.var_fname.get(),
                                                                                        self.var_lname.get(),
                                                                                        self.var_contact.get(),
                                                                                        self.var_email.get(),
                                                                                        self.var_securityQ.get(),
                                                                                        self.var_securityA.get(),
                                                                                        self.var_pass.get()


                                                                                    ))
            conn.commit()
            conn.close()
            messagebox.showinfo("Success","Register Successfully")

    def return_login(self):
        self.root.destroy()

class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1550x800+0+0")

       # lbl_title=Label(self.root,text=" WELCOME",font=("times new roman",60,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        #lbl_title.place(x=10,y=20,width=1550,height=60)



        #first image

        img1=Image.open(r"C:\Users\nrptm\Desktop\5th sem textbooks\dbms h\light2.jpg")    #converts into backward slash
        img1=img1.resize((1550,140),Image.ANTIALIAS)         #antialias coverts high level image to low level
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=140)

        #logo

        img2=Image.open(r"C:\Users\nrptm\Desktop\5th sem textbooks\dbms h\logo.png")    #converts into backward slash
        img2=img2.resize((230,140),Image.ANTIALIAS)         #antialias coverts high level image to low level
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=230,height=140)


        lbl_title=Label(self.root,text="HOTEL MANAGEMENT SYSTEM",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=140,width=1550,height=50)



        main_frame=Frame(self.root,bd=4,relief=SUNKEN)
        main_frame.place(x=0,y=190,width=1550,height=620)




        #menu

        
        lbl_menu=Label(main_frame,text="MENU",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=230)


        #btn frame

        btn_frame=Frame(main_frame,bd=4,relief=SUNKEN)
        btn_frame.place(x=0,y=35,width=228,height=190)

        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details,width=22,font=("times now roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=1)

        room_btn=Button(btn_frame,text="ROOM",command=self.roombooking,width=22,font=("times now roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        room_btn.grid(row=1,column=0,pady=1)  

        details_btn=Button(btn_frame,text="DETAILS",command=self.details_room,width=22,font=("times now roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        details_btn.grid(row=2,column=0,pady=1)

        report_btn=Button(btn_frame,text="REPORT",width=22,font=("times now roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        report_btn.grid(row=3,column=0,pady=1)

        logout_btn=Button(btn_frame,text="LOGOUT",command=self.logout,width=22,font=("times now roman",14,"bold"),bg="black",fg="gold",bd=0,cursor="hand1")
        logout_btn.grid(row=4,column=0,pady=1)


        #right side image

        img3=Image.open(r"C:\Users\nrptm\Desktop\5th sem textbooks\dbms h\light3.webp")    #converts into backward slash
        img3=img3.resize((1310,590),Image.ANTIALIAS)         #antialias coverts high level image to low level
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg1=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lblimg1.place(x=225,y=0,width=1310,height=590)

        #down images

        
        img4=Image.open(r"C:\Users\nrptm\Desktop\5th sem textbooks\dbms h\myth.jpg")    #converts into backward slash
        img4=img4.resize((230,210),Image.ANTIALIAS)         #antialias coverts high level image to low level
        self.photoimg4=ImageTk.PhotoImage(img4)

        lblimg1=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lblimg1.place(x=0,y=225,width=230,height=210)
        
        
        img5=Image.open(r"C:\Users\nrptm\Desktop\5th sem textbooks\dbms h\food.jpg")    #converts into backward slash
        img5=img5.resize((230,190),Image.ANTIALIAS)         #antialias coverts high level image to low level
        self.photoimg5=ImageTk.PhotoImage(img5)

        lblimg1=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        lblimg1.place(x=0,y=420,width=230,height=190)

        



 

    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_win(self.new_window)

    def roombooking(self):
        self.new_window=Toplevel(self.root)
        self.app=Roombooking(self.new_window)

    def details_room(self):
        self.new_window=Toplevel(self.root)
        self.app=DetailsRoom(self.new_window)

    def logout(self):
        self.root.destroy()



         


if __name__=="__main__":
    main()