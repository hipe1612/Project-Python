from domains.Person import *
from tkinter import *
from tkinter import ttk
from tk import *
import utils

def clear_entry(entry_frame, id_entry, name_entry, gend_entry, dob_entry, phone_entry, email_entry, address_entry, salary_entry, position_entry):
    # Delete all Warnings
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                                  ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=0,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=1,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=2,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=3,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=4,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=5,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=6,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=7,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=8,sticky='w')

    # Empty Entry boxes
    id_entry.delete(0, END)
    name_entry.delete(0, END)
    gend_entry.delete(0, END)
    dob_entry.delete(0, END)
    phone_entry.delete(0, END)
    email_entry.delete(0, END)
    address_entry.delete(0, END)
    salary_entry.delete(0, END)
    position_entry.delete(0, END)
   
    # Set selected_staff to -1
    global selected_staff
    selected_staff = -1
    
def staff_add(staff_list, staff_tree, entry_frame, id_entry, name_entry, gend_entry, dob_entry, phone_entry, email_entry, address_entry, salary_entry, position_entry):
    # Delete all Warnings
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                                  ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=0,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=1,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=2,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=3,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=4,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=5,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=6,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=7,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=8,sticky='w')
    
    # Get Entry
    id = id_entry.get()
    name = name_entry.get()
    gend = gend_entry.get()
    dob = dob_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()
    salary = salary_entry.get()
    position = position_entry.get()

    # Validation
    valid_check = 0
    
    #Validate ID
    if len(id) == 0:
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=0,sticky='w')
        valid_check += 1
    elif utils.invalid_id(id, "S-") == 1:
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='INVALID', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=0,sticky='w')
        valid_check += 1
    else:
        for staff in staff_list:
            if staff.get_id() == id:
                Label(entry_frame, bg='#5E95FF', fg='crimson', text='ID already exist', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=0,sticky='w')
                valid_check += 1
                break
    
    # Validate Name
    if len(name) == 0:
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=1,sticky='w')
        valid_check += 1
    
    # Validate Gender
    if len(gend) == 0:
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=2,sticky='w')
        valid_check += 1
    elif utils.invalid_gend(gend) == 1:
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='INVALID', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=2,sticky='w')
        valid_check += 1

    # Validate Date of Birth
    if len(dob) == 0:
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=3,sticky='w')
        valid_check += 1
    elif utils.invalid_dob(dob) == 1:
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='INVALID', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=3,sticky='w')
        valid_check += 1
    
    # Validate Phone
    if len(phone) == 0:
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=4,sticky='w')
        valid_check += 1
    elif utils.invalid_phone(phone) == 1:
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='INVALID', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=4,sticky='w')
        valid_check += 1

    # Validate Salary
    if len(salary) == 0:
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=7,sticky='w')
        valid_check += 1
    elif utils.invalid_salary(salary) == 1:
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='INVALID', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=7,sticky='w')
        valid_check += 1

    # Validate Position
    if len(position) == 0:
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=8,sticky='w')
        valid_check += 1
    
    # Validate Email
    if len(email) == 0:
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=5,sticky='w')
        valid_check += 1
    
    # Validate Address
    if len(address) == 0:
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=6,sticky='w')
        valid_check += 1

    # If All Valid
    if valid_check == 0:
        # Add to staff_list
        new_staff = Staff(id, name, gend, dob, phone, email, address, salary, position)
        
        staff_list.append(new_staff)

        # Display on Treeview
        staff_tree.insert(parent='', index = 'end', iid=id, text='', values=(id, name, gend, dob, phone, email, address, salary, position))

        # Empty Entry boxes
        id_entry.delete(0, END)
        name_entry.delete(0, END)
        gend_entry.delete(0, END)
        dob_entry.delete(0, END)
        phone_entry.delete(0, END)
        email_entry.delete(0, END)
        address_entry.delete(0, END)
        salary_entry.delete(0, END)
        position_entry.delete(0, END)

def staff_remove(staff_list, staff_tree):
    if len(staff_tree.selection())>0:
        selected_staff = staff_tree.selection()[0]
        staff_id = staff_tree.item(selected_staff, 'values')[0]

        for staff in staff_list:
            if staff.get_id()== staff_id:
                staff_list.remove(staff)
                break
        staff_tree.delete(selected_staff)

def all_staff_remove(staff_tree, staff_list):
    for staff in staff_tree.get_children():
        staff_tree.delete(staff)
    staff_list.clear()

def staff_select(staff_list, staff_tree, entry_frame, id_entry, name_entry, gend_entry, dob_entry, phone_entry, email_entry, address_entry, salary_entry, position_entry):
    # Delete all Warnings
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                                  ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=0,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=1,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=2,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=3,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=4,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=5,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=6,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=7,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=8,sticky='w')
    
    # Empty Entry boxes
    id_entry.delete(0, END)
    name_entry.delete(0, END)
    gend_entry.delete(0, END)
    dob_entry.delete(0, END)
    phone_entry.delete(0, END)
    email_entry.delete(0, END)
    address_entry.delete(0, END)
    salary_entry.delete(0, END)
    position_entry.delete(0, END)

    # Show Selected staff Info
    if len(staff_tree.selection())>0:
        global selected_staff
        selected_staff = staff_tree.selection()[0]
        staff_id = staff_tree.item(selected_staff, 'values')[0]
        for staff in staff_list:
            if staff.get_id()== staff_id:
                id_entry.insert(0, staff.get_id())
                name_entry.insert(0, staff.get_name())
                gend_entry.insert(0, staff.get_gend())
                dob_entry.insert(0, staff.get_dob())
                phone_entry.insert(0, staff.get_phone())
                email_entry.insert(0, staff.get_email())
                address_entry.insert(0, staff.get_address())
                salary_entry.insert(0, staff.get_salary())
                position_entry.insert(0, staff.get_position())
                break

def staff_update(staff_list, staff_tree, entry_frame, id_entry, name_entry, gend_entry, dob_entry, phone_entry, email_entry, address_entry, salary_entry, position_entry):
    global selected_staff
    if selected_staff != -1:
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='                                  ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=0,sticky='w')
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=1,sticky='w')
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=2,sticky='w')
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=3,sticky='w')
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=4,sticky='w')
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=5,sticky='w')
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=6,sticky='w')
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=7,sticky='w')
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=8,sticky='w')

        id = id_entry.get()
        name = name_entry.get()
        gend = gend_entry.get()
        dob = dob_entry.get()
        phone = phone_entry.get()
        email = email_entry.get()
        address = address_entry.get()
        salary = salary_entry.get()
        position = position_entry.get()
            
        # Validation
        valid_check = 0
        
        #Validate ID
        if len(id) == 0:
            Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=0,sticky='w')
            valid_check += 1
        elif utils.invalid_id(id, "S-") == 1:
            Label(entry_frame, bg='#5E95FF', fg='crimson', text='INVALID', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=0,sticky='w')
            valid_check += 1
        else:
            # check if new id is different from old id, if yes, check for duplication
            if id != staff_tree.item(selected_staff, 'values')[0]:
                for staff in staff_list:
                    if staff.get_id() == id:
                        Label(entry_frame, bg='#5E95FF', fg='crimson', text='ID already exist', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=0,sticky='w')
                        valid_check += 1
                        break
        
        # Validate Name
        if len(name) == 0:
            Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=1,sticky='w')
            valid_check += 1

        # Validate Gender
        if len(gend) == 0:
            Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=2,sticky='w')
            valid_check += 1
        elif utils.invalid_gend(gend) == 1:
            Label(entry_frame, bg='#5E95FF', fg='crimson', text='INVALID', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=2,sticky='w')
            valid_check += 1

        # Validate Date of Birth
        if len(dob) == 0:
            Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=3,sticky='w')
            valid_check += 1
        elif utils.invalid_dob(dob) == 1:
            Label(entry_frame, bg='#5E95FF', fg='crimson', text='INVALID', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=3,sticky='w')
            valid_check += 1

        # Validate Phone
        if len(phone) == 0:
            Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=4,sticky='w')
            valid_check += 1
        elif utils.invalid_phone(phone) == 1:
            Label(entry_frame, bg='#5E95FF', fg='crimson', text='INVALID', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=4,sticky='w')
            valid_check += 1
        
        # Validate Email
        if len(email) == 0:
            Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=5,sticky='w')
            valid_check += 1
        
        # Validate Address
        if len(address) == 0:
            Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=6,sticky='w')
            valid_check += 1

        # Validate salary
        if len(salary) == 0:
            Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=7,sticky='w')
            valid_check += 1
        elif utils.invalid_salary(salary) == 1:
            Label(entry_frame, bg='#5E95FF', fg='crimson', text='INVALID', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=7,sticky='w')
            valid_check += 1

        # If All Valid
        if valid_check == 0:
            for staff in staff_list:
                if staff.get_id() == staff_tree.item(selected_staff, 'values')[0]:
                    staff.set_id(id)
                    staff.set_name(name)
                    staff.set_gend(gend)
                    staff.set_dob(dob)
                    staff.set_phone(phone)
                    staff.set_email(email)
                    staff.set_address(address)
                    staff.set_salary(salary)
                    staff.set_position(position)
                    break
            
            staff_tree.item(selected_staff, text="", values = (id, name, gend, dob, phone, email, address, salary, position))
            selected_staff = -1
        
            id_entry.delete(0, END)
            name_entry.delete(0, END)
            gend_entry.delete(0, END)
            dob_entry.delete(0, END)
            phone_entry.delete(0, END)
            email_entry.delete(0, END)
            address_entry.delete(0, END)
            salary_entry.delete(0, END)
            position_entry.delete(0, END)

def staff_press(window, width, height, staff_list):
    global selected_staff
    selected_staff = -1
    staff_subwin = Toplevel(window)
    staff_subwin.title("Staff Information")
    staff_subwin.geometry("%dx%d+0+0" % (width, height))
  
    #=====================================================================================
    style = ttk.Style()
    style.theme_use('default')
    style.configure("Treeview",
        background = "silver",
        foreground = "black",
        rowheight = 25,
        font=("Montserrat Bold", 12),
        fieldbackground = "white"
        )
    style.configure("Treeview.Heading", font=("Montserrat Bold", 16,'bold'))
    
    style.map('Treeview', background=[('selected', 'dark blue')])

    # Create TreeView List
    staff_tree = ttk.Treeview(staff_subwin, selectmode='browse', show='headings')

    # Define columns
    staff_tree['columns'] = ("ID", "Name", "Gender", "Date of Birth", "Phone", "Email", "Address", "Salary", "Position")

    # Format columns
    staff_tree.column("#0", width=0, stretch=NO)
    staff_tree.column("ID", anchor='center', width=75)
    staff_tree.column("Name",anchor='w', width=150)
    staff_tree.column("Gender",anchor='center', width=75)
    staff_tree.column("Date of Birth",anchor='center', width=125)
    staff_tree.column("Phone",anchor='center', width=125)
    staff_tree.column("Email",anchor='w', width=200)
    staff_tree.column("Address",anchor='w', width=200)
    staff_tree.column("Salary",anchor='center', width=100)
    staff_tree.column("Position",anchor='w', width=75)

    # Create Headings
    staff_tree.heading("#0", text="")
    staff_tree.heading("ID", text="ID", anchor='center', command= lambda: utils.sort_people_list_by_column(staff_tree, staff_list, "ID", False))
    staff_tree.heading("Name", text="Name", anchor='center', command= lambda: utils.sort_people_list_by_column(staff_tree, staff_list, "Name", False))
    staff_tree.heading("Gender", text="Gender", anchor='center', command= lambda: utils.sort_people_list_by_column(staff_tree, staff_list, "Gender", False))
    staff_tree.heading("Date of Birth", text="Date of Birth", anchor='center', command= lambda: utils.sort_people_list_by_column(staff_tree, staff_list, "Date of Birth", False))
    staff_tree.heading("Phone", text="Phone", anchor='center', command= lambda: utils.sort_people_list_by_column(staff_tree, staff_list, "Phone", False))
    staff_tree.heading("Email", text="Email", anchor='center', command= lambda: utils.sort_people_list_by_column(staff_tree, staff_list, "Email", False))
    staff_tree.heading("Address", text="Address", anchor='center', command= lambda: utils.sort_people_list_by_column(staff_tree, staff_list, "Address", False))
    staff_tree.heading("Salary", text="Salary", anchor='center', command= lambda: utils.sort_people_list_by_column(staff_tree, staff_list, "Salary", False))
    staff_tree.heading("Position", text="Position", anchor='center', command= lambda: utils.sort_people_list_by_column(staff_tree, staff_list, "Position", False))

    staff_tree.bind('<Motion>', 'break')
    
    # Insert Data
    for staff in staff_list:
        staff_tree.insert(parent='', index = 'end', iid=staff.get_id(), text='', values=(staff.get_id(), staff.get_name(), staff.get_gend(), staff.get_dob(), staff.get_phone(), staff.get_email(), staff.get_address(), staff.get_salary(), staff.get_position()))
    
    # GUI treeview
    staff_tree.place(x=50, y= 450, height=height, width=width/2 + 500)


    #=========================================================================================
    
    # Main content : Staff Management
    Label(staff_subwin, bg='#5E95FF', fg='white', text='STAFF MANAGEMENT', font=("Montserrat Bold", 20, 'bold')).place(x=50, y=25, width=width/2 + 670, height=50)
    entry_frame = Frame(staff_subwin, bg='#5E95FF')
    entry_frame.place(x=50, y=100 , width=width/2, height=height/2 - 100)
    
    # Condition Warning
    subentry_frame = Frame(staff_subwin, bg='#5E95FF')
    subentry_frame.place(x=width/2+300, y=100 , width= 420, height=height/2 - 100)
    Label(staff_subwin, text='  - ID must be " S-xxx " ', anchor='w', bg='#5E95FF', fg='white', font=("Montserrat Bold", 14, 'bold')).place(x=width/2+300, y=100, height=30)
    Label(staff_subwin, text='  - Gender must be " M " or " F " ', anchor='w', bg='#5E95FF', fg='white', font=("Montserrat Bold", 14, 'bold')).place(x=width/2+300, y=130, height=30)
    Label(staff_subwin, text='  - Date of Birth must be " dd/mm/yyyy " ', anchor='w', bg='#5E95FF', fg='white', font=("Montserrat Bold", 14, 'bold')).place(x=width/2+300, y=160, height=30)
    Label(staff_subwin, text='  - Phone must be ten numbers ', anchor='w', bg='#5E95FF', fg='white', font=("Montserrat Bold", 14, 'bold')).place(x=width/2+300, y=190, height=30)
    Label(staff_subwin, text='  - Salary must be a number ', anchor='w', bg='#5E95FF', fg='white', font=("Montserrat Bold", 14, 'bold')).place(x=width/2+300, y=220, height=30)

    # Entry Headers
    Label(entry_frame, bg='#5E95FF', fg='white', text='   ID   ', font=("Montserrat Bold", 14, 'bold')).grid(column=2, row=0)
    Label(entry_frame, bg='#5E95FF', fg='white', text='   Name   ', font=("Montserrat Bold", 14, 'bold')).grid(column=2, row=1)
    Label(entry_frame, bg='#5E95FF', fg='white', text='   Gender   ', font=("Montserrat Bold", 14, 'bold')).grid(column=2, row=2)
    Label(entry_frame, bg='#5E95FF', fg='white', text='   DoB   ', font=("Montserrat Bold", 14, 'bold')).grid(column=2, row=3)
    Label(entry_frame, bg='#5E95FF', fg='white', text='   Phone   ', font=("Montserrat Bold", 14, 'bold')).grid(column=2, row=4)
    Label(entry_frame, bg='#5E95FF', fg='white', text='   Email   ', font=("Montserrat Bold", 14, 'bold')).grid(column=2, row=5)
    Label(entry_frame, bg='#5E95FF', fg='white', text='   Address   ', font=("Montserrat Bold", 14, 'bold')).grid(column=2, row=6)
    Label(entry_frame, bg='#5E95FF', fg='white', text='   Salary   ', font=("Montserrat Bold", 14, 'bold')).grid(column=2, row=7)
    Label(entry_frame, bg='#5E95FF', fg='white', text='   Position   ', font=("Montserrat Bold", 14, 'bold')).grid(column=2, row=8)

    # Entries
    id_entry = Entry(entry_frame)
    id_entry.grid(column=4,row=0)

    name_entry = Entry(entry_frame)
    name_entry.grid(column=4,row=1)

    gend_entry = Entry(entry_frame)
    gend_entry.grid(column=4,row=2)

    dob_entry = Entry(entry_frame)
    dob_entry.grid(column=4,row=3)

    phone_entry = Entry(entry_frame)
    phone_entry.grid(column=4,row=4)

    email_entry = Entry(entry_frame)
    email_entry.grid(column=4,row=5)

    address_entry = Entry(entry_frame)
    address_entry.grid(column=4,row=6)

    salary_entry = Entry(entry_frame)
    salary_entry.grid(column=4,row=7)

    position_entry = Entry(entry_frame)
    position_entry.grid(column=4,row=8)


    # Buttons input
    add_staff_button = Button(staff_subwin, text='ADD',anchor='center',font=("Montserrat Bold", 12,'bold'),bg='#5E95FF', fg='white', relief='ridge',
        activebackground='dark blue', activeforeground='white', command=lambda: staff_add(staff_list, staff_tree, entry_frame, id_entry, name_entry, gend_entry, dob_entry, phone_entry, email_entry, address_entry, salary_entry, position_entry))
    add_staff_button.place(x=width/2 + 100 , y= 100 , width=150, height=50)

    update_staff_button = Button(staff_subwin, text='UPDATE',anchor='center',font=("Montserrat Bold", 12,'bold'),bg='#5E95FF', fg='white', relief='ridge',
        activebackground='dark blue', activeforeground='white', command=lambda: staff_update(staff_list, staff_tree, entry_frame, id_entry, name_entry, gend_entry, dob_entry, phone_entry, email_entry, address_entry, salary_entry, position_entry))
    update_staff_button.place(x=width/2 + 100, y= 170, width=150, height=50)

    clear_button = Button(staff_subwin, text='CLEAR',anchor='center',font=("Montserrat Bold", 12,'bold'),bg='#5E95FF', fg='white', relief='ridge',
        activebackground='dark blue', activeforeground='white', command=lambda: clear_entry(entry_frame, id_entry, name_entry, gend_entry, dob_entry, phone_entry, email_entry, address_entry, salary_entry, position_entry))
    clear_button.place(x=width/2 + 100, y=240, width=150, height=50)

    # Button to manage data in treeview

    remove_staff_button = Button(staff_subwin, text='REMOVE SELECTED',anchor='center',font=("Montserrat Bold", 11,'bold'),bg='red', fg='white', relief='ridge',
        activebackground='blue', activeforeground='white', command=lambda: staff_remove(staff_list, staff_tree))
    remove_staff_button.place(x=width/2 +570, y=height/2 +125, width=150, height=50)

    remove_all_staff_button = Button(staff_subwin, text='REMOVE ALL',anchor='center',font=("Montserrat Bold", 11,'bold'),bg='red', fg='white', relief='ridge',
        activebackground='blue', activeforeground='white', command=lambda: all_staff_remove(staff_tree, staff_list))
    remove_all_staff_button.place(x=width/2 +570, y=height/2+200, width=150, height=50)

    select_staff_button = Button(staff_subwin, text='SELECT',anchor='center',font=("Montserrat Bold", 11,'bold'), bg='red',fg='white', relief='ridge',
        activebackground='blue', activeforeground='white', command=lambda: staff_select(staff_list, staff_tree, entry_frame, id_entry, name_entry, gend_entry, dob_entry, phone_entry, email_entry, address_entry, salary_entry, position_entry))
    select_staff_button.place(x= width/2 +570, y=height/2 + 50, width=150, height=50)
