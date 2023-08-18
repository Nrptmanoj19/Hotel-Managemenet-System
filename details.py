from tkinter import *
from PIL import Image,ImageTk  
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from  tkinter import messagebox

class DetailsRoom:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1295x550+230+220")

#title
        lbl_title=Label(self.root,text="ROOMBOOKING DETAILS",font=("times new roman",18,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1295,height=50)


          #logo

        img2=Image.open(r"C:\Users\nrptm\Desktop\5th sem textbooks\dbms h\logo.png")    #converts into backward slash
        img2=img2.resize((100,40),Image.ANTIALIAS)         #antialias coverts high level image to low level
        self.photoimg2=ImageTk.PhotoImage(img2)

        lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
        lblimg.place(x=5,y=2,width=100,height=40)

         #labelframe

        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="New Room Add",font=("arial",12,"bold"),padx=2,)
        labelframeleft.place(x=5,y=50,width=540,height=350)

#labels and entries
        #custcontact

        lbl_floor=Label(labelframeleft,text="Floor",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_floor.grid(row=0,column=0,sticky=W)

        self.var_floor=StringVar()
        entry_floor=ttk.Entry(labelframeleft,textvariable=self.var_floor,font=("arial",13,"bold"),width=20)
        entry_floor.grid(row=0,column=1,sticky=W)

#Room NO
        lbl_RoomNo=Label(labelframeleft,text="Room No",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_RoomNo.grid(row=1,column=0,sticky=W)

        self.var_roomNo=StringVar() 
        entry_RoomNo=ttk.Entry(labelframeleft,textvariable=self.var_roomNo,font=("arial",13,"bold"),width=20)
        entry_RoomNo.grid(row=1,column=1,sticky=W)

#Room Type
        lbl_RoomType=Label(labelframeleft,text="Room Type",font=("arial",12,"bold"),padx=2,pady=6)
        lbl_RoomType.grid(row=2,column=0,sticky=W)

        self.var_RoomType=StringVar()
        entry_RoomType=ttk.Entry(labelframeleft,textvariable=self.var_RoomType,font=("arial",13,"bold"),width=20)
        entry_RoomType.grid(row=2,column=1,sticky=W)

         #buttons
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=412,height=40)

        btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial",12,"bold"),bg="black",fg="gold",width=10)
        btnAdd.grid(row=0,column=0,padx=1)


        btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial",12,"bold"),bg="black",fg="gold",width=10)
        btnUpdate.grid(row=0,column=1,padx=1)

        
        btnDelete=Button(btn_frame,text="Delete",command=self.delete,font=("arial",12,"bold"),bg="black",fg="gold",width=10)
        btnDelete.grid(row=0,column=2,padx=1)

        btnReset=Button(btn_frame ,text="Reset",command=self.reset_data,font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btnReset.grid(row=0,column=3,padx=1)

         #table frame search system

        Table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Show Room Details",font=("arial",12,"bold"),padx=2,)
        Table_Frame.place(x=600,y=55,width=600,height=350)

        Scroll_x=ttk.Scrollbar(Table_Frame,orient=HORIZONTAL)
        Scroll_y=ttk.Scrollbar(Table_Frame,orient=VERTICAL)

        self.room_table=ttk.Treeview(Table_Frame,column=("floor","roomno","roomType"),xscrollcommand=Scroll_x.set,yscrollcommand=Scroll_y.set)

        Scroll_x.pack(side=BOTTOM,fill=X)
        Scroll_y.pack(side=RIGHT,fill=Y)

        Scroll_x.config(command=self.room_table.xview)
        Scroll_y.config(command=self.room_table.yview)


        self.room_table.heading("floor",text="Floor")
        self.room_table.heading("roomno",text="Room-No")
        self.room_table.heading("roomType",text="Room Type")
        
        self.room_table["show"]="headings"

        self.room_table.column("floor",width=100)
        self.room_table.column("roomno",width=100)
        self.room_table.column("roomType",width=100)
        
        self.room_table.pack(fill=BOTH,expand=1)
        self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_floor.get()=="" or self.var_RoomType.get()=="":
            messagebox.showerror("Error","All fields are required")
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="management")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s)",(
                                                                    
                                                                            self.var_floor.get(),
                                                                            self.var_roomNo.get(),
                                                                            self.var_RoomType.get()
                                                                                              
                ))
                

              
                conn.commit()
                self.fetch_data()
                conn.close()                                                                
                messagebox.showinfo("Success","New Room Added Successfully",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"some thing went wrong:{str(es)}",parent=self.root)


    #fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="management")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from details")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
            conn.commit()
        conn.close()

    #get cursor
    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]

        self.var_floor.set(row[0])
        self.var_roomNo.set(row[1])
        self.var_RoomType.set(row[2])
      
   
    #update function
    def update(self):
        if self.var_floor.get()=="":
            messagebox.showerror("Error","Please enter floor number",parent=self.root)
        else:

            conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="management")
            my_cursor=conn.cursor()
            my_cursor.execute("update details set Floor=%s,RoomType=%s where RoomNo=%s",(

                                                                                        self.var_floor.get(),
                                                                                        self.var_RoomType.get(),
                                                                                        self.var_roomNo.get()
                                                                                                                                                                    
                                                                                        ))                  
                                                                                                                                                                        
                                                                                                                                                            

      

        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Update","New Room details has been updated successfully",parent=self.root)


    
#delete function

    def delete(self):
        delete=messagebox.askyesno("Hotel Management System","Do you want to delete this Room Details",parent=self.root)
        if delete>0:
            conn=mysql.connector.connect(host="localhost",username="root",password="1234",database="management")
            my_cursor=conn.cursor()  
            query="delete from details where RoomNo=%s"      
            value=(self.var_roomNo.get(),)
            my_cursor.execute(query,value)
        else:
            if not delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    
#reset function
    def reset_data(self):
        self.var_floor.set(""),
        self.var_roomNo.set(""),
        self.var_RoomType.set("")
        
      
        #self.var_paidtax.set()
        #self.var_actualtotal.set()
        #self.var_total.set()






if __name__=="__main__":
    root=Tk()
    obj=DetailsRoom(root)
    root.mainloop()