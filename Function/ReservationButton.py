from domains.Reservation import *
from domains.Room import *
from domains.Person import *

from tkinter import *
from tkinter import ttk
from tk import *
import utils

def clear_entry(entry_frame, id_entry, guestID_entry, roomID_entry, checkin_entry, checkout_entry):
    # Delete all Warnings
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                                           ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=0,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                                                           ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=1,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                                                           ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=2,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                                                           ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=3,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                                                           ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=4,sticky='w')

    # Empty Entry boxes
    id_entry.delete(0, END)
    guestID_entry.delete(0, END)
    roomID_entry.delete(0, END)
    checkin_entry.delete(0, END)
    checkout_entry.delete(0, END)

    # Set selected_reservation to -1
    global selected_reservation
    selected_reservation = -1
    
def reservation_add(reservation_list, guest_list, room_list, reservation_tree, entry_frame,id_entry, guestID_entry, roomID_entry, checkin_entry, checkout_entry):
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                                     ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=0,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                                                       ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=1,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                                                       ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=2,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                                       ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=3,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                                       ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=4,sticky='w')

    id = id_entry.get()
    guestID = guestID_entry.get()
    roomID = roomID_entry.get()
    checkin = checkin_entry.get()
    checkout = checkout_entry.get()

    # Validation
    valid_check = 0
    
    # Check ID
    if len(id) == 0:
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=0,sticky='w')
        valid_check += 1
    elif utils.invalid_reservationID(id, "RS-") ==1 :
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='INVALID', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=0,sticky='w')
        valid_check += 1
    else:
        for reservation in reservation_list:
            if reservation.get_id() == id:
                Label(entry_frame, bg='#5E95FF', fg='crimson', text='ID already exists', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=0,sticky='w')
                valid_check += 1
                break
            
    # Check Guest ID
    if len(guestID) == 0:
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=1,sticky='w')
        valid_check += 1
    elif utils.invalid_id(guestID, "G-") ==1 :
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='INVALID', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=1,sticky='w')
        valid_check += 1
    else:
        for reservation in reservation_list: 
            for guest in guest_list:
                if guest.get_id() == guestID:
                    break
                elif reservation.get_guestID() == guestID:
                    Label(entry_frame, bg='#5E95FF', fg='crimson', text='Guest already has a reservation', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=1,sticky='w')
                    valid_check += 1
                    break
            else:
                Label(entry_frame, bg='#5E95FF', fg='crimson', text='Guest does not exist', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=1,sticky='w')
                valid_check += 1
                break

    # Check Room ID
    if len(roomID) == 0:
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=2,sticky='w')
        valid_check += 1
    elif utils.invalid_id(roomID, "R-") ==1 :
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='INVALID', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=2,sticky='w')
        valid_check += 1
    else:
        for reservation in reservation_list:
            for room in room_list:
                if room.get_id() ==  roomID:
                    break
                elif reservation.get_RoomID() == roomID:
                    Label(entry_frame, bg='#5E95FF', fg='crimson', text='Room already has a reservation', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=2,sticky='w')
                    valid_check += 1
                    break
            else:
                Label(entry_frame, bg='#5E95FF', fg='crimson', text='Room does not exist', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=2,sticky='w')
                valid_check += 1
                break

    # Check Checkin
    if len(checkin) == 0:
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=3,sticky='w')
        valid_check += 1
    elif utils.invalid_dob(checkin) == 1:
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='INVALID', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=3,sticky='w')
        valid_check += 1
    
    # Check Checkout
    if len(checkout) == 0:
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=4,sticky='w')
        valid_check += 1
    elif utils.invalid_dob(checkout) == 1:
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='INVALID', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=4,sticky='w')
        valid_check += 1

    # If All Valid
    if valid_check == 0:
        # Add to reservation_list
        new_reservation = Reservation( id, guestID, roomID, checkin, checkout)
        
        reservation_list.append(new_reservation)

        # Display on Treeview
        reservation_tree.insert(parent='', index = 'end', iid=id, text='', values=(id, guestID, roomID, checkin, checkout))

        # Empty Entry boxes
        id_entry.delete(0, END)
        guestID_entry.delete(0, END)
        roomID_entry.delete(0, END)
        checkin_entry.delete(0, END)
        checkout_entry.delete(0, END)

def reservation_remove(reservation_list, reservation_tree):
    if len(reservation_tree.selection())>0:
        selected_reservation = reservation_tree.selection()[0]
        reservation_id = reservation_tree.item(selected_reservation, 'values')[0]

        for reservation in reservation_list:
            if reservation.get_id()== reservation_id:
                reservation_list.remove(reservation)
                break
        reservation_tree.delete(selected_reservation)

def all_reservation_remove(reservation_tree, reservation_list):
    for reservation in reservation_tree.get_children():
        reservation_tree.delete(reservation)
    reservation_list.clear()

def reservation_select(reservation_list, reservation_tree, entry_frame,id_entry, guestID_entry, roomID_entry, checkin_entry, checkout_entry):
    # Delete all Warnings
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                                           ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=0,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                                                           ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=1,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                                                           ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=2,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                                               ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=3,sticky='w')
    Label(entry_frame, bg='#5E95FF', fg='crimson', text='                                               ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=4,sticky='w')

    
    # Empty Entry boxes
    id_entry.delete(0, END)
    guestID_entry.delete(0, END)
    roomID_entry.delete(0, END)
    checkin_entry.delete(0, END)
    checkout_entry.delete(0, END)

    # Show Selected reservation Info
    if len(reservation_tree.selection())>0:
        global selected_reservation
        selected_reservation = reservation_tree.selection()[0]
        reservation_id = reservation_tree.item(selected_reservation, 'values')[0]
        for reservation in reservation_list:
            if reservation.get_id()== reservation_id:
                id_entry.insert(0, reservation.get_id())
                guestID_entry.insert(0, reservation.get_guestID())
                roomID_entry.insert(0, reservation.get_RoomID())
                checkin_entry.insert(0, reservation.get_checkin())
                checkout_entry.insert(0, reservation.get_checkout())
                break

def reservation_update(reservation_list, guest_list, room_list, reservation_tree, entry_frame, id_entry, guestID_entry, roomID_entry, checkin_entry, checkout_entry):
    global selected_reservation
    if selected_reservation != -1:
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='                                            ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=0,sticky='w')
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='                                                                 ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=1,sticky='w')
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='                                                                   ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=2,sticky='w')
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='                                               ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=3,sticky='w')
        Label(entry_frame, bg='#5E95FF', fg='crimson', text='                                               ', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=4,sticky='w')

        id = id_entry.get()
        guestID = guestID_entry.get()
        roomID = roomID_entry.get()
        checkin = checkin_entry.get()
        checkout = checkout_entry.get()
            
        # Validation
        valid_check = 0
        
        # Check ID
        if len(id) == 0:
            Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=0,sticky='w')
            valid_check += 1
        elif utils.invalid_reservationID(id, "RS-") ==1 :
            Label(entry_frame, bg='#5E95FF', fg='crimson', text='INVALID', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=0,sticky='w')
            valid_check += 1
        else:
            if id != reservation_tree.item(selected_reservation, 'values')[0]:
                for reservation in reservation_list:
                    if reservation.get_id() == id:
                        Label(entry_frame, bg='#5E95FF', fg='crimson', text='ID already exists', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=0,sticky='w')
                        valid_check += 1
                        break
                
        # Check Guest ID
        if len(guestID) == 0:
            Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=1,sticky='w')
            valid_check += 1
        elif utils.invalid_id(guestID, "G-") ==1 :
            Label(entry_frame, bg='#5E95FF', fg='crimson', text='INVALID', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=1,sticky='w')
            valid_check += 1
        else:
            for reservation in reservation_list:
                for guest in guest_list:
                    if guest.get_id() == guestID:
                        break
                else:
                    Label(entry_frame, bg='#5E95FF', fg='crimson', text='Guest does not exist', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=1,sticky='w')
                    valid_check += 1
                    break
                        
        # Check Room ID
        if len(roomID) == 0:
            Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=2,sticky='w')
            valid_check += 1
        elif utils.invalid_id(roomID, "R-") ==1 :
            Label(entry_frame, bg='#5E95FF', fg='crimson', text='INVALID', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=2,sticky='w')
            valid_check += 1
        else:
            for reservation in reservation_list:
                for room in room_list:
                    if room.get_id() == roomID:
                        break
                else:
                    Label(entry_frame, bg='#5E95FF', fg='crimson', text='Room does not exist', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=2,sticky='w')
                    valid_check += 1
                    break

        # Check Checkin
        if len(checkin) == 0:
            Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=3,sticky='w')
            valid_check += 1
        elif utils.invalid_dob(checkin) == 1:
            Label(entry_frame, bg='#5E95FF', fg='crimson', text='INVALID', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=3,sticky='w')
            valid_check += 1
        
        # Check Checkout
        if len(checkout) == 0:
            Label(entry_frame, bg='#5E95FF', fg='crimson', text='EMPTY', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=4,sticky='w')
            valid_check += 1
        elif utils.invalid_dob(checkout) == 1:
            Label(entry_frame, bg='#5E95FF', fg='crimson', text='INVALID', font=("Montserrat Bold", 14, 'bold')).grid(column=6,row=4,sticky='w')


        # If All Valid
        if valid_check == 0:
            for reservation in reservation_list:
                for guest in guest_list:
                    for room in room_list:
                        if reservation.get_id() == reservation_tree.item(selected_reservation, 'values')[0]:
                            reservation.set_ID(id)
                            reservation.set_GuestID(guestID)
                            reservation.set_RoomID(roomID)
                            reservation.set_Checkin(checkin)
                            reservation.set_Checkout(checkout)

                            break
                
                
            reservation_tree.item(selected_reservation, text="", values = (id, guestID, roomID, checkin, checkout))
            selected_reservation = -1

            id_entry.delete(0, END)
            guestID_entry.delete(0, END)
            roomID_entry.delete(0, END)
            checkin_entry.delete(0, END)
            checkout_entry.delete(0, END)


def reservation_press(window, width, height, reservation_list, guest_list, room_list):
    global selected_reservation
    selected_reservation = -1
    reservation_subwin = Toplevel(window)
    reservation_subwin.title("reservation Information")
    reservation_subwin.geometry("%dx%d+0+0" % (width, height))
  
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
    reservation_tree = ttk.Treeview(reservation_subwin, selectmode='browse', show='headings')

    # Define columns
    reservation_tree['columns'] = ("ID", "GuestID", "RoomID", "Checkin", "Checkout")

    # Format columns
    reservation_tree.column("#0", width=0, stretch=NO)
    reservation_tree.column("ID", anchor='center', width=75)
    reservation_tree.column("GuestID", anchor='center', width=100)
    reservation_tree.column("RoomID",anchor='w', width=100)
    reservation_tree.column("Checkin",anchor='center', width=100)
    reservation_tree.column("Checkout",anchor='center', width=100)


    # Create Headings
    reservation_tree.heading("#0", text="")
    reservation_tree.heading("ID", text="ID", anchor='center', command= lambda: utils.sort_reservation_list_by_column(reservation_tree, reservation_list, "ID", False))
    reservation_tree.heading("GuestID", text="GuestID", anchor='center', command= lambda: utils.sort_reservation_list_by_column(reservation_tree, reservation_list, "GuestID", False))
    reservation_tree.heading("RoomID", text="RoomID", anchor='center', command= lambda: utils.sort_reservation_list_by_column(reservation_tree, reservation_list, "RoomID", False))
    reservation_tree.heading("Checkin", text="Checkin", anchor='center', command= lambda: utils.sort_reservation_list_by_column(reservation_tree, reservation_list, "Checkin", False))
    reservation_tree.heading("Checkout", text="Checkout", anchor='center', command= lambda: utils.sort_reservation_list_by_column(reservation_tree, reservation_list, "Checkout", False))

    reservation_tree.bind('<Motion>', 'break')
    
    # Insert Data
    for reservation in reservation_list:
        reservation_tree.insert(parent='', index = 'end', iid=reservation.get_id(), text='', values=(reservation.get_id(), reservation.get_guestID(), reservation.get_RoomID(), reservation.get_checkin(), reservation.get_checkout()))
    
    # GUI treeview
    reservation_tree.place(x=50, y= 450, height=height, width=width/2 + 500)


    #=========================================================================================
    
    # Main Content : Reservation Management
    Label(reservation_subwin, bg='#5E95FF', fg='white', text='RESERVATION MANAGEMENT', font=("Montserrat Bold", 20, 'bold')).place(x=50, y=25, width=width/2 + 670, height=50)
    entry_frame = Frame(reservation_subwin, bg='#5E95FF')
    entry_frame.place(x=50, y=100 , width=width/2, height=height/2 - 100)
    
    # Condition Warning
    subentry_frame = Frame(reservation_subwin, bg='#5E95FF')
    subentry_frame.place(x=width/2+300, y=100 , width= 420, height=height/2 - 100)
    Label(reservation_subwin, text=' - ID must be "RS-xxx" ', anchor='w', bg='#5E95FF', fg='white', font=("Montserrat Bold", 14, 'bold')).place(x=width/2+300, y=100, height=30)
    Label(reservation_subwin, text=' - Guest ID must be "G-xxx" ', anchor='w', bg='#5E95FF', fg='white', font=("Montserrat Bold", 14, 'bold')).place(x=width/2+300, y=130, height=30)
    Label(reservation_subwin, text=' - Room ID must be "R-xxx" ', anchor='w', bg='#5E95FF', fg='white', font=("Montserrat Bold", 14, 'bold')).place(x=width/2+300, y=160, height=30)
    Label(reservation_subwin, text=' - Checkin/Checkout must be "dd/mm/yyyy" ', anchor='w', bg='#5E95FF', fg='white', font=("Montserrat Bold", 14, 'bold')).place(x=width/2+300, y=190, height=30)

    # Entry Headers
    Label(entry_frame, bg='#5E95FF', fg='white', text='   ID   ', font=("Montserrat Bold", 14, 'bold')).grid(column=2, row=0)
    Label(entry_frame, bg='#5E95FF', fg='white', text='   GuestID   ', font=("Montserrat Bold", 14, 'bold')).grid(column=2, row=1)
    Label(entry_frame, bg='#5E95FF', fg='white', text='   RoomID   ', font=("Montserrat Bold", 14, 'bold')).grid(column=2, row=2)
    Label(entry_frame, bg='#5E95FF', fg='white', text='   Checkin   ', font=("Montserrat Bold", 14, 'bold')).grid(column=2, row=3)
    Label(entry_frame, bg='#5E95FF', fg='white', text='   Checkout   ', font=("Montserrat Bold", 14, 'bold')).grid(column=2, row=4)

    # Entries
    id_entry = Entry(entry_frame)
    id_entry.grid(column=4,row=0)

    guestID_entry = Entry(entry_frame)
    guestID_entry.grid(column=4,row=1)

    roomID_entry = Entry(entry_frame)
    roomID_entry.grid(column=4,row=2)

    checkin_entry = Entry(entry_frame)
    checkin_entry.grid(column=4,row=3)

    checkout_entry = Entry(entry_frame)
    checkout_entry.grid(column=4,row=4)


    # Buttons input
    add_reservation_button = Button(reservation_subwin, text='ADD',anchor='center',font=("Montserrat Bold", 12,'bold'),bg='#5E95FF', fg='white', relief='ridge',
        activebackground='dark blue', activeforeground='white', command=lambda: reservation_add(reservation_list, guest_list, room_list, reservation_tree, entry_frame, id_entry, guestID_entry, roomID_entry, checkin_entry, checkout_entry))
    add_reservation_button.place(x=width/2 + 100 , y= 100 , width=150, height=50)

    update_reservation_button = Button(reservation_subwin, text='UPDATE',anchor='center',font=("Montserrat Bold", 12,'bold'),bg='#5E95FF', fg='white', relief='ridge',
        activebackground='dark blue', activeforeground='white', command=lambda: reservation_update(reservation_list, guest_list, room_list, reservation_tree, entry_frame, id_entry, guestID_entry, roomID_entry, checkin_entry, checkout_entry))
    update_reservation_button.place(x=width/2 + 100, y= 170, width=150, height=50)

    clear_button = Button(reservation_subwin, text='CLEAR',anchor='center',font=("Montserrat Bold", 12,'bold'),bg='#5E95FF', fg='white', relief='ridge',
        activebackground='dark blue', activeforeground='white', command=lambda: clear_entry(entry_frame, id_entry, guestID_entry, roomID_entry, checkin_entry, checkout_entry))
    clear_button.place(x=width/2 + 100, y=240, width=150, height=50)


    # Button to manage data in treeview

    remove_reservation_button = Button(reservation_subwin, text='REMOVE SELECTED',anchor='center',font=("Montserrat Bold", 11,'bold'),bg='red', fg='white', relief='ridge',
        activebackground='blue', activeforeground='white', command=lambda: reservation_remove(reservation_list, reservation_tree))
    remove_reservation_button.place(x=width/2 +570, y=height/2 +125, width=150, height=50)

    remove_all_reservation_button = Button(reservation_subwin, text='REMOVE ALL',anchor='center',font=("Montserrat Bold", 11,'bold'),bg='red', fg='white', relief='ridge',
        activebackground='blue', activeforeground='white', command=lambda: all_reservation_remove(reservation_tree, reservation_list))
    remove_all_reservation_button.place(x=width/2 +570, y=height/2+200, width=150, height=50)

    select_reservation_button = Button(reservation_subwin, text='SELECT',anchor='center',font=("Montserrat Bold", 11,'bold'), bg='red',fg='white', relief='ridge',
        activebackground='blue', activeforeground='white', command=lambda: reservation_select(reservation_list, reservation_tree, entry_frame,id_entry, guestID_entry, roomID_entry, checkin_entry, checkout_entry))
    select_reservation_button.place(x= width/2 +570, y=height/2 + 50, width=150, height=50)
