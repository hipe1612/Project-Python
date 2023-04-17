from domains.Person import *
from tkinter import *
from tkinter import ttk
from tk import *
import utils

def clear_entry(entry_frame, id_entry, name_entry, gend_entry, dob_entry, phone_entry, email_entry, address_entry):
    # Delete all Warnings
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                                  ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=0,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=1,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=2,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=3,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=4,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=5,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=6,sticky='w')

    # Empty Entry boxes
    id_entry.delete(0, END)
    name_entry.delete(0, END)
    gend_entry.delete(0, END)
    dob_entry.delete(0, END)
    phone_entry.delete(0, END)
    email_entry.delete(0, END)
    address_entry.delete(0, END)

    # Set selected_guest to -1
    global selected_guest
    selected_guest = -1
    
def guest_add(guests_list, guest_tree, entry_frame, id_entry, name_entry, gend_entry, dob_entry, phone_entry, email_entry, address_entry):
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                                  ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=0,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=1,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=2,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=3,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=4,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=5,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=6,sticky='w')
    
    id = id_entry.get()
    name = name_entry.get()
    gend = gend_entry.get()
    dob = dob_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    # Validation
    valid_check = 0
    
    #Validate ID
    if len(id) == 0:
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=0,sticky='w')
        valid_check += 1
    elif utils.invalid_id(id, "G-") == 1:
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='INVALID', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=0,sticky='w')
        valid_check += 1
    else:
        for guest in guests_list:
            if guest.get_id() == id:
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


    # If All Valid
    if valid_check == 0:
        # Add to guests_list
        new_guest = Guests(id, name, gend, dob, phone, email, address)
        
        guests_list.append(new_guest)

        # Display on Treeview
        guest_tree.insert(parent='', index = 'end', iid=id, text='', values=(id, name, gend, dob, phone, email, address))

        # Empty Entry boxes
        id_entry.delete(0, END)
        name_entry.delete(0, END)
        gend_entry.delete(0, END)
        dob_entry.delete(0, END)
        phone_entry.delete(0, END)
        email_entry.delete(0, END)
        address_entry.delete(0, END)

def guest_remove(guests_list, guest_tree):
    if len(guest_tree.selection())>0:
        selected_guest = guest_tree.selection()[0]
        guest_id = guest_tree.item(selected_guest, 'values')[0]

        for guest in guests_list:
            if guest.get_id()== guest_id:
                guests_list.remove(guest)
                break
        guest_tree.delete(selected_guest)

def all_guest_remove(guest_tree, guests_list):
    for guest in guest_tree.get_children():
        guest_tree.delete(guest)
    guests_list.clear()

def guest_select(guests_list, guest_tree, entry_frame, id_entry, name_entry, gend_entry, dob_entry, phone_entry, email_entry, address_entry):
    # Delete all Warnings
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                                  ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=0,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=1,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=2,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=3,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=4,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=5,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=6,sticky='w')
    
    # Empty Entry boxes
    id_entry.delete(0, END)
    name_entry.delete(0, END)
    gend_entry.delete(0, END)
    dob_entry.delete(0, END)
    phone_entry.delete(0, END)
    email_entry.delete(0, END)
    address_entry.delete(0, END)

    # Show Selected guest Info
    if len(guest_tree.selection())>0:
        global selected_guest
        selected_guest = guest_tree.selection()[0]
        guest_id = guest_tree.item(selected_guest, 'values')[0]
        for guest in guests_list:
            if guest.get_id()== guest_id:
                id_entry.insert(0, guest.get_id())
                name_entry.insert(0, guest.get_name())
                gend_entry.insert(0, guest.get_gend())
                dob_entry.insert(0, guest.get_dob())
                phone_entry.insert(0, guest.get_phone())
                email_entry.insert(0, guest.get_email())
                address_entry.insert(0, guest.get_address())
                break

def guest_update(guests_list, guest_tree, entry_frame, id_entry, name_entry, gend_entry, dob_entry, phone_entry, email_entry, address_entry):
    global selected_guest
    if selected_guest != -1:
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='                                  ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=0,sticky='w')
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=1,sticky='w')
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=2,sticky='w')
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=3,sticky='w')
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=4,sticky='w')
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=5,sticky='w')
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=6,sticky='w')

        id = id_entry.get()
        name = name_entry.get()
        gend = gend_entry.get()
        dob = dob_entry.get()
        phone = phone_entry.get()
        email = email_entry.get()
        address = address_entry.get()
            
        # Validation
        valid_check = 0
        
        #Validate ID
        if len(id) == 0:
            Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=0,sticky='w')
            valid_check += 1
        elif utils.invalid_id(id, "G-") == 1:
            Label(entry_frame, bg='#5E95FF', fg='crimson', text='INVALID', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=0,sticky='w')
            valid_check += 1
        else:
            # check if new id is different from old id, if yes, check for duplication
            if id != guest_tree.item(selected_guest, 'values')[0]:
                for guest in guests_list:
                    if guest.get_id() == id:
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

        # If All Valid
        if valid_check == 0:
            for guest in guests_list:
                if guest.get_id() == guest_tree.item(selected_guest, 'values')[0]:
                    guest.set_id(id)
                    guest.set_name(name)
                    guest.set_gend(gend)
                    guest.set_dob(dob)
                    guest.set_phone(phone)
                    guest.set_email(email)
                    guest.set_address(address)

                    break
            
            guest_tree.item(selected_guest, text="", values = (id, name, gend, dob, phone, email, address))
            selected_guest = -1
        
            id_entry.delete(0, END)
            name_entry.delete(0, END)
            gend_entry.delete(0, END)
            dob_entry.delete(0, END)
            phone_entry.delete(0, END)
            email_entry.delete(0, END)
            address_entry.delete(0, END)


def guest_press(window, width, height, guests_list):
    global selected_guest
    selected_guest = -1
    guest_subwin = Toplevel(window)
    guest_subwin.title("guest Information")
    guest_subwin.geometry("%dx%d+0+0" % (width, height))
  
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
    guest_tree = ttk.Treeview(guest_subwin, selectmode='browse', show='headings')

    # Define columns
    guest_tree['columns'] = ("ID", "Name", "Gender", "Date of Birth", "Phone", "Email", "Address")

    # Format columns
    guest_tree.column("#0", width=0, stretch=NO)
    guest_tree.column("ID", anchor='center', width=75)
    guest_tree.column("Name",anchor='w', width=150)
    guest_tree.column("Gender",anchor='center', width=75)
    guest_tree.column("Date of Birth",anchor='center', width=125)
    guest_tree.column("Phone",anchor='center', width=125)
    guest_tree.column("Email",anchor='w', width=200)
    guest_tree.column("Address",anchor='w', width=200)


    # Create Headings
    guest_tree.heading("#0", text="")
    guest_tree.heading("ID", text="ID", anchor='center', command= lambda: utils.sort_guest_list_by_column(guest_tree, guests_list, "ID", False))
    guest_tree.heading("Name", text="Name", anchor='center', command= lambda: utils.sort_guest_list_by_column(guest_tree, guests_list, "Name", False))
    guest_tree.heading("Gender", text="Gender", anchor='center', command= lambda: utils.sort_guest_list_by_column(guest_tree, guests_list, "Gender", False))
    guest_tree.heading("Date of Birth", text="Date of Birth", anchor='center', command= lambda: utils.sort_guest_list_by_column(guest_tree, guests_list, "Date of Birth", False))
    guest_tree.heading("Phone", text="Phone", anchor='center', command= lambda: utils.sort_guest_list_by_column(guest_tree, guests_list, "Phone", False))
    guest_tree.heading("Email", text="Email", anchor='center', command= lambda: utils.sort_guest_list_by_column(guest_tree, guests_list, "Email", False))
    guest_tree.heading("Address", text="Address", anchor='center', command= lambda: utils.sort_guest_list_by_column(guest_tree, guests_list, "Address", False))

    guest_tree.bind('<Motion>', 'break')
    
    # Insert Data
    for guest in guests_list:
        guest_tree.insert(parent='', index = 'end', iid=guest.get_id(), text='', values=(guest.get_id(), guest.get_name(), guest.get_gend(), guest.get_dob(), guest.get_phone(), guest.get_email(), guest.get_address()))
    
    # GUI treeview
    guest_tree.place(x=50, y= 450, height=height, width=width/2 + 500)


    #=========================================================================================
    
    # guest Control
    Label(guest_subwin, bg='#5E95FF', fg='white', text='GUEST MANAGEMENT', font=("Montserrat Bold", 20, 'bold')).place(x=50, y=25, width=width/2 + 670, height=50)
    entry_frame = Frame(guest_subwin, bg='#5E95FF')
    entry_frame.place(x=50, y=100 , width=width/2, height=height/2 - 100)
    

    subentry_frame = Frame(guest_subwin, bg='#5E95FF')
    subentry_frame.place(x=width/2+300, y=100 , width= 420, height=height/2 - 100)
    Label(guest_subwin, text='  - ID must be " G-xxx " ', anchor='w', bg='#5E95FF', fg='white', font=("Montserrat Bold", 14, 'bold')).place(x=width/2+300, y=100, height=30)
    Label(guest_subwin, text='  - Gender must be " M " or " F " ', anchor='w', bg='#5E95FF', fg='white', font=("Montserrat Bold", 14, 'bold')).place(x=width/2+300, y=130, height=30)
    Label(guest_subwin, text='  - Date of Birth must be " dd/mm/yyyy " ', anchor='w', bg='#5E95FF', fg='white', font=("Montserrat Bold", 14, 'bold')).place(x=width/2+300, y=160, height=30)
    Label(guest_subwin, text='  - Phone must be ten numbers ', anchor='w', bg='#5E95FF', fg='white', font=("Montserrat Bold", 14, 'bold')).place(x=width/2+300, y=190, height=30)


    Label(entry_frame, bg='#5E95FF', fg='white', text='   ID   ', font=("Montserrat Bold", 14, 'bold')).grid(column=2, row=0)
    Label(entry_frame, bg='#5E95FF', fg='white', text='   Name   ', font=("Montserrat Bold", 14, 'bold')).grid(column=2, row=1)
    Label(entry_frame, bg='#5E95FF', fg='white', text='   Gender   ', font=("Montserrat Bold", 14, 'bold')).grid(column=2, row=2)
    Label(entry_frame, bg='#5E95FF', fg='white', text='   DoB   ', font=("Montserrat Bold", 14, 'bold')).grid(column=2, row=3)
    Label(entry_frame, bg='#5E95FF', fg='white', text='   Phone   ', font=("Montserrat Bold", 14, 'bold')).grid(column=2, row=4)
    Label(entry_frame, bg='#5E95FF', fg='white', text='   Email   ', font=("Montserrat Bold", 14, 'bold')).grid(column=2, row=5)
    Label(entry_frame, bg='#5E95FF', fg='white', text='   Address   ', font=("Montserrat Bold", 14, 'bold')).grid(column=2, row=6)

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


    # Buttons input
    add_guest_button = Button(guest_subwin, text='ADD',anchor='center',font=("Montserrat Bold", 12,'bold'),bg='#5E95FF', fg='white', relief='ridge',
        activebackground='dark blue', activeforeground='white', command=lambda: guest_add(guests_list, guest_tree, entry_frame, id_entry, name_entry, gend_entry, dob_entry, phone_entry, email_entry, address_entry))
    add_guest_button.place(x=width/2 + 100 , y= 100 , width=150, height=50)

    update_guest_button = Button(guest_subwin, text='UPDATE',anchor='center',font=("Montserrat Bold", 12,'bold'),bg='#5E95FF', fg='white', relief='ridge',
        activebackground='dark blue', activeforeground='white', command=lambda: guest_update(guests_list, guest_tree, entry_frame, id_entry, name_entry, gend_entry, dob_entry, phone_entry, email_entry, address_entry))
    update_guest_button.place(x=width/2 + 100, y= 170, width=150, height=50)

    clear_button = Button(guest_subwin, text='CLEAR',anchor='center',font=("Montserrat Bold", 12,'bold'),bg='#5E95FF', fg='white', relief='ridge',
        activebackground='dark blue', activeforeground='white', command=lambda: clear_entry(entry_frame, id_entry, name_entry, gend_entry, dob_entry, phone_entry, email_entry, address_entry))
    clear_button.place(x=width/2 + 100, y=240, width=150, height=50)


    # button for data

    remove_guest_button = Button(guest_subwin, text='REMOVE SELECTED',anchor='center',font=("Montserrat Bold", 11,'bold'),bg='red', fg='white', relief='ridge',
        activebackground='blue', activeforeground='white', command=lambda: guest_remove(guests_list, guest_tree))
    remove_guest_button.place(x=width/2 +570, y=height/2 +125, width=150, height=50)

    remove_all_guest_button = Button(guest_subwin, text='REMOVE ALL',anchor='center',font=("Montserrat Bold", 11,'bold'),bg='red', fg='white', relief='ridge',
        activebackground='blue', activeforeground='white', command=lambda: all_guest_remove(guest_tree, guests_list))
    remove_all_guest_button.place(x=width/2 +570, y=height/2+200, width=150, height=50)

    select_guest_button = Button(guest_subwin, text='SELECT',anchor='center',font=("Montserrat Bold", 11,'bold'), bg='red',fg='white', relief='ridge',
        activebackground='blue', activeforeground='white', command=lambda: guest_select(guests_list, guest_tree, entry_frame, id_entry, name_entry, gend_entry, dob_entry, phone_entry, email_entry, address_entry))
    select_guest_button.place(x= width/2 +570, y=height/2 + 50, width=150, height=50)
