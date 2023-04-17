from tkinter import *

import data

import Function.HotelButton as HotelButton
import Function.StaffButton as StaffButton
import Function.GuestButton as GuestsButton
import Function.RoomButton as RoomButton
import Function.ReservationButton as ReservationButton

#create the window
window = Tk()

#set title of the window
window.title("Hotel Information Management System")

#make window fullscreen
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.geometry(('1200x800'))


# GET DATA
def windows_open():
    data.unzip_data()
    #global hotel_list
    #hotel_list = data.open_hotel()
    global staff_list
    staff_list = data.open_staffs()
    global guests_list
    guests_list = data.open_guests()
    global room_list
    room_list = data.open_room()
    global reservation_list
    reservation_list = data.open_reservation()

# SAVE DATA
def window_close():
    #global hotel_list
    #data.data_hotel(hotel_list)
    global staff_list
    data.data_staffs(staff_list)
    global guests_list
    data.data_guests(guests_list)
    global room_list
    data.data_room(room_list)
    global reservation_list
    data.data_reservation(reservation_list)

    data.zip_data()
    window.destroy()

# CREATE LIST
global hotel_list
hotel_list = []
global staff_list
staff_list = []
global room_list
room_list = []
global guests_list
guests_list = []
global reservation_list
reservation_list = []

# Decorate menu
    #right
        # background
Frame(window, bg="white").place(x = 0, y = 0, width = width, height = height)
        # title
Label(window, text="HOTEL INFORMATION", font=("Montserrat Bold", 50,'bold'), bg="white", fg="#5E95FF").place(x = width/2-550, y = 100, width = width/2, height = 100)
Label(window, text="MANAGEMENT SYSTEM", font=("Montserrat Bold", 50,'bold'), bg="white", fg="#5E95FF").place(x = width/2-550, y = 180, width = width/2, height = 100)
    #left
        # buttons
hotel_button = Button(window, text="HOTEL", anchor='center', font=("Montserrat Bold", 30,'bold'), bg="#5E95FF", fg="white", relief='ridge',
            activebackground='#5E95FF', activeforeground='white', command=lambda: HotelButton.hotel_window(window, width, height, room_list, reservation_list))
hotel_button.place(x=width/2-450, y=height/2-70, width=width/2-200, height = 70)

staff_button = Button(window, text="STAFF", anchor='center', font=("Montserrat Bold", 30,'bold'), bg="#5E95FF", fg="white", relief='ridge', 
            activebackground='#5E95FF', activeforeground='white', command=lambda: StaffButton.staff_press(window, width, height, staff_list))
staff_button.place(x=width/2-450, y=height/2, width=width/2-200, height = 70)

guest_button = Button(window, text="GUEST", anchor='center', font=("Montserrat Bold", 30,'bold'), bg="#5E95FF", fg="white", relief='ridge', 
            activebackground='#5E95FF', activeforeground='white', command=lambda: GuestsButton.guest_press(window, width, height, guests_list))
guest_button.place(x=width/2-450, y=height/2+70, width=width/2-200, height = 70)

room_button = Button(window, text="ROOM", anchor='center', font=("Montserrat Bold", 30,'bold'), bg="#5E95FF", fg="white", relief='ridge', 
            activebackground='#5E95FF', activeforeground='white', command=lambda: RoomButton.room_press(window, width, height, room_list, reservation_list))
room_button.place(x=width/2-450, y=height/2+140, width=width/2-200, height = 70)

reservation_button = Button(window, text="RESERVATION", anchor='center', font=("Montserrat Bold", 30,'bold'), bg="#5E95FF", fg="white", relief='ridge', 
            activebackground='#5E95FF', activeforeground='white', command=lambda: ReservationButton.reservation_press(window, width, height, reservation_list, guests_list, room_list))  
reservation_button.place(x=width/2-450, y=height/2+210, width=width/2-200, height = 70)




# RUN MAIN
def main():
    windows_open()
    window.protocol("WM_DELETE_WINDOW", window_close)
    window.mainloop()

if __name__ == "__main__":
    main()