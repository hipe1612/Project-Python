from domains.Room import *
from domains.Reservation import *
from Function.ReservationButton import *
from tkinter import *
from tkinter import ttk
from tk import *
import utils

def clear_entry(entry_frame, id_entry, type_entry, price_entry):
    # Delete all Warnings
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                                  ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=0,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=1,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=2,sticky='w')

    # Empty Entry boxes
    id_entry.delete(0, END)
    type_entry.delete(0, END)
    price_entry.delete(0, END)
    Label(entry_frame, bg='white', fg='black', text='                                        ', font=("Montserrat Bold", 9, 'bold')).grid(column=4,row=4,sticky='w')
   
    # Set selected_room to -1
    global selected_room
    selected_room = -1
    
def room_add(room_list, room_tree, entry_frame, id_entry, type_entry, price_entry):
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                                  ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=0,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=1,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=2,sticky='w')

    
    id = id_entry.get()
    type = type_entry.get()
    price = price_entry.get()

    # Validation
    valid_check = 0
    
    # Validate ID   
    if len(id) == 0:
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=0,sticky='w')
        valid_check += 1
    elif utils.invalid_id(id, "R-") == 1:
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='INVALID', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=0,sticky='w')
        valid_check += 1
    else:
        for room in room_list:
            if room.get_id() == id:
                Label(entry_frame, bg='#5E95FF', fg='crimson', text='ID already exist', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=0,sticky='w')
                valid_check += 1
                break

    # Validate Type
    if len(type) == 0:
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=1,sticky='w')
        valid_check += 1
    elif utils.invalid_type(type) == 1:
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='INVALID', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=1,sticky='w')
        valid_check += 1

    # Validate Price
    if len(price) == 0:
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=2,sticky='w')
        valid_check += 1
    elif utils.invalid_price(price,type) == 1:
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='INVALID', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=2,sticky='w')
        valid_check += 1

    # If All Valid
    if valid_check == 0:
        # Add to room_list
        new_room = Room(id, type, price)
        
        room_list.append(new_room)

        # Display on Treeview
        room_tree.insert(parent='', index = 'end', iid=id, text='', values=(id, type, price))

        # Empty Entry boxes
        id_entry.delete(0, END)
        type_entry.delete(0, END)
        price_entry.delete(0, END)
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=3,sticky='w')

def room_remove(room_list, room_tree):
    if len(room_tree.selection())>0:
        selected_room = room_tree.selection()[0]
        room_id = room_tree.item(selected_room, 'values')[0]

        for room in room_list:
            if room.get_id()== room_id:
                room_list.remove(room)
                break
        room_tree.delete(selected_room)

def all_room_remove(room_tree, room_list):
    for room in room_tree.get_children():
        room_tree.delete(room)
    room_list.clear()

def room_select(room_list,reservation_list, room_tree, entry_frame, id_entry, type_entry, price_entry):
    # Delete all Warnings
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                                  ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=0,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=1,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=2,sticky='w')

    # Empty Entry boxes
    id_entry.delete(0, END)
    type_entry.delete(0, END)
    price_entry.delete(0, END)
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=3,sticky='w')

    # Show Selected room Info
    if len(room_tree.selection())>0:
        global selected_room
        selected_room = room_tree.selection()[0]
        room_id = room_tree.item(selected_room, 'values')[0]
        for room in room_list:
            for reservation in reservation_list:
                if room.get_id()== room_id:
                    id_entry.insert(0, room.get_id())
                    type_entry.insert(0, room.get_type())
                    price_entry.insert(0, room.get_price())
                    break
                # Get Status
                if reservation.get_RoomID() == room_id:
                    Label(entry_frame, bg='white', fg='black', text='Unavailable              ', font=("Montserrat Bold", 9)).grid(column=4,row=4,sticky='w')
                    break    
                else:
                    Label(entry_frame, bg='white', fg='black', text='Available                       ', font=("Montserrat Bold", 9)).grid(column=4,row=4,sticky='w')
                    break

def room_update(room_list, room_tree, entry_frame, id_entry, type_entry, price_entry):
    global selected_room
    if selected_room != -1:
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='                                  ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=0,sticky='w')
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=1,sticky='w')
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=2,sticky='w')

        id = id_entry.get()
        type = type_entry.get()
        price = price_entry.get()

        # Validation
        valid_check = 0
        
        # Validate ID   
        if len(id) == 0:
            Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=0,sticky='w')
            valid_check += 1
        elif utils.invalid_id(id, "R-") == 1:
            Label(entry_frame, bg='#5E95FF', fg='crimson', text='INVALID', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=0,sticky='w')
            valid_check += 1
        else:
            if id != room_tree.item(selected_room, 'values')[0]:
                for room in room_list:
                    if room.get_id()== id:
                        Label(entry_frame, bg='#5E95FF', fg='crimson', text='EXISTED', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=0,sticky='w')
                        valid_check += 1
                        break

        # Validate Type
        if len(type) == 0:
            Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=1,sticky='w')
            valid_check += 1
        elif utils.invalid_type(type) == 1:
            Label(entry_frame, bg='#5E95FF', fg='crimson', text='INVALID', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=1,sticky='w')
            valid_check += 1

        # Validate Price
        if len(price) == 0:
            Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=2,sticky='w')
            valid_check += 1
        elif utils.invalid_price(price,type) == 1:
            Label(entry_frame, bg='#5E95FF', fg='crimson', text='INVALID', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=2,sticky='w')
            valid_check += 1


        # If All Valid
        if valid_check == 0:
            for room in room_list:
                if room.get_id() == room_tree.item(selected_room, 'values')[0]:
                    room.set_id(id)
                    room.set_type(type)
                    room.set_price(price)
                    break
            
            room_tree.item(selected_room, text="", values = (id, type, price))
            selected_room = -1
        
            id_entry.delete(0, END)
            type_entry.delete(0, END)
            price_entry.delete(0, END)
            Label(entry_frame, bg='#5E95FF', fg='crimson', text='                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=3,sticky='w')

def room_press(window, width, height, room_list, resevation_list):
    global selected_room
    selected_room = -1
    room_subwin = Toplevel(window)
    room_subwin.title("Room Information")
    room_subwin.geometry("%dx%d+0+0" % (width, height))
  
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
    room_tree = ttk.Treeview(room_subwin, selectmode='browse', show='headings')

    # Define columns
    room_tree['columns'] = ("ID", "Type", "Price")

    # Format columns
    room_tree.column("#0", width=0, stretch=NO)
    room_tree.column("ID", anchor='center', width=75)
    room_tree.column("Type",anchor='w', width=100)
    room_tree.column("Price",anchor='center', width=100)

    # Create Headings
    room_tree.heading("#0", text="")
    room_tree.heading("ID", text="ID", anchor='center', command= lambda: utils.sort_room_list_by_column(room_tree, room_list, "ID", False))
    room_tree.heading("Type", text="Type", anchor='center', command= lambda: utils.sort_room_list_by_column(room_tree, room_list, "Type", False))
    room_tree.heading("Price", text="Price", anchor='center', command= lambda: utils.sort_room_list_by_column(room_tree, room_list, "Price", False))

    room_tree.bind('<Motion>', 'break')
    
    # Insert Data
    for room in room_list:
        room_tree.insert(parent='', index = 'end', iid=room.get_id(), text='', values=(room.get_id(), room.get_type(), room.get_price()))
    
    # GUI treeview
    room_tree.place(x=50, y= 450, height=height, width=width/2 + 500)


    #=========================================================================================
    
    # Room Control
    Label(room_subwin, bg='#5E95FF', fg='white', text='ROOM MANAGEMENT', font=("Montserrat Bold", 20, 'bold')).place(x=50, y=25, width=width/2 + 670, height=50)
    entry_frame = Frame(room_subwin, bg='#5E95FF')
    entry_frame.place(x=50, y=100 , width=width/2, height=height/2 - 100)
    
    subentry_frame = Frame(room_subwin, bg='#5E95FF')
    subentry_frame.place(x=width/2+300, y=100 , width= 420, height=height/2 - 100)

    Label(room_subwin, text='  - ID must be " R-xxx " ', anchor='w', bg='#5E95FF', fg='white', font=("Montserrat Bold", 14, 'bold')).place(x=width/2+300, y=100, height=30)
    Label(room_subwin, text='  - Type must be "Luxury" or "Gold" or  ', anchor='w', bg='#5E95FF', fg='white', font=("Montserrat Bold", 14, 'bold')).place(x=width/2+300, y=130, height=30)
    Label(room_subwin, text='  "Normal" ', anchor='w', bg='#5E95FF', fg='white', font=("Montserrat Bold", 14, 'bold')).place(x=width/2+300, y=160, height=30)
    Label(room_subwin, text='  - Price must be " xxx " ', anchor='w', bg='#5E95FF', fg='white', font=("Montserrat Bold", 14, 'bold')).place(x=width/2+300, y=190, height=30)
   
    Label(entry_frame, bg='#5E95FF', fg='white', text='   ID   ', font=("Montserrat Bold", 14, 'bold')).grid(column=2, row=0)
    Label(entry_frame, bg='#5E95FF', fg='white', text='   Type   ', font=("Montserrat Bold", 14, 'bold')).grid(column=2, row=1)
    Label(entry_frame, bg='#5E95FF', fg='white', text='   Price   ', font=("Montserrat Bold", 14, 'bold')).grid(column=2, row=2)
    Label(entry_frame, bg='#5E95FF', fg='white', text='____________', font=("Montserrat Bold", 14, 'bold')).grid(column=2, row=3)
    Label(entry_frame, bg='#5E95FF', fg='white', text='   Status   ', font=("Montserrat Bold", 14, 'bold')).grid(column=2, row=4)

    # Entries
    id_entry = Entry(entry_frame)
    id_entry.grid(column=4,row=0)

    type_entry = Entry(entry_frame)
    type_entry.grid(column=4,row=1)

    price_entry = Entry(entry_frame)
    price_entry.grid(column=4,row=2)

    status_label = Label(entry_frame, bg='white', fg='black', text='                                        ', font=("Montserrat Bold", 9, 'bold'))
    status_label.grid(column=4,row=4)


    # Buttons input
    add_room_button = Button(room_subwin, text='ADD',anchor='center',font=("Montserrat Bold", 12,'bold'),bg='#5E95FF', fg='white', relief='ridge',
        activebackground='dark blue', activeforeground='white', command=lambda: room_add(room_list, room_tree, entry_frame, id_entry, type_entry, price_entry))
    add_room_button.place(x=width/2 + 100 , y= 100 , width=150, height=50)

    update_room_button = Button(room_subwin, text='UPDATE',anchor='center',font=("Montserrat Bold", 12,'bold'),bg='#5E95FF', fg='white', relief='ridge',
        activebackground='dark blue', activeforeground='white', command=lambda: room_update(room_list, room_tree, entry_frame, id_entry, type_entry, price_entry))
    update_room_button.place(x=width/2 + 100, y= 170, width=150, height=50)

    clear_button = Button(room_subwin, text='CLEAR',anchor='center',font=("Montserrat Bold", 12,'bold'),bg='#5E95FF', fg='white', relief='ridge',
        activebackground='dark blue', activeforeground='white', command=lambda: clear_entry(entry_frame, id_entry, type_entry, price_entry))
    clear_button.place(x=width/2 + 100, y=240, width=150, height=50)


    # Button for data

    remove_room_button = Button(room_subwin, text='REMOVE SELECTED',anchor='center',font=("Montserrat Bold", 11,'bold'),bg='red', fg='white', relief='ridge',
        activebackground='blue', activeforeground='white', command=lambda: room_remove(room_list, room_tree))
    remove_room_button.place(x=width/2 +570, y=height/2 +125, width=150, height=50)

    remove_all_room_button = Button(room_subwin, text='REMOVE ALL',anchor='center',font=("Montserrat Bold", 11,'bold'),bg='red', fg='white', relief='ridge',
        activebackground='blue', activeforeground='white', command=lambda: all_room_remove(room_tree, room_list))
    remove_all_room_button.place(x=width/2 +570, y=height/2+200, width=150, height=50)

    select_room_button = Button(room_subwin, text='SELECT',anchor='center',font=("Montserrat Bold", 11,'bold'), bg='red',fg='white', relief='ridge',
        activebackground='blue', activeforeground='white', command=lambda: room_select(room_list, resevation_list, room_tree, entry_frame, id_entry, type_entry, price_entry))
    select_room_button.place(x= width/2 +570, y=height/2 + 50, width=150, height=50)
