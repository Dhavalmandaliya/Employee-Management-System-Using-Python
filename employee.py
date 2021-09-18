from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox
import tkinter.messagebox as MessageBox
root=Tk()


class employee:
    def __init__(self,root):
        self.root=root
        self.root.title("Employee System")
        self.root.geometry("1350x700+0+0")

        title=Label(self.root,text="Employee System",bd=12,relief=GROOVE,font=("times new roman",40,"bold"),bg="navy",fg="cyan")
        title.pack(side=TOP,fill=X)

        #==========Variable=========
        self.Emp_no_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.contact_var=StringVar()
        self.dob_var=StringVar()
        self.gender_var=StringVar()

        self.search=StringVar()
        self.search_txt=StringVar()


        #=======Manage Frame=======

        M_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="#0E4D92")
        M_Frame.place(x=20,y=100,width=450,height=590)

        m_title=Label(M_Frame,text="Manage Employee",bg="#0E4D92",fg="#B0DFE5",font=("times new roman",30,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_emp_num=Label(M_Frame,text="Employee Number",bg="#0E4D92",fg="#B0DFE5",font=("times new roman",15,"bold"))
        lbl_emp_num.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        txt_emp_num=Entry(M_Frame,textvariable=self.Emp_no_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_emp_num.grid(row=1,column=1,pady=10,padx=20,sticky="W")


        lbl_emp_name=Label(M_Frame,text="Employee Name",bg="#0E4D92",fg="#B0DFE5",font=("times new roman",15,"bold"))
        lbl_emp_name.grid(row=2,column=0,pady=10,padx=20,sticky="W")

        txt_emp_name=Entry(M_Frame,textvariable=self.name_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_emp_name.grid(row=2,column=1,pady=10,padx=20,sticky="W")


        lbl_emp_email=Label(M_Frame,text="Employee Email",bg="#0E4D92",fg="#B0DFE5",font=("times new roman",15,"bold"))
        lbl_emp_email.grid(row=3,column=0,pady=10,padx=20,sticky="W")

        txt_emp_email=Entry(M_Frame,textvariable=self.email_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_emp_email.grid(row=3,column=1,pady=10,padx=20,sticky="W")

        lbl_emp_contact=Label(M_Frame,text="Contact Number",bg="#0E4D92",fg="#B0DFE5",font=("times new roman",15,"bold"))
        lbl_emp_contact.grid(row=4,column=0,pady=10,padx=20,sticky="W")

        txt_emp_contact=Entry(M_Frame,textvariable=self.contact_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_emp_contact.grid(row=4,column=1,pady=10,padx=20,sticky="W")

        lbl_emp_dob=Label(M_Frame,text="Date of Birth",bg="#0E4D92",fg="#B0DFE5",font=("times new roman",15,"bold"))
        lbl_emp_dob.grid(row=5,column=0,pady=10,padx=20,sticky="W")

        txt_emp_dob=Entry(M_Frame,textvariable=self.dob_var,font=("times new roman",15,"bold"),bd=5,relief=GROOVE)
        txt_emp_dob.grid(row=5,column=1,pady=10,padx=20,sticky="W")


        lbl_emp_gen=Label(M_Frame,text="Gender",bg="#0E4D92",fg="#B0DFE5",font=("times new roman",15,"bold"))
        lbl_emp_gen.grid(row=6,column=0,pady=10,padx=20,sticky="W")

        combo_gen=ttk.Combobox(M_Frame,textvariable=self.gender_var,font=("times new roman",13,"bold"),state='readonly')
        combo_gen['values']=('Male','Female','Other')
        combo_gen.grid(row=6,column=1,pady=20,padx=10)

        lbl_emp_add=Label(M_Frame,text="Address",bg="#0E4D92",fg="#B0DFE5",font=("times new roman",15,"bold"))
        lbl_emp_add.grid(row=7,column=0,pady=10,padx=20,sticky="w")

        self.txt_add=Text(M_Frame,width=30,height=4,font=('',10))
        self.txt_add.grid(row=7,column=1,pady=10,padx=20,sticky='w')


        #======Button========
        btn_Frame=Frame(M_Frame,bd=4,relief=RIDGE,bg="#0E4D92")
        btn_Frame.place(x=15,y=520,width=420)

        Addbtn=Button(btn_Frame,text="ADD",width=10,command=self.add_employee).grid(row=0,column=0,padx=10,pady=10)
        updbtn=Button(btn_Frame,text="UPDATE",width=10,command=self.update_data).grid(row=0,column=1,padx=10,pady=10)
        delbtn=Button(btn_Frame,text="DELETE",width=10,command=self.delete_data).grid(row=0,column=2,padx=10,pady=10)
        clrbtn=Button(btn_Frame,text="CLEAR",width=10,command=self.clear).grid(row=0,column=3,padx=10,pady=10)




        #======Detail=======

        d_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="#0E4D92")
        d_Frame.place(x=500,y=100,width=800,height=590)

        lbl_search=Label(d_Frame,text="Search",bg="#0E4D92",fg="#B0DFE5",font=("times new roman",15,"bold"))
        lbl_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

        combo_search=ttk.Combobox(d_Frame,textvariable=self.search,width=10,font=("times new roman",13,"bold"),state='readonly')
        combo_search['values']=('emp_no','Name','Contact')
        combo_search.grid(row=0,column=1,pady=10,padx=20)

        txt_search=Entry(d_Frame,textvariable=self.search_txt,width=15,font=("times new roman",14,"bold"),bd=5,relief=GROOVE)
        txt_search.grid(row=0,column=2,pady=10,padx=20,sticky="W")

        searchtn=Button(d_Frame,text="SEARCH",width=10,command=self.search_data,pady=5).grid(row=0,column=3,padx=10,pady=10)
        showallbtn=Button(d_Frame,text="SHOW ALL",width=10,command=self.fetch_data,pady=5).grid(row=0,column=4,padx=10,pady=10)

    #========table Frame=======
        Table_Frame=Frame(d_Frame,bd=4,relief=RIDGE,bg="#0E4D92")
        Table_Frame.place(x=10,y=70,width=770,height=500)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        self.employee_table=ttk.Treeview(Table_Frame,columns=("Employee Number","Name","Email","Contact","DOB","Gender","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)
        self.employee_table.heading("Employee Number",text="Employee Number")
        self.employee_table.heading("Name",text="Name")
        self.employee_table.heading("Email",text="Email")
        self.employee_table.heading("Contact",text="Contact")
        self.employee_table.heading("DOB",text="Date of Birth")
        self.employee_table.heading("Gender",text="Gender")
        self.employee_table.heading("Address",text="Address")
        self.employee_table['show']='headings'
        self.employee_table.column("Employee Number",width=115)
        self.employee_table.column("Name",width=155)
        self.employee_table.column("Email",width=155)
        self.employee_table.column("Contact",width=115)
        self.employee_table.column("DOB",width=115)
        self.employee_table.column("Gender",width=115)
        self.employee_table.column("Address",width=115)
        self.employee_table.pack(fill=BOTH,expand=1)
        self.employee_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_employee(self):
        if self.Emp_no_var.get()=="" or self.name_var.get()=="" or self.email_var.get()=="" or self.contact_var.get()==0 or self.dob_var.get()=="" or self.gender_var.get()=="":
            messagebox.showerror("Error","All fields are Required!!!")
        else:
            conn=pymysql.connect(host="localhost",user="root",password="",database="employee_prj")
            cur=conn.cursor()
            cur.execute("insert into employee values(%s,%s,%s,%s,%s,%s,%s)",(self.Emp_no_var.get(),
                                                                            self.name_var.get(),
                                                                            self.email_var.get(),
                                                                            self.contact_var.get(),
                                                                            self.dob_var.get(),
                                                                            self.gender_var.get(),
                                                                            self.txt_add.get('1.0',END)
                                                                            ))
            conn.commit()
            self.fetch_data()
            self.clear()
            conn.close()
            messagebox.showinfo("Success","Record has been Inserted")
    def fetch_data(self):
        conn=pymysql.connect(host="localhost",user="root",password="",database="employee_prj")
        cur=conn.cursor()
        cur.execute("select * from employee")
        rows=cur.fetchall()
        if (rows)!=0:
            self.employee_table.delete(*self.employee_table.get_children())
            for row in rows:
                self.employee_table.insert('',END,values=row)
            conn.commit()
        conn.close()

    def clear(self):
        self.Emp_no_var.set("")
        self.name_var.set("")
        self.email_var.set('')
        self.contact_var.set("")
        self.dob_var.set("")
        self.gender_var.set("")
        self.txt_add.delete("1.0",END)

    def get_cursor(self,ev):
        cursor_row=self.employee_table.focus()
        content=self.employee_table.item(cursor_row)
        row=content['values']
        self.Emp_no_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.contact_var.set(row[3])
        self.dob_var.set(row[4])
        self.gender_var.set(row[5])
        self.txt_add.delete("1.0",END,)
        self.txt_add.insert(END,row[6])

    def update_data(self):
        conn=pymysql.connect(host="localhost",user="root",password="",database="dbms_project")
        cur=conn.cursor()
        cur.execute("update employee set name=%s,email=%s,contact=%s,dob=%s,gender=%s,address=%s where emp_no=%s",(
                                                                          self.name_var.get(),
                                                                          self.email_var.get(),
                                                                          self.contact_var.get(),
                                                                          self.dob_var.get(),
                                                                          self.gender_var.get(),
                                                                          self.txt_add.get('1.0',END),
                                                                          self.Emp_no_var.get()
                                                                          ))
        conn.commit()
        self.fetch_data()
        self.clear()
        conn.close()
    
    def delete_data(self):
        conn=pymysql.connect(host="localhost",user="root",password="",database="dbms_project")
        cur=conn.cursor()
        cur.execute("delete  from employee where emp_no=%s",self.Emp_no_var.get())
        conn.commit()
        conn.close()
        self.fetch_data()
        self.clear()

    
    def search_data(self):
        conn=pymysql.connect(host="localhost",user="root",password="",database="dbms_project")
        cur=conn.cursor()
        cur.execute("select * from employee where "+str(self.search.get())+" Like '%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.employee_table.delete(*self.employee_table.get_children())
            for row in rows:
                self.employee_table.insert('',END,values=row)
            conn.commit()
        conn.close()

    


root.configure(bg="grey")
ob=employee(root)
root.mainloop()
