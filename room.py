from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
from time import strftime
from datetime import datetime
import mysql.connector
from tkinter import messagebox


class Room_booking:
    def __init__(self,root):

            self.root=root
            self.root.title("CUSTOMER MANAGEMENT SYSTEM")
            self.root.geometry("1140x500+230+220")
            
            #--------------variables-------------
            self.var_contact=StringVar()
            self.var_checkin=StringVar()
            self.var_checkout=StringVar()
            self.var_roomtype=StringVar()
            self.var_avialableroom=StringVar()
            self.var_noofdays=StringVar()
            self.var_tax=StringVar()
            self.var_actualprice=StringVar()
            self.var_total=StringVar()

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
            labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Booking",padx=2,font=("times new roman",12,"bold"))
            labelframeleft.place(x=5,y=50,width=425,height=490)

            #=============labels and entries---------------
            #Customer contact
            lbl_cust_Contact=Label(labelframeleft,text="Customer Contact",font=("arial",12,"bold"),padx=2,pady=6)
            lbl_cust_Contact.grid(row=0,column=0)

            entry_Contact=ttk.Entry(labelframeleft,textvariable=self.var_contact,width=20,font=("arial",13,"bold"))
            entry_Contact.grid(row=0,column=1,sticky="w")

            #fetch button
            
            btnfetch=Button(labelframeleft,command=self.fetch_contact,text="fetch data",font=("arial ",10,"bold"),bg="black",fg="gold",width=8)
            btnfetch.place(x=335,y=3)

            #check_in_date
            check_in_date=Label(labelframeleft,text="Check in date",font=("arial",12,"bold"),padx=2,pady=6)
            check_in_date.grid(row=1,column=0)

            entry_check_in_date=ttk.Entry(labelframeleft,textvariable=self.var_checkin,width=29,font=("arial",13,"bold"))
            entry_check_in_date.grid(row=1,column=1,sticky="w")

            #check_out_date
            check_out_date=Label(labelframeleft,text="Check out date",font=("arial",12,"bold"),padx=2,pady=6)
            check_out_date.grid(row=2,column=0)

            entry_check_out_date=ttk.Entry(labelframeleft,textvariable=self.var_checkout,width=29,font=("arial",13,"bold"))
            entry_check_out_date.grid(row=2,column=1,sticky="w")

            #Room type
            room_type=Label(labelframeleft,text="Room type",font=("arial",12,"bold"),padx=2,pady=6)
            room_type.grid(row=3,column=0)

            combo_roomtype=ttk.Combobox(labelframeleft,textvariable=self.var_roomtype,font=("arial",12,"bold"),width=27,state="readonly")
            combo_roomtype["value"]=("Single","duplex","luxary")
            combo_roomtype.current(0)
            combo_roomtype.grid(row=3,column=1,sticky="w")

            #Room available
            Available_room=Label(labelframeleft,text="Available room",font=("arial",12,"bold"),padx=2,pady=6)
            Available_room.grid(row=4,column=0)

            #copied data from details table
            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="customer")
            my_cursor=conn.cursor()
            my_cursor.execute("select RoomNo from details")
            rows=my_cursor.fetchall()

            combo_RoomNo=ttk.Combobox(labelframeleft,textvariable=self.var_avialableroom,font=("arial",12,"bold"),width=27,state="readonly")
            combo_RoomNo["value"]=rows
            combo_RoomNo.current(0)
            combo_RoomNo.grid(row=4,column=1,sticky="w")

            

            #no of days
            no_of_days=Label(labelframeleft,text="No of days",font=("arial",12,"bold"),padx=2,pady=6)
            no_of_days.grid(row=5,column=0)

            entry_noofdays=ttk.Entry(labelframeleft,textvariable=self.var_noofdays,width=29,font=("arial",13,"bold"))
            entry_noofdays.grid(row=5,column=1,sticky="w")
            
            
            # paid tax
            paid_tax=Label(labelframeleft,text="Tax",font=("arial",12,"bold"),padx=2,pady=6)
            paid_tax.grid(row=6,column=0)

            entry_tax=ttk.Entry(labelframeleft,textvariable=self.var_tax,width=29,font=("arial",13,"bold"))
            entry_tax.grid(row=6,column=1,sticky="w")

            #Cost of room
            room_cost=Label(labelframeleft,text="Room cost",font=("arial",12,"bold"),padx=2,pady=6)
            room_cost.grid(row=7,column=0)

            entry_roomcost=ttk.Entry(labelframeleft,textvariable=self.var_actualprice,width=29,font=("arial",13,"bold"))
            entry_roomcost.grid(row=7,column=1,sticky="w")
            
            #total cost
            total_cost=Label(labelframeleft,text="Total cost",font=("arial",12,"bold"),padx=2,pady=6)
            total_cost.grid(row=8,column=0)

            entry_totalcost=ttk.Entry(labelframeleft,textvariable=self.var_total,width=29,font=("arial",13,"bold"))
            entry_totalcost.grid(row=8,column=1,sticky="w")
            
            #billl button
            btnBill=Button(labelframeleft,text="Bill",command=self.total,font=("arial ",10,"bold"),bg="black",fg="gold",width=5)
            btnBill.grid(row=9,column=0,padx=1)


            #-------buttons--------------

            btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
            btn_frame.place(x=0,y=350,width=412,height=40)

            btnAdd=Button(btn_frame,text="Add",command=self.add_data,font=("arial ",13,"bold"),bg="black",fg="gold",width=9)
            btnAdd.grid(row=0,column=0,padx=1)

            btnUpdate=Button(btn_frame,text="Update",command=self.update,font=("arial ",13,"bold"),bg="black",fg="gold",width=9)
            btnUpdate.grid(row=0,column=1,padx=1)

            btnDelete=Button(btn_frame,text="Delete",command=self.Delete,font=("arial ",13,"bold"),bg="black",fg="gold",width=9)
            btnDelete.grid(row=0,column=3,padx=1)
            
            btnReset=Button(btn_frame,text="Reset",command=self.reset,font=("arial ",13,"bold"),bg="black",fg="gold",width=9)
            btnReset.grid(row=0,column=4,padx=1)

            #---------------right side image----------------

            img3=Image.open(r"C:\Users\Prathamesh\Desktop\Hotel_management_system\Hotel_images\hotel images\bed.jpg")
            img3=img3.resize((550,200),Image.LANCZOS)
            self.photoimg3=ImageTk.PhotoImage(img3)

            lblimg=Label(self.root,image=self.photoimg3,bd=0,relief=RIDGE)
            lblimg.place(x=750,y=55,width=550,height=200)

            #-----------------table frame search system---------------
            labelTableframe=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and search system",padx=2,font=("times new roman",12,"bold"))
            labelTableframe.place(x=435,y=250,width=700,height=200)
            
            #search bar
            lbl_Searchbar=Label(labelTableframe,text="Searchbar",font=("arial ",12,"bold"),bg="red",fg="white")
            lbl_Searchbar.grid(row=0,column=0,sticky="w")

            self.search_var=StringVar()
            combo_Search=ttk.Combobox(labelTableframe,textvariable=self.search_var,font=("arial",12,"bold"),width=24,state="readonly")
            combo_Search["value"]=("Contact","Availableroom")
            combo_Search.current(0)
            combo_Search.grid(row=0,column=1,sticky="w")
        
            self.txt_var=StringVar()
            entry_Search=ttk.Entry(labelTableframe,textvariable=self.txt_var,width=15,font=("arial ",13,"bold"))
            entry_Search.grid(row=0,column=2,sticky="w",padx=2)

            btnSearch=Button(labelTableframe,text="Search",command=self.search_btn,font=("arial ",13,"bold"),bg="black",fg="gold",width=9)
            btnSearch.grid(row=0,column=3,padx=1)

            btnShowAll=Button(labelTableframe,command=self.fetch_data,text="Show All",font=("arial ",13,"bold"),bg="black",fg="gold",width=9)
            btnShowAll.grid(row=0,column=4,padx=1)

            #---------------show data table-------------------
            details_table=Frame(labelTableframe,bd=2,relief=RIDGE)
            details_table.place(x=0,y=50,width=850,height=130)

            #scroll bar
            scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
            scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

            self.room_table=ttk.Treeview(details_table,column=("Contact","checkinDate","checkoutDate","roomtype","Availableroom","noofdays","tax","roomcost","totalcost"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
            scroll_x.pack(side=BOTTOM,fill=X)
            scroll_y.pack(side=RIGHT,fill=Y)

            scroll_x.config(command=self.room_table.xview)
            scroll_y.config(command=self.room_table.yview)

            self.room_table.heading("Contact",text="Contact")
            self.room_table.heading("checkinDate", text="Check in date")
            self.room_table.heading("checkoutDate", text="Check out date")
            self.room_table.heading("roomtype", text="Room type")
            self.room_table.heading("Availableroom", text="Available room")
            self.room_table.heading("noofdays", text="No of days")
            
            

            self.room_table["show"]="headings"
            #column
            self.room_table.column("Contact", width=100)
            self.room_table.column("checkinDate", width=100)
            self.room_table.column("checkoutDate", width=100)
            self.room_table.column("roomtype", width=100)
            self.room_table.column("Availableroom", width=100)
            self.room_table.column("noofdays", width=150)
            
            self.room_table.pack(fill=BOTH,expand=1)
            self.room_table.bind("<ButtonRelease-1>",self.get_cursor)
            self.fetch_data()

    #--------------------add function for data----------------
    def add_data(self):
        if self.var_contact.get()=="" or self.var_checkin.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="root",database="customer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s)",(
                                                                                self.var_contact.get(),
                                                                                self.var_checkin.get(),
                                                                                self.var_checkout.get(),
                                                                                self.var_roomtype.get(),
                                                                                self.var_avialableroom.get(),
                                                                                self.var_noofdays.get()
                                                                                

                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()                                                                                
                messagebox.showinfo("Success","Room has been Booked",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)

    #to fetch data from sql
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="root",database="customer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from room")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("",END,values=i)
        conn.commit()
        conn.close()


    #get cursor function once clicked then all data is visible on the screen 
    def get_cursor(self,event=""):
        cursor_row=self.room_table.focus()
        content=self.room_table.item(cursor_row)
        row=content["values"]

        self.var_contact.set(row[0]),
        self.var_checkin.set(row[1]),
        self.var_checkout.set(row[2]),
        self.var_roomtype.set(row[3]),
        self.var_avialableroom.set(row[4]),
        self.var_noofdays.set(row[5])


    #Update function
    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)

        else:

            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="customer")
            my_cursor=conn.cursor()
            my_cursor.execute("update room set check_in_Date=%s,check_out_Date=%s,roomtype=%s,Availableroom=%s,noofdays=%s where Contact=%s",(
                 
                                                                                                                                                self.var_checkin.get(),
                                                                                                                                                self.var_checkout.get(),
                                                                                                                                                self.var_roomtype.get(),
                                                                                                                                                self.var_avialableroom.get(),
                                                                                                                                                self.var_noofdays.get(),
                                                                                                                                                self.var_contact.get()

                                                                                                                                            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Room details has been updated successfully",parent=self.root)
                 
    def Delete(self):
        Delete = messagebox.askyesno("Confirm", "Do you want to delete this room details?", parent=self.root)
        
        if Delete > 0:  # User confirmed
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="root", database="customer")
                my_cursor = conn.cursor()
                
                query = "DELETE FROM room WHERE Contact=%s"
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                conn.commit()  # Commit the changes immediately
                
                # Refresh the table data to show updated state
                self.fetch_data()
                
                messagebox.showinfo("Success", "Room details have been deleted successfully", parent=self.root)
            
            except Exception as es:
                messagebox.showerror("Error", f"An error occurred: {str(es)}", parent=self.root)
            
            finally:

                conn.close()  # Ensure the connection is closed

        else:  # User declined deletion
            return 
    
    #Reset function
    def reset(self):
        self.var_contact.set(""),
        self.var_checkin.set(""),
        self.var_checkout.set(""),
        self.var_roomtype.set(""),
        self.var_avialableroom.set(""),
        self.var_noofdays.set("")
        #for resetting
        self.var_tax.set("")
        self.var_actualprice.set("")
        self.var_total.set("")

    #---------all data fetch for th box near right side image----------------
    def fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please enter conatct number",parent=self.root)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="customer")
            my_cursor=conn.cursor()

            query=("select Name from customer where Mobile=%s")
            value=(self.var_contact.get(),)
            my_cursor.execute(query,value)
            rows=my_cursor.fetchone()

            if rows==None:
                messagebox.showerror("Error","This number not found",parent=self.root)
            else:
                conn.commit()
                conn.close()

                #name
                showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataframe.place(x=440,y=55,width=300,height=180)

                lblName=Label(showDataframe,text="Name:",font=("arial",12,"bold"))
                lblName.place(x=0,y=0)

                lbl=Label(showDataframe,text=rows,font=("arial",12,"bold"))
                lbl.place(x=70,y=0)

                #Gender
                conn=mysql.connector.connect(host="localhost",user="root",password="root",database="customer")
                my_cursor=conn.cursor()
                query=("select Gender from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                rows=my_cursor.fetchone()

                lblGender=Label(showDataframe,text="Gender:",font=("arial",12,"bold"))
                lblGender.place(x=0,y=30)

                lbl2=Label(showDataframe,text=rows,font=("arial",12,"bold"))
                lbl2.place(x=70,y=30)

                #Email
                conn=mysql.connector.connect(host="localhost",user="root",password="root",database="customer")
                my_cursor=conn.cursor()
                query=("select Email from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                rows=my_cursor.fetchone()

                lblEmail=Label(showDataframe,text="Email:",font=("arial",12,"bold"))
                lblEmail.place(x=0,y=60)

                lbl3=Label(showDataframe,text=rows,font=("arial",12,"bold"))
                lbl3.place(x=70,y=60)

                #Idproof
                conn=mysql.connector.connect(host="localhost",user="root",password="root",database="customer")
                my_cursor=conn.cursor()
                query=("select Idproof from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                rows=my_cursor.fetchone()

                lblIdproof=Label(showDataframe,text="Idproof:",font=("arial",12,"bold"))
                lblIdproof.place(x=0,y=90)

                lbl4=Label(showDataframe,text=rows,font=("arial",12,"bold"))
                lbl4.place(x=70,y=90)

                #idprood no
                conn=mysql.connector.connect(host="localhost",user="root",password="root",database="customer")
                my_cursor=conn.cursor()
                query=("select IdproofNo from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                rows=my_cursor.fetchone()

                lblIdproofNo=Label(showDataframe,text="Idno:",font=("arial",12,"bold"))
                lblIdproofNo.place(x=0,y=120)

                lbl5=Label(showDataframe,text=rows,font=("arial",12,"bold"))
                lbl5.place(x=70,y=120)

                #address
                conn=mysql.connector.connect(host="localhost",user="root",password="root",database="customer")
                my_cursor=conn.cursor()
                query=("select Address from customer where Mobile=%s")
                value=(self.var_contact.get(),)
                my_cursor.execute(query,value)
                rows=my_cursor.fetchone()
    
                lblAddress=Label(showDataframe,text="Address:",font=("arial",12,"bold"))
                lblAddress.place(x=0,y=150)

                lbl6=Label(showDataframe,text=rows,font=("arial",12,"bold"))
                lbl6.place(x=70,y=150)


    def total(self):
        inDate=self.var_checkin.get()
        outDate=self.var_checkout.get()
        inDate=datetime.strptime(inDate,"%d/%m/%Y")
        outDate=datetime.strptime(outDate,"%d/%m/%Y")
        self.var_noofdays.set(abs(outDate-inDate).days)

        if(self.var_roomtype.get()=="duplex"):
            q1=float(1000)
            q2=float(self.var_noofdays.get())
            q3=float(q1*q2)
            Tax="Rs."+str("%.2f"%((q3)*0.1))
            Subtotal="Rs."+str("%.2f"%((q3)))
            Ftotal="Rs."+str("%.2f"%(q3+((q3)*0.1)))
            self.var_tax.set(Tax)
            self.var_actualprice.set(Subtotal)
            self.var_total.set(Ftotal)

        elif(self.var_roomtype.get()=="single"):
            q1=float(300)
            q2=float(self.var_noofdays.get())
            q3=float(q1*q2)
            Tax="Rs."+str("%.2f"%((q3)*0.1))
            Subtotal="Rs."+str("%.2f"%((q3)))
            Ftotal="Rs."+str("%.2f"%(q3+((q3)*0.1)))
            self.var_tax.set(Tax)
            self.var_actualprice.set(Subtotal)
            self.var_total.set(Ftotal)

        elif(self.var_roomtype.get()=="luxary"):
            q1=float(1200)
            q2=float(self.var_noofdays.get())
            q3=float(q1*q2)
            Tax="Rs."+str("%.2f"%((q3)*0.1))
            Subtotal="Rs."+str("%.2f"%((q3)))
            Ftotal="Rs."+str("%.2f"%(q3+((q3)*0.1)))
            self.var_tax.set(Tax)
            self.var_actualprice.set(Subtotal)
            self.var_total.set(Ftotal)

    def search_btn(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="root", database="customer")
        my_cursor = conn.cursor()
        
                # Fetch the column and search value
        column_name = self.search_var.get()  # Get selected column from combobox (like "Mobile", "Reference")
        search_value = self.txt_var.get()    # Get the input search value

        # Check if the values are correct
        if column_name and search_value:
            # Step 3: Execute the query using parameterized SQL to avoid SQL injection issues
            query = f"SELECT * FROM room WHERE {column_name} LIKE %s"
            my_cursor.execute(query, ("%"+search_value+"%",))  # Using wildcards to match partial strings
            
            rows = my_cursor.fetchall()
            
            # If rows are found, update the table
            if rows:
                self.room_table.delete(*self.room_table.get_children())
                for row in rows:
                    self.room_table.insert("", END, values=row)
                conn.commit()
            else:
                messagebox.showinfo("No details","No details found",parent=self.root)  # Debugging: Show a message if no rows are found
        else:
            messagebox.showwarning("Error","Invalid search parameters!",parent=self.root)  # Debugging: Show a message if inputs are not valid













if __name__=="__main__":
    root=Tk()
    obj=Room_booking(root)
    root.mainloop() 