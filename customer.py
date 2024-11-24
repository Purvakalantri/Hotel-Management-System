from tkinter import*
from PIL import Image,ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox

class Cust_Win:
    def __init__(self,root):
            self.root=root
            self.root.title("CUSTOMER MANAGEMENT SYSTEM")
            self.root.geometry("1140x500+230+220")

            #-----------variables--------------
            self.var_ref=StringVar()
            x=random.randint(1000,9999)
            self.var_ref.set(str(x))

            self.var_cust_name=StringVar()
            self.var_Surname=StringVar()
            self.var_Gender=StringVar()
            self.var_mobile=StringVar()
            self.var_Email=StringVar()
            self.var_Nationality=StringVar()
            self.var_IdProof=StringVar()
            self.var_IdproofNo=StringVar()
            self.var_Address=StringVar()
            



            #------------title-------------------
            lbl_title=Label(self.root,text="ADD CUSTOMER DETAILS",font=("times new roman",20,"bold"),bg="black",fg="gold",bd=4,relief=RIDGE)
            lbl_title.place(x=0,y=0,width=1295,height=50)

            #--------------logo------------------
            img2=Image.open(r"C:\Users\Prathamesh\Desktop\Hotel_management_system\Hotel_images\hotel images\logohotel.png")
            img2=img2.resize((100,40),Image.LANCZOS)
            self.photoimg2=ImageTk.PhotoImage(img2)

            lblimg=Label(self.root,image=self.photoimg2,bd=0,relief=RIDGE)
            lblimg.place(x=5,y=2,width=100,height=40)

            #------------label frame---------------
            labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Customer Details",padx=2,font=("times new roman",12,"bold"))
            labelframeleft.place(x=5,y=50,width=425,height=490)

            #--------------labels & entries-------------
            #Customer reference
            lbl_cust_ref=Label(labelframeleft,text="Customer Ref",font=("arial",12,"bold"),padx=2,pady=6)
            lbl_cust_ref.grid(row=0,column=0)

            entry_ref=ttk.Entry(labelframeleft,width=29,textvariable=self.var_ref,font=("arial",13,"bold"),state="readonly")
            entry_ref.grid(row=0,column=1,sticky="w")

            #cst name
            cname=Label(labelframeleft,text="Customer Name",font=("arial",12,"bold"),padx=2,pady=6)
            cname.grid(row=1,column=0)

            txtcname=ttk.Entry(labelframeleft,width=29,textvariable=self.var_cust_name,font=("arial ",13,"bold"))
            txtcname.grid(row=1,column=1,sticky="w")

            #mother name    
            lbl_Surname=Label(labelframeleft,text="Surname name",font=("arial ",12,"bold"),padx=2,pady=6)
            lbl_Surname.grid(row=2,column=0)

            entry_Surname=ttk.Entry(labelframeleft,width=29,textvariable=self.var_Surname,font=("arial ",13,"bold"))
            entry_Surname.grid(row=2,column=1,sticky="w")

            #gender combox

            lbl_gender=Label(labelframeleft,text="Gender",font=("arial",12,"bold"),padx=2,pady=6)
            lbl_gender.grid(row=3,column=0)

            combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_Gender,font=("arial",12,"bold"),width=27,state="readonly")
            combo_gender["value"]=("Male","Female","other")
            combo_gender.current()
            combo_gender.grid(row=3,column=1,sticky="w")

            #mobilenumber
            lbl_Mobile=Label(labelframeleft,text="Mobile number",font=("arial ",12,"bold"),padx=2,pady=6)
            lbl_Mobile.grid(row=4,column=0)

            entry_Mobile=ttk.Entry(labelframeleft,width=29,textvariable=self.var_mobile,font=("arial ",13,"bold"))
            entry_Mobile.grid(row=4,column=1,sticky="w")

            #email

            lbl_Email=Label(labelframeleft,text="Email name",font=("arial ",12,"bold"),padx=2,pady=6)
            lbl_Email.grid(row=5,column=0)

            entry_Email=ttk.Entry(labelframeleft,width=29,textvariable=self.var_Email,font=("arial ",13,"bold"))
            entry_Email.grid(row=5,column=1,sticky="w")

            #nationality combox
            lbl_Nationality=Label(labelframeleft,text="Nationality name",font=("arial ",12,"bold"),padx=2,pady=6)
            lbl_Nationality.grid(row=6,column=0)
            
            combo_Nationality=ttk.Combobox(labelframeleft,textvariable=self.var_Nationality,font=("arial",12,"bold"),width=26,state="readonly")
            combo_Nationality["value"]=("Indian","American","British","Irish","Brazilian","Canadian")
            combo_Nationality.current()
            combo_Nationality.grid(row=6,column=1,sticky="w")
        

            #idproof type combox

            lbl_IdProof=Label(labelframeleft,text="IdProof name",font=("arial ",12,"bold"),padx=2,pady=6)
            lbl_IdProof.grid(row=7,column=0)

            combo_IdProof=ttk.Combobox(labelframeleft,textvariable=self.var_IdProof,font=("arial",12,"bold"),width=27,state="readonly")
            combo_IdProof["value"]=("Aadhar","Passport","Pancard")
            combo_IdProof.current()
            combo_IdProof.grid(row=7,column=1,sticky="w")

            #_--------------id proof number-------------------
            lbl_Idproof_NO=Label(labelframeleft,text="Id proof number",font=("arial ",12,"bold"),padx=2,pady=6)
            lbl_Idproof_NO.grid(row=8,column=0)

            entry_Idproof_NO=ttk.Entry(labelframeleft,textvariable=self.var_IdproofNo,width=28,font=("arial ",13,"bold"))
            entry_Idproof_NO.grid(row=8,column=1,sticky="w")

            #address
            lbl_Address=Label(labelframeleft,text="Address",font=("arial ",12,"bold"),padx=2,pady=6)
            lbl_Address.grid(row=9,column=0)

            entry_Address=ttk.Entry(labelframeleft,textvariable=self.var_Address,width=29,font=("arial ",13,"bold"))
            entry_Address.grid(row=9,column=1,sticky="w")


            #-------------------buttons-----------------

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

            #-----------------table frame search system---------------
            labelTableframe=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details and search system",padx=2,font=("times new roman",12,"bold"))
            labelTableframe.place(x=435,y=50,width=860,height=490)
            
            #search bar
            lbl_Searchbar=Label(labelTableframe,text="Searchbar",font=("arial ",12,"bold"),bg="red",fg="white")
            lbl_Searchbar.grid(row=0,column=0,sticky="w")

            self.search_var=StringVar()
            combo_Search=ttk.Combobox(labelTableframe,textvariable=self.search_var,font=("arial",12,"bold"),width=24,state="readonly")
            combo_Search["value"]=("Mobile","Ref")
            combo_Search.current(0)
            combo_Search.grid(row=0,column=1,sticky="w")
        
            self.txt_var=StringVar()
            entry_Search=ttk.Entry(labelTableframe,textvariable=self.txt_var,width=15,font=("arial ",13,"bold"))
            entry_Search.grid(row=0,column=2,sticky="w",padx=2)

            btnSearch=Button(labelTableframe,text="Search",command=self.search_btn,font=("arial ",13,"bold"),bg="black",fg="gold",width=9)
            btnSearch.grid(row=0,column=3,padx=1)

            btnShowAll=Button(labelTableframe,text="Show All",command=self.fetch_data,font=("arial ",13,"bold"),bg="black",fg="gold",width=9)
            btnShowAll.grid(row=0,column=4,padx=1)

            #---------------show data table-------------------
            details_table=Frame(labelTableframe,bd=2,relief=RIDGE)
            details_table.place(x=0,y=50,width=850,height=350)

            #scroll bar
            scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
            scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

            self.Cust_Details_Table=ttk.Treeview(details_table,column=("Ref","Name","Surname","Gender","Mobile","Email","Nationality","Idproof","IdproofNo","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
            scroll_x.pack(side=BOTTOM,fill=X)
            scroll_y.pack(side=RIGHT,fill=Y)

            scroll_x.config(command=self.Cust_Details_Table.xview)
            scroll_y.config(command=self.Cust_Details_Table.yview)

            self.Cust_Details_Table.heading("Ref",text="Refer Number")
            self.Cust_Details_Table.heading("Name", text="Name")
            self.Cust_Details_Table.heading("Surname", text="Surname")
            self.Cust_Details_Table.heading("Mobile", text="Mobile")
            self.Cust_Details_Table.heading("Gender", text="Gender")
            self.Cust_Details_Table.heading("Email", text="Email")
            self.Cust_Details_Table.heading("Nationality", text="Nationality")
            self.Cust_Details_Table.heading("Idproof", text="Idproof")
            self.Cust_Details_Table.heading("IdproofNo", text="IdproofNo")
            self.Cust_Details_Table.heading("Address", text="Address")

            self.Cust_Details_Table["show"]="headings"
            #column
            self.Cust_Details_Table.column("Ref", width=100)
            self.Cust_Details_Table.column("Name", width=100)
            self.Cust_Details_Table.column("Surname", width=100)
            self.Cust_Details_Table.column("Gender", width=100)
            self.Cust_Details_Table.column("Mobile", width=100)
            self.Cust_Details_Table.column("Email", width=150)
            self.Cust_Details_Table.column("Nationality", width=100)
            self.Cust_Details_Table.column("Idproof", width=100)
            self.Cust_Details_Table.column("IdproofNo", width=100)
            self.Cust_Details_Table.column("Address", width=200)
            self.Cust_Details_Table.pack(fill=BOTH,expand=1)
            self.Cust_Details_Table.bind("<ButtonRelease-1>",self.get_cursor)
            self.fetch_data()

    def add_data(self):
        if self.var_mobile.get()=="" or self.var_Surname.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",user="root",password="root",database="customer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                    self.var_ref.get(),
                                                                                                    self.var_cust_name.get(),
                                                                                                    self.var_Surname.get(),
                                                                                                    self.var_Gender.get(),
                                                                                                    self.var_mobile.get(),
                                                                                                    self.var_Email.get(),
                                                                                                    self.var_Nationality.get(),
                                                                                                    self.var_IdProof.get(),
                                                                                                    self.var_IdproofNo.get(),
                                                                                                    self.var_Address.get()                                      
                                                                                                ))
                conn.commit()
                self.fetch_data()
                conn.close()                                                                                
                messagebox.showinfo("Success","Customer has been added",parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning",f"Something went wrong:{str(es)}",parent=self.root)           

    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",user="root",password="root",database="customer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from customer")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("",END,values=i)
        conn.commit()
        conn.close()

    def get_cursor(self,event=""):
        cursor_row=self.Cust_Details_Table.focus()
        content=self.Cust_Details_Table.item(cursor_row)
        row=content["values"]

        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1]),
        self.var_Surname.set(row[2]),
        self.var_Gender.set(row[3]),
        self.var_mobile.set(row[4]),
        self.var_Email.set(row[5]),
        self.var_Nationality.set(row[6]),
        self.var_IdProof.set(row[7]),
        self.var_IdproofNo.set(row[8]),
        self.var_Address.set(row[9])

    def update(self):
        if self.var_mobile.get()=="":
            messagebox.showerror("Error","Please enter mobile number",parent=self.root)

        else:

            conn=mysql.connector.connect(host="localhost",user="root",password="root",database="customer")
            my_cursor=conn.cursor()
            my_cursor.execute("update customer set Name=%s,Surname=%s,Gender=%s,Mobile=%s,Email=%s,Nationality=%s,IdProof=%s,IdproofNo=%s,Address=%s where Ref=%s",(
                 
                                                                                                                                                                self.var_cust_name.get(),
                                                                                                                                                                self.var_Surname.get(),
                                                                                                                                                                self.var_Gender.get(),
                                                                                                                                                                self.var_mobile.get(),
                                                                                                                                                                self.var_Email.get(),
                                                                                                                                                                self.var_Nationality.get(),
                                                                                                                                                                self.var_IdProof.get(),
                                                                                                                                                                self.var_IdproofNo.get(),
                                                                                                                                                                self.var_Address.get(),
                                                                                                                                                                self.var_ref.get()

                                                                                                                                                                ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update","Customer details has been updated successfully",parent=self.root)
                 
    def Delete(self):
        Delete = messagebox.askyesno("Confirm", "Do you want to delete this customer?", parent=self.root)
        
        if Delete > 0:  # User confirmed
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="root", database="customer")
                my_cursor = conn.cursor()
                
                query = "DELETE FROM customer WHERE Ref=%s"
                value = (self.var_ref.get(),)
                my_cursor.execute(query, value)
                conn.commit()  # Commit the changes immediately
                
                # Refresh the table data to show updated state
                self.fetch_data()
                
                messagebox.showinfo("Success", "Customer details have been deleted successfully", parent=self.root)
            
            except Exception as es:
                messagebox.showerror("Error", f"An error occurred: {str(es)}", parent=self.root)
            
            finally:
                conn.close()  # Ensure the connection is closed

        else:  # User declined deletion
            return

    def reset(self):
        #self.var_ref.set(""),
        self.var_cust_name.set(""),
        self.var_Surname.set(""),
        self.var_Gender.set(""),
        self.var_mobile.set(""),
        self.var_Email.set(""),
        self.var_Nationality.set(""),
        self.var_IdProof.set(""),
        self.var_IdproofNo.set(""),
        self.var_Address.set("")
        
        x=random.randint(1000,9999)
        self.var_ref.set(str(x))

    def search_btn(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="root", database="customer")
        my_cursor = conn.cursor()
        
                # Fetch the column and search value
        column_name = self.search_var.get()  # Get selected column from combobox (like "Mobile", "Reference")
        search_value = self.txt_var.get()    # Get the input search value

        # Check if the values are correct
        if column_name and search_value:
            # Step 3: Execute the query using parameterized SQL to avoid SQL injection issues
            query = f"SELECT * FROM customer WHERE {column_name} LIKE %s"
            my_cursor.execute(query, ("%"+search_value+"%",))  # Using wildcards to match partial strings
            
            rows = my_cursor.fetchall()
            
            # If rows are found, update the table
            if rows:
                self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
                for row in rows:
                    self.Cust_Details_Table.insert("", END, values=row)
                conn.commit()
            else:
                print("No results found!")  # Debugging: Show a message if no rows are found
        else:
            print("Invalid search parameters!")  # Debugging: Show a message if inputs are not valid



if __name__=="__main__":
    root=Tk()
    obj=Cust_Win(root)
    root.mainloop() 