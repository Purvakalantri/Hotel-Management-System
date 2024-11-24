from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox


class DetailsRoom:
    def __init__(self,root):

            self.root=root
            self.root.title("CUSTOMER MANAGEMENT SYSTEM")
            self.root.geometry("1140x500+230+220")

            self.var_Floor=StringVar()
            self.var_RoomNo=StringVar()
            self.var_RoomType=StringVar()

            #---------------title------------------
            lbl_title=Label(self.root,text="Room Booking Details",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
            lbl_title.place(x=0,y=0,width=1295,height=50)

            #--------------logo------------------
            img2=Image.open(r"C:\Users\Prathamesh\Desktop\Hotel_management_system\Hotel_images\hotel images\logohotel.png")
            img2=img2.resize((100,40),Image.LANCZOS)
            self.photoimg2=ImageTk.PhotoImage(img2)

            lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
            lblimg.place(x=5,y=2,width=100,height=40)

            #------------label frame---------------
            labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="New room add",padx=2,font=("times new roman",12,"bold"))
            labelframeleft.place(x=5,y=50,width=600,height=350)


            #floor
            lbl_floor=Label(labelframeleft,text="Floor",font=("arial",12,"bold"),padx=2,pady=6)
            lbl_floor.grid(row=0,column=0)

            entry_floor=ttk.Entry(labelframeleft,textvariable=self.var_Floor,width=20,font=("arial",13,"bold"))
            entry_floor.grid(row=0,column=1,sticky="w")

            #Room no

            lbl_Room_no=Label(labelframeleft,text="Room No",font=("arial",12,"bold"),padx=2,pady=6)
            lbl_Room_no.grid(row=1,column=0)

            entry_Room_no=ttk.Entry(labelframeleft,textvariable=self.var_RoomNo,width=20,font=("arial",13,"bold"))
            entry_Room_no.grid(row=1,column=1,sticky="w")

            #Room type
            lbl_Room_type=Label(labelframeleft,text="Room type",font=("arial",12,"bold"),padx=2,pady=6)
            lbl_Room_type.grid(row=2,column=0)

            entry_Room_type=ttk.Entry(labelframeleft,textvariable=self.var_RoomType,width=20,font=("arial",13,"bold"))
            entry_Room_type.grid(row=2,column=1,sticky="w")

            #---------buttons----------
            btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
            btn_frame.place(x=400,y=150,width=100,height=135)

            btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial ",13,"bold"),bg="black",fg="gold",width=9)
            btnAdd.grid(row=0,column=0,padx=1)

            btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial ",13,"bold"),bg="black",fg="gold",width=9)
            btnUpdate.grid(row=1,column=0,padx=1)

            btnDelete=Button(btn_frame,text="Delete",command=self.Delete,font=("arial ",13,"bold"),bg="black",fg="gold",width=9)
            btnDelete.grid(row=2,column=0,padx=1)
            
            btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial ",13,"bold"),bg="black",fg="gold",width=9)
            btnReset.grid(row=3,column=0,padx=1)

            #-----------------table frame search system---------------
            labelTableframe=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Detials",padx=2,font=("times new roman",12,"bold"))
            labelTableframe.place(x=600,y=50,width=600,height=350)

            #--------scroll bar--------------------
            scroll_x=ttk.Scrollbar(labelTableframe,orient=HORIZONTAL)
            scroll_y=ttk.Scrollbar(labelTableframe,orient=VERTICAL)

            self.room_table=ttk.Treeview(labelTableframe,column=("Floor","RoomNo","RoomType"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
            scroll_x.pack(side=BOTTOM,fill=X)
            scroll_y.pack(side=RIGHT,fill=Y)

            scroll_x.config(command=self.room_table.xview)
            scroll_y.config(command=self.room_table.yview)

            self.room_table.heading("Floor",text="Floor")
            self.room_table.heading("RoomNo", text="Room No")
            self.room_table.heading("RoomType", text="Room Type")
           

            self.room_table["show"]="headings"
            #column
            self.room_table.column("Floor", width=100)
            self.room_table.column("RoomNo", width=100)
            self.room_table.column("RoomType", width=100)
            
            self.room_table.pack(fill=BOTH,expand=1)
            self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
            self.fetch_data()

    def add_data(self):
        if self.var_Floor.get()=="" or self.var_RoomNo.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="root",database="customer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into details values(%s,%s,%s)",(
                                                                                self.var_Floor.get(),
                                                                                self.var_RoomNo.get(),
                                                                                self.var_RoomType.get(),                                                                   

                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()                                                                                
                messagebox.showinfo("Success","New Room Added successfully",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="root",database="customer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from details")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
        conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]

        self.var_Floor.set(row[0]),
        self.var_RoomNo.set(row[1]),
        self.var_RoomType.set(row[2]),
    #Update function
    def update(self):
        if self.var_Floor.get()=="":
            messagebox.showerror("Error","Please enter Floor",parent=self.root)

        else:

            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="customer")
            my_cursor=conn.cursor()
            my_cursor.execute("update details set Floor=%s,RoomType=%s where RoomNo=%s",(
                 
                                                                                            self.var_Floor.get(),
                                                                                            self.var_RoomType.get(),
                                                                                            self.var_RoomNo.get()
                                                                                                                                               

                                                                                            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","floor details has been updated successfully",parent=self.root)

    def Delete(self):
        Delete = messagebox.askyesno("Confirm", "Do you want to delete this room details?", parent=self.root)
        
        if Delete > 0:  # User confirmed
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="root", database="customer")
                my_cursor = conn.cursor()
                
                query = "DELETE FROM details WHERE RoomNo=%s"
                value = (self.var_RoomNo.get(),)
                my_cursor.execute(query, value)
                conn.commit()  # Commit the changes immediately
                
                # Refresh the table data to show updated state
                self.fetch_data()
                
                messagebox.showinfo("Success", "Floor and room details have been deleted successfully", parent=self.root)
            
            except Exception as es:
                messagebox.showerror("Error", f"An error occurred: {str(es)}", parent=self.root)
            
            finally:

                conn.close()  # Ensure the connection is closed

        else:  # User declined deletion
            return 

    def reset(self):
        self.var_Floor.set(""),
        self.var_RoomNo.set(""),
        self.var_RoomType.set(""),
        
    
                    
        





            


if __name__=="__main__":
    root=Tk()
    obj=DetailsRoom(root)
    root.mainloop() 